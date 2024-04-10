# Generated by Django 5.0.3 on 2024-03-21 10:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_alter_article_categorie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='categorie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categorie_articles', to='blog.categorie'),
        ),
    ]
