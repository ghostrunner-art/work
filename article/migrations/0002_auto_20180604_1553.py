# Generated by Django 2.0.5 on 2018-06-04 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='content',
            new_name='内容',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='title',
            new_name='标题',
        ),
    ]