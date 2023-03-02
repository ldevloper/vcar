from django.db import models

# Create your models here.
class Carro(models.Model):
    placa = models.CharField(max_length=7, primary_key=True)
    marca = models.CharField(max_length=150)
    ano = models.CharField(max_length=7)
    modelo = models.CharField(max_length=150)
    data_compra = models.DateField()

    def __str__(self):
        return self.modelo

class Cliente(models.Model):
    cpf = models.CharField(max_length=15, primary_key=True)
    nome = models.CharField(max_length=250)
    telefone = models.CharField(max_length=50)
    data_nascimento = models.DateField()
    endereco = models.CharField(max_length=150)

    def __str__(self):
        return self.nome

class Aluguel(models.Model):
    codigo = models.AutoField(primary_key=True, unique=True)
    data_alugel = models.DateField()
    data_entrega = models.DateField()
    diaria = models.DecimalField(max_digits=10, decimal_places=2)
    placa = models.ForeignKey(Carro, on_delete=models.CASCADE)
    cpf = models.ForeignKey(Cliente, on_delete=models.CASCADE)