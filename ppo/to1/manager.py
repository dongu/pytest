from person_start import Person

class Manager(Person):
    def giveRaise(self, percent, bonus=0.1):
        Person.giveRaise(self, percent+bonus )


if __name__ == '__main__':
    tom = Manager(name = 'Tom Doe', age = 50, pay=50000 )
    print(tom.lastName() )
    tom.giveRaise( .20)
    
    print(tom.pay)
    
    print(tom )