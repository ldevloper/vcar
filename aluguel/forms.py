from django.forms import ModelForm
from .models import Carro, Cliente, Aluguel

class CarroForm(ModelForm):
    
    class Meta:
        model = Carro
        fields = ['placa','marca','ano','modelo','data_compra']

class ClienteForm(ModelForm):

    class Meta:
        model = Cliente
        fields = ['cpf','nome','telefone','data_nascimento','endereco']

class AluguelForm(ModelForm):
    
    class Meta:
        model = Aluguel
        fields = ['codigo','data_alugel','data_entrega','valor','devolucao','diaria','placa','cpf']