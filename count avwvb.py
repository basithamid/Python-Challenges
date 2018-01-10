str1 = input()
min_count = 0
max_count = 0
v_count = 0

for char in str1:
    if char is not 'w' and char is not 'v':
        min_count = min_count + 1
        max_count = max_count + 1

    elif char is 'w':
        min_count = min_count + 1
        max_count = max_count + 2

    elif char is 'v':
        max_count = max_count + 1
        if v_count == 0:
            v_count = v_count + 1
            min_count = min_count + 1

        elif v_count == 1:
            v_count = 0


print("min count {}".format(min_count))
print("max count {}".format(max_count))
