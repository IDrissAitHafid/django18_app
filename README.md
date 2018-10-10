# django18_app

# Note:
-Si vous avez éxecuté les tests selenium pour la première fois, et vous voulez tester une deuxième fois il faut changer les informations pour sign up à l'application (ligne 42 - ligne 48).
-Les tests s'executent sur le navigateur Firefox.

# Installation:

Clone this repository.

cd into django18_app: cd django18_app.

Create a new virtualenv called ayomi_test: mkvirtualenv ayomi_test.
install django: pip install django==1.8.
install selenium: pip install selenium.

command to run the server: python manage.py runserver.
command to run tests: python manage.py test django18_app.
