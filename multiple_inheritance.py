class Father():

    def gardening(self):
        print("I enjoy gardening")


class Mother():

    def cooking(self):
        print("I love cooking")


class Child(Father, Mother):

    def sport(self):
        print("I enjoy sports")


c = Child()
c.gardening()
c.cooking()
c.sport()