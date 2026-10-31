"""
imatlab.py

Matemática Discreta - IMAT
ICAI, Universidad Pontificia Comillas

Grupo: GP14
Integrantes:
    - Ana Jordán de Urries López
    - Nerea Alonso González

Descripción:
Sistema interactivo IMAT-LAB de resolución de ecuaciones en aritmética modular.

Interfaz de acceso interactivo o por lotes a la librería modular.py. Si este script se ejecuta sin par´ametros,
lanzar´a la interfaz de usuario para el modo interactivo.
"""

from typing import TextIO
import modular
import sys
from modular import IncompatibleEquationError 

def cambio_numero(numero: str, cant: int) -> int:
    numero = numero.strip(")")
    if cant == 1: 
        numero = int(numero)
        return numero
    elif cant == 2:
        num1,num2 = numero.split(",")
        num1 = int(num1)
        num2 = int(num2)
        return num1,num2
    elif cant == 3: 
        num1,num2,num3 = numero.split(",")
        num1 = int(num1)
        num2 = int(num2)
        num3 = int(num3)
        return num1,num2,num3
    elif cant == 4: 
        num1,num2,num3,num4 = numero.split(",")
        num1 = int(num1)
        num2 = int(num2)
        num3 = int(num3)
        num4 = int(num4)
        return num1,num2,num3,num4
    
def cambio_num_sist(numero:str):
    numero = numero.strip(")")
    listas = numero.split("],[")

    listas[0] = listas[0].replace("[", "")
    listas[-1] = listas[-1].replace("]", "")

    alist = []
    blist = []
    plist = []

    for lista in listas:

        a, b, p = lista.split(";")

        alist.append(int(a))
        blist.append(int(b))
        plist.append(int(p))
    return alist,blist,plist

def saber_comando(linea:str):
    linea = linea.strip()
    if linea[-1] != ")" or "(" not in linea:
        return "NOP"
    else: 
        comando,numero = linea.split("(",1)
    return comando,numero

def ejecutar_comando(linea:str):
    
    tupla= saber_comando(linea)
    if tupla != "NOP":
        comando,numero = tupla
        if comando == "primo":

            numero=cambio_numero(numero,1)
            res = modular.es_primo(numero)
            if res: 
                res = "Sí"
            elif not res: 
                res = "No"

        elif comando == "primos":

            num1,num2=cambio_numero(numero,2)
            resul = modular.lista_primos(num1,num2)
            if len(resul) == 0:
                return "NE"
            res = ""
            for i in resul: 
                i = str(i)
                res += i+", "
            
            res = res[:-2]

        elif comando == "factorizar":

            numero = cambio_numero(numero,1)
            if numero == -1 or numero == 0 or numero == 1:
                res = str(numero)
            else:
                resul = modular.factorizar(numero)
                res = ""
                for primo in resul:
                    exponente = resul[primo]
                    res += str(primo) + ": " + str(exponente) + ", "
                res = res[:-2]

        elif comando == "mcd":
            numero = numero.strip(")")
            numeros = numero.split(",")

            lista = []

            for i in numeros:
                lista.append(int(i))

            res = modular.mcd_n(lista)
            res = str(res)

        elif comando == "coprimos":

            num1,num2=cambio_numero(numero,2)
            res =modular.coprimos(num1,num2)
            if res: 
                res = "Sí"
            elif not res: 
                res = "No"

        elif comando == "pow":
            try: 
                num1,num2,num3=cambio_numero(numero,3)
                res =modular.potencia_mod_p(num1,num2,num3)
                res = str(res)
            except ZeroDivisionError:
                return "NE"

        elif comando == "inv":
            try: 
                num1,num2=cambio_numero(numero,2)
                res =modular.inversa_mod_p(num1,num2)
            except ZeroDivisionError: 
                return "NE"

        elif comando == "euler":

            numero = cambio_numero(numero,1)
            res =modular.euler(numero)

        elif comando == "legendre":
            try: 
                num1,num2=cambio_numero(numero,2)
                res =modular.legendre(num1,num2)
            except ZeroDivisionError: 
                return "NE"

        elif comando == "resolverSistema":
            try: 
                alist,blist,plist= cambio_num_sist(numero)
                resul = modular.resolver_sistema_congruencias(alist,blist,plist)
                r = resul[0]
                m = resul[1]
                res = str(r) + " (mod " + str(m) + ")"
            except IncompatibleEquationError:
                return "NE" 
        else:
            return "NOP"
        return res
    else: 
        return "NOP"

    


def run_commands(fin:TextIO,fout:TextIO):
    """ Recibe un manejador fin de un fichero de texto ya abierto para lectura y otro de un fichero de salida
    ya abierto para escritura y ejecuta línea por línea los comandos proporcionados por fin, escribiendo los resultados en fout.
    Si fin y fout no corresponden con la entrada y salida esáandar, esta función ejecuta el modo de procesamiento
    por lotes de IMAT-LAB para la entrada fin, guardando el resultado en el fichero fout.

    Args:
        fin (TextIO): Fichero de entrada. Manejador de un fichero de texto ya abierto para lectura.
        fout (TextIO): Fichero de salida. Manejador de un fichero de texto ya abierto para escritura.
    
    Returns: None
    
    Raises: None
    
    Examples:
        run_commands(sys.stdin,sys.stdout) lanza el modo interactivo y ejecuta línea por línea los comandos que
            el usuario lanza desde la entrada estándar.
    """
    modo_interactivo = fin is sys.stdin and fout is sys.stdout
    no_blanco = True
    while no_blanco: 
        if modo_interactivo: 
            linea = input("IMAT-LAB> ")
            if linea != "":
                resultado = ejecutar_comando(linea)
                print(resultado)
            else: 
                no_blanco = False

        else: 
            linea = fin.readline()
            if linea != "":
                linea = linea.rstrip("\n")
                resultado = ejecutar_comando(linea)
                resultado = str(resultado)
                fout.write(resultado + "\n")
            else: 
                no_blanco = False
        


    


        
if __name__ == "__main__":
    argumentos = sys.argv
    if len(argumentos) == 1:
        run_commands(sys.stdin, sys.stdout)

    elif len(argumentos) == 3:
        with open(argumentos[1], "r", encoding="utf-8") as fin:
            with open(argumentos[2], "w", encoding="utf-8") as fout:
                run_commands(fin, fout)

