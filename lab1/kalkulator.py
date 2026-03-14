import string
import unittest

def add(tekst):
    a=0
    b=0
    
    for i in tekst:  
        #if (not i.isdigit()) :
        #    raise ValueError
        if(i==',') : 
            a=a+b       
            b=0
        else:
            if( b != 0 ):
                b= b*10
            b= b+int(i)
            
        
    a=a+b

    return a




