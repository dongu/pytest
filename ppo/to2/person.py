class Person:
    def __init__( self, name, age, pay, job=None):
        self.name = name
        self.age = age 
        self.pay = pay
        self.job = job


if __name__ == '__main__':
    bob = Person( 'Bob Smith', 40, 40000, 'software')
    print( bob.name,  )
