# Generated by Django 3.2.10 on 2021-12-19 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0008_auto_20211219_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sessionyearmodel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
