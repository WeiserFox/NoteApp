# Generated by Django 4.2.7 on 2023-11-04 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='author',
            field=models.CharField(default='noname', max_length=10),
        ),
    ]