# Generated by Django 4.1.7 on 2023-02-28 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=7)),
                ('marca', models.CharField(max_length=150)),
                ('ano', models.DateField()),
                ('modelo', models.CharField(max_length=150)),
                ('data_compra', models.DateField()),
            ],
        ),
    ]
