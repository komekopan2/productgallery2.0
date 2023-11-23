# Pythonのイメージを指定
FROM python:3.8
# PYTHONDONTWRITEBYTECODEとPYTHONUNBUFFEREDはオプション
# pycファイル(および__pycache__)の生成を行わないようにする
ENV PYTHONDONTWRITEBYTECODE=1
# 標準出力・標準エラーのストリームのバッファリングを行わない
ENV PYTHONUNBUFFERED=1
# コンテナのワークディレクトリを/codeに指定
WORKDIR /code
# ローカルのrequirements.txtをコンテナの/codeフォルダ直下に置く
COPY requirements.txt /code/
# コンテナ内でpipをアップグレードした後、pip install -r requirements.txtを実行
RUN pip install --upgrade pip && \
    pip install -r requirements.txt
# ソースコードをコンテナにコピー
COPY ./containers/django/static /static/
COPY ./containers/django /code/

# COPY ./containers/django/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /code/entrypoint.sh
