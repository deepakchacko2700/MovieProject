# Generated by Django 4.1.4 on 2022-12-17 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='exit', upload_to='Gallery'),
            preserve_default=False,
        ),
    ]
