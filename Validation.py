import re

from Principal import Principal


class Validation:

    def __init__(self):
        self.Fin = ""
        self.digitA = "[a|A]"
        self.digitB = "[b|B]"

    def regularExpressions(self, character):

        # comparamos si es digito o operador
        if re.match(self.digitA, character):
            # caracter a
            return 0
        elif re.match(self.digitB, character):
            # caracter b"
            return 1
        elif character == self.Fin:
            # caracter ""
            return 2
        else:
            # cualquier otro caracter
            return 3

    def validate(self, expression):
        # tabla de trancisiones
        table = [[1, 2, "E"], [2, "E", "E"], [1, 2, "A"]]
        state = 0
        # ciclo para recorrer la cadena
        for character in expression:

            # llamamos al metodo para saber si es un caracter valido y el valor retornado se guarda en charcaracter
            charcaracter = self.regularExpressions(character)
            if(charcaracter==3):
                print("Error")
                break
            # guardamos en estado el valor obtenido en la tabla segun las cordenadas que recibio anteriormente
            state = table[state][charcaracter]

            if state == "E":
                print("cadena no válida")
                break;

