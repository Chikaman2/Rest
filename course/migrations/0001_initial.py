# Generated by Django 4.1.7 on 2023-04-02 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('language', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=10)),
            ],
        ),
    ]
