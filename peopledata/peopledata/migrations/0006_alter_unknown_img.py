# Generated by Django 4.0 on 2022-05-25 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peopledata', '0005_alter_unknown_img_alter_unknown_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unknown',
            name='img',
            field=models.TextField(null=True),
        ),
    ]
