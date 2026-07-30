name = "Nusrat"
# this is call slicing in python
nameshort = name[0:3] #start from index 0 all the way till 3 (excluding 3)
print(nameshort)
character1 = name[1]
print(character1)


# negative slicing

name1 = "Harry"

print(name1[0:3])

print(name1[-4:-1])
print(name1[1:4]) # is same as print (name1[-4:-1])

print(name1[:4]) #is same as print(name1[0:4])
print(name1[1:]) #is same as print(name1[1:5])
print(name1[1:5]) # is same as print(name1[1:])


# slicing with skip value

word = "amazing"
print(word[1:6:3])

#other advanced slicing techniques

word1 = "Beautiful"
print(word1[:7]) # word[0:7] = Beutif
print(word1[0:]) # word[0:7] = Beautiful
