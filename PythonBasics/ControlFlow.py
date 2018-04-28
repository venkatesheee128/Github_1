#if statements
#x=int(input("please enter an integer: "))
x=34
if x<0:
    x=0
    print('negative replaced with 0')
elif x == 0:
    print('zero')
elif 0 <x<=42:
    print("value is between 0 and 42:" + str(x))
else:
    print(x)


#for statement
words=['cat','window','defenestrate']
for w in words:
    print(w,len(w))

#modify the sequence you are iterating over while inside the loop
for w in words[:]:
    if len(w)>6:
        words.insert(0,w)
print(words)

#the range() function: iterate over sequence of numbers
for i in range(5):
    print(i)

for i in range(5,10):
    print(i)

for i in range(0,16,3):
    print(i)

for i in range(-10,-100,-30):
    print(i)

a=['mary','had','a','little','lamb']
for i in range(len(a)):
    print(i,a[i])

#the break statement,breaks out of the innermost enclosing off
#or while loop
#a try statement's else cause runs when no exception occurs
for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(n,'equals',x,'*',n//x)
            break
    else:
        print(n,'is a prime number')

#the continue statement,continue with the next iteration of the loop:
for num in range(2,10):
     if num % x == 0:
        print("found an even number",num)
        continue
     print('found a number',num)

#pass statements- the pass statement does nothing.It can be used
#when a statement is required syntacticallybut the program requires no action
def tlog(*args):
    pass #remember to implement this!

def fib2(n):
    """Return a list containing the Fibonacci series upto n."""
    result=[]
    a,b=0,1
    while  a<n:
        result.append(a)
        a,b=b,a+b
    return result

f100=fib2(100)
print (f100)


#default argument argument values
def ask_ok(promt,retries=4,reminder='please try again!'):
    while True:
        ok=input(promt)
        if ok in ('y','ye','yes'):
            return True
        if ok in ('n','no','nop','nope'):
            return False
        retries=retries-1
        if retries<0:
            raise ValueError('invalid user response')
        print(reminder)


#ask_ok('Do you really want to quit?')
#ask_ok('Do you really want to quit?',2)
#ask_ok('Do you really want to quit?',2,'come on,only yes or no!')

#keyword arguments

def parrot(voltage,state='a stiff'):
    print (voltage,state)

#parrot(voltage=1000,state='dfd')
#parrot(1000,state='dfd')
#parrot('dfd',voltage=1000)


#when a final formal parameter of the form **name is present,
#it receives a dictionary containing all keyword arguments except
#for those corresponding to a formal parameter.This may be combined
#with a formal parameter of the form *name which receives a tuple
#contining the positional arguments beyond the formal parameter list.
# (*name must occur before **name.)
def cheese(kind,*arguments,**keywords):
    print(kind)
    for arg in arguments:
        print('tuple values :' ,arg)
    for w in keywords:
        print('dictionary values :',w)


cheese("first argument","first argument in tuple","second argument in tuple",language='python',technology='deep learning')

#Arbitrary argument lists
def concat(*args,sep="/"):
    return sep.join(args)


print(concat("earth","mars","venus"))

#Unpacking argument lists
print(list(range(3,6))) #normal callwith sepearte arguments
args=[3,6]
print(list(range(*args))) #cll with arguments

#In the same fashion,dictionaries call deliver keyword arguments
#with the **-operator
def parrot(voltage,state='a stiff',action='voom'):
    print(state)
    print(action)
    print(voltage)

d={"voltage": "four million","state": "bleeding demised","action": "voom"}
parrot(**d)


#lambda expressions
#python supports the creation of anonymous functions
#(i.e. functions that are bound to a name) at runtime,
#using a construct called "Lambda"

def make_incrementor(n):
    return lambda x:x+n

f=make_incrementor(42)

print(f(0))
print(f(1))
print(f(8))

#pass small function as argument:
pairs=[(1,'one'),(2,'two'),(3,'three'),(4,'four')]
pairs.sort(key=lambda pair:pair[1])
print(pairs)

#coding style
#https://www.python.org/dev/peps/pep-0008/

