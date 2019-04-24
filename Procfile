release: python manage.py migrate
web: gunicorn varwish.wsgi:application --log-file - --log-level debug --preload --workers 1
