"""recursive_reverse_list.py

SWDV-610-4W 20/SP2 DATA STRUCTURES WK 3
Module 3.9 Writing Recursive Functions PE-2
      
Maryville University of St. Louis, MO
John E. Simon School of Business
Professor Timothy Kyle
Student Mike Craft """
# ------------------------------------------------
"""2. Write a recursive function to reverse a
      list."""
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
program produced that output."""
# ------------------------------------------------
"""Rubric Recursive Reverse List
1. List Readability; Code is readable and
   organized.
2. List Output; Output correctly produces a
   reversed list.
3. List Recursive Style. Code is styled
   recursively.
4. Answer all canvas questions below.   
5. Video Submission; Video clearly explains the
   organization and output of the code.
6. Answer all weekly feedback and submit
   separately."""
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
def recursiveReverseList(return_list, start, \
                         stop):
    """Provides a recursive function to reverse list indexes.

    1. Has a base case starting point, index 0
    2. Changes state to move to base case by reducing index
       by one to until at base case (index 0). Performs search/
       compare/replace as appropriate of Min/Max values each cycle 
    3. Makes call to itself to recur to base case
    4. Uses parameters:
       return_list (list to reverse)
       start (list index to start reverse on)
       stop (list index to stop reverse on)
    5. Performs a slice on start_list[start:stop]."""
    
    # prints list before each recur
    # used to show steps of reverse
    print(return_list)
    
    # if at least 2 elements (if one stops)
    # check for base case
    if start < stop - 1:
        
    # simultaneous assignment; swap first and last
    # then recur on inward remaining indexes
        return_list[start], return_list[stop-1] =\
        return_list[stop-1], return_list[start]
    
    # function calls itself
    # changes state, moves toward base case
    # reverses one set of indexes at a time
    #   from outside towards center
        recursiveReverseList(return_list, \
                             start+1, stop-1)
    return return_list

def main():
    """Main function; calls recursiveReverseList 

    Initializes and prints/shows start list.
    Allows rodeo comment/uncomment variation
    calls reverse function
    prints final list after complete"""
    
    # Initializes list (even)
    start_list = [0,1,2,3,4,5,6,7,8,9]
    
    # Initializes list (odd)
    #start_list = [0,1,2,3,4,5,6,7,8]  
    """comment/uncomment to run various versions."""

    print("List prior to reverse: ")
    print(start_list)
    print("\nSteps of reverse, initial to final:")
    
    """Calls function recursive reverse list."""
    
    # This version flips 0-9 (use 10 to work 9)
    # This version is to answer the assignment
    """toggle comment110/116; use with even start_list line96"""
    final_list = recursiveReverseList(start_list, 0, 10) 

    # This version leaves ends in place (0 and 9)
    # and flips inside (1 to 8)
    # This version is for the video for demo.
    """toggle comment 110/116; use with even start_list line96"""
    #final_list = recursiveReverseList(start_list, 1, 9) 
    
    # This version flips 0-8 (use 9 to work 8)
    # This version is for the video for demo.
    """toggle comment121/127; use with odd start_list line99""" 
    #final_list = recursiveReverseList(start_list, 0, 9) 

    # This version leaves ends in place (0 and 8)
    # and flips inside (1 to 7)
    # This version is for the video for demo.
    """toggle comment 121/127; use with even start_list line99""" 
    #final_list = recursiveReverseList(start_list, 1, 8) 
    
    print()
    print("List after completion of reverse: ")
    print(final_list)

if __name__ == "__main__":
    main()