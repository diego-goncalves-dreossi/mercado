# Generated by Django 4.0.4 on 2022-06-01 02:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0003_filial_fornecedor_pedido_delete_formapagamento_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='qntnovosprods',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='produto',
            name='fornecedor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='sistema.fornecedor'),
        ),
    ]