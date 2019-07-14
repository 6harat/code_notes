# sources:

* data types:
- https://docs.python.org/3/library/stdtypes.html#set

* global interpreter lock:
- https://www.youtube.com/watch?v=Obt-vMVdM8s

* new features:
- https://www.python.org/dev/peps/pep-0567/
- https://www.python.org/dev/peps/pep-0492/
- https://www.python.org/dev/peps/pep-0487/

* collections:
- https://docs.python.org/3.3/library/collections.html
- https://github.com/topper-123/Articles/blob/master/New-interesting-data-types-in-Python3.rst

* descriptors:
- https://www.blog.pythonlibrary.org/2016/06/10/python-201-what-are-descriptors/
- http://martyalchin.com/2007/nov/23/python-descriptors-part-1-of-2/

* colored print statements:
- https://www.geeksforgeeks.org/print-colors-python-terminal/

* interfaces and duck typing:
    - http://masnun.rocks/2017/04/15/interfaces-in-python-protocols-and-abcs/
    - https://stackoverflow.com/questions/37363764/python3-abstract-class-typeerror-not-raised


* decorators:
    ```python
    def collect_args_passed_to_decorator(*dargs):
        def collect_func_to_be_decorated(func):
            @functools.wraps(func)
            def collect_args_kwargs_passed_to_func(*args, **kwargs):
                """
                functools.wraps copies the name, module, and docstring of the decorated function to its wrapper providing much more legible stack trace
                ref: https://gist.github.com/Zearin/2f40b7b9cfc51132851a#best-practices-decorators
                """
                return func(*args, **kwargs)
            return collect_func_to_be_decorated
        return collect_args_passed_to_decorator
    ```

* code_style: https://docs.python-guide.org/writing/style/#zen-of-python
* itertools: https://docs.python.org/3/library/itertools.html#recipes
* dev_only_dependencies: https://stackoverflow.com/questions/28509965/setuptools-development-requirements
* python_code_objects: https://late.am/post/2012/03/26/exploring-python-code-objects.html
* data_classes: 
    https://www.geeksforgeeks.org/data-classes-in-python-an-introduction/
    https://www.geeksforgeeks.org/data-classes-in-python-set-2-decorator-parameters/
* patterns: https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Metaprogramming.html
* internals:
    https://leanpub.com/insidethepythonvirtualmachine/read
    dynamic_programming_languages:
        http://pgbovine.net/cpython-internals.htm
        https://www.youtube.com/playlist?list=PLzV58Zm8FuBL6OAv1Yu6AwXZrnsFbbR0S
        https://medium.com/@dawran6/getting-started-with-python-internals-a5474ccb8022
    https://stackoverflow.com/questions/3298464/how-can-i-learn-more-about-python-s-internals
    https://akaptur.com/blog/2014/08/03/getting-started-with-python-internals/
* metaclasses: https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python?noredirect=1&lq=1
* slots:
    https://stackoverflow.com/questions/472000/usage-of-slots
    http://book.pythontips.com/en/latest/__slots__magic.html
* style_guide: https://google.github.io/styleguide/pyguide.html
* types: https://docs.python.org/3/library/types.html?highlight=types#module-types
* immutability:
    - nothing should be instantiated in __init__
        ```python
        class Buggy:
            def __init__(self, a, b):
                self._a = a
                self._b = b
            @property
            def a(self):
                return self._a
            @property
            def b(self):
                return self._b
        ```
        the above pattern breaks easily as follows:
        ```python
        g = Buggy(1, 2)
        g.a                 # 1
        g.a = 4             # throws attribute error
        g.__init__(4, 7)    # executes without error and modifies the state
        g.a                 # 4
        ```
    - namedtuple not to be used:
        ```python
        from collections import namedtuple
        fruit = namedtuple('fruit', 'name price')
        crayon = namedtuple('crayon', 'name length')
        orange_fruit = fruit('orange', '23')
        orange_crayon = crayon('orange', '23')
        orange_fruit == orange_crayon           # True, as the comparison is based on tuple
        ```
        ```python
        from collections import namedtuple
        user = namedtuple('user', 'name age')
        superuser = namedtuple('superuser', user._fields + ('city',))
        u = user('bharat', 26)
        s = superuser('gulati', 25, 'delhi')
        isinstance(s, user)                     # False, which breaks multiple inheritance
        ```
        ```python
        class user(namedtuple('user', 'name age')):
            def prettyprint(self):
                return '{} is {} year(s) old'.format(self.name, self.age)

        class superuser(namedtuple('superuser', user._fields + ('city',)), User):
            def prettyprint(self):
                return '{} is {} year(s) old and lives in {}'.format(
                    self.name,
                    self.age,
                    self.city
                )
        u = user('bharat', 26)
        s = superuser('gulati', 25, 'delhi')
        isinstance(s, user)                     # True, resolves inheritance issue but not equality
        ```
        ```python
        from dataclasses import dataclass

        @dataclass(frozen=True)
        class User:
            name: str
            age: int
            def prettyprint(self):
                return '{} is {} year(s) old'.format(
                    self.name, self.age
                )

        @dataclass(frozen=True)
        class SuperUser(User):
            city: str
            def prettyprint(self):
                return '{} is {} year(s) old and lives in {}'.format(
                    self.name, self.age, self.city
                )
        u = User('bharat', 24)
        s = SuperUser('gulati', 25, 'delhi')
        u.age = 27                              # prevents modification
        isinstance(s, User)                     # supports inheritance
                                                # preserves equality check
        u.__init__('hamitlon', 44)              # immutability breaks


        # another similar flavour of the above one is using `attr`
        import attr

        @attr.s(frozen=True)
        class Driver:
            name: str = attr.ib()
            car_num: int = attr.ib()
        
        v = Driver('vettel', 5)
        v.name = 'hamilton'                     # prevents modification
        v.__init__('hamilton', 44)              # immutability breaks
        ```
* hashing:
    - if an object is used as a key it should be immutable.
        ```python
        from dataclasses import dataclass

        @dataclass(unsafe_hash=True)
        class User:
            name: str
            age: int

        d = {}
        u = User('bharat', 23)
        d[u] = 'great'
        d[u]    # prints 'great'
        u.name = 'gulati'
        d[u]    # throws 'KeyError'
        ```
    - all sub-properties of the object to be hashed should be hashable.
        ```python
        from dataclasses import dataclass
        d = {}
        @dataclass(frozen=True)
        class User:
            name: str
        u = User('bharat', 23)
        d[u] = 'great'          # works as all properties of User are immutable => hashable
        class Superuser:
            name: str
            tags: list
        s = Superuser('gulati', 25, ['coder'])
        d[s] = 'not-so-great'   # does not work as list(mutable) is unhashable
        ```
* __new__ vs __init__
* old-style classes (sub-class of `type`) vs new-style classes (sub-class of `object`)
* visualize python code: http://pythontutor.com/visualize.html#mode=edit

* proxy pattern:
    - http://code.activestate.com/recipes/496741-object-proxying/

* dunder methods:
    - https://github.com/RafeKettler/magicmethods
    - https://docs.python.org/3/reference/datamodel.html#special-method-names

* asyncio_vs_tornado:
    - https://github.com/universe-proton/universe-topology/issues/14