# Generated by Django 2.2.6 on 2019-10-16 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("houses", "0001_initial")]

    operations = [
        migrations.AlterModelOptions(
            name="house",
            options={"verbose_name": "Дом", "verbose_name_plural": "Дома"},
        )
    ]