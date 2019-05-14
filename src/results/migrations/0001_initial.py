# Generated by Django 2.1.7 on 2019-05-08 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.IntegerField(help_text='The id of the task relative to the result')),
                ('started', models.DateTimeField(help_text='The time the task started')),
                ('finished', models.DateTimeField(help_text='The time the task finished')),
                ('duration', models.DurationField(help_text='Task duration in seconds')),
                ('result', models.CharField(choices=[(1, 'success'), (2, 'failure')], help_text='"success" or "failure"', max_length=7)),
                ('detail', models.CharField(blank=True, help_text='Arbitrary detail string', max_length=512)),
                ('schedule_entry', models.ForeignKey(help_text='The schedule entry relative to the result', on_delete=django.db.models.deletion.CASCADE, related_name='results', to='schedule.ScheduleEntry')),
            ],
            options={
                'ordering': ('task_id',),
            },
        ),
        migrations.AlterUniqueTogether(
            name='taskresult',
            unique_together={('schedule_entry', 'task_id')},
        ),
    ]
