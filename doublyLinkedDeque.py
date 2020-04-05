""" doublyLinkedDeque.py

SWDV-610-4W 20/SP2 DATA STRUCTURES WK 4
Module 4.10 Stacks and Queues and Deques and Lists
and Lists and Lists. PE 3

Maryville University of St. Louis, MO
John E. Simon School of Business
Professor Timothy Kyle
Student Mike Craft   """
# ------------------------------------------------
""" Complete the following tasks

    Implement a deque using linked lists
    (separate file, PE 3)
    
    PE3: Implement use of a deque using linked
    lists. Create the Deque class and Node Class
    with basic accessors and methods. Create a
    Deque Demonstration function that
    demonstrates all features of the Deque.
    
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
"""Provides a doubly linked list deque.

   Allows use of FIFO, FILO, LIFO, or LILO,
   allowing insert or delete at either end.
   Includes use of a class Node object."""   
#-------------- class Node -----------------------
class Node: 
    
    #--------- Node constructor ------------------
    def __init__(self, data): 
        self.data = data # Assign data 
        self.next = None # Initialize next as null 
        self.prev = None # Initialize prev as null 
           
#---------------- class Deque --------------------          
# Deque class contains a Node object 
class Deque: 
    """Deque or double ended queue(doubly linked)
       
       Allows use of FIFO or LIFO, allowing insert
       or delete at either end. """
    #--------- Deque constructor -----------------
    def __init__(self): 
        self.front = None
        self.rear=None
           
    #------- Deque public accessors --------------
    # Function to return front element in Deque  
    def get_front(self): 
   
        return self.front.data 
   
    # Function to return rear element in Deque  
    def get_rear(self): 
   
        return self.rear.data 
   
    # Function to return the size of the Deque 
    def size(self): 
   
        temp=self.front 
        count=0
        if temp == None:
            return 0
        while temp is not None: 
            count=count+1
            temp=temp.next
        return count 
       
    # Function to check if Deque is empty or not       
    def is_empty(self): 
   
        if self.front is None: 
            return True
        else: 
            return False
               
    #------------ Deque methods ------------------        
    # Function to add new last element in Deque 
    def add_rear(self, data): 
        if self.rear is None: 
            self.front =Node(data) 
            self.rear =self.front 
        else: 
            self.rear.next = Node(data) 
            self.rear.next.prev=self.rear 
            self.rear = self.rear.next
            
    # Function to add new front element in Deque 
    def add_front(self, data): 
        if self.rear is None: 
            self.front =Node(data) 
            self.rear =self.front 
        else: 
            new_node = Node(data) 
            self.front.prev = new_node 
            new_node.next = self.front 
            #new_node.prev = None
            self.front = new_node             
           
    # Function to remove first element and
    # return the element from the Deque  
    def remove_front(self): 
   
        if self.front is None: 
            return None
        else: 
            temp= self.front.data 
            self.front = self.front.next
            self.front.prev=None
            return temp 
   
    # Function to remove last element and
    # return the element from the queue  
    def remove_rear(self): 
   
        if self.rear is None: 
            return None
        else:
            temp = self.rear.data
            self.rear = self.rear.prev
            self.rear.next = None
            return temp 

    def erase(self):
        
        if self.rear == None:
            return None
        while (self.front != None):
            self.front = self.front.next
            self.front = None
            self.rear = None
        
        return print("Deque erased")

    # Function to print the Deque  
    def print_deque(self): 
           
        print("Deque elements are: ", end='') 
        temp=self.front
        if temp == None:
            print("None")
        while temp is not None: 
            print(temp.data,end="->") 
            temp=temp.next
       
# ------------------------------------------------
def deque_demo():
    
    # Initialize empty queue 
    my_deque = Deque() 
   
    print("Deque Demo using doubly linked list\n")
    print("Initialized Deque is empty: ", \
          my_deque.is_empty())
    print("Initialized Deque size is: ", \
          my_deque.size())
    my_deque.print_deque()
   
    # Insert 3 at rear. Deque becomes 3->None
    print("\nAdd to Rear:")
    my_deque.add_rear(3) 
    # Print the queue  _r
    my_deque.print_deque()
    print()
   
    # Insert 4 at rear. Deque becomes 3->4None   
    print("\nAdd to Rear:")
    my_deque.add_rear(4) 
    # Print the queue  
    my_deque.print_deque()
   
    # Insert 2 at front.
    # Deque becomes 2->3->4->None
    print("\n\nAdd to Front:")
    my_deque.add_front(2) 
    # Print the queue  
    my_deque.print_deque()
    print()
   
    # Insert 1 at end.
    # Deque becomes 1->2->3->4->None
    print("\nAdd to Front:")
    my_deque.add_front(1) 
    # Print the queue  
    my_deque.print_deque()
    print()
   
    # Print the Front element  
    print("\nFront element is:",\
          my_deque.get_front())
  
    # Print the Rear element  
    print("\nRear element is:",\
          my_deque.get_rear())
  
    # Print the Deque size  
    print("\nSize of the deque is:",\
          my_deque.size())
   
    # remove the Front element
    print("\nRemove Front element: ", \
          end='')
    print(my_deque.remove_front())
    print()
    my_deque.print_deque()
    print()
   
    # remove the Rear element
    print("\nRemove Rear element: ", \
          end='')
    print(my_deque.remove_rear()) 
    print()
    # Print the queue  
    my_deque.print_deque()
    print()
     
    # Print True if Deque is empty, else False  
    print("\nDeque is empty:",\
          my_deque.is_empty())
  
    print("\nDeque contents:") 
    my_deque.print_deque()
    print()
  
    print("Erase deque:")
    my_deque.erase()
    # Print True if Deque is empty, else False  
    print("\nDeque is empty:",\
          my_deque.is_empty())
  
    #print("Deque elements:") 
    my_deque.print_deque()
    print("Deque size is: ", \
          my_deque.size())
    print()
    
    print("add value zero to rear of deque:")
    my_deque.add_rear(0)
    my_deque.print_deque()
    print("\nDeque is empty:",\
          my_deque.is_empty())
    print("Deque size is: ", \
          my_deque.size())

def main():
    deque_demo()
    
# Code execution starts here           
if __name__=='__main__':
    main()

