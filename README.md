Django Login Authentication practice project
========================================

Overview
----------------------------------------

This project is a simple login app designed as to test Django framework (my very first attempt at it) and its deployment out.

I have coded this one as a practice project following Jose Portilla's proposed exercises on his 'Python and Django Full Stack Web Developer Bootcamp' Udemy course. Definitely check it out if you want to learn this framework, HTML, CSS, JQuery, Bootstrap and Python basics from scratch.

The idea behind this project is to allow users to register an account, log in and be granted access to URL paths only accessible when logged in.

It is a similar concept to the one uploaded in 'NodeJSLoginAuthentication' repository if you have already checked it out, or if you wish to do so.

As a first project, I kept it as simple as it could get. Everything is over-commented, sorry for that. It is the way I keep track of stuff when learning :P

Instructions
------------------------------------------

A navbar is displayed at all times, which will have a 'Register' link for you to create your account.

Password encrypting applying several algorithms is being applied. I have added Argon2, bCrypt and PBKDF2 hashers. A minimum length of 8 characters is also required for the password.

Portfolio website and profile pics are optional.

The portfolio website must be supplied as a full web path - like https://www.facebook.com - (I did not add validators to keep the project simple). The profile pic is processed by 'Pillow' module and is stored inside 'media/profile_pics folder'.

Once registered, you can log into that account. You can always logged in (if not already in session), using the proper link in the navbar.

And once logged in, you can access '/basic_app/special/' URL path (a link will be provided in the navbar), which acts as a dummy to prove that protected paths are accessible only when you are able to. If you attempt to get into that path without being logged in, then you will be redirected to the login page.

If you are inside your account, you will have the logout option available to at all times.
