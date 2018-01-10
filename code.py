str1 = input()
min_count = 0
max_count = 0
v_count = 0

for char in str1:
    if char is not 'w' and char is not 'v':
        min_count = min_count + 1
        max_count = max_count + 1
        new_str = new_str + char
    elif char is 'w':
        min_count = min_count + 1
        max_count = max_count + 2
        new_str = new_str + "vv"
    elif char is 'v':
        max_count = max_count + 1
        v_count = v_count + 1
        if v_count == 2:
            v_count = 0
            min_count = min_count + 1


print("min count {}".format(min_count))
print("max count {}".format(max_count))
