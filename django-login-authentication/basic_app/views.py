from django.shortcuts import render
from basic_app.forms import UserForm, UserProfileInfoForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'basic_app/index.html')


def register(request):

    # Flag to check if the user is registered
    registered = False

    if request.method == 'POST':

        # instantiate Form objects with the retrieved data
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            # save the user form in plain text
            user = user_form.save()

            # hash the password
            user.set_password(user.password)

            # then save those changes on the password (re-save)
            user.save()

            # Do same for profile_form, but DO NOT commit to DB yet
            profile = profile_form.save(commit=False)

            # The OneToOne relationship defined in models.py is
            # reflected here. We are linking both forms togehter
            # in this line of code, keeping profile_form as master
            profile.user = user

            # if a profile picture was provided
            if 'profile_pic' in request.FILES:

                # grab the value of the profile_pic
                profile.profile_pic = request.FILES['profile_pic']

            # save the changes
            profile.save()

            # registration successful, flag it.
            registered = True

        # there was an error in the registration, print it.
        else:

            print(user_form.errors, profile_form.errors)

    # Request was NOT POST (Get or other one)
    else:

        # so show the forms to be completed
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    # at any case, return the view with its context view
    return render(
        request,
        'basic_app/registration.html',
        {
            'user_form' : user_form,
            'profile_form' : profile_form,
            'registered' : registered
        }
    )


# We CANNOT use login() as a function name, since it shares
# the same as the import from django.contrib.auth!

def user_login(request):

    if request.method == 'POST':

        # get the data posted from the 'username' input text field in
        # login.html. Same for the password.
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built in authentication for username and password
        user = authenticate(username=username, password=password)

        # if the user authenticates, then it won't be a falsy value
        if user:

            # user has a valid session (no lost password, no lost connection
            # on login, session not expired, etc)
            if user.is_active:

                # Django's built-in login function.
                # > Needs the request and user authenticated objects
                login(request, user)

                # once logged in, redirect them to index.
                # > They are now in index.html, logged in
                return HttpResponseRedirect(reverse('index'))


            # if the account is not active, respond it
            else:

                return HttpResponse('Account inactive!')


        # on a failed authentication, print it and return response
        else:

            print('Someone tried to log in and failed')
            print('Username: {} - Password {}'.format(username, password))

            return HttpResponse('Invalid login details')


    # on a request != 'POST'
    else:

        # render the login page with an empty context
        # dictionary as a context
        return render(request, 'basic_app/login.html', {})



# a logout function, which requires the user to be logged in
# to be able to call it, that is why we use the proper decorator.

@login_required
def user_logout(request):

    # Django's built-in logout function
    logout(request)

    # redirect the logged-out user to index.html
    return HttpResponseRedirect(reverse('index'))


# dummy function to test logged-in functionality

@login_required
def special(request):
    return render(request, 'basic_app/special.html', {})
