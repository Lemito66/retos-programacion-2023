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


def is_expression_correct(expression: str) -> bool:
    separate = expression.split(" ")
    valid_expression = ["+", "-", "*", "/", "%"]

    if len(separate) % 2 == 0 or len(separate) < 3:
        return False

    check = True

    for i, j in enumerate(separate):
        if i % 2 == 0:
            try:
                float(j)
            except ValueError:
                check = False
        else:
            check = j in valid_expression

        if not check:
            return False
    return check


print(is_expression_correct("1+ + 2"))