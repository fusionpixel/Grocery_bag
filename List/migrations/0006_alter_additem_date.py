# Generated by Django 3.2.5 on 2021-08-02 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('List', '0005_alter_additem_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additem',
            name='date',
            field=models.DateTimeField(),
        ),
    ]