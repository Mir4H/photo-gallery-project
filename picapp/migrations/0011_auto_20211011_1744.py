# Generated by Django 3.2.7 on 2021-10-11 14:44

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('picapp', '0010_auto_20211005_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='is_public',
            field=models.BooleanField(default=True, verbose_name='Public image (Uncheck for private)'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
