# Generated by Django 3.0.3 on 2020-04-11 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentor',
            name='name',
            field=models.CharField(default=0, max_length=64),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='organisation',
            field=models.CharField(default=0, max_length=64),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='phone',
            field=models.IntegerField(default=0),
        ),
    ]
