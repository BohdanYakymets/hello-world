import traceback
class Iterator:
    def __init__(self,polinom):
        self.current = 0
        self.polinom = polinom

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < len(self.polinom.data):
            res = self.current
            self.current+=1
            return res
        else:
            raise StopIteration



class Pair:
    def __init__(self,value,power):
        self.value = value
        self.power = power
    
    def __str__(self):
        return '{}*x^{}'.format(self.value,self.power)

    def __lt__(self,other):
        return self.power < other.power

    def __gt__(self,other):
        return self.power > other.power

    def __radd__(self,other):
        self.value += other.value

    

class Polinom():
    def __init__(self):
        self.data = []

    def __iter__(self):
        return Iterator(self)

    def __setitem__(self,value,power):
        isFound = False
        for i in self.data:
            if i.power == power:
                i.value = value
                isFound = True
        if not isFound:
            self.data.append(Pair(value,power))
            self.data = sorted(self.data)

    def __getitem__(self,power):
        for i in self.data:
            if power < i.power:
                return 0
            if i.power == power:
                return i.value
        return 0

    def __call__(self,x):
        res = 0
        for i in self.data:
            res += i.value * (x**i.power)
        return res
    

    def __str__(self):
        shos = ''
        isStart = True
        for i in self.data:
            if i.value == 0:
                continue
            elif i.value < 0:
                shos += '{}'.format(i)
            else:
                if not isStart:
                    shos += '+{}'.format(i)
                else:
                    shos += '{}'.format(i)
                    isStart = False
        return shos

    def __add__(self, other):
        newPolinom = Polinom()
        X = []
        selfPower = [x.power for x in self.data]
        otherPower = [x.power for x in other.data]
        for i in selfPower + otherPower:
            if i not in X:
                X.append(i)
        for i in X:
            sumOfVal = self[i] + other[i]
            newPolinom.__setitem__(sumOfVal, i)

        return newPolinom

class PolynomManager:
    def __init__(self, arr):
        self.arr = arr
        self.polynomial = Polinom()
    def __enter__(self):
        print("Start!!!")
        for (value, power) in self.arr:
            self.polynomial[power] = value
        return self.polynomial
    def __exit__(self, type, value, traceback):
        print("The end")
        self.polynomial = None

if __name__ == '__main__':
    with PolynomManager([(1,1), (2, 2), (3, 3), (1, 4)]) as p:
        a = Polinom()
        a[2] = 4
        print(p)
        print('a')
        count = True
        while count:
            try:
                power = int(input("enter degree: "))
                value = p[power]
                if power < 0:
                    raise Exception("Power < 0")
                if value == 0:
                    raise Exception("Does not exist degree")
            except Exception as exc:
                print(exc)
            else:
                print(f'{value}x^{power}')



    
