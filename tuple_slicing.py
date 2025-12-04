my_tuple = (10, 20, 30, 40, 50, 60, 70, 80, 90)
slice1 = my_tuple[2:6]
print(f"Slice 1 (my_tuple[2:6]): {slice1}")
slice2 = my_tuple[:4]
print(f"Slice 2 (my_tuple[:4]): {slice2}")  
slice3 = my_tuple[5:]
print(f"Slice 3 (my_tuple[5:]): {slice3}") 
slice4 = my_tuple[:]
print(f"Slice 4 (my_tuple[:]): {slice4}")  
slice5 = my_tuple[1:8:2]
print(f"Slice 5 (my_tuple[1:8:2]): {slice5}") 
slice6 = my_tuple[-4:-1]
print(f"Slice 6 (my_tuple[-4:-1]): {slice6}") 
slice7 = my_tuple[::-1]
print(f"Slice 7 (my_tuple[::-1]): {slice7}")  