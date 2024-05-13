# num = 3
# W = 65000
# kg = {
#     1: 1,
#     2: 0.000001,
#     3: 0.001,
#     4: 1000,
#     5: 100
# }
# result = W * kg[num]
# print(result)

num = 3
w = 65000
if num == 1:
    print(w)
elif num == 2:
    print(w / 1000000)
elif num == 3:
    print(w / 1000)
elif num == 4:
    print(w * 1000)
elif num == 5:
    print(w * 100)