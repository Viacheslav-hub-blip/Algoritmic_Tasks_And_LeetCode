import math


class Fraction:
    def __init__(self, chislitel, znamenatel):
        if znamenatel <= 0:
            raise ValueError('Знаменатель не может быть нулевым или отрицательным')

        if chislitel == 0:
            znamenatel = 0
        else:
            nod = math.gcd(chislitel, znamenatel)
            if nod != 1:
                chislitel /= nod
                znamenatel /= nod

        self.numerator = int(chislitel)
        self.denominator = int(znamenatel)

    def lcm(self, a, b):
        return (a * b) // math.gcd(a, b)

    def calc_new_ch_zn(self, self_ch, self_zn, other_ch, other_zn):
        nok = self.lcm(self_zn, other_zn)
        if nok == self_ch:
            k = nok / other_zn
            new_ch_self = self_ch
            new_ch_other = other_ch * k
        elif nok == other_zn:
            k = nok / self_zn
            new_ch_self = self_ch * k
            new_ch_other = other_ch
        else:
            k1, k2 = nok / self_zn, nok / other_zn
            new_ch_self = self_ch * k1
            new_ch_other = other_ch * k2
        return (new_ch_self, new_ch_other, nok)

    def __add__(self, other):
        if isinstance(other, Fraction):
            new_ch_self, new_ch_other, nok = self.calc_new_ch_zn(self.numerator, self.denominator, other.numerator,
                                                                 other.denominator)
            return Fraction(int(new_ch_self + new_ch_other), nok)

    def __sub__(self, other):
        if isinstance(other, Fraction):
            new_ch_self, new_ch_other, nok = self.calc_new_ch_zn(self.numerator, self.denominator, other.numerator,
                                                                 other.denominator)
            return Fraction(int(new_ch_self - new_ch_other), nok)

    def __mul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            if other.numerator != 0:
                return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)
            else:
                raise ZeroDivisionError

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __eq__(self, other):
        if isinstance(other, Fraction):
            new_ch_self, new_ch_other, nok = self.calc_new_ch_zn(self.numerator, self.denominator, other.numerator,
                                                                 other.denominator)
            if new_ch_self == new_ch_other:
                return True
            else:
                return False

    def __ne__(self, other):
        if isinstance(other, Fraction):
            new_ch_self, new_ch_other, nok = self.calc_new_ch_zn(self.numerator, self.denominator, other.numerator,
                                                                 other.denominator)
            if new_ch_self != new_ch_other:
                return True
            else:
                return False

    def __lt__(self, other):
        if isinstance(other, Fraction):
            new_ch_self, new_ch_other, nok = self.calc_new_ch_zn(self.numerator, self.denominator, other.numerator,
                                                                 other.denominator)
            if new_ch_self < new_ch_other:
                return True
            else:
                return False

    def __gt__(self, other):
        if isinstance(other, Fraction):
            new_ch_self, new_ch_other, nok = self.calc_new_ch_zn(self.numerator, self.denominator, other.numerator,
                                                                 other.denominator)
            if new_ch_self > new_ch_other:
                return True
            else:
                return False


frac = Fraction(0, 2)
frac2 = Fraction(5, 6)
frac3 = frac + frac2
frac4 = frac - frac2
frac5 = frac / frac2
print('3', frac3)
print(frac4.numerator, frac4.denominator)
print(frac5.numerator, frac5.denominator)

print(frac < frac3)
