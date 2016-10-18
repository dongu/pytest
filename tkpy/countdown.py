def countdown(s, n):
    if n <= 0:
        print('Blastoff!')
    else:
#        print(n)
        s.append(n)
        print(s)
        countdown(s, n-1) 
    return s


if __name__ == '__main__' :
    s=[]
    a=10
    for i in   countdown(s, a)  :
        print 'No:',  i  
