from django.forms import ModelForm
from .models import Carro,Cliente,Aluguel

class CarroForm(ModelForm):
    model = Carro
    fields = ['placa','marca','ano','modelo','data_compra']

class ClienteForm(ModelForm):
    model = Cliente
    fields = ['cpf','nome','telefone','data_nascimento','endereco']

class AlugelForm(ModelForm):
    model = Aluguel
    fields = ['codigo','data_alugel','data_entrega','diaria','placa','cpf']