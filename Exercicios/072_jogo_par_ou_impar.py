from random import randint
entrada = 1
numero = 1
pontos = 0
numero_pc = 0
pontos_pc = 0
par_impar = 0
resultado = bool()

print("-="*50)
print("++++++++++++++++++++ JOGO ++++++++++++++++++++".center(100))
print("+--PLACAR---+","---------- [PAR OU IMPAR] ----------".center(70))
print(f"|Jogador: {pontos:2}|","Escolha um valor, e depois chute se a soma do seu".center(75))
print(f"|Comput.: {pontos_pc:2}|","numero, mais, o do computador, vai dar par, ou impar.".center(75))
print("-="*50)




def verifica_int(dados):
    try:
        int(entrada)
        return True
    except ValueError:
        return False

def define_jogada():
    global numero, par_impar, entrada
    while True:
        entrada = input("Escolha um numero ou [0]-sair: ")
        if verifica_int(entrada):
            numero = int(entrada)
            break
    if numero >= 1:
        while True:
            entrada = input("[0]-PAR ou [1]-IMPAR? ")
            if verifica_int(entrada) and entrada in ['0','1']:
                par_impar = int(entrada)
                break

while numero > 0:
    define_jogada()
    if numero >= 1:
        numero_pc = randint(0,10)
        print()
        print(" 1... 2... 3... VALENDO! ".center(25, '-'))
        print()
        print(f"Jogador: [{numero} + {numero_pc}] :Computador")
        print(f"Total: {numero+numero_pc}".center(25))
        resultado = (numero+numero_pc) %2
        if resultado:
            print("[IMPAR]".center(25))
        else:
            print("[PAR]".center(25))
        print()
        
        if resultado == par_impar:
            pontos += 1
            print("[Você ganhou!]")
        else:
            pontos_pc += 1
            print("[Você perdeu!]")
    print("-"*25)
    print(f"PLACAR")
    print(f"Jogador: {pontos}  X  Comput.: {pontos_pc}")
    print("-"*25)

print()
print("-="*50)

