# Generated by Django 4.1 on 2022-09-05 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="group",
            field=models.CharField(
                choices=[("D", "D"), ("C", "C"), ("B", "B"), ("A", "A")],
                max_length=6,
                null=True,
                verbose_name="그룹",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="level",
            field=models.CharField(
                choices=[("3", "참여자"), ("2", "기획단"), ("1", "관리자"), ("0", "개발자")],
                default=3,
                max_length=18,
                verbose_name="등급",
            ),
        ),
    ]
