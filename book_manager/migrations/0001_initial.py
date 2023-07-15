# Generated by Django 4.2.3 on 2023-07-15 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('author', models.CharField(default='anonymous', max_length=150)),
                ('genre', models.CharField(max_length=100)),
                ('height', models.IntegerField()),
                ('publisher', models.CharField(max_length=100)),
            ],
        ),
    ]