# Generated by Django 4.1 on 2022-09-18 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hobeapp', '0009_alter_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(null=True, upload_to='static/image/'),
        ),
    ]
