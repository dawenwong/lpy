print('yield')

def testyield():
    for i in range(5):
        yield i*i
 
 
generator = testyield()
g = testyield()
 
val = next(generator)
print(type(g))