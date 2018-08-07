import sys


print('The	command	line	arguments	are:')
for i in sys.argv:
    print(i)

print('\n\nThe	PYTHONPATH	is', sys.path, '\n')

#  一般来说，你应该尽量避免使用		from...import		语句，而去使用		import		语句。 这是为了避免在你的程序中出现名称冲突，同时也为了使程序更加易读

if _name_ == '_main_':
    print('This	program	is	being	run	by	itself')
else:
    print('I	am	being	imported	from	another	module')
