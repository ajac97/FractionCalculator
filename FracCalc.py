class Fraction:
    def __init__(self, numerator, denominator):
        self.__num = numerator
        self.__den = denominator

    def mult_frac(self, frac2):
        new_numer = self.__num * frac2.__num
        new_denom = self.__den * frac2.__den
        new_frac = Fraction(new_numer, new_denom)
        new_frac.simplify()
        return new_frac

    def div_frac(self, frac2):
        new_numer = self.__num * frac2.__den
        new_denom = self.__den * frac2.__num
        new_frac = Fraction(new_numer, new_denom)
        new_frac.simplify()
        return new_frac

    def add_frac(self, frac2):
        new_numer = (self.__num * frac2.__den) + (frac2.__num * self.__den)
        new_denom = self.__den * frac2.__den
        new_frac = Fraction(new_numer, new_denom)
        new_frac.simplify()
        return new_frac

    def sub_frac(self, frac2):
        new_numer = (self.__num * frac2.__den) - (frac2.__num * self.__den)
        new_denom = self.__den * frac2.__den
        new_frac = Fraction(new_numer, new_denom)
        new_frac.simplify()
        return new_frac

    def simplify(self):
        gcd = self.gcd(self.__num, self.__den)
        self.__num = int(self.__num / gcd)
        self.__den = int(self.__den / gcd)

    def gcd(self, num1, num2):
        while num2:
            num1, num2 = num2, num1 % num2
        return num1

    def __str__(self):
        return str(self.__num) + "/" + str(self.__den)

def main():
    again="y"
    while again=="y":
        fraction1, fraction2, oper = get_frac()
        result = get_result(fraction1, fraction2, oper)
        print(result)
        again=input("Would you like to calculate another equation? press y to go again: ")

def get_frac():
    user_equation = input("Enter an equation that adds, subtracts, multiplies, or divides 2 fractions (make sure to put spaces between fractions and operator): ")
    equation_list = user_equation.split(" ")
    frac1 = equation_list[0]
    oper = equation_list[1]
    frac2 = equation_list[2]
    frac1l = frac1.split("/") #split the fraction into a numerator and denominator and create a list
    frac2l = frac2.split("/") #split the fraction into a numerator and denominator and create a list
    numerator1 = int(frac1l[0]) #intify the numerator
    denominator1 = int(frac1l[1]) #intify the denominator
    numerator2 = int(frac2l[0])#repeat the process for second fraction
    denominator2 = int(frac2l[1])
    fraction1 = Fraction(numerator1, denominator1) #create fraction object
    fraction2 = Fraction(numerator2, denominator2) #create fraction object
    return fraction1, fraction2, oper


def get_result(fraction1, fraction2, oper):
    if oper == "+":
        result = fraction1.add_frac(fraction2)
    elif oper == "-":
        result = fraction1.sub_frac(fraction2)
    elif oper == "*":
        result = fraction1.mult_frac(fraction2)
    elif oper == "/":
        result = fraction1.div_frac(fraction2)
    return result


main()