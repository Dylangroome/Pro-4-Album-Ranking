# Generated by Django 3.2.18 on 2023-04-27 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_album_genre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='rate',
            new_name='rates',
        ),
    ]