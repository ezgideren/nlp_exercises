import math

#dot product is the sum of the coordinate products of the two vectors taken along each dimension.
#cosine(vec1, vec2) = doc_product(vec1,vec2)/(length(vec1)*length(vec2))

query = [1,1]

#Hardcoded two different vectors as follows
doc1 = [3,5]
doc2 = [6,4]

#length is calculated by the euclidean distance and 0,0 is omitted. For complex version see euclidean_distance.py. 
def length(vector):
    sq_length = 0
    for index in range(0, len(vector)):
        sq_length += math.pow(vector[index], 2)
    return math.sqrt(sq_length)

def dot_product(vector1, vector2):
    if len(vector1)==len(vector2):
        dot_prod = 0
        for index in range(0, len(vector1)):
            dot_prod += vector1[index]*vector2[index]
        return dot_prod
    else:
        return "Unmatching dimensionality"
    
cosine = dot_product(query,doc1)/(length(query)*length(doc1))
print(cosine)