# Generated by Django 3.0.6 on 2020-05-17 00:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corona_app', '0003_auto_20200516_1800'),
    ]

    operations = [
        migrations.RenameField(
            model_name='noticias',
            old_name='link',
            new_name='fuente',
        ),
    ]