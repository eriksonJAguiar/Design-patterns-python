# -*- coding: UTF-8 -*-

# Design Patterns Decorator

# Modulo para classe abstrata 
from abc import ABCMeta, abstractmethod

#classe abstrata
class Imposto(object):
    def __init__(self,outro_imposto = None):
        self.__outro_imposto = outro_imposto
    
    def calculo_do_outro_imposto(self,orcamento):
        if self.__outro_imposto is None:
            return 0
        
        return self.__outro_imposto.calcula(orcamento)

    @abstractmethod
    def calcula(self,orcamento):
        pass

class Template_imposto_condicional(Imposto):
    
    #classe abstrata -- indicador
    __metaclass__ = ABCMeta
    
    def calcula(self, orcamento):
        if self.deve_usar_maxima_taxacao(orcamento):
            return self.maxima_taxacao(orcamento) + self.calculo_do_outro_imposto(orcamento)
        else:
            return self.minima_taxacao(orcamento) + self.calculo_do_outro_imposto(orcamento)
    
    #Obriga implementar este método
    @abstractmethod
    def deve_usar_maxima_taxacao(self,orcamento):
        pass
    
    @abstractmethod
    def maxima_taxacao(self,orcamento):
        pass
    
    @abstractmethod
    def minima_taxacao(self,orcamento):
        pass

#funcao decorator
def IPVX(metodo_ou_funcao):
    def wrapper(self,orcamento):
        return metodo_ou_funcao(self, orcamento) + 50
    
    return wrapper


class ISS(Imposto):
    #Decorator padrao do Python, o complicado que o mesmo não é 
    # flexivel
    @IPVX
    def calcula(self, orcamento):
        return (orcamento.valor * 0.1) + self.calculo_do_outro_imposto(orcamento)


class ICMS(Imposto):
    
    def calcula(self, orcamento):
        return (orcamento.valor*0.06) + self.calculo_do_outro_imposto(orcamento)

class ICPP(Template_imposto_condicional):
    
    def deve_usar_maxima_taxacao(self,orcamento):
        return orcamento.valor > 500
    
    
    def maxima_taxacao(self,orcamento):
        return orcamento.valor * 0.07
    
    
    def minima_taxacao(self,orcamento):
        return orcamento.valor * 0.05
    

class ICKV(Template_imposto_condicional):
    
    def __tem_item_maior_que_100_reais(self,orcamento):
        for it in orcamento.obter_itens():
            if it.valor > 100:
                return True
        
        return False
    
    def deve_usar_maxima_taxacao(self,orcamento):
        return orcamento.valor > 500 and self.__tem_item_maior_que_100_reais(orcamento)
           
    def maxima_taxacao(self,orcamento):
        return orcamento.valor*0.1
     
    def minima_taxacao(self,orcamento):
        return orcamento.valor*0.06