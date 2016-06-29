import unittest


class SampleMath:

    def add_two_numbers(x, y):
        return x+y

    def sub_two_numbers(x, y):
        return x-y

    def second_power(x):
        return x*x

    def check_even(x):
        if x%2 == 0:
            return True
        else:
            return False


class Test (unittest.TestCase):

    def test_even_number_for_even_method(self):
        x = SampleMath
        self.assertTrue(SampleMath.check_even(2))

    def test_odd_number_for_even_method(self):
        x = SampleMath
        self.assertFalse(SampleMath.check_even(3))




if __name__ == '__main__':
    unittest.main()

#x = sample_math
#print (x.add_two_numbers(1, 2))
#print (x.second_power(4))
#print (x.sub_two_numbers(4,2))
#print (x.check_even(3))





