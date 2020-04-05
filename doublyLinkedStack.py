"""doublyLinkedStack.py

SWDV-610-4W 20/SP2 DATA STRUCTURES WK 4
Module 4.10 Stacks and Queues and Deques and Lists
and Lists and Lists. PE 1

Maryville University of St. Louis, MO
John E. Simon School of Business
Professor Timothy Kyle
Student Mike Craft   """
# ------------------------------------------------
"""Complete the following tasks:

    Implement a stack using linked lists:
    
    PE1: Implement an algorithm for concatenating
    two stacks (stackL and stackM), into stackN,
    that contains all the elements of stackL
    followed by the elements of stackM.
    
In addition to coding these tasks, you must post
a video running and explaining your code.  This
allows for you to demonstrate what is occurring in
the code as it is happening and how it is
organized.  You must also run your code in the
video to explain the output and why the program
produced that output.

Please upload .py files or insert a github link"""
# ------------------------------------------------
"""GitHub Link:
https://classroom.github.com/a/nUSsBI1q"""
# ------------------------------------------------
"""Stack, Queue, and Deque Rubric
1. Stack Readability - Code is readable and well
   organized.
2. Stack Funtionality - Stack is functional and
   displays an output.
3. Queue Readability - Queue is readable and
   organized. 
4. Queue Functionality - Queue is functional and
   displays proper output.
5. Deque Readability - Deque is readable and
   organized.
6. Deque Functionality - Deque is functional and
   produces a proper output.
7. Answer all canvas questions.
8. Video Submission - Clearly explains the
   organization and out put of submitted programs.
"""
# ------------------------------------------------
"""When you have completed this assignment and
pushed your work to the remote GitHub repository,
answer the following question(s):

1. How many hours do you estimate you used
     completing this assignment?

2. What was easiest for you when completing
     this assignment?

3. What was the most difficult challenge you
     experienced when completing this assignment
"""
# ------------------------------------------------
"""Provides a doubly linked list stack.

   Provides a Last In / First Out LIFO Stack.
   Includes use of a class Node. Items are added
   and removed at the top of the stack. Provides
   for the dynamic allocation of data to avoid
   stack overflow error issues associated
   with when the size of the stack is restricted
   and the size of the stack exceeds the maximum
   size, throwing an error."""   
#-------------- class Node -----------------------
class Node: 
  
    #--------- Node constructor ------------------
    def __init__(self, data): 
        self.data = data # Assign data 
        self.next = None # Initialize next as null 
        self.prev = None # Initialize prev as null         
    
#---------------- class Stack --------------------          
# Stack class contains a Node object 
class Stack:
    """LIFO Stack implementation using a doubly
       linked list for storage."""

    #----------- Stack constructor ---------------
    def __init__(self): 
        self.head = None
        
    #----------- Stack public accessors ----------
    # Function to return top element in the stack  
    def top(self): 
  
        return self.head.data 
  
    # Function to return the size of the stack  
    def size(self): 
   
        temp=self.head
        count=0
        if temp == None:
            return 0
        while temp is not None: 
            count=count+1
            temp=temp.next
        return count 
      
    # Function to check if stack is empty or not   
    def is_empty(self):
          
        if self.head is None: 
            return True
        else: 
            return False
                    
    #-------------- Stack methods ----------------
    # Function to add element data to top of stack  
    def push(self, data): 
  
        if self.head is None: 
            self.head = Node(data) 
        else: 
            new_node = Node(data) 
            self.head.prev = new_node 
            new_node.next = self.head 
            new_node.prev = None
            self.head = new_node 
              
    # Function to pop top element off stack and
    # return element temp removed from the stack  
    def pop(self): 
  
        if self.head is None: 
            return None
        else: 
            temp = self.head.data 
            self.head = self.head.next
            return temp   
    # Function to print the stack 
    def print_stack(self): 
          
        print("stack elements are:") 
        temp = self.head
        if temp == None:
            print("None")

        while temp is not None: 
            print(temp.data, end ="->") 
            temp = temp.next           

# ------------------------------------------------
# main runs the program, initializes the stacks as
# empty, then loads values into the stacks. Then
# main will pop an element from stackL and push to
# stackN, then pop an element from stackM and push
# to stackN. Each will iterate for the size of
# stackL and stackM to pop all elements out and
# push all elements to stackN.
def main():
    stackL = Stack() # initialize empty stack
    stackM = Stack() # initialize empty stack
    stackN = Stack() # initialize empty stack
    print("Merge two stacks into a third\n")
    print("stackL and stackM prior to merge into stackN:\n")

    # loading stackL and stackM with elements
    for i in range(0,10): # push i  of 0 to 9 
        stackL.push(i)    # into stackL

    print("stackL ", end='') # prints stack ID
    stackL.print_stack()      # calls method to 
                             # print stack
    
    # pushes i of elements A to J into stackM
    for i in ('A', 'B', 'C', 'D', 'E', 'F', \
              'G', 'H', 'I', 'J'):
        stackM.push(i)

    print("\n\nstackM ", end='') # prints stack ID
    stackM.print_stack()        # calls method to
                               # print stack
                               
    # this is where the real work is
    # pulls elements from stackL and
    # puts in stackN
    for i in range(stackL.size()):
        L = stackL.top()
        stackL.pop()
        stackN.push(L)
    
    # this is where the real work is
    # pulls elements from stackM and
    # puts in stackN    
    for i in range(stackM.size()):
        M = stackM.top()
        stackM.pop()
        stackN.push(M)
    
    # print final results
    print("\n\nAfter merge of stackL and stackM into stackN:\n")
    print("stackN ", end='')
    stackN.print_stack()

# Calls main to run the main function
main()