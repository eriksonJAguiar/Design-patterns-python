# -*- coding: UTF-8 -*-

from impostos import ICMS, ISS

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
    from orcamento import Orcamento
    calculador = Calulador_de_impostos()
    orcamento = Orcamento(500)
    
    #version 1 
    # calculador.realiza_calculo(orcamento,'ISS')
    # calculador.realiza_calculo(orcamento,'ICMS')

    #Strategy em python - Passar a função por paramêtro
    calculador.realiza_calculo(orcamento, ISS())
    calculador.realiza_calculo(orcamento, ICMS())