# Generated by Django 5.0.3 on 2024-03-06 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_produit_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='static/media/produits'),
        ),
    ]
