"""this is the pythonAdventure module"""
# #Collection types
# #---------List----------
# from os import stat


# int_list=[1, 2, 3]
# string_list=['idriss', 'memoria']
# empty_list=[]
# mixed_list=["idriss", 1998, None, True]
# nested_list=[['a', 'b', 'c'], [1,2,3]]

# names=['idriss', 'ali', 'reda', 'omar']
# print(names[0])
# print(names[2])
# print(names[-1])#omar
# print(names[-4])#idriss

# names[0]='idrissUpdated'#mutable
# names.append('simo')
# names.insert(2, 'hamada')#add element to a specific index
# names.remove('simo')#remove the first occurence of this value
# print(names.index('ali'))
# print(len(names))
# print(names.count('reda'))
# names.reverse()
# print(names)
# names.pop(1)#without index remove the last item
# print(names)
# for name in names:
#   print(name)

# #Tuples(fixed and immutable)
# ip_iddress=('127.0.0.1', 8000)
# one_member_tuple=('only member',)
# one_member_tuple=tuple(['only member'])

# #dictionnaries(resembles JSON syntax)
# state_capitals = {
#   'arkansas':'little rock',
#   'colorado':'denver',
#   'california':'sacramento',
#   'georgia':'atlanta'
# }
# print(state_capitals['colorado'])
# for k in state_capitals.keys():
#   print('{} is the capital of {}'.format(state_capitals[k], k))

# #set(no repeats, some things are goruped together, no insertion order)
# first_names = {'adam', 'rayan', 'ranya'}

# my_list = [1,2,3]
# my_set = set(my_list)

# if 'rayan' in first_names:
#   print('found')

# #defaultdict(default value for keys, never raise a keyError)
# from collections import defaultdict
# state_capitals = defaultdict(lambda:'Boston')
# state_capitals['arkansas']='little rock'
# state_capitals['california']='sacramento'
# state_capitals['colorado']='denver'
# print(state_capitals['alabama'])#Boston

# User input
# name = input("whats your name?")#input always is a string type
# print(name)
# x = input("write a number")#(try/except recommended with the input)
# print(float(x)/2)

#Built in modules and functions
# print(dir(__builtins__))
# help(pow)# to know the functionality of any function
# import math
# print(dir(math))
# math.sqrt(16)
# print(math.__doc__)#documentation for a module
# print(__doc__)

#creating a module(hello.py) 
#the module need to be in the same dir
# import hello
# hello.say_hello()
# from hello import say_hello#importing specific function in a  module
# say_hello()
# import hello as h #aliased
# h.say_hello()
#if the module is inside a directory and needs to be detected by python , the dir should contain a file named __init__.py


#string function (str() and repr())
#diff between them is that str(object) does not always attempt to return a string that is acceptable to eval()

# s = """w'o"w"""
# print(repr(s))#'w\'o"w'
# print(str(s))#w'o"w
# eval(str(s)) == s #SyntaxError 
# eval(repr(s)) == s #True

# import datetime
# today = datetime.datetime.now()
# print(str(today))
# print(repr(today))

class Represent(object):
  def __init__(self, x, y) :
    self.x, self.y = x, y
  
  def __repr__(self):
      return "Represent(x={},y=\"{}\")".format(self.x, self.y)

  def __str__(self):
    return "Representing x as {} and y as {}".format(self.x, self.y)

r = Represent(1, "idriss")
print(r)
print(r.__repr__)
rep = r.__repr__()
print(rep)
r2 = eval(rep)
print(r2)
print(r2 == r)
      
