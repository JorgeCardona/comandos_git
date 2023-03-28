def suma(x, y):
    
    resultado =  x + y
    print(f'el resultado de la SUMA {x} + {y} es {resultado}')

def resta(x, y):
    
    resultado =  x - y
    print(f'el resultado de la RESTA  {x} - {y}es {resultado}')

def multiplicacion(x, y):
    
    resultado =  x * y
    print(f'el resultado de la MULTIPLICACION  {x} * {y} es {resultado}')

def division_decimal(x, y):
    
    resultado =  x / y
    print(f'el resultado de la DIVISION DECIMAL {x} / {y} es {resultado}')

def division_entera(x, y):
    
    resultado =  x // y
    print(f'el resultado de la DIVISION ENTERA {x} // {y} es {resultado}')

def potencia(x, y):
    
    resultado =  x ** y
    print(f'el resultado de la POTENCIA  {x} elevado a {y} es {resultado}')
 
def raiz_cuadrada(x, y):
    import math
    
    resultado =  math.sqrt(abs(x + y))
    print(f'el resultado de la raiz cuadrada del valor absoluto de {x} + {y} es {resultado}')

def logaritmo(x, y):
    import math
    
    resultado = math.log(abs(x), abs(y))
    print(f'el logaritmo del valor absoluto de {x} en base {y} es {resultado}')
                      
def ejecutar_funciones():
    
    x, y = 7, 0
    suma(x, y)
    resta(x, y)
    multiplicacion(x, y)
    division_decimal(x, y)
    division_entera(x, y)
    potencia(x, y)
    raiz_cuadrada(x, y)
    logaritmo(x, y)
                       
if __name__ == "__main__":
    ejecutar_funciones()