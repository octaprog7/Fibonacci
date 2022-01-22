from abc import ABC, abstractmethod


class MultiIter(ABC):
    """возвращает независимые(!) итераторы"""

    def __init__(self):
        """Обязательно вызывайте в наследниках!"""
        self.__iter_count = 0

    @abstractmethod
    def __next__(self):
        # часть протокола итератора
        ...

    @abstractmethod
    def make_instance(self):
        """return instance of class."""
        ...

    def __iter__(self):
        """Не переопределяйте в наследниках!"""
        # часть протокола итератора
        if 0 == self.__iter_count:  # первый вызов возвращает себя!
            self.__iter_count += 1
            return self
        else:  # последующие вызовы возвращают новый(!) экземпляр.
            return self.make_instance()


"""
class MyIter(MultiIter):
    def __init__(self):
        super().__init__()

    def make_instance(self):
        print("MyIter.make_instance")
        return MyIter()

    def __next__(self):
        print(f"MyIter.__next__ at {id(self)}")
"""

if __name__ == "__main__":
    pass
    # m = MyIter()
    # for i in range(10):
    #    print(iter(m))
