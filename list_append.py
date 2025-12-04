my_list = [10, 20, 30]
print(f"Original list: {my_list}")
my_list.append(40)
print(f"List after appending 40: {my_list}")
my_list.append("hello")
print(f"List after appending 'hello': {my_list}")
another_list = [50, 60]
my_list.append(another_list)
print(f"List after appending another_list: {my_list}")
empty_list = []
for i in range(3):
    empty_list.append(f"item_{i+1}")
print(f"List built using append in a loop: {empty_list}")