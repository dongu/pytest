from person_start import Person

class Manager(Person):
    def __init__( Person.self, bonus ):
        Person(self.name, self.age, self.job, self.pay)
        self.bonus=bonus

    def giveRaise(self, percent, bonus=0.1):
        Person.giveRaise(self, percent+bonus )

    def __str__(self):
#        Person.__str__(self) 
        return  '%s [%s], bonus: %.2lf' % ( self.name, self.job, self.bonus  )


if __name__ == '__main__':
    tom = Manager(name = 'Tom Doe', age = 50, pay=50000 , 0.2 )
    print(tom.lastName() )
    tom.giveRaise( .20)
    
    print(tom.pay)
    
    print(tom )
