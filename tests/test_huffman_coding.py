import unittest

from src.algorithms.greedy_algorithms.huffmann_coding import HuffmanEncoding


class TestHuffManCoding(unittest.TestCase):
    def setUp(self):
        self.text = "This is an example for huffman encoding"
        self.file = "fixture/plain_file"
        self.char_frequency_table = [
            {'T': 1}, {'h': 2}, {'i': 3}, {'s': 2}, {' ': 6}, {'a': 3},
            {'n': 4}, {'e': 3}, {'x': 1}, {'m': 2}, {'p': 1}, {'l': 1},
            {'f': 3}, {'o': 2}, {'r': 1}, {'u': 1}, {'c': 1}, {'d': 1},
            {'g': 1}
        ]
        self.char_frequency_map = {
            'T': 1, 'h': 2, 'i': 3, 's': 2, ' ': 6, 'a': 3,
            'n': 4, 'e': 3, 'x': 1, 'm': 2, 'p': 1, 'l': 1,
            'f': 3, 'o': 2, 'r': 1, 'u': 1, 'c': 1, 'd': 1,
            'g': 1
        }
        self.resultant_encoding_table = {
            ' ': '101',
            'n': '010',
            'a': '1001',
            'e': '1100',
            'f': '1101',
            'h': '0001',
            'i': '1110',
            'm': '0011',
            'o': '0110',
            's': '1000',
            'd': '00000',
            'g': '00001',
            'l': '00100',
            'p': '00101',
            'r': '01110',
            'u': '01111',
            'x': '11110',
            'T': '111110',
            'c': '111111'
        }

    def test_file_encoding(self):
        huffman_encoder = HuffmanEncoding(self.file)
        encoded_string, frequency_table = huffman_encoder.encode()
        assert encoded_string == "done"
        assert frequency_table == self.resultant_encoding_table

    def test_text_encoding(self):
        huffman_encoder = HuffmanEncoding(self.text)
        encoded_string, frequency_table = huffman_encoder.encode()
        expected_string = "1111100001111010001011110100010110010101011100111101001001100101001001100101110101100111010100010111111011101001110010101011100010111111011000000111001000001"
        assert encoded_string == expected_string
        assert len(self.text)*8 > len(encoded_string)
        assert frequency_table == self.resultant_encoding_table

    def test_char_frequency_table_encoding(self):
        huffman_encoder = HuffmanEncoding(self.char_frequency_table)
        encoded_string, frequency_table = huffman_encoder.encode()
        assert encoded_string == "done"
        assert frequency_table == self.resultant_encoding_table

    def test_char_frequency_map_encoding(self):
        huffman_encoder = HuffmanEncoding(self.char_frequency_map)
        encoded_string, frequency_table = huffman_encoder.encode()
        assert encoded_string == "done"
        assert frequency_table == self.resultant_encoding_table
