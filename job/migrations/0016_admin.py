# Generated by Django 4.2.1 on 2023-06-04 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0015_apply'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=15, null=True)),
                ('pwd', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=15, null=True)),
            ],
        ),
    ]
