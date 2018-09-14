#python 3.5.2

Y1 ={ 'bb':11}

Y10 = {'hhh':555}

Y7 = { 'ff':44, 'gg': Y10}

Y = {'a': Y1, 'c':2, 'd':3, 'e': Y7 }

print(Y)

'''
OUTPUT:

{'a': {'bb': 11}, 'c': 2, 'd': 3, 'e': {'gg': {'hhh': 555}, 'ff': 44}}
'''