
class ImagNmb:
    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im

    def __str__(self):
        return f"{self.re}{'+' if self.im > 0 else ''}{self.im}j"

    def __add__(self, other):
        return ImagNmb(self.re + other.re, self.im + other.im)

    def __sub__(self, other):
        return ImagNmb(self.re - other.re, self.im - other.im)


nmb1 = ImagNmb(2, 3)
nmb2 = ImagNmb(3, -1)

imag_sum = nmb1 + nmb2
imag_dif = nmb1 - nmb2

print(f"Number 1: {nmb1}")
print(f"Number 2: {nmb2}")
print(f"Sum: {imag_sum}")
print(f"Difference: {imag_dif}")
