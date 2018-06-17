"""
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025- 385 = 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

# Method 1
start = 1
end = 10

# Calculate square of sums
sum = 0
a = start
while a <= end:
    sum += a
    a += 1

sqSum = sum**2

# Calculate sum of squares
sumSq = 0
b = start
while b <= end:
    sumSq += b**2
    b += 1

diff = (sqSum - sumSq)

print diff




"""
# Method 2 - thought trying something out with the maths might make it faster, but I was very wrong
end =  

nums = range(1,end+1)
sum = 0

for i in range(1,end+1):    # won't work if range(1,end+1) is replaced by nums, since nums changes after each loop and so only odd i's will be removed
    nums.remove(i)
    for n in nums:
        sum += n*i
print sum*2

Reasoning behind method 2:
(a + b + c +...)^2 - (a^2 + b^2 + c^2 +...) = 2(ab + ac + bc +...)

"""