"""Calculadora simple para realizar operaciones matemáticas básicas."""
import matplotlib as plt
class Calculadora:
    """Clase para realizar operaciones matemáticas básicas."""
    def __init__(self, primer_numero, segundo_numero):
        """Inicializa la calculadora con dos números."""
        self.primer_numero = primer_numero
        self.segundo_numero = segundo_numero

    def suma(self):
        """Devuelve la suma de los dos números."""
        return self.primer_numero + self.segundo_numero

    def resta(self):
        """Devuelve la resta de los dos números."""
        return self.primer_numero - self.segundo_numero

    def multiplicacion(self):
        """Devuelve el producto de los dos números."""
        return self.primer_numero * self.segundo_numero

    def division(self):
        """mensaje de error si el segundo número es cero."""
        if self.segundo_numero == 0:
            return "Error: División por cero."
        return self.primer_numero / self.segundo_numero

if __name__ == "__main__":
    while True:
        try:
            entrada = input(" (+, -, *, /, **, salir): ").strip()
            if entrada.lower() == "salir":
                break

            Fnumber = int(input("Ingrese el primer numero: "))
            Snumber = int(input("Ingrese el segundo numero: "))

            calc = Calculadora(Fnumber, Snumber)

            if entrada == "+":
                print("Resultado:", calc.suma())
            elif entrada == "-":
                print("Resultado:", calc.resta())
            elif entrada == "*":
                print("Resultado:", calc.multiplicacion())
            elif entrada == "/":
                print("Resultado:", calc.division())
            elif entrada == "**":
                print(f"Suma: {calc.suma()}")
                print(f"Resta: {calc.resta()}")
                print(f"Multiplicación: {calc.multiplicacion()}")
                print(f"División: {calc.division()}")
            else:
                print("El valor ingresado no es el correcto.")
        except EOFError:
            print("\nEntrada no válida. Asegúrate de ingresar datos.")
            break
        except ValueError:
            print("Por favor, ingresa solo números válidos.")
