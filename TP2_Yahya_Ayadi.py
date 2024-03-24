"""
File: TP2.py
Author: Ayadi Yahya
TP: 2
"""
'#Exercice1&2'


def gcd(a, b):
    # Function to find the greatest common divisor
    while b != 0:
        a, b = b, a % b
    return a


class Fraction:
    def __init__(self, numerator, denominator):
        # Check if denominator is zero
        if denominator == 0:
            raise ValueError('Denominator must be non zero')
        self.__numerator = numerator
        self.__denominator = denominator

    def numerator(self):
        # Get the numerator
        return self.__numerator

    def denominator(self):
        # Get the denominator
        return self.__denominator

    def set_numerator(self, new_numerator):
        # Set a new numerator
        if not isinstance(new_numerator, int):
            raise ValueError('Numerator must be an integer')
        self.__numerator = new_numerator
        return self.__numerator

    def set_denominator(self, new_denominator):
        # Set a new denominator
        if not isinstance(new_denominator, int):
            raise ValueError('Denominator must be an integer')
        if new_denominator == 0:
            raise ValueError('Denominator must be non zero')
        self.__denominator = new_denominator
        return self.__denominator

    def add(self, fraction):
        # Add two fractions
        new_numerator = self.__numerator * fraction.__denominator + self.__denominator * fraction.__numerator
        new_denominator = self.__denominator * fraction.__denominator
        return Fraction(new_numerator, new_denominator)

    def multiply(self, fraction):
        # Multiply two fractions
        new_numerator = self.__numerator * fraction.__numerator
        new_denominator = self.__denominator * fraction.__denominator
        return Fraction(new_numerator, new_denominator)

    def simplify(self):
        # Simplify the fraction
        gcd_value = gcd(self.__numerator, self.__denominator)
        new_numerator = self.__numerator // gcd_value
        new_denominator = self.__denominator // gcd_value
        return Fraction(new_numerator, new_denominator)

    def display(self):
        # Display the fraction
        return str(self.set_numerator(self.numerator())) + '/' + str(self.set_denominator(self.denominator()))


'#Exercice 3:'


def harmonic_sum(n):
    # Calculate the harmonic sum
    result = Fraction(0, 1)
    for i in range(1, n + 1):
        result = result.add(Fraction(1, i))
    return result


'#Exercice 4:'


def leibniz_sum(n):
    # Calculate the Leibniz sum
    result = Fraction(1, 1)
    for i in range(1, n + 1):
        result = result.add(Fraction((-1)**i, 2*i+1))
    return result


if __name__ == '__main__':
    # Test cases for Exercises 1 and 2
    print('============================\n' '===== Exercises 1=====\n''============================\n')
    fraction1 = Fraction(3, 4)
    print(f'Fraction(3,4) = {fraction1.display()}')
    assert fraction1.display() == "3/4", "Error in Exercise 1"

    print('============================\n' '===== Exercises 2=====\n''============================\n')
    fraction2 = Fraction.add(Fraction(3, 4), Fraction(2, 5))
    print(f'{Fraction(3,4).display()} + {Fraction(2,5).display()} = {fraction2.display()}')
    assert fraction2.display() == "23/20", "Error in Exercise 2 addition"

    fraction3 = Fraction(1, 3).multiply(Fraction(2, 5))
    print(f'{Fraction(1,3).display()} * {Fraction(2,5).display()} = {fraction3.display()}')
    assert fraction3.display() == "2/15", "Error in Exercise 2 multiplication"

    fraction4 = Fraction.simplify(Fraction(20, 16))
    print(f'{Fraction(20,16).display()} = {fraction4.display()}')
    assert fraction4.display() == "5/4", "Error in Exercise 2 simplification"

    # Function harmonic_sum(n) - Exercise 3
    print('============================\n' '======== Exercises 3========\n''============================\n')
    harmonic_sum_10000 = harmonic_sum(10000)
    numerator1 = harmonic_sum_10000.numerator()
    denominator1 = harmonic_sum_10000.denominator()
    print(f'harmonic_sum(10000) = {numerator1/denominator1}\n'f'Expected result: 9.787606036044382')
    assert harmonic_sum_10000.numerator()/harmonic_sum_10000.denominator() == 9.787606036044382, "Error in Exercise 3"
    # Function leibniz_sum() - Exercise 4
    print('============================\n' '======== Exercises 4========\n''============================\n')
    leibniz_10000 = leibniz_sum(10000)
    numerator2 = leibniz_10000.numerator()
    denominator2 = leibniz_10000.denominator()
    print(f'leibniz_sum(10000) = {numerator2 /denominator2}\n' f'Expected result: {0.7854231608976358}')
    assert leibniz_10000.numerator() / leibniz_10000.denominator() == 0.7854231608976358, "Error in Exercise 4"
