
# 1- UPDATE VALUES IN DICTIONARIES AND LISTS
# x=[[5,2,3],[10,8,9]]
# students=[
#   {'first_name': 'Michael', 'last_name':'Jordan'},
#   {'first_name': 'John', 'last_name':'Rosales'}
# ]

# sports_directory={
#   'basketball':['Kobe','Jordan','James','Curry'],
#   'soccer':['Messi','Ronaldo','Rooney']
# }

# z=[{'x':10, 'y': 20}]

# x[1][0]=15
# print(x)

# students[0]['last_name']='Bryant'
# print(students)

# sports_directory['soccer'][0]='Andres'
# print(sports_directory)


# 2- ITERATE THROUGH A LIST OF DICTIONARIES
# def iterateDictionary(some_list):
#   n=len(some_list)
#   for x in range(n):
#     for key, value in some_list[x].items():
#       print(key, "-", value)

# students = [
#     {'first_name': 'Michael', 'last_name': 'Jordan'},
#     {'first_name': 'John', 'last_name': 'Rosales'},
#     {'first_name': 'Mark', 'last_name': 'Guillen'},
#     {'first_name': 'KB', 'last_name': 'Tonel'}
# ]


# iterateDictionary(students)


# 3- GET VALUES FROM A LIST OF DICTIONARIES
# def iterateDictionary2(key_name, some_list):
#   n=len(some_list)
#   for x in range(n):
#     print(some_list[x][key_name])
      


# students = [
#     {'first_name': 'Michael', 'last_name': 'Jordan'},
#     {'first_name': 'John', 'last_name': 'Rosales'},
#     {'first_name': 'Mark', 'last_name': 'Guillen'},
#     {'first_name': 'KB', 'last_name': 'Tonel'}
# ]

# iterateDictionary2("first_name", students)
# iterateDictionary2("last_name", students)


# 4- ITERATE THROUGH A DICTIONARY WITH LIST VALUES
# def printInfo(some_dict):
#   n=len(some_dict)
#   for key, value in some_dict.items():
#     print(len(some_dict[key]), key)
#     for x in some_dict[key]:
#       print(x)

# dojo= {
#   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago'],
#   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham']
# }

# printInfo(dojo)

