# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 06:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.CharField(max_length=2500)),
                ('post_pic', models.CharField(max_length=211)),
                ('post_date', models.DateField(blank=True, verbose_name='Blog Date')),
                ('post_time', models.TimeField(blank=True, verbose_name='Blog Time')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.CharField(max_length=1024)),
                ('profile_pic', models.CharField(max_length=211)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=211)),
                ('email', models.CharField(max_length=211)),
                ('password', models.CharField(max_length=211)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User'),
        ),
        migrations.AddField(
            model_name='post',
            name='User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User'),
        ),
    ]