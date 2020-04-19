# -*- coding: UTF-8 -*-

# Template methodo - obriga a classe a implementar o método da
#  classe abstrata

# Modulo para classe abstrata 
from abc import ABCMeta, abstractmethod

#classe abstrata
class Template_imposto_condicional(object):
    
    #classe abstrata -- indicador
    __metaclass__ = ABCMeta
    
    def calcula(self, orcamento):
        if self.deve_usar_maxima_taxacao(orcamento):
            return self.maxima_taxacao(orcamento)
        else:
            return self.minima_taxacao(orcamento)
    
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

class ISS(object):
    
    def calcula(self, orcamento):
        return orcamento.valor * 0.1


class ICMS(object):
    
    def calcula(self, orcamento):
        return orcamento.valor*0.06

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