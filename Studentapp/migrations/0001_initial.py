# Generated by Django 4.2.1 on 2023-05-08 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('maths', models.CharField(max_length=200)),
                ('eng', models.CharField(max_length=200)),
                ('kis', models.CharField(max_length=200)),
                ('cre', models.CharField(max_length=200)),
                ('science', models.CharField(max_length=200)),
            ],
        ),
    ]
