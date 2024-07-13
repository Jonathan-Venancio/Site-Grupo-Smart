from django.db import models

# Create your models here.

#cliente
    #nome
    #email
    #telefone
    #usuario

#produto
    #imagem
    #nome
    #preço
    #ativo
    #categoria
    #tipo

#categorias (HP, Epson, Canon, Brother, Material de escritório, Gaming, Computadores)
    #nome


#tipos (Compativeis, originais, toners, )
    #nome

#itemestoque
    #produto
    #cor ()
    #tamanho
    #quantidade


#ItensPedido
    #itemestoque
    #quantidade

#pedidos
    #cliente
    #data_finalização
    #finalizado
    #id_transacao
    #endereco
    #itenspedido

#endereço
    #rua
    #numero
    #complemento
    #cep
    #cidade
    #estado
    #cliente