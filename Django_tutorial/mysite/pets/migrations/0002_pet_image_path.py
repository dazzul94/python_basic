# Generated by Django 2.2.4 on 2019-10-03 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='image_path',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
