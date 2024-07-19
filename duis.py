class MyClass:
    def __init__(self, c_value):
        self._c = c_value

    def c(self) -> int:
        return self._c

obj = MyClass(42)
result = obj.c()
print(result)  # Output: 42
