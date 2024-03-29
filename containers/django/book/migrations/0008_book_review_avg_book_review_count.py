# Generated by Django 4.2.1 on 2023-12-03 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_alter_book_category_alter_book_text_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='review_avg',
            field=models.FloatField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='review_count',
            field=models.IntegerField(default=0),
        ),
    ]
