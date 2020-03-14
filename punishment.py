"""punishment.py
SWDV-610-4W DATA STRUCTURES: WK 1 
Module 1.9: Reinforcement and Punishment
Maryville University of St. Louis, MO
John E. Simon School of Business
Professor Timothy Kyle
Student Mike Craft """
# ------------------------------------------------
"""A common punishment for school children is to
write out a sentence multiple times.  Write a
Python stand-alone program that will write the
following sentence one hundred times: "I will
never spam my friends again."""
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
1. Punishment Readability - Your code should
     have clearly articulated comments, easy to
     understand variables, constants, etc., and
     have a clear flow of how the code is
     carried out.
2. Punishment Output - Returns the proper
     output
3. Punishment - Style and Use of Functions"""
# ------------------------------------------------
"""Answer 3 canvas questions in the canvas
   submission text box.
1. How many hours do you estimate you used
   completing this assignment?
2. What was easiest for you when completing
   this assignment?
3. What was the most difficult challenge you
   experienced when completing this assignment"""
# ------------------------------------------------
def main():           # main function
    a = 0             # initialize accumulator
# for loop, 100 loops, index 0 to 99    
    for L in range(100): 
        a = a + 1     # increment the accumulator
        # line to print loaded into variable L.
        L = "I will never spam my friends again."
#string formatting with line number and string        
        #print("{:3}. {}".format(a, L))
        print("%3i. %s" % (a, L))

main() # call main