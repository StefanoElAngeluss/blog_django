# Generated by Django 5.0.3 on 2024-04-28 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_alter_musique_fichier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musique',
            name='fichier',
            field=models.FileField(upload_to='sons'),
        ),
    ]
