def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(f):
    def left(a, b):
        return a
    return f(left)

def cdr(f):
    def right(a, b):
        return b
    return f(right)


a=input("Enter first element a ")
b=input("Enter second element b ")
print(car(cons(a,b)))
print(cdr(cons(a,b)))