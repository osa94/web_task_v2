import os

if 'db.sqlite3' in os.listdir('.'):
    os.system('python manage.py runserver')
else:
    os.system('python manage.py makemigrations')
    os.system('python manage.py migrate')
    os.system('python fill_database.py')
    os.system('python manage.py runserver')

