# Generated by Django 5.0.3 on 2024-03-04 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=128)),
                ('prix', models.FloatField(default=0.0)),
                ('quantite', models.IntegerField(default=0)),
                ('description', models.TextField(blank=True)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='produits')),
            ],
        ),
    ]
