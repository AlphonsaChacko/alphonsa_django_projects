# Generated by Django 4.1.5 on 2023-01-16 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_doctors'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='doctors',
            new_name='doctor',
        ),
    ]
