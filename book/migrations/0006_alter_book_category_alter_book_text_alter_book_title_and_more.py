# Generated by Django 4.2.1 on 2023-12-03 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_alter_book_category_alter_book_text_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(choices=[('homepage', 'Homepage'), ('web', 'web'), ('mobile', 'mobile'), ('xr', 'XR'), ('game', 'game'), ('other', 'other')], help_text='本のカテゴリーを選択してください。', max_length=100, verbose_name='カテゴリー(任意)'),
        ),
        migrations.AlterField(
            model_name='book',
            name='text',
            field=models.TextField(help_text='本の説明を入力してください。', verbose_name='説明'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(help_text='本のタイトルを入力してください。', max_length=100, verbose_name='タイトル'),
        ),
        migrations.AlterField(
            model_name='book',
            name='url',
            field=models.URLField(blank=True, help_text='本の詳細情報へのURLを任意で入力してください。', null=True, verbose_name='URL(任意)'),
        ),
    ]
