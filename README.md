#Creeply
The concept is simple, the goal is to create a platform in which individuals can enter a name and have a *likely profile* built for that user based on their online presence

We will pull in data from
* Facebook
* LinkedIn
* Twitter
* And so on

To build a context for a user

##Setup/Configuration
Creeply is run on a virtualenv, and requires a MySQL database server

Steps to get up and running:

1. Add ```127.0.0.1       creeply.dev``` to your hosts file

2. Fire up your mysql server, and create the database (match the settings in settings.py)

3. Navigate to hobby/env and then run ```source bin/activate``` to fire up the virtual environment

4. ```python manage.py runserver 8000``` to begin running the server at http://creeply.dev:8000

5. Sell your soul to creeply.