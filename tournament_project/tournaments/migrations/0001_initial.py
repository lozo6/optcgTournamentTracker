# Generated by Django 4.2.13 on 2024-05-22 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_event', models.DateField()),
                ('tournament_owner', models.CharField(max_length=100)),
                ('leader', models.CharField(max_length=100)),
                ('decklist', models.URLField()),
                ('entry_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
