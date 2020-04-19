# -*- coding: UTF-8 -*-

from datetime import date

'''
    Padrao de projeto Observer
    Pode ser aplicado quando o acoplamento da nossa classe está crescendo, 
    ou quando temos diversas ações diferentes a serem executadas após um 
    determinado processo. Além disso, Ele permite que diversas ações 
    sejam executadas de forma transparente à classe principal.
'''

class Item(object): 

    def __init__(self, descricao, valor):
        self.__descricao = descricao
        self.__valor = valor

    @property
    def descricao(self):
        return self.__descricao

    @property
    def valor(self):
        return self.__valor


class Nota_fiscal(object):
    #parametros opcionais e devem sem os ultimo
    def __init__(self, razao_social, cnpj, itens, data_de_emissao=date.today(), detalhes='', observadores=[]):
        self.__razao_social = razao_social
        self.__cnpj = cnpj
        self.__data_de_emissao = data_de_emissao
        if len(detalhes) > 20:
            raise Exception(
                'Detalhes da nota não pode ter mais do que 20 caracteres')
        self.__detalhes = detalhes
        self.__itens = itens

       
        for observador in observadores:
           observador(self)


    @property
    def razao_social(self):
        return self.__razao_social

    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def data_de_emissao(self):
        return self.__data_de_emissao

    @property
    def detalhes(self):
        return self.__detalhes


if __name__ == '__main__':
    from criador_de_nota_fiscal import Criador_de_nota_fiscal
    from observadores import imprime,envia_por_email,salva_no_banco
    itens = [
        Item(
            'ITEM A',
            100
        ),
        Item(
            'ITEM B',
            200
        )
    ]
    #Parametros nomeados
    nota_fiscal = Nota_fiscal(
        cnpj='012345678901234',
        razao_social='FHSA Limitada',
        itens=itens,
        data_de_emissao=date.today(),
        detalhes='',
        observadores=[imprime,envia_por_email,salva_no_banco]
    )


