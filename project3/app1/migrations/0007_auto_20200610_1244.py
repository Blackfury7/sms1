# Generated by Django 2.2 on 2020-06-10 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_query_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]