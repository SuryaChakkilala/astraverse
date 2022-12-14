# Generated by Django 4.1.1 on 2022-10-14 14:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("pages", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="HospitalDonation",
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
                ("time_of_donation", models.DateTimeField(auto_now_add=True)),
                (
                    "donor",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "hospital",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="pages.hospital",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(name="Donation",),
    ]
