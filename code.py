str1 = input()
min_count = 0
max_count = 0
new_str = ""

for char in str1:
    if char is not 'w':
        max_count = max_count + 1
        new_str = new_str + char
    else:
        max_count = max_count + 2
        new_str = new_str + "vv"

v = 0
for char in new_str:
    if char is not 'v':
        min_count = min_count + 1
    elif char is 'v':
        if v == 0:
            v = 1

        elif v == 1:
            min_count = min_count + 1
            v = 0

print("min count {}".format(min_count))
print("max count {}".format(max_count))