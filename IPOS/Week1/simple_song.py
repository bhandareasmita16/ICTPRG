# x = []
# x = list()
# # different type (heterogeneous)
# x = [True, 4.0, [4, 2, 3], "hello"]
# # mutable
# x.append(42)
# x[1] = 42
# # index 0
# # last element
# len(x) - 1
# x[-1] # last element
#
#
# x = [True, 4.0, [4, 2, 3], "hello", 1, 42, 5]
# x[4:]
# # y = x[:]
# y = x
#
# x = (4, 3, 2, 1) # tuple
#
# x = (True, [4, 2, 3], 3) # mixed
#
# x = "Rafael", "Avigad"
# first_name, last_name = x
#
# x = (255, 255, 0)
#
# x = {'a': 42, 'b': 343} #mutable
# x['b'] = 21
# x = {'a': 42, 'b': [4, 3, 2]}
# x = {'a': 42, 3: [4, 3, 2]}
# x = {'a': 42, (2, 3): [4, 3, 2]}
# color_descriptions = {(255, 0, 0): "red"}

x = [1, 2, [3, 4], "hello"]
y = x[2:]
y.append(5)
print(x)

x = [1, 2, [3, 4, "hello"]]
e = x[2][2][1]
x[2][2] = 'z'
print(e)

x = {3, 4, 5, 2}
x.add(6)
x.add(4)
x = set([2, 3, 4,5, 5, 5, 6, 7, 8])
len(x)