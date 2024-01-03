# Generated by Django 5.0 on 2024-01-03 17:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("community", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="board",
            name="writer",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="작성자",
            ),
        ),
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(
                max_length=250, unique=True, verbose_name="category"
            ),
        ),
    ]
