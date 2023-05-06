import csv
import datetime
import os

from django.conf import settings
from django.core.management.base import BaseCommand

from ...models import Book, Review


class Command(BaseCommand):
    help = "Backup Book and Review data"

    def handle(self, *args, **options):
        date = datetime.date.today().strftime("%Y%m%d")
        book_file_path = settings.BACKUP_PATH+"book_"+date+".csv"
        review_file_path = settings.BACKUP_PATH+"review_"+date+".csv"

        all_model = [Book, Review]

        all_file_path = [book_file_path, review_file_path]

        os.makedirs(settings.BACKUP_PATH, exist_ok=True)

        # for key, value in dict.items():
        for i in range(0, 2):
            with open(all_file_path[i], "w") as file:
                writer = csv.writer(file)

                header = [field.name for field in all_model[i]._meta.fields]
                writer.writerow(header)

                tables = all_model[i].objects.all()

                for table in tables:
                    if i == 0:
                        writer.writerow([
                            table.title,
                            table.text,
                            str(table.thumbnail),
                            str(table.category),
                            str(table.url),
                            str(table.user),
                            str(table.views)
                        ])
                    if i == 1:
                        writer.writerow([
                            str(table.book),
                            table.title,
                            table.text,
                            str(table.rate),
                            str(table.user),
                        ])

        files = os.listdir(settings.BACKUP_PATH)

        if len(files) >= settings.NUM_SAVED_BACKUP:
            files.sort()
            os.remove(settings.BACKUP_PATH+files[0])
