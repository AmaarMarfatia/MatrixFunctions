# MatrixFunctions
Python package for working with 2d arrays/matrices

## Purpose
I am learning Python and this project is to help me practice my fundamentals.

## How to use
Copy the `matrixFuncs` folder into your project folder to import and use

### Matrix/Vector Multiplication
```python
from matrixFuncs.multiply import multiply

a = [[1, 2, 3],[4,5,6]]
b = [[1, 2], [3, 4],[5,6]]
print(multiply(a, b))
```

### Matrix/Vector Addition
```python
from matrixFuncs.add import add

a = [[1, 2, 3],[4, 5, 6]]
b = [[1, 2, 3],[4, 5, 6]]
print(add(a, b))
```

### Matrix/Vector Subtraction
```python
from matrixFuncs.subtract import subtract

a = [[4, 5, 6],[4, 5, 6]]
b = [[1, 2, 3],[1, 2, 3]]
print(subtract(a, b))
```

### Matrix Determinant
```python
from matrixFuncs.determinant import determinant

a = [[1,2,3],[4,5,6],[7,8,9]]
print(determinant(a))
```