# Generated by Django 4.0 on 2022-05-25 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peopledata', '0004_alter_unknown_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unknown',
            name='img',
            field=models.ImageField(blank=True, max_length=500, null=True, upload_to='unknown'),
        ),
        migrations.AlterModelTable(
            name='unknown',
            table='unknowns',
        ),
    ]
