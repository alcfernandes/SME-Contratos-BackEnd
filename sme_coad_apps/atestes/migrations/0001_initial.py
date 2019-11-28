# Generated by Django 2.2.4 on 2019-11-28 17:43

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GrupoVerificacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('alterado_em', models.DateTimeField(auto_now=True, verbose_name='Alterado em')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('nome', models.CharField(max_length=100, verbose_name='Nome do Grupo')),
            ],
            options={
                'verbose_name': 'Grupo de Verificacao',
                'verbose_name_plural': 'Grupos de verificação',
            },
        ),
        migrations.CreateModel(
            name='ModeloAteste',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('alterado_em', models.DateTimeField(auto_now=True, verbose_name='Alterado em')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('titulo', models.CharField(max_length=100, verbose_name='Titulo do Modelo')),
            ],
            options={
                'verbose_name': 'Modelo de Ateste',
                'verbose_name_plural': 'Modelos de Atestes',
            },
        ),
        migrations.CreateModel(
            name='ItensVerificacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('alterado_em', models.DateTimeField(auto_now=True, verbose_name='Alterado em')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('item', models.SmallIntegerField(default=0, verbose_name='Item')),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grupo_verificacao', to='atestes.GrupoVerificacao')),
            ],
            options={
                'verbose_name': 'Item de Verificação',
                'verbose_name_plural': 'Itens de Verificação',
            },
        ),
        migrations.AddField(
            model_name='grupoverificacao',
            name='modelo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modelo_ateste', to='atestes.ModeloAteste'),
        ),
    ]
