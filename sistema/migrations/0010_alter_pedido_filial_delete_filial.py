# Generated by Django 4.0.4 on 2022-06-03 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0009_alter_pedido_fornecedor_alter_produto_fornecedor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='filial',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='Filial',
        ),
    ]
