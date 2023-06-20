# Generated by Django 4.2.1 on 2023-06-13 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HMSapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('room', models.CharField(max_length=12)),
                ('guests', models.CharField(max_length=20)),
                ('arrival', models.DateField()),
                ('departure', models.DateField()),
                ('special', models.TextField()),
            ],
        ),
    ]