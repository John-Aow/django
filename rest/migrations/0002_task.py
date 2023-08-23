# Generated by Django 4.2.4 on 2023-08-21 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('description', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('complete', models.BooleanField()),
            ],
            options={
                'db_table': 'task',
                'ordering': ['-date_created'],
            },
        ),
    ]