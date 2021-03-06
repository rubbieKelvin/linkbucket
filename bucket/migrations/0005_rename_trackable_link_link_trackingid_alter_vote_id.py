# Generated by Django 4.0.2 on 2022-02-10 18:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('bucket', '0004_vote_link_alter_vote_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='link',
            old_name='trackable_link',
            new_name='trackingID',
        ),
        migrations.AlterField(
            model_name='vote',
            name='id',
            field=models.UUIDField(default=uuid.UUID('34a136b8-9f35-43f6-a4ce-ee1a5232fdc1'), primary_key=True, serialize=False),
        ),
    ]
