# Generated by Django 4.0.4 on 2022-06-01 04:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0001_initial'),
        ('sistema', '0007_alter_produto_fornecedor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='categorias.categoria'),
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
    ]
