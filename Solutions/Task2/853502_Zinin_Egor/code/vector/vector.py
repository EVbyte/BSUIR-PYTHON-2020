import numpy as np
import math
import unittest


class NDimVec:
    def __init__(self, *a):
        self.a = a

    def __check(self, *v):
        try:
            if len(self.a) != len(v):
                raise Exception("The dimension of the vectors must match")
        except Exception as e:
            print("The dimension of the vectors must match")

    def get(self):
        return [i for i in self.a]

    def plus(self, *plus):
        self.check(*plus)
        self.a = [i + j for i, j in zip(self.a, plus)]
        return self.a

    def id(self, i):
        return self.a[i]

    def minus(self, *v):
        self.check(*v)
        self.a = [i - j for i, j in zip(self.a, v)]
        return self.a

    def multiply_const(self, v):
        self.a = [v * i for i in self.a]
        return self.a

    def multiply(self, *v):
        self.check(*v)
        self.a = np.cross(self.get(), [i for i in v])
        return self.a

    def len(self):
        return math.sqrt(sum(map(lambda i: i * i, self.a)))

    def compare(self, v):
        if v.get() == self.get():
            return True
        else:
            return False

    def __str__(self):
        return "Vector: {}".format(self.a)


class TestVector(unittest.TestCase):
    def setUp(self):
        self.x = NDimVec(1, 2, 3)
        self.y = NDimVec(1, 2, 3)

    def test_multiply(self):
        self.assertEqual(self.x.id(0), 1)

    def test_compare(self):
        self.assertTrue(self.x.compare(self.y))

    def test_mul(self):
        self.x.multiply(2, 3, 4)
        lst = self.x.get()
        self.assertEqual(lst, [-1, 2, -1])


if __name__ == '__main__':
    unittest.main()
