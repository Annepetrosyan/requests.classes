class Rectangular:

    def __init__(self, a, b, c):
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)
        self.s = 2 * (self.a * self.b + self.a * self.c + self.b * self.c)
        self.v = self.a * self.b * self.c

    def count_v(self):

        return self.v

    def count_s(self):

        return self.s

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b and self.c == other.c \
               or self.a == other.a and self.b == other.c and self.c == other.b \
               or self.a == other.b and self.b == other.a and self.c == other.c \
               or self.a == other.b and self.b == other.c and self.c == other.a \
               or self.a == other.c and self.b == other.a and self.c == other.b \
               or self.a == other.c and self.b == other.b and selfc == other.a





    def __gt__(self, other):
        return self.v > other.v



    def __lt__(self, other):

        return self.v < other.v


















r1 = Rectangular(4, 3, 2)
r2 = Rectangular(3, 2, 4)
print(r1.count_v())
print(r1.count_s())
print(r1 == r2)
print(r1 < r2)
print(r1 > r2)