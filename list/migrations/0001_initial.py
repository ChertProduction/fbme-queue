# Generated by Django 3.2.5 on 2021-07-19 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admins',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('tg_id', models.IntegerField(blank=True, null=True)),
                ('username', models.CharField(blank=True, max_length=200, null=True)),
                ('spec', models.CharField(blank=True, max_length=200, null=True)),
                ('super', models.BooleanField(blank=True, null=True)),
                ('fullname', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'admins',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Gifs',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('gif_id', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'gifs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('tg_id', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('text', models.CharField(blank=True, max_length=5000, null=True)),
                ('command', models.CharField(blank=True, max_length=200, null=True)),
                ('command_description', models.CharField(blank=True, max_length=200, null=True)),
                ('disable_web_page_preview', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'db_table': 'links',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Texts',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('text_name', models.CharField(blank=True, max_length=200, null=True)),
                ('text_title', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'db_table': 'texts',
                'managed': False,
            },
        ),
    ]
