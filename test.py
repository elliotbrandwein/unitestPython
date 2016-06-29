import unittest

# You are declaring a class here and definiting the functions as static since they 
# have no access to the 'self' reference. However you are not explicitly telling
# the class that these are static functions. If you were to create an instance of
# this class, shit would go haywire.
class SampleMath:

    # FIXME Must add the staticmethod decorators
    @staticmethod
    def add_two_numbers(x, y):
        return x+y

    @staticmethod   
    def sub_two_numbers(x, y):
        return x-y

    @staticmethod
    def second_power(x):
        return x*x

    @staticmethod
    def check_even(x):
        if x%2 == 0:
            return True
        else:
            return False


class Test (unittest.TestCase):

    def test_even_number_for_even_method(self):
        x = SampleMath   # What is this for???
        self.assertTrue(SampleMath.check_even(2))

    def test_odd_number_for_even_method(self):
        x = SampleMath   # What is this for???
        self.assertFalse(SampleMath.check_even(3))




if __name__ == '__main__':
    unittest.main()

#x = sample_math
#print (x.add_two_numbers(1, 2))
#print (x.second_power(4))
#print (x.sub_two_numbers(4,2))
#print (x.check_even(3))





