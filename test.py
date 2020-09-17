# x = '0.10'
# # x = '10'

# if '.' in x:
#   x = float(x)
# else:
#   x = int(x)
# # print(type(x))
# # print(x*2)

x = 8
x = x.replace(',', '')
x = x.replace('$', '')
x = int(x)
print(x)