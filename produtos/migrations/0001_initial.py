# Generated by Django 4.0.4 on 2022-06-03 03:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categorias', '0001_initial'),
        ('autenticacao', '0001_initial'),
        ('fornecedores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('preco', models.FloatField()),
                ('descricao', models.TextField()),
                ('img', models.ImageField(blank=True, null=True, upload_to='produtos')),
                ('estoque', models.IntegerField(default=0)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='categorias.categoria')),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='fornecedores.fornecedor')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='autenticacao.usuario')),
            ],
        ),
    ]