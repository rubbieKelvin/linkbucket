# Generated by Django 4.0.2 on 2022-04-03 17:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('bucket', '0005_rename_trackable_link_link_trackingid_alter_vote_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='id',
            field=models.UUIDField(default=uuid.UUID('5fbb3b3e-233e-4c1a-baa3-6080037b0ba6'), primary_key=True, serialize=False),
        ),
    ]
