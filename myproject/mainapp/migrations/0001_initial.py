# Generated by Django 3.0.2 on 2020-01-03 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='uploaded',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charfield', models.CharField(max_length=1000)),
                ('filefield', models.FileField(upload_to='uploads')),
            ],
        ),
    ]