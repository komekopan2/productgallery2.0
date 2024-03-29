# Generated by Django 4.2.1 on 2023-12-03 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_alter_book_category_alter_book_text_alter_book_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(choices=[('homepage', 'Homepage'), ('web', 'web'), ('mobile', 'mobile'), ('xr', 'XR'), ('game', 'game'), ('other', 'other')], max_length=100, verbose_name='カテゴリー'),
        ),
        migrations.AlterField(
            model_name='book',
            name='text',
            field=models.TextField(verbose_name='説明'),
        ),
        migrations.AlterField(
            model_name='book',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='サムネイル(任意)'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=100, verbose_name='タイトル'),
        ),
        migrations.AlterField(
            model_name='book',
            name='url',
            field=models.URLField(blank=True, null=True, verbose_name='URL(任意)'),
        ),
        migrations.AlterField(
            model_name='review',
            name='rate',
            field=models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], verbose_name='星の数'),
        ),
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.TextField(verbose_name='レビュー内容'),
        ),
        migrations.AlterField(
            model_name='review',
            name='title',
            field=models.CharField(max_length=100, verbose_name='タイトル'),
        ),
    ]
