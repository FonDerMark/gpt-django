# Generated by Django 4.2.1 on 2023-05-09 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_messages_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messages',
            name='user',
        ),
    ]
