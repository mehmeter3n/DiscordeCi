# Generated by Django 4.1.2 on 2022-11-09 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0014_alter_uyediscordlog_discordid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uye',
            name='DiscordID',
            field=models.CharField(max_length=19, null=True, unique=True),
        ),
    ]
