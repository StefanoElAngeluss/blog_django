# Generated by Django 5.0.3 on 2024-03-19 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_article_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name_plural': 'Articles'},
        ),
    ]