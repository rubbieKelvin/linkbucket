# Generated by Django 4.0.2 on 2022-04-03 19:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('bucket', '0008_alter_vote_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='id',
            field=models.UUIDField(default=uuid.UUID('cbde20e3-cd64-495c-b9cd-92ffbf473982'), primary_key=True, serialize=False),
        ),
    ]
