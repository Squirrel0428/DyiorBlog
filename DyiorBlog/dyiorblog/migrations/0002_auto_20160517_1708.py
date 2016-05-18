# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('dyiorblog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('name', models.CharField(max_length=16)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.DeleteModel(
            name='ViewableManager',
        ),
        migrations.AlterField(
            model_name='article',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 17, 17, 8, 10, 554471)),
        ),
        migrations.AlterField(
            model_name='article',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 17, 17, 8, 10, 554508)),
        ),
        migrations.AddField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(to='dyiorblog.Article'),
        ),
    ]
