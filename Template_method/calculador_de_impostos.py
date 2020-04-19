# -*- coding: UTF-8 -*-

from impostos import ICMS, ISS, ICPP,ICKV

class Calulador_de_impostos(object):
    
    def realiza_calculo(self,orcamento, imposto):
        
        #versao 1
        # if imposto == 'ISS':
        #     imposto_calculado = calcula_ISS(orcamento)
        # elif imposto == 'ICMS':
        #     imposto_calculado = calcula_ICMS(orcamento)

        imposto_calculado = imposto.calcula(orcamento)

        print(imposto_calculado)


if __name__ == "__main__":
    from orcamento import Orcamento, Item

    orcamento = Orcamento()
    calculador = Calulador_de_impostos()
    orcamento.adiciona_item(Item('Item A', 100.0))
    orcamento.adiciona_item(Item('Item B', 50.0))
    orcamento.adiciona_item(Item('Item C', 400.0))
    

    print("ISS e ICMC")
    calculador.realiza_calculo(orcamento, ISS())
    calculador.realiza_calculo(orcamento, ICMS())

    print("ICPP e ICKV")
    calculador.realiza_calculo(orcamento, ICPP())
    calculador.realiza_calculo(orcamento, ICKV())