# Generated by Django 4.1.2 on 2022-11-03 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0008_alter_uyeadres_uyeid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uye',
            name='UyeEMAIL',
            field=models.EmailField(max_length=50, unique=True),
        ),
    ]
