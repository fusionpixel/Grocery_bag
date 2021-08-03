# Generated by Django 3.2.5 on 2021-07-21 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.CharField(max_length=25)),
                ('status', models.CharField(choices=[('pending', 'PENDING'), ('bought', 'BOUGHT'), ('not available', 'NOT AVAILABLE')], default='pending', max_length=20)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
