# Generated by Django 5.0.3 on 2024-04-28 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_alter_musique_fichier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musique',
            name='fichier',
            field=models.FileField(upload_to='sons/'),
        ),
    ]