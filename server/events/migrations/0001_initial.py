# Generated by Django 3.0.3 on 2020-04-01 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventPlayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(blank=True, max_length=32, null=True)),
                ('goals_in_game', models.IntegerField(default=0)),
                ('assists_in_game', models.IntegerField(default=0)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='base_player', to='players.Player')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('location', models.CharField(max_length=32)),
                ('score_a', models.IntegerField(default=0)),
                ('score_b', models.IntegerField(default=0)),
                ('team_a', models.CharField(blank=True, max_length=32, null=True)),
                ('team_b', models.CharField(blank=True, max_length=32, null=True)),
                ('completed', models.BooleanField(default=False)),
                ('players', models.ManyToManyField(blank=True, to='events.EventPlayer')),
            ],
        ),
    ]