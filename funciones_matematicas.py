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
             
def ejecutar_funciones():
    
    x, y = 7, 5
    suma(x, y)
    resta(x, y)
    multiplicacion(x, y)
    division_decimal(x, y)
    division_entera(x, y)
                                  
if __name__ == "__main__":
    ejecutar_funciones()