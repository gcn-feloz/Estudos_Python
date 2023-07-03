# Para importar funcionalidades de outros programas, podemos criar modulos e pacotes, para organizar melhor as chamadas dessas funções.
"""
O arquivo deve ser salvo na mesma pasta do programa que vai fazer a chamada:

pasta/programa_principal.py
pasta/funcao.py

E a função deve ser importada no cabeçalho do programa principal:
import funcao


"""

import funcao #Referencia o arquivo funcao.py presente na mesma pasta desse arquivo.

funcao.funcao_1() #Chama a funcao_1() do arquivo funcao.py