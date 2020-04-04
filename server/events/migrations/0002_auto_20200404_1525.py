# Generated by Django 3.0.3 on 2020-04-04 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='players',
        ),
        migrations.AddField(
            model_name='eventplayer',
            name='event',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='events.Event'),
            preserve_default=False,
        ),
    ]
