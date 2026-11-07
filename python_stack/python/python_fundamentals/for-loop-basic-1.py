# # Basics
# for x in range(0, 151, 1):
#   print(x)

# Multiple of 5s
# for x in range(1,201, 1):
#   print(x*5)


# Counting, the dojo way
# for x in range(0, 101, 1):
#   if(x%10 == 0):
#       print(x, "Coding Dojo")
#   elif(x%5 == 0):
#     print(x, "Coding")
#   else:
#     print(x)


# # Whoa, that sucker's huge
# result=0
# for x in range(0,500001, 1):
#    if(x%2 != 0):
#       result += x
# print(result) 


# # Countdown by Fours
# for x in range(2018, 0, -4):
#   print(x)

# Flexible Counter
lowNum=2
highNum=9
mult=3

for x in range(lowNum,highNum+1,1):
  if(x%mult == 0):
    print(x)