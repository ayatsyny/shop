# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=80, verbose_name='\u0438\u043c\u044f')),
                ('last_name', models.CharField(max_length=80, verbose_name='\u0444\u0430\u043c\u0438\u043b\u0438\u044f')),
                ('sex', models.SmallIntegerField(verbose_name='\u043f\u043e\u043b', choices=[(0, '\u043c\u0443\u0436\u0441\u043a\u043e\u0439'), (1, '\u0436\u0435\u043d\u0441\u043a\u0438\u0439')])),
                ('birth_date', models.DateField(verbose_name='\u0434\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f')),
                ('email', models.EmailField(unique=True, max_length=75)),
            ],
            options={
                'ordering': (b'first_name', b'last_name'),
                'verbose_name': '\u043a\u043e\u043d\u0442\u0430\u043a\u0442\u043d\u043e\u0435 \u043b\u0438\u0446\u043e',
                'verbose_name_plural': '\u043a\u043e\u043d\u0442\u0430\u043a\u0442\u043d\u044b\u0435 \u043b\u0438\u0446\u0430',
            },
            bases=(models.Model,),
        ),
    ]
