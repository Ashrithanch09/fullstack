# Generated by Django 5.0.2 on 2024-06-19 11:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("chat", "0002_conversation_summary"),
    ]

    operations = [
        migrations.CreateModel(
            name="File",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=255)),
                ("path", models.CharField(max_length=255)),
                ("hash", models.CharField(max_length=32, unique=True)),
                ("uploaded_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
