from abc import ABC, abstractmethod


class Parent(ABC):

    def common(self):
        print("we are at the parent")

    @abstractmethod
    def vary(self):
        pass


class Child1(Parent):
    def vary(self):
        print("we are at the vary method oc child1")


class Child2(Parent):
    def vary(self):
        print("we are at the vary method of child2")


# Calling the method from Child1 class
ob1 = Child1()
ob1.common()
ob1.vary()

# Calling the method from child2 class
ob2 = Child2()
ob2.common()
ob2.vary()