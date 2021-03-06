# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-14 18:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djcloudbridge', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aws',
            name='compute',
        ),
        migrations.RemoveField(
            model_name='aws',
            name='object_store',
        ),
        migrations.AddField(
            model_name='aws',
            name='ec2_endpoint_url',
            field=models.CharField(default='https://ec2.us-east-1.amazonaws.com', max_length=255, verbose_name='EC2 endpoint url'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aws',
            name='ec2_is_secure',
            field=models.BooleanField(default=True, verbose_name='EC2 is secure'),
        ),
        migrations.AddField(
            model_name='aws',
            name='ec2_validate_certs',
            field=models.BooleanField(default=True, verbose_name='EC2 validate certificates'),
        ),
        migrations.AddField(
            model_name='aws',
            name='region_name',
            field=models.CharField(default='us-east-1', max_length=100, verbose_name='AWS region name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aws',
            name='s3_endpoint_url',
            field=models.CharField(default='https://s3.amazonaws.com', max_length=255, verbose_name='S3 endpoint url'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aws',
            name='s3_is_secure',
            field=models.BooleanField(default=True, verbose_name='S3 is secure'),
        ),
        migrations.AddField(
            model_name='aws',
            name='s3_validate_certs',
            field=models.BooleanField(default=True, verbose_name='S3 validate certificates'),
        ),
        migrations.DeleteModel(
            name='EC2',
        ),
        migrations.DeleteModel(
            name='S3',
        ),
    ]
