# Generated by Django 3.2.7 on 2021-09-19 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usr', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=40)),
            ],
        ),
    ]
