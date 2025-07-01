# Problem-2: With a single integer as the input, generate the following until a = x [series of numbers as shown in below examples]
 
#   Output: (examples)
#     1) input a = 1, then output : 1
#     2) input a = 2, then output : 1, 3
#     3) input a = 3, then output : 1, 3, 5
#     4) input a = 4, then output : 1, 3, 5, 7
#     .
#     .
#     5) input a = x, then output : 1, 3, 5, 7, .......

# ----------------------------------------------

def first_n_odd(a):
    series = []
    for i in range(a):
        series.append(2 * i + 1)
    return ", ".join(map(str, series))

a = int(input("Input a =  "))
print(first_n_odd(a))


# Output:
# Input a =  1
# 1
# Input a =  2
# 1, 3
# Input a =  3
# 1, 3, 5
# Input a =  4 
# 1, 3, 5, 7
# Input a =  5
# 1, 3, 5, 7, 9