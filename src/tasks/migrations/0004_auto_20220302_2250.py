# Generated by Django 3.1.14 on 2022-03-02 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0003_auto_20220302_1504"),
    ]

    operations = [
        migrations.AlterField(
            model_name="taskresult",
            name="status",
            field=models.CharField(
                choices=[
                    (1, "success"),
                    (2, "failure"),
                    (3, "in-progress"),
                    (4, "notification_failed"),
                ],
                default="in-progress",
                help_text='"success", "failure", or "notification_failed"',
                max_length=19,
            ),
        ),
    ]
