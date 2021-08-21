# Generated by Django 3.2.6 on 2021-08-21 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squad',
            name='homeTown',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='squad',
            name='members',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracks', to='api.members'),
        ),
        migrations.AlterField(
            model_name='squad',
            name='secretBase',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='squad',
            name='squadName',
            field=models.CharField(max_length=150),
        ),
    ]
