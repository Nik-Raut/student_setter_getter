class Address:
    def setCity(self,c):
        self.c=c
    def getCity(self):
        return self.c
    def setPin(self,p):
        self.p=p
    def getPin(self):
        return self.p

    def setAll(self,c,p):
        self.c=c
        self.p=p
    def getAll(self):
        return self.c,self.p


class Student:
     #for rn

    def setRn(self,r):
        self.r=r

    def getRn(self):
        return self.r
    
    #for name
    def setName(self,n):
        self.n=n
        
    def getName(self):
        return self.n

     #for marks
    def setMarks(self,m):
        self.m=m
        
    def getMarks(self):
        return self.m
     #for address object
    def setAddress(self,obj):
        self.obj=obj

    def getAddress(self):
        return self.obj.getCity()

    
#exception handling

class OptionError(Exception):
    def __init__(self,msg):
        self.msg=msg


def option_check(x):
    if x.isdigit()==False:
        raise OptionError('Enter value in Integers only')
    elif int(x)<=0:
        raise OptionError('Enter non-zero non-negative Intergers only')
    elif int(x)>3:
        raise OptionError('Enter choice from above options only')


class AddressOptionError(Exception):
    def __init__(self,msg):
        self.msg=msg


def address_option_check(x):
    if x.isdigit()==False:
        raise AddressOptionError('Enter value in Integers only')
    elif int(x)<=0:
        raise AddressOptionError('Enter non-zero non-negative Intergers only')
    elif int(x)>5:
        raise AddressOptionError('Enter choice from above options only')


class StudentOptionError(Exception):
    def __init__(self,msg):
        self.msg=msg


def student_option_check(x):
    if x.isdigit()==False:
        raise StudentOptionError('Enter value in Integers only')
    elif int(x)<=0:
        raise StudentOptionError('Enter non-zero non-negative Intergers only')
    elif int(x)>5:
        raise StudentOptionError('Enter choice from above options only')


class PincodeError(Exception):
    def __init__(self,msg):
        self.msg=msg

def pincode_check(p):
    if p.isdigit()==False:
        raise PincodeError('Enter value in Integers only')
    elif len(p)<6 or len(p)>6:
        raise PincodeError('Pincode can have 6 digits only')
    

class IntegerError(Exception):
    def __init__(self,msg):
        self.msg=msg


def integer_check(x):
    if x.isdigit()==False:
        raise IntegerError('Enter value in Integers only')
    elif int(x)<=0:
        raise IntegerError('Enter non-zero non-negative Intergers only')
   
class Name_Error(Exception):
    def __init__(self,msg):
        self.msg=msg
def Name_check(x):
    if x.isalpha()==False:
        raise Name_Error('Enter Name in alphabets only')
    


class City_Not_Found_Error(Exception):
    def __init__(self,msg):
        self.msg=msg
def city_check(city,L):
    city_list=[]
    for x in L:
        city_list.append(x.getCity())
    if city not in city_list:
        raise City_Not_Found_Error('Invalid City.If you want to assign new city,then add it through Address Menu')

class Rn_Not_Found_Error(Exception):
    def __init__(self,msg):
        self.msg=msg
def Rn_check(rn,L):
    rn_list=[]
    for x in L:
        rn_list.append(x.getRn())
    if rn.isdigit()==False:
        raise IntegerError('Enter value in Integers only')
    elif int(rn) not in rn_list:
        raise Rn_Not_Found_Error('Roll Number did not match')
    




