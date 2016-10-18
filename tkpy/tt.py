import math
import sys



def distance(x1,y1,x2,y2):
    dx=x2-x1
    dy=y2-y1
    dsquuard = dx**2+dy**2
    result = math.sqrt( dsquuard )
    return result



if __name__ == '__main__':
    print( distance( 0,0, 3 ,4) )
 #   print(sys.version)
