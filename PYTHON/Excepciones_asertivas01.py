# Module Imports

from types import *
import pandas as pd
import numpy as np
from collections import Iterable

# Igual o no igual a valor

assert 1 == 1 # Success example

assert 5 == 2, "5 is not equal to 2" # Failure example

--------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last) 
<ipython-input-1-9b2f9d5d7e2b> in <module>
----> 1 assert 5 == 2, "5 is not equal to 2"


AssertionError:

assert 5 != 2  # Succes example

assert 1 != 1, "1 is equal to 1" # Failure example

--------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
<ipython-input-2-9b2f9d5d7e2b> in <module>
----> 1 assert 1 != 1, "1 is equal to 1" # Fail example

# type() is [valor]

assert type(1) is int # Success example

assert type(1) is not int, "1 is not an integer" # Failure example

--------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)

<ipython-input-3-9b2f9d5d7e2b> in <module>
----> 1 assert type(1) is not int, "1 is not an integer" # Failure example

AssertionError:

# isinstance

assert type(1) is int # Success example

assert type(1) is not int, "1 is not an integer" # Failure example

--------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)

<ipython-input-3-9b2f9d5d7e2b> in <module>
----> 1 assert type(1) is not int, "1 is not an integer" # Failure example

AssertionError:

# is [tipo booleano]

assert True is True # Success example

assert True is False, "True is not False" # Failure example

--------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)

<ipython-input-5-9b2f9d5d7e2b> in <module>
----> 1 assert True is False, "True is not False" # Failure example

AssertionError:

# in y not in [iterable]

list_one = [1, 3, 5, 6]

assert 5 in list_one # Success example
assert 2 in list_one, "2 is not in list_one" # Failure example

--------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)

<ipython-input-6-9b2f9d5d7e2b> in <module>
----> 1 assert 2 in list_one, "2 is not in list_one" # Failure example

AssertionError:

# mayor o menor que [valor]

assert 5 > 2 # Success example

assert 2 > 5, "2 is not greater than 5" # Failure example

--------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)

<ipython-input-7-9b2f9d5d7e2b> in <module>
----> 1 assert 2 > 5, "2 is not greater than 5" # Failure example

AssertionError:

assert 2 < 5 # Success example

assert 5 < 2, "5 is not less than 2" # Failure example

--------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)

<ipython-input-8-9b2f9d5d7e2b> in <module>

----> 1 assert 5 < 2, "5 is not less than 2" # Failure example

AssertionError:

__________________________________________________________________________

# El módulo % es igual a [valor]

assert 2 % 2 == 0 # Success example

assert 3 % 2 == 0, "3 % 2 is not equal to 0" # Failure example

--------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)

<ipython-input-9-9b2f9d5d7e2b> in <module>
----> 1 assert 3 % 2 == 0, "3 % 2 is not equal to 0" # Failure example

AssertionError:

__________________________________________________________________________

# declaración de afirmación any()

example = [5,3,1,6,6]
booleans = [False, False,True, False]
>>> any(example)
True
>>> any(booleans)
True

assert any(example) == True # Success example
assert any(booleans) == True # Success example

__________________________________________________________________________

# declaración de afirmación all()

>>> all(example)
True
>>> all(booleans)
False

assert all(example) # Success Example
assert all(booleans) # Failure Example

--------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)

<ipython-input-12-9b2f9d5d7e2b> in <module>
----> 1 assert all(booleans) # Failure Example

AssertionError:

__________________________________________________________________________

# Objetos personalizados

type(object).__name__
df = pd.DataFrame()

>>> type(df).__name__

'DataFrame'

type(df).__name__ == 'DataFrame' # True Boolean
type(df).__name__ is 'DataFrame' # True Boolean
type(df).__name__ == type([]).__name__ # False Boolean
type(df).__name__ is type([]).__name__ # False Boolean
assert type(df).__name__ == 'DataFrame' # Success example
assert type(df).__name__ ==type([]).__name__, "df is not equal to list" # Failure example

--------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)

<ipython-input-13-9b2f9d5d7e2b> in <module>
----> 1 assert type(df).__name__ ==type([]).__name__, "df is not equal to list" # Failure example

AssertionError:

__________________________________________________________________________

# Iterables

from collections.abc import Iterable
Iterable_item = [3,6,4,2,1]

>>> isinstance(Iterable_item, Iterable)
True

>>> isinstance(5, Iterable)
False

assert isinstance(Iterable_item, Iterable) # Success example
assert isinstance(5, Iterable) # Failure example

--------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)

<ipython-input-14-9b2f9d5d7e2b> in <module>
----> 1 assert isinstance(5, Iterable) # Failure example

AssertionError:

__________________________________________________________________________

# Combinación de varias declaraciones and/or con declaraciones de afirmación

true_statement =  5 == 5 and 10 == 10
false_statement = 5 == 3 and 10 == 2

print(true_statement, false_statement)
True False
assert true_statement # Success example
assert false_statement, "false_statement is not True" # Failure example

--------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)

<ipython-input-15-9b2f9d5d7e2b> in <module>
----> 1 assert false_statement, "false_statement is not True" # Failure example

AssertionError:

__________________________________________________________________________

true_statement =  5 == 5 or 10 == 10
false_statement = 5 == 3 or 10 == 2

>>> print(true_or_statement, false_or_statement)
True False
assert true_statement # Success example
assert false_statement, "false_statement is not True" # Failure example

--------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)

<ipython-input-16-9b2f9d5d7e2b> in <module>
----> 1 assert false_statement, "false_statement is not True" # Failure example

AssertionError:

__________________________________________________________________________

# Prueba de varios comandos

class Test(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def test_all_class_arguments(self):
        print('Testing both of the class variables '
        'to see whether they are both strings!')

        for _ in [self.first_name, self.last_name]:
            assert (type(_) is str)
        print('----')
        print('Passed all of the test')
yay = Test('James', 'Phoenix') # Success example
yay.test_all_class_arguments()

Testing both of the class variables to see whether they are both strings!

----
Passed all of the tests

yay = Test(5 , 'Phoenix') # Failure example
yay.test_all_class_arguments()

Testing both of the class variables to see whether they are both strings!

--------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)

<ipython-input-17-9b2f9d5d7e2b> in <module>

1 yay = Test(5 , 'Phoenix') # Failure example
----> 2 yay.test_all_class_arguments()

<ipython-input-16-9b2f9d5d7e2b> in test_all_class_arguments(self)
8
9   for _ in [self.first_name, self.last_name]:
    10    assert (type(_) is str)
11   print('----')
12   print('Passed all of the test')

AssertionError:

__________________________________________________________________________

# Escribir declaraciones de afirmación

class Example():
    def __init__(self, id_, name):
        self.id_ = id_
        self.name = name

    def subtract(self):
        answer = 5 + 5
        return answer
    
    def test_lambda_function(self):
        assert (lambda x: x is LambdaType)

    def test_subtract_function(self):
        assert(self.subtract is LambdaType)
example_class = Example("123", 'James Phoenix') # Success example 

>>> print(example_class._id, example_class.name)
123 James Phoenix

__________________________________________________________________________

example_class.test_lambda_function() # Failure example
example_class.test_subtract_function() # Failure example

--------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)

<ipython-input-19-9b2f9d5d7e2b> in <module>
----> 1 example_class.test_subtract_function() # Success example

<ipython-input-18-9b2f9d5d7e2b> in test_subtract_function(self)
14
15 def test_subtract_function(self):
    16 assert(self.subtract is LambdaType)

AssertionError:




