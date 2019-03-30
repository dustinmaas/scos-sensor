# Generated by Django 2.1.7 on 2019-03-30 06:18

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acquisition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.IntegerField(help_text='The id of the task relative to the acquisition')),
                ('sigmf_metadata', jsonfield.fields.JSONField(help_text='The sigmf meta data for the acquisition')),
                ('data', models.BinaryField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True, help_text='The time the acquisition was created')),
            ],
            options={
                'db_table': 'acquisitions',
                'ordering': ('created',),
            },
        ),
    ]
