# Generated by Django 4.0.4 on 2022-06-01 02:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0006_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='fornecedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sistema.fornecedor'),
        ),
    ]