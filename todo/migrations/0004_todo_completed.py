# Generated by Django 4.0.4 on 2022-05-24 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_alter_todo_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='completed',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]