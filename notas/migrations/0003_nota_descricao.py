# Generated by Django 5.0.6 on 2024-06-17 15:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("notas", "0002_alter_nota_quantidade"),
    ]

    operations = [
        migrations.AddField(
            model_name="nota",
            name="descricao",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]