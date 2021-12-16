# Generated by Django 3.2.10 on 2021-12-15 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0002_alter_students_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='address',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='students',
            name='profile_pic',
            field=models.ImageField(default='students/avatar.jpg', upload_to='students'),
        ),
    ]
