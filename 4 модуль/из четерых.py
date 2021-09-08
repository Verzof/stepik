# # a = int(input())
# # b = int(input())
# # d = int(input())
# # c = int(input())
# #
# #
# # if a < b:
# #     a = b
# #
# # elif:
# #     a < c
# #     a = c
# # else:
# #     a < d
# #     a = d
# #
# # # if: a < b
# # #     a = b
# # #
# # # else:
# # #     a < d
# # #     a = d
# # #
# # # else:
# # #     a < c
# # #     a = c
# #
# # print(a)
# a = int(input())
# b = int(input())
# c = int(input())
# x = int(input())
#
# if (a < b) and (a < c) and (a < x):
#     print(a)
#
# if (b < a) and (b < c) and (b < x):
#     print(b)
#
# if (c < a) and (c < b) and (c < x):
#     print(c)
#
# if (x < b) and (x < b) and (x < c):
#     print(x)
#
#
#
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = min(a, b, c, d)
print(e)