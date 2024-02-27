
""" 
Jack really likes his number five: the trick here is that you have to multiply each number by 5 raised to the number of digits of each numbers, so, for example:

"""



def multiply(n):
    exp = len(str(abs(n)))
    return n * pow(5,exp)