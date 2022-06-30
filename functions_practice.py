# Function simply prints a hello message
#
def hello() :
    print("\nHi Bro!\n")

# Function takes in 3 args and returns them in a list.
#
def pack(a, b, c):
    return [a,b,c]

# Function takes a list as input (ideally foods) and will print out the first food
# as "First I eat {food}" and the rest as "Next I eat {food}"
#
def eat_lunch(my_list):

    j = 0
    for i in my_list:
        if (j == 0):
            print("First I eat", i)
        else:
            print("Next I eat", i)
        j+=1


# Call all three functions
#
hello()
print(pack("aa", "bb", "cc"),"\n")
eat_lunch(["candy", "cereal", "fruit", "pizza"])

# Should print out:
# Hi Bro!
#
# ['aa', 'bb', 'cc']
#
# First I eat candy
# Next I eat cereal
# Next I eat fruit
# Next I eat pizza