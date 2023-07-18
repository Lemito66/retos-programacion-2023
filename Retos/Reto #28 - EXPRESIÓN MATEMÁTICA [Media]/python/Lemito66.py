"""
* Crea una función que reciba una expresión matemática (String)
 * y compruebe si es correcta. Retornará true o false.
 * - Para que una expresión matemática sea correcta debe poseer
 *   un número, una operación y otro número separados por espacios.
 *   Tantos números y operaciones como queramos.
 * - Números positivos, negativos, enteros o decimales.
 * - Operaciones soportadas: + - * / % 
 *
 * Ejemplos:
 * "5 + 6 / 7 - 4" -> true
 * "5 a 6" -> false 
"""



def is_expression_correct(expression):
    separate = expression.split(" ")
    valid_expression = ["+", "-", "*", "/", "%"]
    for i in range(1, len(separate), 2):
        if separate[i] not in valid_expression:
            return False
    
    return True
        
        