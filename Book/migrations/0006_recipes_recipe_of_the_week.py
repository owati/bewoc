# Generated by Django 3.1.2 on 2020-10-24 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0005_recipes'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipes',
            name='recipe_of_the_week',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
