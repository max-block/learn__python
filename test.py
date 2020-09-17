from typing import List, Type, TypeVar

T = TypeVar("T", bound="Base")


class Base2:
    var2 = []

    @classmethod
    def fun1(cls, data) -> List[T]:
        cls.var2.append(1)


class Base:
    var1 = []

    @classmethod
    def fun1(cls: Type[T]) -> List[T]:
        cls.var1.append(1)  # Pycharm тут не видит, что у cls есть var1
        return [cls(), cls()]


class A(Base):
    pass


print(A.fun1())  # -- список объектов класса A
