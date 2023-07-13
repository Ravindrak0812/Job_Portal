# Generated by Django 4.0.4 on 2023-06-01 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0014_alter_recruiter_pwd_alter_studentuser_pwd'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.FileField(null=True, upload_to='')),
                ('applydate', models.DateField()),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.job')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.studentuser')),
            ],
        ),
    ]
