# Generated by Django 4.2.9 on 2024-03-16 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessAutomationInterne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('dep', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
    ]