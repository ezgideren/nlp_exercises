import math


query = [1,1]

#Hardcoded two different vectors as follows
doc1 = [3,5,5]
doc2 = [6,4,7]

first_sq_length = 0
second_sq_length = 0

len_query = len(query)


#Estimating the distance and calculating the square(degree of 2) of the input.
for index in range(0, len_query):
    first_sq_length += math.pow((doc1[index] - query[index]), 2)

for index in range(0, len_query):
    second_sq_length += math.pow(doc2[index] - query[index], 2)
    
print (math.sqrt(first_sq_length))
print (math.sqrt(second_sq_length))

if second_sq_length > first_sq_length:
    print ("Doc 2 is closer")

else:
    print ("Doc 1 is closer")


