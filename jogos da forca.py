#https://www.jdoodle.com
#Site acima é outra opção para executação online de código Python

#Jogo da Forca
import os
import getpass
import netrc
import random

def Clear():
    os.system('cls')
    print("\n" *10)

def Desintegrar(string):
    CPalavra = list()
    for c in string:
        CPalavra.append(c.upper())
    print(CPalavra)

Palavra = ""
Copia = ""
Acertos = 0
Tentat = 6
LErros = 0
Id = tam = 0
Acerto = False
Letras = ""
Letra = ""

print("\033[32m ===== JOGO DA FORCA =====\033[m")
print("\033[32m COLEGIO IRENE BRANCO!\033[m") # COR VERDE
print("\033[33m CURSO: DESENVOLVIMENTO DE SISTEMAS\033[m")
print("\033[34m TURMA 2 CD !\033[m")
print("\033[32m AULA DE LOGICA DE PROGRAMAÇÃO \033[m")
print("\033[31m Começando o Jogo \033[m")
print("\033[96m ALUNO:  \033[m")

try:
    Palavra = str(input("\033[34mDigite uma Palavra para Ocultar: \033[m")).upper()
    while Palavra.isnumeric():
        print("\033[31m > Palavra Inválida. Tente Novamente...\033[m")
        Palavra = str(input("\033[32mDigite uma Palavra para Ocultar: \033[m")).upper()
except ValueError:
    print("\033[31m > Valor Inválido.\033[m")

tam = len(Palavra)
Clear()

print("\033[32mPalavra ocultada com Sucesso!\033[m")
PalavraCóp = list()
for ele in Palavra:
    PalavraCóp.append(ele.replace(ele, '_'))

while Acertos < tam or Tentat < 6:
    print("\n\033[33mPalavra é: ", end='')
    for item in PalavraCóp:
        print(f"{item}", end=' ')
    print("\033[m")

    try:
        Letra = str(input("\n\033[34m> Digite uma Letra: \033[m")).upper()[0]
        Letras += Letra
        while Letra.isnumeric():
            print("\033[31m> Letra Inválida. Tente Novamente...\033[m")
            Letra = str(input("\n\033[34m> Digite uma Letra: \033[m")).upper()[0]
            Letras += Letra
    except ValueError():
        print("\033[31m > Valor Inválido.\033[m")

    for c, value in enumerate(Palavra):
        if value == Letra:
            print(f"\033[32m> Letra [{Letra}] encontrada com sucesso.\033[m")
            PalavraCóp[c] = Letra
            Acerto = True
            Acertos += 1

    if Acertos == tam:
        print(f"\033[92m=============== FIM ================\n"
              f"=========== Você Venceu. =========== \033[m")
        break

    if Acerto == False:
        LErros += 1
        Tentat-=1
        print(f"\033[31m > Letra [{Letra}] não encontrada. Tente Novamente...\033[m")
        print("\033[33m > Tentativas restantes: [{}].\033[m".format(Tentat))

    if Tentat == 0:
        print("\n\033[33m ========= FIM =========="
              "\n> As tentativas acabaram.\n\033[m")
        break
    Acerto = False

print(f"\033[96m => Palavra encontrada: {PalavraCóp}")
print(f" => Letras Digitadas: [{Letras}]")
print(f" => Total de Letras Digitadas: [{len(Letras)}]")
print(f" => Total de Tentativas com sucesso: [{tam}]")
print(f" => Total de Tentativas Erradas: [{LErros}]\033[m")
print("\033[92m====================================\033[m")

