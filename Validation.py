import re
from design.interfaz import *

class Validation:

    def __init__(self):
        self.Fin = ""
        self.digitA = "[a|A]"
        self.digitB = "[b|B]"
        self.general = "[a|A|B|b]"
        self.arrayStates = []

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

        if re.match(self.general, expression):
            # tabla de trancisiones

            table = [["E", 1], [3, 2], [5, 4], [6, "E"], [3, 4], [6, 7], [3, 4], [8, "E"], ["E", 7]]
            state = 0
            self.arrayStates.append(state)
            # ciclo para recorrer la cadena
            for character in expression:

                # llamamos al metodo para saber si es un caracter valido y el valor retornado se guarda en charcaracter
                charcaracter = self.regularExpressions(character)
                # guardamos en estado el valor obtenido en la tabla segun las cordenadas que recibio anteriormente
                if  charcaracter==3:
                 return -1
                state = table[state][charcaracter]
                if (state == "E"):
                    break
                self.arrayStates.append(state)
            if state == 1 or state == 2 or state == 4 or state == 5 or state == 6 or state == 8:
                return  0
            else:
               return -1
        else:
            return -1


