# Generated by Django 4.1.6 on 2023-03-18 11:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shopapp", "0010_productimage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
        #     name="description",
        #     field=models.CharField(blank=True, db_index=True, max_length=200),
        # ),
        # migrations.AlterField(
        #     model_name="product",
            name="name",
            field=models.CharField(db_index=True, max_length=100),
        ),
    ]
