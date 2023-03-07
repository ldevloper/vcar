# Generated by Django 4.1.7 on 2023-03-06 23:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aluguel', '0004_alter_carro_ano'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluguel',
            name='devolucao',
            field=models.BooleanField(default=False, verbose_name='Devolvido'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aluguel',
            name='valor',
            field=models.DecimalField(decimal_places=2, default=False, max_digits=15, verbose_name='Valor'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aluguel',
            name='cpf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='cliente_alugueis', to='aluguel.cliente'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nome',
            field=models.CharField(max_length=250, verbose_name='Nome'),
        ),
    ]