# Generated by Django 2.0 on 2020-01-29 04:57

from django.db import migrations, models
import polls.models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_auto_20200129_0450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image_original',
            field=models.ImageField(default='image-3.jpg', upload_to=polls.models.user_directory_path),
        ),
    ]
