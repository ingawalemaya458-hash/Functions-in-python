#1.Even or Odd Function Write a function is_even(n) that returns "Even" if the number is even, otherwise "Odd".

def is_even(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(is_even(4))  # Output: Even
print(is_even(7))  # Output: Odd

#2. Largest of Two Numbers- Write a function largest(a, b) that returns the larger number.

def largest(a, b):
    if a > b:
        return a
    else:
        return b
    
print(largest(10, 20))  # Output: 20
print(largest(30, 15))  # Output: 30

#3. Print Numbers- Write a function print_numbers(n) that prints numbers from 1 to n using a loop.

def print_numbers(n):
    for i in range(1, n + 1):
        print(i)
        
print_numbers(5)  # Output: 1 2 3 4 5

#4. Sum of Numbers- Write a function sum_n(n) that returns the sum of numbers from 1 to n.

def sum_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
print(sum_n(5))  # Output: 15

#5. Multiplication Table- Write a function table(n) that prints the multiplication table of n from 1 to 10.

def table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

table(5)  # Output: Multiplication table of 5

#6. Count Even Numbers- Write a function that takes a list and returns how many even numbers it contains.- Example:count_even([1, 2, 3, 4, 6]) Output:3

def count_even(lst):
    count = 0
    for num in lst:
        if num % 2 == 0:
            count += 1
    return count

print(count_even([1, 2, 3, 4, 6]))  # Output: 3

# 7. Find Maximum - Without using max(), write a function that returns the largest number in a list.

def find_maximum(lst):
    if not lst:
        return None  # Return None for empty list
    max_num = lst[0]
    for num in lst:
        if num > max_num:
            max_num = num
    return max_num

print(find_maximum([3, 5, 2, 8, 1]))  # Output: 8

#8. FizzBuzz - Write a function that prints numbers from 1 to 100. - If divisible by 3, print "Fizz". - If divisible by 5, print "Buzz". - If divisible by both, print "FizzBuzz".

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz()  # Output: FizzBuzz sequence from 1 to 100

#9. Palindrome Checker - Write a function that returns True if a string is a palindrome.

def is_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False
    
print(is_palindrome("madam"))  # Output: True
print(is_palindrome("hello"))    # Output: False

#10.Count Vowels - Write a function that counts the vowels in a string.

def count_vowels(s):
    count = 0
    vowels = "aeiouAEIOU"
    for char in s:
        if char in vowels:
            count += 1
    return count

print(count_vowels("Hello World"))  # Output: 3

#11. Second Largest Number - Write a function that returns the second largest number in a list without using sort()

def second_largest(lst):
    largest = lst[0]
    second = None
    
    for i in lst:
        if i > largest:
            second = largest
            largest = i
        elif second is None or (i > second and i != largest):
            second = i
            
    return second

print(second_largest([3, 5, 2, 8, 1]))  # Output: 5

#Guessing Game - Generate a random number between 1 and 10. -Keep asking the user to guess until they get it right. -Use a loop, conditionals, and functions.

import random

def guessing_game():
    num = random.randint(1, 10)
    
    while True:
        guess = int(input("Guess a number between 1 and 10: "))
        
        if guess == num:
            print( "correct guess")
            break
        else:
            print("Wrong guess! Try again!")
            
guessing_game()  # Starts the guessing game

#Write a function grade(marks) that:
#Returns "A" for marks ≥ 90
#Returns "B" for marks ≥ 80
#Returns "C" for marks ≥ 70
#Returns "D" for marks ≥ 60
#Otherwise returns "F"

def grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"
    
print(grade(85))  # Output: B
print(grade(72))  # Output: C
print(grade(65))  # Output: D
print(grade(55))  # Output: F
