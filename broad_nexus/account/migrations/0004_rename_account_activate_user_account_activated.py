# Generated by Django 4.2.3 on 2023-07-14 01:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_user_account_activate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='account_activate',
            new_name='account_activated',
        ),
    ]
