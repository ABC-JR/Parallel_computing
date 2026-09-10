# Aglanbek Baglanbek   04 -P





#task 1



x = 5
y = 2

x = x +y
y = x*2
x =  y-x
print(x , y)

# answer is 7 14



numbers = [10, 20, 30, 40, 50]
total = 0
for i in range(len(numbers)):
    total += numbers[i]
print(total)

# here i could have to calculate total number instead we on the code total equling to just number btw total is 150





for i in range(10):
    for j in range(10):
        print(i, j)


# a )  10 × 10 = 100


# b  1000 × 1000 = 1,000,000


# c   10 × 1,000,000 = 10,000,000





# task  4


# of course which first algortihm because he take o(n) time  second one o(n**2)




# n² log₂n n nlog₂n 1 2ⁿ


#  1 log₂n   nlog₂n n  n²   2ⁿ


#   2ⁿ  become particularly problematic when n becomes much larger





# task 6

#    if you do not know the list is sorted;       o(n)

#  if you know it is sorted.  log(n)


# why becase on the first  we have to search each elements it takes n times but second it is already sorted that why dividing comparing whith near elements we taking the side like we doing some search then we would have figure it






# task 7

# we do like this time o(n)  aa space is o(1)

max  = float('-inf')

for i in range(len(numbers)):
    if(max < numbers[i]):
        max = numbers[i]


print(max)

# we did it


# task 8
# I would use a dictionary/hash map.



