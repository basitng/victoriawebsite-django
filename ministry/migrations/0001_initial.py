# Generated by Django 4.1 on 2022-09-01 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ministry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.CharField(max_length=2000)),
                ('title', models.CharField(max_length=2000)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('content', models.CharField(max_length=2000)),
            ],
        ),
    ]
