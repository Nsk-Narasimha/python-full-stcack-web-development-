"""inheritence
single inheritence:parent>>child
multi level:grandfather>>father>>child
multiple:father>>son<<mother
herachical:son<<father>>daughter
hybrid:2 or more

super()
"""
class animal:
    def __init__(self,ab):
        self.ab=ab
        print('animals make sounds')
    def name(self):
        print(self.ab)
class dog(animal):
    def __init__(self,ab,bc):
        super().__init__(ab)
        self.bc=bc
        print('dog barks',self.bc)
class cat(animal):
    def __init__ (self,ab):
        print('cat meow')
animal("nsk")
d=dog("nsk","k")
d.name()
class father:
    def land(self):
        print('5 ar of land')
class son(father):
    def flat(self):
        super().land()
        print('3bhk')
s=son()
s.flat()

class nsk:
    def __init__(self):
        self.e="nsk"
        print(self.e)

N=nsk()





























