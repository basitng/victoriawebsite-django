# Generated by Django 4.1 on 2022-09-01 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=200000, null=True)),
                ('picture1', models.TextField(max_length=2000, null=True)),
                ('picture2', models.TextField(max_length=2000, null=True)),
            ],
        ),
    ]