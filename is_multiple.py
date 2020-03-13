# is_mutiple.py
# SWDV-610-4W DATA STRUCTURES: WK 1 - Module 1.9
#     Reinforcement and Punishment
# Maryville University of St. Louis, MO
# John E. Simon School of Business
# Professor Timothy Kyle
# Student Mike Craft
# ------------------------------------------------
# Write a short Python function, is_multiple(n,
# m), that takes two integer values and returns
# True is n is a multiple of m, that is, n = mi
# for some integer i, and False otherwise.
# ------------------------------------------------
# GitHub Link: https://classroom.github.com/a/nUSsBI1q
# ------------------------------------------------
# In addition to coding these tasks, you must post
# a video running and explaining your code.  This
# allows for you to demonstrate what is occurring
# in the code as it is happening and how it is
# organized.  You must also run your code in the
# video to explain the output and why the program
# produced that output. Refer to the attached
# rubric to see how it is scored.
# ------------------------------------------------
# Rubric
# 1. Multiple Readability - Your code should have
#      clearly articulated comments, easy to
#      understand variables, constants, etc., and
#      have a clear flow of how the code is
#      carried out.
# 2. Multiple Computation - Code should be able to
#      run and carry out the necessary tasks. Aim
#      to have your code complete the required
#      tasks.
# 3. Multiple Output - Returns the proper output
# ------------------------------------------------
# Answer 3 canvas questions in the canvas
#    submission text box.

# 1. How many hours do you estimate you used
#    completing this assignment?

# 2. What was easiest for you when completing
#    this assignment?

# 3. What was the most difficult challenge you
#    experienced when completing this assignment
# ------------------------------------------------
# Python function, is_multiple(n, m),
#   that takes two integer values and returns True
#   is n is a multiple of m, that is,
#   n = mi for some integer i,
#   and False otherwise.

def is_multiple(n,m): # call from main with variables n,m
# boolean True if n is / m and remainder is equal to 0
#   (modulo or remainder is 0). This also means
#   n is a multiple of m, that is, n = mi for some
#   integer i, and False otherwise.

    if n % m == 0: 
        print(n, "is a multiple of ", m)
    else:
        print(n, "is not a multiple of ", m)

def main():
# print introduction
    print("""This program takes two integer values
as inputs and outputs to screen (if True) that
integer 1 is a multiple of integer 2, or will
output to screen (if False) that integer 1 is not
a multiple of integer 2.

If either number is not an integer (text or symbol,
or is a decimal number, you will get and error and
will try again to enter that integer.""")
    print()
    
    # validation loop 1 to catch n errors. Will only
    #   allow an int entry; str or float excepted.
    while True:
        try:
            n = int(input("Enter integer number 1: "))
        except ValueError:
            print("ERROR: Entry must be an integer. Try again.")
            continue # loop again if error
        else: # if an int break out of loop
            break
            
    # validation loop 2 to catch m errors. Will only
    #   allow an int entry; str or float excepted.
    while True:
        try:
            m = int(input("Enter integer number 2: "))
        except ValueError:
            print("ERROR: entry must be an integer. Try again.")
            continue # loop again if error
        else: # if an int break out of loop
            break
        
    is_multiple(n,m) # call the function with variables n,m

main()