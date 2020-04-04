import os
import tempfile
import random
import unittest


class MergeSort():
    def __init__(self, file_input, file_output, size):
        self.file_name = file_input
        self.size = size
        self.file_output = file_output
        self.blocks = []

    def create_big_file(self, size):
        with open(self.file_name, 'w') as f:
            f.writelines('{}\n'.format(random.randint(-1000000, 1000000)) for _ in range(int(size)))

    def start(self):
        self.split()
        self.sort_file()
        self.input_file()

    def merge(self, array):
        if len(array) > 1:
            mid = len(array) // 2
            left_half = array[:mid]
            right_half = array[mid:]

            self.merge(left_half)
            self.merge(right_half)

            i, j, k = 0, 0, 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    array[k] = left_half[i]
                    i = i + 1
                else:
                    array[k] = right_half[j]
                    j = j + 1
                k = k + 1

            while i < len(left_half):
                array[k] = left_half[i]
                i = i + 1
                k = k + 1

            while j < len(right_half):
                array[k] = right_half[j]
                j = j + 1
                k = k + 1

    def split(self):
        with open(self.file_name, 'r') as f:
            temp_array = []
            i = 1
            for digit in f:
                temp_array.append(int(digit))
                i += 1
                if i > self.size:
                    i = 1
                    self.merge(temp_array)
                    with tempfile.NamedTemporaryFile(delete=False, mode='w') as t_file:
                        t_file.writelines(f'{i}\n' for i in temp_array)
                        self.blocks.append(t_file.name)
                    temp_array = []

    def sort_file(self):
        while len(self.blocks) > 1:
            with tempfile.NamedTemporaryFile(delete=False, mode='w') as t_file:
                with open(self.blocks[0], 'r') as first, open(self.blocks[1], 'r') as second:
                    first_digits = first.readline()
                    second_digits = second.readline()
                    while first_digits and second_digits:
                        if int(first_digits) <= int(second_digits):
                            t_file.writelines(first_digits)
                            first_digits = first.readline()
                        else:
                            t_file.writelines(second_digits)
                            second_digits = second.readline()

                    while first_digits:
                        t_file.writelines(first_digits)
                        first_digits = first.readline()
                    while second_digits:
                        t_file.writelines(second_digits)
                        second_digits = second.readline()

                    self.blocks.append(t_file.name)

            if os.path.exists(first.name):
                self.blocks.pop(0)
                os.remove(first.name)

            if os.path.exists(second.name):
                self.blocks.pop(0)
                os.remove(second.name)
        self.input_file()

    def input_file(self):
        with open(self.blocks[0], 'r') as file:
            with open(self.file_output, 'w') as sorted:
                for line in file:
                    sorted.writelines(line)


class TestVector(unittest.TestCase):
    def setUp(self):
        self.sort = MergeSort("test_input.txt", "test_out.txt", 40000)
        self.sort.create_big_file(40000)
        with open("test_input.txt", 'r') as f:
            self.input_string = f.read().splitlines()
        self.sort.start()
        with open('test_out.txt', 'r') as f:
            self.output_string = f.read().splitlines()
        self.input_string = [int(item) for item in self.input_string]
        self.output_string = [int(item) for item in self.output_string]
        self.input_string.sort()

    def test_multiply(self):
        self.assertEqual(self.output_string, self.input_string)


if __name__ == '__main__':
    unittest.main()
    sort = MergeSort("digits.txt", "sorted.txt", 1000000)
    # sort.create_big_file(500000000)
    #ort.start()
