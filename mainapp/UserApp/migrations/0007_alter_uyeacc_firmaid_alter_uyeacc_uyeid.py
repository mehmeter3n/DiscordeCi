# Generated by Django 4.1.2 on 2022-11-03 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FirmaApp', '0006_alter_discord_options'),
        ('UserApp', '0006_uyeacc_uyeaccdurum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uyeacc',
            name='FirmaID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FirmaApp.firma'),
        ),
        migrations.AlterField(
            model_name='uyeacc',
            name='UyeID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.uye'),
        ),
    ]
