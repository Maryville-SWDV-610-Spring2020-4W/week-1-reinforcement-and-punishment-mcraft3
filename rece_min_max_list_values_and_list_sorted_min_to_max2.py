"""rec_min_max_values_and_list_sorted_min_to_max.py

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
   
    """ To see Min/Max Recursive steps, uncomment line 64 and 153.
        To suppress the Min/Max Recursive steps output, comment out line 64 and 153."""
    # print min and max for each recur    
    print("Min Value: {:16}       Max Value: {:16}".format(finalMin, finalMax)) # toggle comment on/off
       
    # if true, process and recur down to base case, return and exit function
    if searchIndex >= 0: # if index more than 0, do below and recur
        if searchData[searchIndex] > finalMax:#check val to Max, if greater
            finalMax = searchData[searchIndex]#replace if greater
        if searchData[searchIndex] < finalMin:#check val to Min, if smaller
            finalMin = searchData[searchIndex]# replace to Min
                      
        # make recursive call to self, reducing index by -1    
        return recursiveMinMax(searchData, searchIndex-1, finalMax, finalMin)

    # if true return and exit function; toggle 77 and 83 to see that 83 is the return for finall   
    if searchIndex != 0: # if base case, compare, set if needed, print final  
        #if searchData[searchIndex] > finalMax:# check val to Max, if greater
        #    finalMax = searchData[searchIndex] # replace if greater
        #if searchData[searchIndex] < finalMin:# check val to Min, if smaller
        #    finalMin = searchData[searchIndex]#replace to Min
        #print header line & final values    
        return finalMin, finalMax # toggle comment line 77 and 83 to throw error and see this line is return to main

def merge(mergeList1, mergeList2, tempList3):
    # merge sorted lists mergeList1 and mergeList2 into tempList3
    i1 = i2 = i3 = 0 # initialize;  accumulators keep track of current position in each list (count up from index 0, not down)
    # mergeIndexes track total indexes of list for each cycle (doesn't change)
    mergeIndex1, mergeIndex2 = len(mergeList1), len(mergeList2)

    # Loop while both pieces have data
    while i1 < mergeIndex1 and i2 < mergeIndex2:
        if mergeList1[i1] < mergeList2[i2]: # copy from mergeList1
            tempList3[i3] = mergeList1[i1]     
            i1 = i1 + 1
        else:                       # copy from mergeList2
            tempList3[i3] = mergeList2[i2]     
            i2 = i2 + 1
        i3 = i3 + 1                 # item added to tempList3

    # Here either mergeList1 or mergeList2 is done, One of the
    # following loops will execute to finish up the merge.
    
    # Copy remaining items (if any) from mergeList1
    while i1 < len(mergeList1):
        tempList3[i3] = mergeList1[i1]
        i1 = i1 + 1
        i3 = i3 + 1
    # Copy remaining items (if any) from mergeList2
    while i2 < len(mergeList2):
        tempList3[i3] = mergeList2[i2]
        i2 = i2 + 1
        i3 = i3 + 1

def mergeSort(mergeSortList): # divide and concquer (mergeSort) and combine (merge)
    # Put items of mergeSortList in ascending order
    mergeIndex = len(mergeSortList)
    # Do nothing if mergeSortList contains 0 or 1 items
    if mergeIndex > 1:
        # split into two sublist halves
        slicePoint = mergeIndex // 2
        mergeSortListHalfA, mergeSortListHalfB = mergeSortList[:slicePoint], mergeSortList[slicePoint:]
        
        """To see internal D&C Steps and Combine Steps leave uncommentd.
           To toggle off printed steps uncomment lines 126,127,133,134, 142 and 171"""
        print("D&C starting mergeSortListHalfA:                                {}".format(mergeSortListHalfA)) # toggle comment on/off
        print("D&C starting mergeSortListHalfB:                                                               {}".format(mergeSortListHalfB)) # toggle comment on/off
        
        # recursively sort each piece        
        mergeSort(mergeSortListHalfA)
        mergeSort(mergeSortListHalfB)
        
        print("D&C mergeSortListHalfA:                                         {}".format(mergeSortListHalfA)) # toggle comment on/off               
        print("D&C mergeSortListHalfB:                                                                        {}".format(mergeSortListHalfB)) # toggle comment on/off
        
        """Merge the sorted pieces. Toggle below merge line 139.
           (uncommented) to see merge data back together (Combine (sorted) after D&C)
           or (commented) to see mergeSort (Divide and Concquer (not sorted) without Combined"""
        merge(mergeSortListHalfA, mergeSortListHalfB, mergeSortList)          # unique toggle on/off
        
        # prints steps of (combined) merge data or if above turned off D&C mergeSort (pre combined).
        print("Combined merged:                 {}\n".format(mergeSortList))    # toggle comment on/off
        
        
        """ toggle this off to see that this return is the one that goes back to main"""
    return mergeSortList # returns final back to main; prints out of main.    #Unique toggle on/off
                                                                       
def main():
    # print function introduction; 16 char limit is for the nicely formatted output
    print("Find Min and Max Value (int up to 16 char) of a sequence, pos or neg.\n")

    """print step introduction. toggle comment for 64 and 153 together if suppressing."""
    print("Values for Min / Max start, and for each Min / Max recursive step:\n") # toggle comment on/off

    # initialize
    startData = [-293, -50,421,34,21,-42,94857,8,9,-6,342,71,36]
    startIndex = len(startData)-1
    startMax = 0
    startMin = 9999999999999999
    minToMaxStartSortList = startData
    
    # call function recursiveMinMax with parameters
    endMin, endMax = recursiveMinMax(startData, startIndex, startMax, startMin)
    print("\nFinal Min and Final Max Values (Base Case):")
    print("Min Value: {:16}       Max Value: {:16}\n".format(endMin, endMax))
    
    print("List prior to Sort:\n{}".format(minToMaxStartSortList))
    print()
    
    """ toggle comment on/off 126,127,133,134, 143 and 171 as a group"""
    print("Merging sorted list halves back into final sorted list:")  # toggle comment on/off
    
    finalSortedList = mergeSort(minToMaxStartSortList)
    print("\nFinal list Sorted Min to Max:\n {}".format(finalSortedList))
    
if __name__ == "__main__":
    main()