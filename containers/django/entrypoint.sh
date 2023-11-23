#!/bin/sh
python manage.py makemigrations --noinput --settings bookproject.docker_settings
python manage.py migrate --noinput --settings bookproject.docker_settings
# python manage.py collectstatic --noinput --settings bookproject.docker_settings
python manage.py test --noinput --settings bookproject.docker_settings
# 環境変数のDEBUGの値がTrueの時はrunserverを、Falseの時はgunicornを実行します
DEBUG_VALUE=$DEBUG
if [ "$DEBUG_VALUE" = "True" ]; then
    python manage.py runserver 0.0.0.0:8000 --settings bookproject.docker_settings
elif [ "$DEBUG_VALUE" = "False" ]; then
    # gunicornを起動させる時はプロジェクト名を指定します
    # 今回はbookprojectにします
    gunicorn bookproject.wsgi:application --bind 0.0.0.0:8000
else
    echo "DEBUG is not True or False"
fi
