# Generated by Django 2.2 on 2020-06-10 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_auto_20200610_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]