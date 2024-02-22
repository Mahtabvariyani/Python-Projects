""" 
Or also Called Type Casting


its means changing the data Type of for Example  int to String  and it happens Automaticlly 

there is a Rule is python that it Converts the Lower Data type to Higher Data type 

for Example

5 + 10.98
15.98
type(15.89)
<class 'float'>



"""

sum = 5 + 10.98
print(sum)

print(type(sum))


""" 
this result is  flooat but the 5 is not a float data Type its Intiger in this case the Conversion happened so the int is changed to the Float
 <class 'float'>
 
 so python changes the 5 to 5.0 so it can be added
 
 """


""" 
Python also have another Rule which means HYpothetical Rule which means it is not the way PYthon works but somthimes it  Happens and in this case means the PYthon converts the high data Type to lower Data type 

it also depends on the  operator which being used 

for example in this  one the 5 and the 60 are normal Intigers but after deviding it they become the float 
** but if we Use the // we will get the int 

"""


sum_d = 5 //60 

print(sum_d)
print(type(sum_d))
