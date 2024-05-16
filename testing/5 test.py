class Book:
    def set_price(self, val):
        self._price = val + 1

    def get_price(self):
        return self._price +1
    
obj = Book()
obj.set_price(15)
print(obj.get_price())


'''
This code defines a class `Book` with two methods: `set_price` and `get_price`, along with an instance variable `_price`.

1. **Class Definition**: `class Book:` defines a class named `Book`.

2. **`set_price` Method**: 
   - `def set_price(self, val):` defines a method named `set_price` that takes two arguments, `self` (which refers to the instance of the class) and `val`.
   - `self._price = val + 1` sets the instance variable `_price` to `val + 1`. This means that when you call `set_price(15)` on an instance of `Book`, `_price` will be set to 16.

3. **`get_price` Method**:
   - `def get_price(self):` defines a method named `get_price` that takes only `self` as an argument.
   - `return self._price + 1` returns the value of `_price` plus 1. So, if `_price` is 16, `get_price` will return 17.

4. **Instance Creation and Method Calls**:
   - `obj = Book()` creates an instance of the `Book` class named `obj`.
   - `obj.set_price(15)` calls the `set_price` method on the `obj` instance with `val` set to 15.
   - `print(obj.get_price())` calls the `get_price` method on the `obj` instance and prints the returned value, which is 17 (since `_price` was set to 16 in `set_price` and then incremented by 1 in `get_price`).
'''