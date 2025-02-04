# Generated by Django 5.0.6 on 2024-07-09 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medilabapp', '0002_register_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('DOB', models.CharField(max_length=200)),
                ('department', models.CharField(max_length=150)),
                ('doctor', models.CharField(max_length=200)),
                ('message', models.TextField()),
            ],
        ),
    ]
