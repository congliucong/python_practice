# coding=UTF-8


class Robot:
    """表示有一个带有名字的机器人。"""

    # 一个类变量，用来计数机器人的数量
    population = 0

    def __init__(self, name):
        self.name = name
        print("(Initializing {})".format(self.name))

        Robot.population += 1

    def die(self):
        print("{} is being destroyed!".format(self.name))

        Robot.population -=1
        if Robot.population == 0:
            print("{}	was	the	last	one.".format(self.name))
        else:
            print("There are still {:d}	robots	working.".format(Robot.population))

    def say_hi(self):
        print("Greetings,	my	masters	call	me	{}.".format(self.name))

    def say_self(self):
        print("！！！", self.population)

    @classmethod
    def how_many(cls):
        print("We	have	{:d}	robots.".format(cls.population))


droid1 = Robot("aa-aa")
droid1.say_hi()
droid1.say_self()
Robot.how_many()

droid2 = Robot("bb-bb")
droid2.say_hi()
droid2.say_self()
Robot.how_many()

droid1.die()
droid2.die()
Robot.how_many()

