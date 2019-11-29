# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('place', '__first__'),
        ('stock', '__first__'),
        ('person', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=80, verbose_name='\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('address', models.CharField(max_length=250, verbose_name='\u0430\u0434\u0440\u0435\u0441')),
                ('website', models.URLField(verbose_name='\u0432\u0435\u0431-\u0441\u0430\u0439\u0442', blank=True)),
                ('city', models.ForeignKey(to='place.City', to_field='id', verbose_name='\u0433\u043e\u0440\u043e\u0434')),
                ('owner', models.ForeignKey(to='person.Person', to_field='id', verbose_name='\u0432\u043b\u0430\u0434\u0435\u043b\u0435\u0446')),
                ('sellers', models.ManyToManyField(to='person.Person', verbose_name='\u043f\u0440\u043e\u0434\u0430\u0432\u0446\u044b')),
                ('stocks', models.ManyToManyField(to='stock.Stock', verbose_name='\u0441\u043a\u043b\u0430\u0434\u044b')),
            ],
            options={
                'ordering': (b'name',),
                'verbose_name': '\u043c\u0430\u0433\u0430\u0437\u0438\u043d',
                'verbose_name_plural': '\u043c\u0430\u0433\u0430\u0437\u0438\u043d\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ShopType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
            ],
            options={
                'ordering': (b'name',),
                'verbose_name': '\u0442\u0438\u043f \u043c\u0430\u0433\u0430\u0437\u0438\u043d\u0430',
                'verbose_name_plural': '\u0442\u0438\u043f\u044b \u043c\u0430\u0433\u0430\u0437\u0438\u043d\u0430',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='shop',
            name='type',
            field=models.ForeignKey(to='shop.ShopType', to_field='id', verbose_name='\u0442\u0438\u043f \u043c\u0430\u0433\u0430\u0437\u0438\u043d\u0430'),
            preserve_default=True,
        ),
    ]
