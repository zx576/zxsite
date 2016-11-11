# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-08 07:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='标题')),
                ('content', models.TextField(verbose_name='正文')),
                ('abstract', models.CharField(max_length=50, verbose_name='摘要')),
                ('status', models.CharField(choices=[('P', 'PUBLIC'), ('E', 'EDITING'), ('D', 'DELETED')], max_length=1, verbose_name='文章状态')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('lasted_modified_time', models.DateTimeField(auto_now=True, verbose_name='最新修改时间')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='浏览数')),
                ('likes', models.PositiveIntegerField(default=0, verbose_name='点赞数')),
                ('topped', models.BooleanField(default=False, verbose_name='是否置顶')),
            ],
        ),
        migrations.CreateModel(
            name='Bloger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.PositiveIntegerField(default=0)),
                ('gender', models.CharField(choices=[('F', 'FEMALE'), ('M', 'MALE')], max_length=5)),
                ('signiture', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='评论内容')),
                ('status', models.CharField(choices=[('P', 'PUBLIC'), ('D', 'DELETE')], max_length=1)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('likes', models.PositiveIntegerField(default=0)),
                ('topped', models.BooleanField(default=False, verbose_name='是否置顶')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bodypage.Article', verbose_name='对应文章')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bodypage.Bloger', verbose_name='作者')),
            ],
        ),
        migrations.CreateModel(
            name='Subcomment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='评论内容')),
                ('status', models.CharField(choices=[('P', 'PUBLIC'), ('D', 'DELETE')], max_length=1)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bodypage.Bloger', verbose_name='作者')),
                ('parent_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bodypage.Comment', verbose_name='评论')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='标签名')),
                ('status', models.CharField(choices=[('P', 'PUBLIC'), ('D', 'DELETE')], max_length=1)),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('related_articles', models.PositiveIntegerField(verbose_name='相关文章数')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bodypage.Bloger', verbose_name='作者'),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(to='bodypage.Tag', verbose_name='标签'),
        ),
    ]