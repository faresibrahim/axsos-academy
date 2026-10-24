# biggie size
# def biggie(list):
#   n=len(list)
#   for x in range(0, n, 1):
#     if(list[x] > 0):
#       list[x]="big"
#   return list

# li=[-1,3,5,-5]
# newList=biggie(li)
# print(newList)  


# Count Positives
# def count(list):
#   n=len(list)
#   result=0
#   for x in range(0, n ,1):
#     if(list[x] > 0):
#       result += 1
#   list[n-1] = result
#   return list

# li = [-1,1,1,1]
# newList=count(li)
# print(newList)


#Sum Total
# def sum(list):
#   n=len(list)
#   result=0
#   for x in range(0,n,1):
#     result += list[x]
#   return result

# li=[1,2,3,4]
# result=sum(li)
# print(result)

#Average
# def average(list):
#   n=len(list)
#   sum=0
#   for x in range(0,n,1):
#     sum += list[x]
#   result=sum/n
#   return result

# li=[1,2,3,4,5]
# res=average(li)
# print(res)

#Length
# def length(list)
#   n=len(list)
#   return n

#Minimum
# def min(list):
#   minVal=list[0]
#   n=len(list)
#   for x in range(0,n,1):
#     if(list[x]<minVal):
#       minVal=list[x]
#   return minVal

# li=[37,2,1,-9]
# res=min(li)
# print(res)


#Maximum
# def max(list):
#   maxVal=list[0]
#   n=len(list)
#   for x in range(0,n,1):
#     if(list[x]>maxVal):
#       maxVal=list[x]
#   return maxVal

# li=[37,2,1,-9]
# res=max(li)
# print(res)

#Ultimate Analysis
# def ultimateAnalysis(list):
#   n=len(list)
#   my_dict = {}
#   min=list[0]
#   max=list[0]
#   sum=0
#   for x in range(0,n,1):
#     sum += list[x]
#     if(list[x]>max):
#       max=list[x]
#     elif(list[x]<min):
#       min=list[x]
#   average = sum/n
#   my_dict = {
#     "length": n,
#     "minimum": min,
#     "maximum": max,
#     "sum total": sum,
#     "average": average
#   }
#   return my_dict

# li=[37,2,1,-9]
# dict=ultimateAnalysis(li)
# print(dict)

#Reverse List
# def reverse(list):
#   n=len(list)
#   x=0 #1st index
#   y=n-1 #2nd index
#   for i in range(n//2):
#     temp=list[x]
#     list[x]=list[y]
#     list[y] = temp
#     x+=1
#     y-=1
#   return list

# li=[37,2,1,-9]
# newList=reverse(li)
# print(newList)
  




