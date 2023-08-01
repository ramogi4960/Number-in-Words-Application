# Number-in-words-application
This is a python script that can return a non-negative number in words. For example, 123 in words is One Hundred Twenty Three

# Description
I got this idea from a problem I was solving from leetcode.com. It was assigned a difficulty of hard and took me more than an hour to complete it
It has a linear time complexity and I could not think of any other better optimisation
It also works only for non-negative integers within the 32-bit range of integers (maximum of 2**31 - 1)
You should try to solve the question through this link https://leetcode.com/problems/integer-to-english-words/

# How I did it
First, I had to define a dictionary with numbers within range(0, 20) as the keys and their respective values as their representation in words
For some of the integers, their word representation was a string that could be split into two.
For example, the value of key '3' is 'Three Thirty' and '5' is 'Five Fifty'. This was to be able to cater for two digit numbers
