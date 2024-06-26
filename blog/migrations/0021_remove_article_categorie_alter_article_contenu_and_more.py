# Generated by Django 5.0.3 on 2024-03-27 23:45

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_alter_commentaire_auteur'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='categorie',
        ),
        migrations.AlterField(
            model_name='article',
            name='contenu',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AddField(
            model_name='article',
            name='categorie',
            field=models.ManyToManyField(to='blog.categorie'),
        ),
    ]
