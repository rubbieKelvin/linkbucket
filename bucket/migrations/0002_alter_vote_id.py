# Generated by Django 4.0.2 on 2022-02-10 00:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('bucket', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='id',
            field=models.UUIDField(default=uuid.UUID('7896d2c2-0ff3-4636-9bb2-dec2e0abb6b1'), primary_key=True, serialize=False),
        ),
    ]