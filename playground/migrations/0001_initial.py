# Generated by Django 5.0 on 2024-01-03 13:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=90)),
                ("category", models.TextField(blank=True, null=True)),
                ("card_image", models.ImageField(upload_to="books/")),
                (
                    "profile_image",
                    models.ImageField(blank=True, null=True, upload_to="profiles/"),
                ),
                ("prologue", models.TextField(blank=True, null=True)),
                ("year_of_life", models.TextField(blank=True, null=True)),
                ("quiz", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Episodes",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "episode_number",
                    models.PositiveIntegerField(default=1, help_text="에피소드 번호"),
                ),
                (
                    "scene_number",
                    models.PositiveIntegerField(default=1, help_text="장면 번호"),
                ),
                (
                    "title",
                    models.CharField(default=None, help_text="에피소드 이름", max_length=30),
                ),
                (
                    "image",
                    models.ImageField(
                        default=None, help_text="에피소드 장면 이미지", upload_to="contents/"
                    ),
                ),
                (
                    "voice",
                    models.FileField(
                        default=None, help_text="기본음성", upload_to="voices/"
                    ),
                ),
                (
                    "voice_text",
                    models.CharField(
                        default=None, help_text="음성 대사 텍스트", max_length=100
                    ),
                ),
                (
                    "image_segment",
                    models.ImageField(
                        default=None, help_text="인물 테두리 이미지", upload_to="contents/"
                    ),
                ),
                (
                    "x_index",
                    models.IntegerField(default=0, help_text="css right 에 들어갈 x 값"),
                ),
                (
                    "y_index",
                    models.IntegerField(default=0, help_text="css top 에 들어갈 y 값"),
                ),
                (
                    "height",
                    models.IntegerField(default=0, help_text="css height에 들어갈 높이값"),
                ),
                (
                    "width",
                    models.IntegerField(default=0, help_text="css width에 들어갈 넓이값"),
                ),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="episodes",
                        to="playground.book",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Quiz",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quiz_index", models.IntegerField(default=None)),
                (
                    "quiz_text",
                    models.CharField(
                        default=None, help_text="퀴즈 문제 내용", max_length=1000
                    ),
                ),
                (
                    "quiz_answer",
                    models.CharField(
                        default=None, help_text="퀴즈 문제 정답", max_length=100
                    ),
                ),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="quizzes",
                        to="playground.book",
                    ),
                ),
            ],
        ),
    ]
