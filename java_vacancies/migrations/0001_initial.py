# Generated by Django 4.1.5 on 2023-01-14 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='top_vacancies_skillls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('count', models.IntegerField()),
                ('year', models.IntegerField(default='0')),
            ],
        ),
    ]
