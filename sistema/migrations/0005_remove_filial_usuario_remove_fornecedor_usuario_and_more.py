# Generated by Django 4.0.4 on 2022-06-01 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0004_pedido_qntnovosprods_produto_fornecedor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filial',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='fornecedor',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='filial',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='fornecedor',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='produto',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='fornecedor',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.DeleteModel(
            name='Filial',
        ),
        migrations.DeleteModel(
            name='Fornecedor',
        ),
        migrations.DeleteModel(
            name='Pedido',
        ),
        migrations.DeleteModel(
            name='Produto',
        ),
    ]
