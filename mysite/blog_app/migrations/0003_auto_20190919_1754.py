# Generated by Django 2.2.1 on 2019-09-19 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_auto_20190918_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpost',
            name='author',
            field=models.CharField(max_length=128),
        ),
    ]