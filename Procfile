release: python manage.py migrate

web: gunicorn arkham.wsgi --log-file -

worker: python manage.py rqworker default