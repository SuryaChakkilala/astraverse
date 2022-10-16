# Generated by Django 4.1.1 on 2022-10-14 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0003_hospitaluse"),
    ]

    operations = [
        migrations.CreateModel(
            name="DonationRequest",
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
                ("blood_group", models.CharField(max_length=50)),
                ("satisfied", models.BooleanField(default=False)),
                ("time_of_request", models.DateTimeField(auto_now_add=True)),
                (
                    "hospital",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="pages.hospital"
                    ),
                ),
            ],
        ),
    ]