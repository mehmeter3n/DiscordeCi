# Generated by Django 4.1.2 on 2022-11-03 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0007_alter_uyeacc_firmaid_alter_uyeacc_uyeid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uyeadres',
            name='UyeID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.uye'),
        ),
    ]