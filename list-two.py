x = object()
y = object()

x_list = [x] * 10  # create 10 instances of the variable x
y_list = [y] * 10  # create 10 instances of the variable y
big_list = x_list + y_list


print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")

# The target of this exercise is to create two lists called x_list and y_list,
# which contain 10 instances of the variables x and y, respectively.
# This code also creates another list called big_list,
# which contains the variables x and y, 10 times each, by adding the two lists created previously together.
