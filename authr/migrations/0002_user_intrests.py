# Generated by Django 4.0.2 on 2022-02-10 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bucket', '0002_alter_vote_id'),
        ('authr', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='intrests',
            field=models.ManyToManyField(related_name='users', to='bucket.Tag'),
        ),
    ]
