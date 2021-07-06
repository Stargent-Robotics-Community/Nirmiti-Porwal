# create a list of your fav tv shows and movies. after creating the list of at least 4 items,
# iterate over the whole list and print it's elements

fav_shows = ["Money heist", "friends", "up", "harry potter", "dark", "peaky blinders", "rock n key"]
for x in fav_shows:
    print(x)

# now ask the user to enter 2 of his favourite tv shows .take that as input and then use the append() function
# to add those  inputs into the the list

shows = input("enter two of your fav shows:-")
fav_shows.append(shows)
print(fav_shows)

# use slicing to print every 2nd element from the list starting from the second element.

num = ["2", "4", "6", "7", "8", "9", "1", "2", "3"]
print(num[1::2])

# create a list of 5 integers and use a while loop to calculate their sum

add = 0
numbers = [2, 4, 6, 7, 8]
i = 0
while i < len(numbers):
    add = add + numbers[i]
    i = i + 1
    print(add)

# print the following pattern using loop
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print(' ')
