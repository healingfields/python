#Collection types
#---------List----------
from os import stat


int_list=[1, 2, 3]
string_list=['idriss', 'memoria']
empty_list=[]
mixed_list=["idriss", 1998, None, True]
nested_list=[['a', 'b', 'c'], [1,2,3]]

names=['idriss', 'ali', 'reda', 'omar']
print(names[0])
print(names[2])
print(names[-1])#omar
print(names[-4])#idriss

names[0]='idrissUpdated'#mutable
names.append('simo')
names.insert(2, 'hamada')#add element to a specific index
names.remove('simo')#remove the first occurence of this value
print(names.index('ali'))
print(len(names))
print(names.count('reda'))
names.reverse()
print(names)
names.pop(1)#without index remove the last item
print(names)
for name in names:
  print(name)

#Tuples(fixed and immutable)
ip_iddress=('127.0.0.1', 8000)
one_member_tuple=('only member',)
one_member_tuple=tuple(['only member'])

#dictionnaries(resembles JSON syntax)
state_capitals = {
  'arkansas':'little rock',
  'colorado':'denver',
  'california':'sacramento',
  'georgia':'atlanta'
}
print(state_capitals['colorado'])
for k in state_capitals.keys():
  print('{} is the capital of {}'.format(state_capitals[k], k))

#set(no repeats, some things are goruped together, no insertion order)
first_names = {'adam', 'rayan', 'ranya'}

my_list = [1,2,3]
my_set = set(my_list)

if 'rayan' in first_names:
  print('found')

#defaultdict(default value for keys, never raise a keyError)
from collections import defaultdict
state_capitals = defaultdict(lambda:'Boston')
state_capitals['arkansas']='little rock'
state_capitals['california']='sacramento'
state_capitals['colorado']='denver'
print(state_capitals['alabama'])#Boston


