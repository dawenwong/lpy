# def get_info():
    # name="wong"
    # age = 30
    # return name,age
 
def get_num():
    return 1,2,3,4,5,6,7,8,9,10,11
# name,age = get_info()
# info = get_info()

#num1,num2,num3 = get_num()
#print(num1,num2,num3)
nums = get_num()
num = [num for num in nums]
print(num)
print(type(nums))
# print()
# print(type(info))

a = (1,2,3,4,5,6,7,8)  #创建tuple
#print(type(a))
b = (8)
#print(8*b) #64
c = (8,)

print(8*c)  #(8,8,8,8,8,8,8,8)


#真加
temp = ("小明","小红","小张")
temp = temp[:2]+("小米",)+temp[2:]   #("小米",)逗号是必须的
print(temp)

#减少
temp = ("小明","小红","小米","小张")
temp = temp[:2]+temp[3:]
print(temp)