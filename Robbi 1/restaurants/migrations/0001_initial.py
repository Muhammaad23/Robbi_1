# Generated by Django 5.1.3 on 2024-11-20 10:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Menu",
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
                ("image", models.ImageField(upload_to="menus/")),
                ("title", models.CharField(max_length=100)),
                (
                    "price",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Restoran_malumotlari",
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
                ("jop_time", models.CharField(max_length=50)),
                ("address", models.CharField(max_length=255)),
                ("latitude", models.FloatField(blank=True, null=True)),
                ("longitude", models.FloatField(blank=True, null=True)),
                ("info", models.TextField()),
                (
                    "tel",
                    models.CharField(
                        blank=True,
                        max_length=20,
                        null=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Enter a valid phone number. Allowed formats: +1234567890, +1 234 567 890, etc.",
                                regex="^\\+?[0-9\\s\\-\\(\\)]{9,20}$",
                            )
                        ],
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Restoranlar",
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
                ("title", models.CharField(max_length=100)),
                ("jop_time", models.CharField(max_length=50)),
                ("image", models.ImageField(upload_to="images/")),
                ("address", models.CharField(max_length=255)),
                ("latitude", models.FloatField(blank=True, null=True)),
                ("longitude", models.FloatField(blank=True, null=True)),
            ],
        ),
    ]