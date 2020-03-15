"""is_mutiple.py
SWDV-610-4W DATA STRUCTURES: WK 1 - Module 1.9
   Reinforcement and Punishment
Maryville University of St. Louis, MO
John E. Simon School of Business
Professor Timothy Kyle
Student Mike Craft """
# ------------------------------------------------
"""Write a short Python function, is_multiple(n,
m), that takes two integer values and returns
True if n is a multiple of m, that is, n = mi
for some integer i, and False otherwise."""
# ------------------------------------------------
"""GitHub Link:
https://classroom.github.com/a/nUSsBI1q"""
# ------------------------------------------------
"""In addition to coding these tasks, you must
post a video running and explaining your code.
This allows for you to demonstrate what is
occurring in the code as it is happening and how
it is organized.  You must also run your code in
the video to explain the output and why the
program produced that output. Refer to the
attached rubric to see how it is scored."""
# ------------------------------------------------
"""Rubric
1. Multiple Readability - Your code should have
     clearly articulated comments, easy to
     understand variables, constants, etc., and
     have a clear flow of how the code is
     carried out.
2. Multiple Computation - Code should be able to
     run and carry out the necessary tasks. Aim
     to have your code complete the required
     tasks.
3. Multiple Output - Returns the proper output"""
# ------------------------------------------------
"""Answer 3 canvas questions in the canvas
submission text box.

1. How many hours do you estimate you used
     completing this assignment?

2. What was easiest for you when completing
     this assignment?

3. What was the most difficult challenge you
     experienced when completing this assignment
"""
# ------------------------------------------------
"""Python function, is_multiple(n, m),
that takes two integer values and returns True
n = mi for some integer i,
and False otherwise."""

def is_multiple(n,m):
# called by main function, variables as inputs.    
# call from main with variables n,m
#   boolean True if n is / m and remainder is
#   equal to 0 (modulo or remainder is 0). This
#   also means n is a multiple of m, that is,
#   n = mi for some integer i,
#   and False otherwise.

    if n % m == 0: 
        print()
        print(n, "is a multiple of", m)
    else:
        print()
        print(n, "is not a multiple of", m)
# ------------------------------------------------
def getInput(): # called by main.
    
# validation loop 1 to catch n errors. Will only
# allow an int entry; str or float excepted.
    running = True # initialize variable for True
    
    #while True: # alt to use of while var
    
    # conditional loop to get valid n input
    while running: 
        try: # try/except to handle errors
            n = int(input("Enter integer n: "))
        # exception error here to block system
        # error and stop / crash program.            
        except ValueError: 
            print("""

Error: Entry must be an integer (not a decimal,
letter, or non whole number). Try again.

""")
            #continue if error not required here
              
        else: # if input is valid exit loop
            #break  # break exits loop; required
            #if you don't initialize while var
            
            running = False # while var exits loop
                         # eliminates use of break
# ------------------------------------------------        
# validation loop 2 to catch m errors.

# First checks for divide by zero here so it
#   doesn't show up on line 65 from modulo.

# Second checks for whole number integer, not
#   decimal, or letter, or non whole number
#   character. Will only allow an int entry; str
#   or float excepted.

    looping = True # initialize variable for True
    
    #while True: alt to use of while var
    
    # conditional loop to get valid m input
    while looping:
        try: # try/except to handle errors
            # get input, set to variable m            
            m = int(input("Enter integer m: "))
            # boolean if true (they entered 0,
            # try again.)                     
            if m == 0:
                print("""
ZeroDivisionError: Can not divide by zero,
integer division or modulo by zero;
2nd number can not be zero. Try again.
""")
                continue # loop again if error
            
        # exception error here to block system
        # error and stop / crash program.            
        except ValueError: 
            print("""

Error: Entry must be an integer (not a decimal,
letter, or non whole number). Try again.

""")
            #continue if error not required here
                   
        else: # if input is valid exit loop
            #break  # break exits loop; required
            #if you don't initialize while var
            
            looping = False # while var exits loop
                      # eliminates use of break
                      
# return the variables to the function that
#   called (main).        
    return n, m    
# ------------------------------------------------      
def main():
# print introduction
    print("""
This program takes two integer values (positive or
negative whole number integers) as inputs and
outputs to screen (if True) that integer n is a
multiple of integer m (that is, n = mi for some
integer i), or will output to screen (if False)
that integer n is not a multiple of integer m.
Under this definition, a 0 is allowed for n, and
is considered a multiple of m as 0 = m*0.

If either number is not an integer (text or
symbol, or is a decimal number, you will get and
error and will try again to enter that integer.

If the second entry m is a 0, this program will
show an error, and require the user to try again.
A 0 in the second entry is an attempt to divide
by zero and not allowed.

""")

# call the function to get inputs and return
#   variables.    
    n, m = getInput()
# call the function with variables n,m
    is_multiple(n,m) 
    
main()