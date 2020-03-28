"""recursive_min_max_values_in_sequence.py

SWDV-610-4W 20/SP2 DATA STRUCTURES WK 3
Module 3.9 Writing Recursive Functions PE-1
      
Maryville University of St. Louis, MO
John E. Simon School of Business
Professor Timothy Kyle
Student Mike Craft """
# ------------------------------------------------
"""1. Write a short recursive Python function that
finds the minimum and maximum values in a sequence
without using any loops."""
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
"""Rubric Minimum Maximum
1. Loop Readability; Code is readable and
   organized
2. Loop Output; Output correctly produces a
   minimum to maximum list.
3. Recursive Style; Loop is styled recursively.
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
def recursiveMinMax(searchData, searchIndex, finalMax, finalMin):
    """Provides a recursive search of a sequence for Min & Max.

    1. Has a base case starting point, index 0
    2. Changes state to move to base case by reducing index
       by one to until at base case (index 0). Performs search/
       compare/replace as appropriate of Min/Max values each cycle 
    3. Makes call to itself to recur to base case
    """
   
    # print min and max for each recur    
    print("Min Value: {:16}       Max Value: {:16}".format(finalMin, finalMax))
    
    # if false (not base case, skip to elif); if true do below and finish   
    if searchIndex == 0: # if base case, compare, set if needed, print final
        if searchData[searchIndex] > finalMax:# check val to Max, if greater
            finalMax = searchData[searchIndex] # replace if greater
        if searchData[searchIndex] < finalMin:# check val to Min, if smaller
            finalMin = searchData[searchIndex]#replace to Min
        #print header line & final values    
        print("\nFinal Min and Final Max Values (Base Case):\n")
        print("Min Value: {:16}       Max Value: {:16}".format(finalMin, finalMax))
        
    # elif true (not base case), process and recur
    elif searchIndex > 0: # if index more than 0, do below and recur
        if searchData[searchIndex] > finalMax:#check val to Max, if greater
            finalMax = searchData[searchIndex]#replace if greater
        if searchData[searchIndex] < finalMin:#check val to Min, if smaller
            finalMin = searchData[searchIndex]# replace to Min
        # make recursive call to self, reducing index by -1    
        recursiveMinMax(searchData, searchIndex-1, finalMax, finalMin)

def main():
    # print function introduction; 16 char limit is for the nicely formatted output
    print("Find Min and Max Value (int up to 16 char) of a sequence, pos or neg.\n")

    #print step introduction
    print("Values for start, and for each recursive step:\n")

    # initialize
    startData = [-293, -50,421,34,21,-42,9485760392841523,8,9,-6,342,71,36]
    startIndex = len(startData)-1
    startMax = 0
    startMin = 9999999999999999

    # call function recursiveMinMax with parameters
    recursiveMinMax(startData, startIndex, startMax, startMin)
    
if __name__ == "__main__":
    main()