# Generated by Django 4.0.2 on 2022-04-03 19:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('bucket', '0007_alter_link_image_alter_link_link_alter_vote_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='id',
            field=models.UUIDField(default=uuid.UUID('a7d11fd2-410e-4bcb-b641-085bd9b75cbd'), primary_key=True, serialize=False),
        ),
    ]
