# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=16)),
                ('slug', models.SlugField()),
                ('markdown_content', models.TextField()),
                ('html_content', models.TextField()),
                ('status', models.IntegerField(default=1, choices=[(1, b'No Permission'), (2, b'Needs Editor'), (3, b'Needs Approval'), (4, b'Published'), (5, b'Archived'), (6, b'Record')])),
                ('created', models.DateTimeField(default=datetime.datetime(2016, 5, 17, 16, 33, 4, 662840))),
                ('modified', models.DateTimeField(default=datetime.datetime(2016, 5, 17, 16, 33, 4, 662873))),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['modified'],
                'verbose_name_plural': 'articles',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=16, blank=True)),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pag', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='ViewableManager',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(to='dyiorblog.Category'),
        ),
    ]
