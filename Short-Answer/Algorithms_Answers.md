#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
```python
a)  a = 0                   # O(1)
    while (a < n * n * n):  # O(n) * O(1)
      a = a + n * n         # O(1)
```
The _a_ assignment is a constant of O(1) in both instances.
The while loop is of _O(n)_.
The entire runtime of this code will thus be **O(n)** after removing all instances of constants.

b)
```python
b)  sum = 0             # O(1)
    for i in range(n):  # O(n) * O(1)
      j = 1             # O(1)
      while j < n:      # O(n) * O(n!)
        j *= 2          # O(n!)
        sum += 1        # O(n)
```
The `sum` assignment has a constant runtime - _O(1)_.
The `for` loop has an _O(n)_ runtime because what follows it is an assignment of _1_ to _j_ which is a constant.
The while loop has _O(n) * O(n!)_ because of the multiplying of j by 2 which will increase and keep running as n increases or is more than j.
The final sum assignment is _O(n)_ as the sum will keep running/incrementing based on the _n_.
This algorithm has a runtime of Factorial **O(n!)**

c)
```python
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```
The function call `bunnyEars` is a constant of O(1).
The if condition and its return statement are also constants of O(1).
The last return statement makes a recursive call of `bunnies` times till it meets the base condition. Each call performs one operation of (bunnies - 1) which is a constant. This is thus O(n).
Summing it all up, we have:
```
O(1) + O(1) + O(1) + O(n)
```
The runtime of `bunnyEars` is **O(n)**

## Exercise II
let n = number of floors
let e = egg to be thrown
let f - 1 = optimal height at which egg is not broken

1. Find median of n
2. Split n into 2 halves based on the median - n1 and n2
3. At each median of n1 and n2, throw egg
4. If egg breaks in n1, it means f - 1 is not in n1
    i. Repeat steps 1 to 3 till egg does not break

5. If egg breaks in n2, discard this case
    If not, Repeat steps 1 to 3 till egg does not break
6. Once we discover egg does not break in a particular case or set  
    Repeat steps 1 to 3 to find the optimal point at which we can throw the most eggs

The runtime of this algorithm is **O(log n)** since we recurse based on the median of the given n
