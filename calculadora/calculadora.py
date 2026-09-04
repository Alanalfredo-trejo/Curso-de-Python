def sumar(a, b):
    return a + b 

def restar(a, b):
    return a - b 

def multiplicar(a, b):
    return a * b 

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir entre cero"
    return a / b 
   
def mostrar_menu():
    print("\n--- CALCULADORA BASICA ---")
    print("1. Sumar")
    print("2. Restar") 
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    
def ejecutar_calculadora():
    while True:
        mostrar_menu()
        opcion = input("Elige una opcion (1-5)")
        
        if opcion == '5':
            print("¡Hasta luego!")
            break
        
        if opcion in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))
            except ValueError:
                print("Error: Por favor ingresa números válidos.")
                continue
            
            if opcion == '1':
                print(f"Resultado: {num1} + {num2} = {sumar(num1, num2)}")
            elif opcion == '2':
                print(f"Resultado: {num1} - {num2} = {restar(num1, num2)}")
            elif opcion == '3':
                print(f"Resultado: {num1} * {num2} = {multiplicar(num1, num2)}")
            elif opcion == '4':
                print(f"Resultado: {num1} / {num2} = {dividir(num1, num2)}")
        else:
            print("Opción no valida. Intenta de nuevo.")


#Iniciar el programa
if __name__ == "__main__":
    ejecutar_calculadora()
            
         
             
