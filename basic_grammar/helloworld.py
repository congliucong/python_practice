# 这是个注释
print("aaaaaaa")
age = 20
name = 'Swaroop'
# python 中的format 方法所做的事情将每个参数替换至格式所在位置
print('{0} was {1} years old when he wrote this book'.format(name, age))

# 在处理正则表达式时，应全程使用原始字符串

# 放置在一起的语句必须拥有同样的缩进
i = 5
print('value is ', i)
i = i + 6
print(i)

# 乘方
i = 2 ** 3
print(i)

# 整除 //
# 取模 %
# 左移<<  右移 >>  not 非 and  与 or 或

# if 语句
# number = 23
# guess = int(input('Wnter an interger :'))
# if guess == number:
#     print('a')
# elif guess<number:
#     print('b')
# else:
#     print('c')

# for 循环

for i in range(1, 5):
    print(i)
else:
    print('this loop is over')


# 函数定义 def
def say_hello():
    print('hello')


say_hello()


# global 语句 在不使用global语句的情况下 不能为定义与函数之外的变量赋值

# 默认参数值 在函数定义时附加一个赋值运算符来为参数指定默认参数值

# 关键字参数
def func(a, b=5, c=10):
    print('a is ', a, 'and b is ', b, 'and c is ', c)


func(3, 7)
func(25, c=24)
func(c=50, a=100)


# 可变参数 使用*来实现
def total(a=5, *numbers, **phonebook):
    print('a', a)

    # 遍历元祖中的所有项目
    for single_item in numbers:
        print('single_item', single_item)

    # 遍历字典中的所有项目
    for first_part, sencod_part in phonebook.items():
        print(first_part, sencod_part)


print(total(10, 1, 2, 3, jach=1123, john=2231, Inga=1560))
