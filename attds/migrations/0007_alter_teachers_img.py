# Generated by Django 4.0.3 on 2022-05-16 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attds', '0006_alter_students_img_alter_teachers_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachers',
            name='img',
            field=models.ImageField(default='def_img/tchr.png', upload_to='images/'),
        ),
    ]