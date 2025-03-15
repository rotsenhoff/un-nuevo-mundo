
import unittest
import bin_to_dec

class TestBinaryToDecimal(unittest.TestCase):

    def test_binario_decimal_con_entradas_validas(self):

        # El metodo bin de Python convierte un entero en una cadena binaria.

        # Los bucles son útiles: testeamos un rango de números
        
        for d in range(100):

            binary = bin(d)    # En formato '0b10101'
            binary = binary[2:]    # Elimina los primeros dos caracteres '0b'

            dec_output = bin_to_dec.decimal(binary)

            self.assertEqual(d, dec_output)

    def test_numeros_mas_grandes(self):
        # Testeamos algunos números más grandes
        test_vals = [4000, 4001, 4002, 1024, 1099511627776, 1099511627777, 1099511627778]

        for d in test_vals:
            binary = bin(d)    # En formato '0b10101'
            binary = binary[2:]    # Elimina los primeros dos caracteres '0b'

            dec_output = bin_to_dec.decimal(binary)
            
            self.assertEqual(d, dec_output)

    def test_con_strings(self):
        # Test con strings
        test_bin_str = [ '101010', '111111', '000111', '0', '1']
        expected_dec = [42, 63, 7, 0, 1]

        for binary_input, expected_dec_output in zip(test_bin_str, expected_dec):
            dec_output = bin_to_dec.decimal(binary_input)

            self.assertEqual(expected_dec_output, dec_output)

    def test_binario_decimal_con_entradas_invalidas(self):

        # Testeamos que se genere un error con cadenas que no estén compuestas por 0 y 1.

        valid = '010101'
        valid2 = '111111'

        invalid = [ '123456', 'abc', '101010012', '@#€~€¬&^€%']
        for invalid_input in invalid:

            with self.assertRaises(ValueError):

                bin_to_dec.decimal(invalid_input)

if __name__ == '__main__':
    unittest.main()
