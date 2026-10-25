import random

def randInt(min_num=0, max_num=100):

    return round(random.random() * (max_num - min_num) + min_num)

print(randInt())                         
print(randInt(max_num=50))               
print(randInt(min_num=50))                
print(randInt(min_num=50, max_num=500))   