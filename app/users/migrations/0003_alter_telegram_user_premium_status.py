# Generated by Django 4.2.1 on 2023-05-12 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_telegram_user_day_of_limit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telegram_user',
            name='premium_status',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]