# Generated by Django 4.2.7 on 2023-11-05 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deapp', '0004_remove_user_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='text',
            field=models.CharField(default='Nothing', max_length=250),
        ),
    ]
