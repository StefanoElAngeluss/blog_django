# Generated by Django 5.0.3 on 2024-03-18 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_article_publier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(default=1, max_length=128),
            preserve_default=False,
        ),
    ]
