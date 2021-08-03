# Generated by Django 3.2.5 on 2021-07-21 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('List', '0002_alter_additem_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additem',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='additem',
            name='status',
            field=models.CharField(choices=[('PENDING', 'pending'), ('BOUGHT', 'bought'), ('NOT AVAILABLE', 'not available')], default='PENDING', max_length=20),
        ),
    ]
