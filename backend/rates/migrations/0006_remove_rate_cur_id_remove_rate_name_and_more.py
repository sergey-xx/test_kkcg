# Generated by Django 4.1.13 on 2024-02-15 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("rates", "0005_rename_char_code_rate_charcode"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="rate",
            name="cur_id",
        ),
        migrations.RemoveField(
            model_name="rate",
            name="name",
        ),
        migrations.RemoveField(
            model_name="rate",
            name="nominal",
        ),
        migrations.RemoveField(
            model_name="rate",
            name="num_code",
        ),
        migrations.RemoveField(
            model_name="rate",
            name="previous",
        ),
    ]
