#numbers
print(2+2)
print((50-5*6)/4)

print(8/5) # division always return a floating number

print(17//3) #floor division discards the fractional part
print(17%3) # the % operator returns the reminder of the revision
print(2**7) # 2 to the power of 7

#strings
print('Welcome to python world')
print("doesn't")
print('print first line \nsecond line')

#if you dont want characters prefaced by \ to be interpreted
#as special characters
#you can use raw string by adding an r before the first quote:
print(r'c:\some\name')
print('c:\some\name')

#string literals can span multiple lines
#one way is using triple-quotes:"""...""" or '''...'''
#End of lines are automatically included in the string,
#but it's possible to prevent this by addings a \at the end of the line.

print("""\
Usage: thingy [OPTIONS]
    -h                         Dislay this usage message
    -H hostname                Host name to connect to
""")

#strings cane be concatenated with the + operator,and repeated with *:
print(3 * 'un' + 'ium')
print('py' 'thon')
print('this is a test '
      'to write long strings '
      'concatenated together')

#can't concatenate a variable and a string literial,but (+) will work
prefix='py'
 #print(prefix 'thon')
print(prefix + 'thon')

#strings can be indexed,
word='python'
print(word[0])
print(word[4])

#indeces may also be negative numbers,to start counting from the right:
print(word[-1])
print(word[-2])
print(word[-6])


#while indexing is used to obtain invidual characters,
#slicing allows you to obtain substring:
print(word[0:2]) ## characters from position 0 [included] to 2 [Excluded]

#note how the start is always inclluded,and the end always excluded
#this makes sure that s[:i] + s[i:] is always equal to s:
print(word[:2] + word[2:])
print(word[:4] + word[4:])

#characters from the second-last (included) to the end
print(word[-2:])

#python strings can not be changed-- they are immutable
#therefore,assigning to an indexd position in the string
#results in as error:
#word[0]='j'
#word[:2]='py'

#if you need a different string,you should create a new one:
print('j' + word[1:])

#len() returns length of string
print(len('python'))

#Lists
#Lists might contain items of different types,
#but usually the items all have the same type
squares=[1,4,9,16,25]
print(squares)
print(squares[0])
print(squares[-3:])

#unlike strings,which are immmutable
#lists aremutable type,i.e. it is possible to change their content:
cubes=[1,8,27,65,125]
cubes[3]=64
print(cubes)
cubes.append(6**3)
print(cubes)

#replace some values
cubes[2:1]=[20]
print(cubes)
#clear the list by replacing all the elements with an empty list
cubes[:]=[]
print(cubes)
cubes=[1,8,27,65,125]
cubes[2:2]=[20]
print(cubes)

#length of the lists
print(len(['a','b']))
a=['a','b','c']
n=[1,2,3]
x=[a,n]

print(x)
print(x[0])
print(x[1][0])

#fibonacci series
a,b=0,1
while b<1000:
      print(b,end=',')
      a,b=b,a+b