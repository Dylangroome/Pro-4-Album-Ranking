# Generated by Django 3.2.18 on 2023-04-21 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20230421_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='genre',
            field=models.IntegerField(choices=[(1, 'HipPop'), (2, 'RnB')], default=1),
        ),
    ]
