# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(verbose_name='Name', max_length=512)),
                ('price', models.PositiveIntegerField(verbose_name='Price')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(verbose_name='Title', max_length=255)),
                ('rating', models.PositiveIntegerField(verbose_name='Rating')),
                ('cost', models.PositiveIntegerField(verbose_name='Cost')),
                ('preparation_time', models.TimeField(verbose_name='Preparation Time')),
                ('cooking_time', models.TimeField(verbose_name='Cooking Time')),
                ('rest_time', models.TimeField(verbose_name='Rest Time')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RecipeComment',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(verbose_name='Title', max_length=75)),
                ('comment', models.CharField(verbose_name='Comment', max_length=1200)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('recipe', models.ForeignKey(to='cooking.Recipe', verbose_name='Recipe')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RecipeDifficulty',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('difficulty', models.CharField(verbose_name='Difficulty', max_length=25)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RecipePhoto',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(verbose_name='Photo', upload_to='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RecipeType',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(verbose_name='Name', max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='recipe',
            name='difficulty',
            field=models.OneToOneField(verbose_name='Difficulty', to='cooking.RecipeDifficulty'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(to='cooking.Ingredient', verbose_name='Ingredients'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recipe',
            name='photos',
            field=models.ManyToManyField(to='cooking.RecipePhoto', verbose_name='Photos'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recipe',
            name='type',
            field=models.OneToOneField(verbose_name='Type', to='cooking.RecipeType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recipe',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='User'),
            preserve_default=True,
        ),
    ]
