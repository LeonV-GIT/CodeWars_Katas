# https://www.codewars.com/kata/5e0b72d2d772160011133654


# You are given three piles of casino chips: white, green and black chips:

# the first pile contains only white chips
# the second pile contains only green chips
# the third pile contains only black chips
# Each day you take exactly two chips of different colors and head to the casino. 
# You can choose any color, but you are not allowed to take two chips of the same color in a day.

# You will be given an array representing the number of chips of each color and 

# your task is to return the maximum number of days you can pick the chips. Each day you need to take exactly two chips.


def solve(arr):
    a,b,c = sorted(arr)
    if c > (a+b): return (a+b)
    else: return sum(arr)//2