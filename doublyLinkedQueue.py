""" doublyLinkedQueue.py

SWDV-610-4W 20/SP2 DATA STRUCTURES WK 4
Module 4.10 Stacks and Queues and Deques and Lists
and Lists and Lists. PE 2

Maryville University of St. Louis, MO
John E. Simon School of Business
Professor Timothy Kyle
Student Mike Craft   """
# ------------------------------------------------
""" Complete the following tasks

    Implement a queue using linked lists
    (separate file, PE 2)
    
    PE2: Implement use of a queue to play a game
    of musical chairs. Use an input to get an
    unspecified number of players. Utilize 
    randomness to play the music and when it stops
    remove a player from the game. Output players
    each round and output winner of the game.
    
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
from random import randrange

"""Provides a doubly linked list queue.

   Provides a First In / First Out FIFO Queue.
   Includes use of a class Node. Elements are
   added at the rear/last of the queue and
   elements are deleted or accessed from the front
   /head of the queue. Provides for the dynamic
   allocation of data to avoid queue overflow
   error issues associated with when the size of
   the queue is restricted and the size of the
   queue exceeds the maximum size, throwing an
   error."""   
#-------------- class Node -----------------------
class Node: 
    
    #--------- Node constructor ------------------
    def __init__(self, data): 
        self.data = data # Assign data 
        self.next = None # Initialize next as null 
        self.prev = None # Initialize prev as null 
           
#---------------- class Queue --------------------          
# Queue class contains a Node object 
class Queue: 
    """FIFO Queue implementation using a doubly
       linked list for storage."""
   
    #--------- Queue constructor -----------------
    def __init__(self): 
        self.head = None
        self.last=None
           
    #--------- Queue public accessors ------------
    # Function to return head element in the queue  
    def get_first(self): 
   
        return self.head.data 
   
    # Function to return the size of the queue 
    def size(self): 
   
        temp=self.head
        count=0
        if temp == None:
            return 0
        while temp is not None: 
            count=count+1
            temp=temp.next
        return count 
       
    # Function to check if queue is empty or not       
    def is_empty(self): 
   
        if self.head is None: 
            return True
        else: 
            return False
               
    #------------ Queue methods ------------------        
    # Function to add an element data in the Queue 
    def enqueue(self, data): 
        if self.last is None: 
            self.head =Node(data) 
            self.last =self.head 
        else: 
            self.last.next = Node(data) 
            self.last.next.prev=self.last 
            self.last = self.last.next
            
    # Function to remove first element and
    # return the element from the queue  
    def dequeue(self): 
   
        if self.head is None: 
            return None
        else: 
            temp= self.head.data 
            self.head = self.head.next
            self.prev=None
            return temp 
   
    # Function to print the queue  
    def print_queue(self): 
           
        print("Players are: ", end='') 
        temp=self.head 
        while temp is not None: 
            print(temp.data,end="->") 
            temp=temp.next
       
# ------------------------------------------------
""" Implements use of a queue to play a game
    of musical chairs. Use an input to get an
    unspecified number of players. Utilize 
    randomness to play the music and when it stops
    remove a player from the game. Output players
    each round and output winner of the game."""

# game initializes with one parameter playerlist
def musical_chairs(playerlist): 
    gameQueue = Queue() # creates empty queue
    # loop to load the queue
    for player in playerlist: 
        # enqueues each player in the playerlist
        gameQueue.enqueue(player) 
    
    print("gameQueue before the music:")
    
    # prints starting queue
    gameQueue.print_queue()
    print()
    
    # stop rotation with randomness
    rotate = randrange(1,7) # initialize rotation 
    while gameQueue.size() > 1: # more than 1 play
        for i in range(rotate): # loop random
            print("\nPlay the music!")            
            # rotate players around chairs
            # move head player to last player
            gameQueue.enqueue(gameQueue.dequeue())
            
            # print players
            gameQueue.print_queue()
            # generate new random rotation
            rotate = randrange(1,7) 
            print()
        
        # remove chair and player; last is winner    
        gameQueue.dequeue() 
    
    # return winner to main
    return gameQueue.dequeue() 

# ------------------------------------------------
def main():
    # Print introduction
    print("Welcome to the game musical chairs!\n") 
    musicalChairsList = [] # initialize empty list
    
    # initialize player; allows to keep adding
    m = 0 
    while m != "": # if enter (no data, exits)
        m = input("Enter name of player <enter to quit adding>: ")
        if m == "":
            break # exit
        # otherwise you have data, append to list
        else: 
            musicalChairsList.append(m)
            continue # loop again
        
    # print list being sent to game musicalChairs    
    print("\nPlayer List: {}".format\
          (musicalChairsList))
    print()
    print("gameQueue elements from head/front to tail/last:\n")
    # call to run the game
    # with parameter of list created
    # game will return winner
    winner = musical_chairs(musicalChairsList)
    print("\nThe Musical Chairs Winner is: {}!".format(winner))

# call to run main
main()