# Generated by Django 3.2.7 on 2021-09-29 08:27

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('picapp', '0002_auto_20210929_0752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='picapp.album'),
        ),
    ]