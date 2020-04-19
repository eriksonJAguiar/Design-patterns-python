# -*- coding: UTF-8 -*-

class Orcamento(object):

    def __init__(self, valor):
        #vibilidade privado
        self.__valor = valor
    

    #Property
    @property
    def valor(self):
        return self.__valor