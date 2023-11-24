import csv
import datetime
import os

from django.conf import settings
from django.core.management.base import BaseCommand

from ...models import Book, Review


# カスタム管理コマンドで、BookとReviewのデータをバックアップします。
class Command(BaseCommand):
    help = "Backup Book and Review data"  # コマンドの説明

    # この管理コマンドが実行されるとhandle関数が呼ばれる。
    def handle(self, *args, **options):
        # 今日の日付をYYYYMMDD形式で取得
        date = datetime.date.today().strftime("%Y%m%d")

        # BookとReviewモデルのバックアップファイルへのパス
        book_file_path = settings.BACKUP_PATH + "book_" + date + ".csv"
        review_file_path = settings.BACKUP_PATH + "review_" + date + ".csv"

        # バックアップするモデルのリスト
        all_model = [Book, Review]

        # 各モデルに対応するファイルパスのリスト
        all_file_path = [book_file_path, review_file_path]

        # バックアップディレクトリが存在することを確認し、存在しない場合は作成
        os.makedirs(settings.BACKUP_PATH, exist_ok=True)

        # 各モデルと対応するファイルパスに対してループ
        for i in range(0, 2):
            # ファイルパスを開いて書き込む
            with open(all_file_path[i], "w") as file:
                writer = csv.writer(file)

                # モデルのフィールド名でヘッダー行を書き込む
                header = [field.name for field in all_model[i]._meta.fields]
                writer.writerow(header)

                # モデルのすべてのオブジェクトをクエリ
                tables = all_model[i].objects.all()

                # 各オブジェクトのデータをファイルに書き込む
                for table in tables:
                    if i == 0:  # Bookモデルを書き込んでいる場合
                        writer.writerow(
                            [
                                table.title,
                                table.text,
                                str(table.thumbnail),
                                str(table.category),
                                str(table.url),
                                str(table.user),
                                str(table.views),
                            ]
                        )
                    if i == 1:  # Reviewモデルを書き込んでいる場合
                        writer.writerow(
                            [
                                str(table.book),
                                table.title,
                                table.text,
                                str(table.rate),
                                str(table.user),
                            ]
                        )

        # バックアップディレクトリ内のファイルリストを取得
        files = os.listdir(settings.BACKUP_PATH)

        # 設定された数を超えるバックアップがある場合
        if len(files) >= settings.NUM_SAVED_BACKUP:
            files.sort()
            # 最も古いバックアップファイルを削除
            os.remove(settings.BACKUP_PATH + files[0])
