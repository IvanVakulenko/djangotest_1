# Generated by Django 4.1 on 2022-08-18 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tg_token', models.CharField(max_length=200, verbose_name='Token')),
                ('tg_chat', models.CharField(max_length=200, verbose_name='Chat id')),
                ('tg_message', models.TextField(verbose_name='Message')),
            ],
            options={
                'verbose_name': 'Settings',
                'verbose_name_plural': 'More Settings',
            },
        ),
    ]
