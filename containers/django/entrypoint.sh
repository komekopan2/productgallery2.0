#!/bin/sh
python manage.py makemigrations --noinput --settings bookproject.docker_settings
python manage.py migrate --noinput --settings bookproject.docker_settings
# python manage.py collectstatic --noinput --settings bookproject.docker_settings
python manage.py test --noinput --settings bookproject.docker_settings
# 環境変数のDEBUGの値がTrueの時はrunserverを、Falseの時はgunicornを実行します
# シェルスクリプトでは`[`と`$DEBUG`、`1`と`]`の間にスペースを一つ空けておかないと[]内の式を認識できないので注意
echo $DEBUG
if [ $DEBUG = 1 ]; then
    python manage.py runserver 0.0.0.0:8000 --settings bookproject.docker_settings
else
    # gunicornを起動させる時はプロジェクト名を指定します
    # 今回はbookprojectにします
    gunicorn bookproject.wsgi:application --bind 0.0.0.0:8000
fi
