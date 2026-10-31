"""
modular.py

Matemática Discreta - IMAT
ICAI, Universidad Pontificia Comillas

Grupo: GP14
Integrantes:
    - Nerea Alonso Gonzalez
    - Ana Jordan de Urries Lopez

Descripción:
Librería para la realización de cálculos y resolución de problemas de aritmética modular.
"""

from typing import Tuple, List, Dict

class IncompatibleEquationError(Exception):
    pass



def es_primo(n:int)->bool:
    """ Reciba un entero n y devuelva verdadero si es un número primo y falso en caso contrario

    Args:
        n (int): Entero
    
    Returns:
        true si el entero es un número primo.
        false en caso contrario.

    Raises: None
    
    Examples:
        es_primo(5)=True
        es_primo(4)=False
    """
    if n < 2:
        return False
    
    r = int(n**(1/2))

    for i in range(2,r+1):
        if n % i == 0: 
            return False
        
    return True


def lista_primos(a,b)-> List[int]:
    """ Recibe dos enteros a y b y devuelva la lista de números primos en el intervalo [a, b)

    Args:
        a (int): Elemento inicial del intervalo (incluido)
        b (int): Elemento final del intervalo (no incluido)
    
    Returns:
        List[int]: lista ordenada de primos mayores o iguales que a y menores que b.

    Raises: None
    
    Examples:
        lista_primos(1,11)=[2,3,5,7]
    """
    lista = []
    for i in range(a,b):
        if es_primo(i): 
            lista.append(i)
    return lista



def factorizar(n:int)-> dict[int,int]:
    """ Recibe  un entero n y devuelve un diccionario cuyas claves son los primos que dividen a n y sus valores los
    correspondientes exponentes en la descomposición en producto de factores primos de n.
    Args:
        n (int): Entero que se desea factorizar.
    
    Returns:
        factores[int,int]: Diccionario en el que las claves son primos positivos p_i que dividen a n y, para cada p_i,
            su valor asociado es el máximo exponente e_i tal que p_i^(e_i) divide a n. Si n=0, devuelve un diccionario vacío.

    Raises: None

    Examples:
        factorizar(12)={2: 2, 3: 1}
        factorizar(0)={}
    """
    if n > 1:
        if not es_primo(n):
            factores = {}

            # El dos es factor de todos los números pares por lo que lo contamos por separado:
            e = 0
            while n % 2 == 0:
                e += 1
                n = n // 2
            if e != 0:
                factores[2] = e

            raiz = int(n**(1/2))

            for i in range(3, raiz + 1, 2):
                e = 0
                while n % i == 0:
                    e += 1
                    n = n // i
                if e != 0:
                    factores[i] = e

            if n > 1:
                factores[n] = 1

            return factores
        return {n:1}
    return {}


def mcd(a:int,b:int) -> int:
    """ Calcula el máximo común divisor de dos enteros a y b.
    Args:
        a (int): Primer entero.
        b (int): Segundo entero.
    
    Returns:
        int: devuelve el máximo común divisor de a y b

    Raises: None

    Examples:
        mcd(10,15)=5
    """
    a = abs(a)
    b = abs(b)
    if a == 0 or b == 0:  
        return 0
    
    if a > b:
        a, b = b, a

    while a != 0: 
        r = b % a
        b = a
        a = r
    return b 




def bezout(a:int, b:int) -> Tuple[int,int,int]:
    """ Calcula el máximo común divisor d de dos enteros a y b junto con dos enteros x e y tales que
            d=ax+by

    Args:
        a (int): Primer entero.
        b (int): Segundo entero.
    
    Returns: (d,x,y)
        d (int): Máximo común divisor.
        x (int): Coeficiente de a.
        y (int): Coeficiente de b.

    Raises: None

    Examples:
        bezout(6,10)=(2,2,-1)
    """

    r0, r1 = a, b
    x0, x1 = 1, 0
    y0, y1 = 0, 1

    while r1 != 0:
        q = r0 // r1

        r0, r1 = r1, r0 - q*r1
        x0, x1 = x1, x0 - q*x1
        y0, y1 = y1, y0 - q*y1

    if r0 < 0:
        r0 = -r0
        x0 = -x0
        y0 = -y0

    return r0, x0, y0

def mcd_n(nlist:List[int])->int:
    """ Dados una lista de enteros, devuelve el máximo divisor común a todos ellos.
    Args:
        nList (List[int]): Lista de enteros.        
    
    Returns:
        int: devuelve el máximo entero que divide a todos los enteros de la lista.

    Raises: None

    Examples:
        mcd([4,10,14])=2
    """
    #Opcional
    d = 0
    for i in nlist:
        if d == 0:
            d = i
        else:
            d = mcd(i,d)
    return d


def bezout_n(nlist:List[int])->Tuple[int,List[int]]:
    #Opcional
    """ Dada una lista de enteros [a_1,...,a_n], devuelve el máximo divisor común d a todos ellos y una
    lista de coeficientes [x_1,...,x_n] tal que
        d=a_1*x_1+...a_n*x_n

    Args:
        nList (List[int]): Lista de enteros.        
    
    Returns: (d,X)
        d (int): Máximo entero que divide a todos los enteros de la lista.
        X (List[int]): Lista de coeficientes [x_1,...,x_n].

    Raises: None

    Examples
        bezout_n([4,10,14])=(2,[-2,1,0])
    """
    d = nlist[0]
    coef = [1]

    for i in range(1, len(nlist)):
        d_nuevo, a, b = bezout(d, nlist[i])

        for j in range(len(coef)):
            coef[j] = coef[j] * a

        coef.append(b)
        d = d_nuevo
    
    return d, coef





def coprimos(n:int,m:int)->bool:
    """ Determina si dos enteros son coprimos.
    Args:
        a (int): Primer entero.
        b (int): Segundo entero.
    
    Returns:
        bool: Verdadero si son coprimos y falso si no.

    Raises: None

    Examples:
        coprimos(14,20)=False
        coprimos(14,15)=True
    """
    if mcd(n,m) == 1:
        return True
    return False


def potencia_mod_p(base:int, exp:int, p:int) -> int:
    """ Calcula potencias módulo p.

    Args:
        base (int): Base de la potencia.
        exp (int): Exponente al que se eleva la base.
        p (int): Módulo.
    
    Returns:
        int: Resto de dividir base^exp módulo p.

    Raises:
        ZeroDivisionError: Si el módulo es 0 o si la base y el exponente
        son ambos 0 al mismo tiempo.

    Examples:
        potencia_mod_p(2,3,7)=1
    """
    if p == 0 or (base == 0 and exp == 0):
        raise ZeroDivisionError

    p = abs(p)

    base = base % p

    if exp < 0:
        base = inversa_mod_p(base, p)
        exp = -exp

    return (base ** exp) % p


def inversa_mod_p(n:int,p:int)->int:
    """ Calcula la inversa de un número n módulo p.

    Args:
        n (int): Número que se desea invertir
        p (int): Módulo.
    
    Returns:
        int: Entero x entre 0 y p-1 tal que n*x es congruente con 1 módulo p.

    Raises:
        ZeroDivisionError: Si el módulo es 0 o si n no es invertible módulo p.
    
    Examples:
        inversa_mod_p(2,7)=4
    """
    if p == 0 or mcd(n,p) != 1:
        raise ZeroDivisionError
    p = abs(p)
    n = n % p

    d, x, y = bezout(n, p)
    return x % p


def euler(n:int)->int:
    """ Calcula la función phi de Euler de un entero positivo n, es decir, cuenta cúantos enteros positivos
    menores que n son coprimos con n.

    Args:
        n (int): Número entero positivo.
    
    Returns:
        int: Función phi de Euler de n.

    Raises: None

    Examples:
        euler(7)=6
        euler(15)=8
    """
    sol = n
    p = 2

    while p**2 <= n:
        if n % p == 0:
            while n % p == 0:
                n = n // p
            sol -= sol // p

        p += 1

    if n > 1:
        sol -= sol // n

    return sol



def legendre(n:int,p:int)->int:
    """ Dado un entero n y un número primo p, calcula el símbolo de Legendre de n módulo p.

    Args:
        n (int): Número entero.
        p (int): Número primo.
    
    Returns:
        int: Símbolo de Legendre de Euler de n módulo p:
            0 si es múltiplo de p
            1 si es un cuadrado perfecto (distinto de 0), módulo p
            -1 en caso contrario.

    Raises:
        ZeroDivisionError: Si el módulo p es 0.

    Examples:
        legendre(2,5)=-1
        legendre(2,7)=1
        legendre(10,5)=0
    """
    if p == 0:
        raise ZeroDivisionError

    n = n % p

    if n == 0:
        return 0

    for i in range(1,p):
        if i**2 % p == n:
            return 1

    return -1


def resolver_sistema_congruencias(alist:List[int],blist:List[int],plist:List[int])->Tuple[int,int]:
    """ Dadas tres listas de números enteros [a_1,...,a_n], [b_1,...,b_n] y [p_1,...,p_n], resuelve el sistema de congruencias
    
    a_i * x = b_i (mod p_i)   i=1,...,n
    
    devolviendo un entero r y un módulo m tales que las soluciones del sistema corresponden a todos los enteros
    x congruentes con r módulo m.

    Args:
        alist (List[int]): Lista de coeficientes de la variable x, [a_1,...,a_n].
        blist (List[int]): Lista de términos independientes [b_1,...,b_n].
        plist (List[int]): Lista de módulos [p_1,...,p_n]
    
    Returns: (r,m)
        r (int): Entero entre 0 y m-1.
        m (int): Entero positivo, módulo de la solución.

    Raises:
        IncompatibleEquationError: Si no es posible resolver el sistema.

    Examples:
        resolver_sistema_congruencias([2],[3],[5]])=(4,5)
        resolver_sistema_congruencias([2],[4],[6])=(2,3)
        resolver_sistema_congruencias([1,4],[1,7],[3,11])=(10,33)
    """
    if len(alist) != len(blist) or len(blist) != len(plist):
        raise IncompatibleEquationError
    l = len(plist)
    #Simplificación
    for j in range(l):
        d = mcd(alist[j], plist[j])
        # Si d no divide a b, la ecuación es incompatible
        if blist[j] % d != 0:
            raise IncompatibleEquationError
        alist[j] = alist[j] // d
        blist[j] = blist[j] // d
        plist[j] = plist[j] // d
        inv = inversa_mod_p(alist[j], plist[j])

        blist[j] = (blist[j] * inv) % plist[j]
        alist[j] = 1
    #Comprobamos compatibilidad entre congruencias
    for i in range(l):
        for j in range(i + 1, l):

            d = mcd(plist[i], plist[j])

            if (blist[i] - blist[j]) % d != 0:
                raise IncompatibleEquationError
    #Teorema chino del resto
    m = 1
    for p in plist:
        m = m * p
    suma = 0
    for k in range(l):
        n = m // plist[k]
        try:
            x = inversa_mod_p(n, plist[k])

        except ZeroDivisionError:
            raise IncompatibleEquationError

        suma += blist[k] * x * n
    return suma % m, m





def raiz_mod_p(n:int,p:int)->int:
    """ Encuentra, si existe, una raíz cuadrada para un entero n módulo un número primo p.

    Args:
        n (int): Entero del que se desea hallar la raíz.
        p (int): Módulo. Se asume que es un número primo.
    
    Returns:
        int: Entero x entre 0 y p-1 tal que x^2 = n (mod p).

    Raises:
        IncompatibleEquationError: Si no es posible hallar dicha raíz.

    Examples:
        raiz_mod_p(2,7)=3
    """
    #Opcional
    pass


def ecuacion_cuadratica(a:int,b:int,c:int,p:int)->Tuple[int,int]:
    """ Halla, si es posible, las dos posibles soluciones de la ecuación cuadrática ax^2+bx+c=0 (mod p).
    Devuelve una tupla con las dos raíces (distintas o una misma raíz repetida en caso de ser doble).

    Args:
        a (int): Coeficiente de x^2.
        b (int): Coeficiente de x.
        c (int): Término independiente.
        p (int): Módulo. Se asume que es un número primo.
    
    Returns: (x1,x2)
        x1 (int): Primera solución. Entero entre 0 y p-1.
        x2 (int): Segunda solución. Entero entre 0 y p-1.

    Raises:
        IncompatibleEquationError: Si no es posible resolver la ecuación.

    Examples:
        ecuacion_cuadratica(4,1,3,11)
        ecuacion_cuadratica(4,1,5,11)=(3, 5)
        ecuacion_cuadratica(1,2,1,11)=(10,10)
    """
    #Opcional
    pass



