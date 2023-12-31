# Generated by Django 4.0.4 on 2023-04-28 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentuser',
            old_name='mobile',
            new_name='fname',
        ),
        migrations.RenameField(
            model_name='studentuser',
            old_name='type',
            new_name='pwd',
        ),
        migrations.RemoveField(
            model_name='studentuser',
            name='user',
        ),
        migrations.AddField(
            model_name='studentuser',
            name='contact',
            field=models.IntegerField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='studentuser',
            name='email',
            field=models.EmailField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='studentuser',
            name='lname',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
