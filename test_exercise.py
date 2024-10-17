# @ EJECUCIÓN DE PUREBAS E IDENTIFICACIÓN DEL ERROR
# def str_to_bool(value):
#     true_values = ['y','yes']
#     false_values = ['no', 'n']

#     # if value in true_values: 
#     #     return True
#     # if value in false_values:
#     #     return False

#     #Al hacer el test daría error al escribir uno de los resultados en mayúscula

#     if value.lower() in true_values:
#         return True
#     if value.lower() in false_values:
#         return 
#     #Agregamos .lower() para que cualquier parámetro que se incluya pase a estar en minúscula

# import unittest

# class TestStrToBool(unittest.TestCase):

#     def test_y_is_true(self):
#         result = str_to_bool('y')
#         self.assertTrue(result)

#     def test_yes_is_true(self):
#         result = str_to_bool('Yes')
#         self.assertTrue(result)

# if __name__ == '__main__':
#     unittest.main()

# @ CÓDIGO NUEVO CON PRUEBAS
def str_to_bool(value):
    try:
        value = value.lower()
    except AttributeError:
        raise AttributeError(f"{value} must be of type string")
    true_values = ['y','yes']
    false_values = ['no', 'n']

    if value in true_values:
        return True
    if value in false_values:
        return False

import unittest

class TestStrToBool(unittest.TestCase):

    def test_y_is_true(self):
        result = str_to_bool('y')
        self.assertTrue(result)

    def test_yes_is_true(self):
        result = str_to_bool('Yes')
        self.assertTrue(result)
        
    def test_invalid_input(self):
        with self.assertRaises(AttributeError):
            str_to_bool(1)

if __name__ == '__main__':
    unittest.main()