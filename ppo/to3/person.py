class Person:
    def __init__(self, name, age, pay, job=None ):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job
    
    def lastName(self):
        return self.name.split()[-1]
    
    def __str__(self):
        return '%s => %s: %d years old, salary: %.02lf  Rank: %s\n' % ( self.__class__.__name__ , self.name, self.age, self.pay, self.job )
    
    
if __name__ == '__main__':
    bob = Person('Bob Smith', 40, 40000, "software")
    print(bob)
    
    print(bob.pay )