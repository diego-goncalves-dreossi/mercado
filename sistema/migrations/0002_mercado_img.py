# Generated by Django 4.0.4 on 2022-05-29 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mercado',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='mercados'),
        ),
    ]