def squaresub(num): return num**2

class Members:
    # public data member
    var1 = None

    # protected data member
    _var2 = None

    # private data member
    __var3 = None


var = Members()
print(var.var1)
print(var._var2) #protected member.. same class so ok
#print(var.__var3) #private member.. not ok to access

