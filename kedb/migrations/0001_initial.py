# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KnownError',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('description', models.TextField(verbose_name='description', blank=True)),
                ('check', models.CharField(max_length=255, verbose_name='sensu check')),
                ('output_pattern', models.CharField(max_length=255, verbose_name='output pattern')),
                ('level', models.CharField(default=b'level1', max_length=55, verbose_name='level', choices=[(b'l1', 'Level 1'), (b'l2', 'Level 2')])),
                ('severity', models.CharField(default=b'medium', max_length=55, verbose_name='severity', choices=[(b'int', 'Internal'), (b'999', 'SLA 99.9'), (b'9999', 'SLA 99.99')])),
                ('ownership', models.CharField(default=b'cloudlab', max_length=55, verbose_name='ownership', choices=[(b'cloud', 'Cloud'), (b'network', 'Network'), (b'hardware', 'Hardware')])),
            ],
            options={
                'verbose_name': 'known error',
                'verbose_name_plural': 'known errors',
            },
        ),
        migrations.CreateModel(
            name='Workaround',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(verbose_name='description', blank=True)),
                ('temporary', models.BooleanField(max_length=255, verbose_name='temporary')),
                ('engine', models.CharField(default=b'salt', max_length=255, verbose_name='engine', choices=[(b'salt', 'Salt call'), (b'jenkins', 'Jenkins job'), (b'misc', 'Misc')])),
                ('action', models.TextField(verbose_name='description', blank=True)),
                ('known_error', models.ForeignKey(related_name='workarounds', verbose_name='known error', to='kedb.KnownError')),
            ],
            options={
                'verbose_name': 'workaround',
                'verbose_name_plural': 'workarounds',
            },
        ),
    ]
