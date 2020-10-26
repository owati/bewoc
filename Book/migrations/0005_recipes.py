# Generated by Django 3.1.2 on 2020-10-23 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0004_files_image_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('steps', models.TextField()),
                ('image', models.FileField(upload_to='static')),
            ],
        ),
    ]