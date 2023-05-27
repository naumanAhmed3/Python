#===================================
#===================================
# Name   : 
# Roll no: 
# Section: 
# Date   : 
#===================================
#===================================


#------------------------------------
# Node class for a Doubly Linked List
#------------------------------------
class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
#------------------------------------
#-----------------------------------

class TextEditor:
    def __init__(self, row= -1 , col= -1):
        '''
        Predefined member variables. 
        
        WARNING: DO NOT MODIFY THE FOLLOWING VARIABLES
        '''
        
        self.doc = None   # The root of everything. See page 2 for details
        
        #======================
        # Insert your Member
        #   variables here (if any):
        self.row = row 
        self.col = col 
        self.temp = self.doc
      
        
        #----------------------
        
        
        #======================
        
#======================
    def goto(self, row, col):
        '''
        Moves the cursor to the location indicated by the 
          row and col parameters
 
        Parameters:
            row --> row number to move to
            col --> column number to move to
        
        Return value:
            None
        '''
        row_count = 0
        col_count = 0


        if row==0 and col==0:
            if self.doc!=None:
                self.cursor=[0,0]
                return
            n=Node("")
            self.doc=Node(n)
            n.prev=self.doc
            self.cursor=[row,col]
            return 

        if (row<0) or (col<0):
            print ('asshole')
            return


        temp = self.doc 
        for i in range(row) :
            if (temp.next == None) :
                temp.next = Node('fccu' , temp) 
            temp = temp.next
            return (temp.data) 

        c_temp = temp.data
        if (c_temp == None) :
            c_temp = Node(' ',c_temp)
            temp.data = c_temp 
            return

        for i in range(row) :
       
            if (c_temp.next == None) :
                c_temp.next = Node(' ', c_temp) 
            c_temp = c_temp.next  


        self.cursor  = [row , col] 

#======================

#======================
    def forward(self):
        '''
        Moves the cursor one step forward
 
        Parameters:
            None
        
        Return value:
            None
        '''
        r_temp=self.doc
        for r in range(self.cursor[0]):
            if r_temp==None:
                return
            r_temp=r_temp.next
        c_temp = c_temp.data
        for c_temp in range(self.cursor[1]+1):
            if c_temp==None:
                if r_temp.next==None:
                    return
                else:
                    self.cursor=[self.cursor[0]+1,0]
                    return
        self.cursor=[self.cursor[0],self.cursor[1]+1]
        print(r_temp.data)
            
#======================

#======================
    def back(self):
        '''
        Moves the cursor one step backwards
 
        Parameters:
            None
        
        Return value:
            None
        '''
        
        self.temp = self.temp.prev
        print(self.temp.data)

        return None 
#======================

#======================
    def home(self):
        '''
        Moves the cursor to the start of the current line
 
        Parameters:
            None
        
        Return value:
            None
        '''
        if (self.temp.prev == None):
            return
        elif (temp.prev != None ) :
            while (temp.prev != None):
                temp = temp.prev

        return None 

            

#======================

#======================
    def end(self):
        '''
        Moves the cursor to the end of the current line
 
        Parameters:
            None
        
        Return value:
            None
        '''
        if (self.temp.next == None):
            return 
        
        elif (self.temp.next != None) :
            self.temp = self.temp.next 

        return None 
#======================

#======================
    def insert(self, string):
        '''
        Inserts the given string immediately after the cursor
 
        Parameters:
            a string
        
        Return value:
            None
        '''
        self.temp = self.doc 
        for i in (string) :
            new_node = Node(i)


            if (self.temp.next != None) :

               
                self.temp_copy = self.temp.next 
                self.temp.next = new_node 
                new_node.prev = self.temp
                self.temp = new_node
                self.temp_copy.prev = self.temp
                self.temp.next = self.temp_copy 


            else :

                self.temp.next = new_node 
                new_node.prev = self.temp 
                new_node.next = None 

                

        
        
#======================

#======================
    def delete(self, num):
        '''
        Deletes specified number of characters from the cursor position
 
        Parameters:
            integer number of characters to delete
        
        Return value:
            None
        '''
        raised=False
        r_temp =self.doc
        for i in range(self.cursor[0]):
            r_temp =r_temp .next
        c_temp=r_temp .data
        for i in range(self.cursor[1]):
            c_temp=c_temp.next
        c_temp2=c_temp.next
        for i in range (num):
            c_temp2=c_temp.next
            if c_temp2==None:
                if i!=num:
                    raised=True #checks if deleting more characters than available in row
                break
        if raised:
            c_temp.prev.next=c_temp2
            self.cursor[1]-=1
        else:
            c_temp.next=c_temp2
#======================

#======================
    def countCharacters(self):
        '''
        Moves the cursor to the start of the current line
 
        Parameters:
            None
        
        Return value:
            total number of characters in the document, basically
               the total number of pink nodes in the document.
        '''
        
        count_of_chars =0
        self.cursor[1]=0     #changing row 
        r_temp=self.doc


        for i in range(self.cursor[0]):
            c_temp=r_temp.data
            while c_temp!=None:
                c_temp=c_temp.next
                c+=1
            r_temp=r_temp.next
        return count_of_chars 
#======================

#======================
    def countLines(self):
        '''
        Count total of non-empty lines in the document.
 
        Parameters:
            None
        
        Return value:
            integer number of non-empty lines in the document
        '''
        
        count_of_lines = 0
        temp = self.doc 
        while (temp.next != None ):
            if (temp.data != None ) :
                count_of_lines += 1 
            temp = temp.next 

        return count_of_lines 

#======================


#======================
    def printDoc(self):
        '''
        Prints the entire document on the screen.
        '''
        
        self.cursor[1]=0     #
        r_temp=self.doc


        for i in range(self.cursor[0]):
            c_temp=r_temp.data
            while c_temp!=None:
                c_temp=c_temp.next
                print(c_temp.data)
            r_temp=r_temp.next
        

      

        
       

        
#======================

            
#======================
#======================
#    BONUS
#======================
    def undo(self):
        '''
        Undos the previous action by user.
 
        Parameters:
            None
        
        Return value:
            None 

        '''
        
        raise NotImplementedError

#----------------------

    def redo(self):
        '''
        Redos the previous action undone by user.
 
        Parameters:
            None
        
        Return value:
            None 

        '''
        
        raise NotImplementedError

#----------------------

    def save(self, fileName):
        '''
        Saves the spreadsheet to a file with name given as Parameter
 
        Parameters:
            fileName
        
        Return value:
            None 

        '''
        self.cursor[1]=0     #
        r_temp=self.doc


        for i in range(self.cursor[0]):
            c_temp=r_temp.data
            while c_temp!=None:
                c_temp=c_temp.next
                with open(fileName , 'w' ) as f:
                  f.write(str(i).replace('[' , '').replace(']','').replace(',','  ')) 
                f.write('\n')
                
            r_temp=r_temp.next


#----------------------

    def load(self, fileName):
        '''
        Loads the spreadsheet from a file with name given as Parameter
 
        Parameters:
            fileName
        
        Return value:
            None 

        '''
        
        raise NotImplementedError
            
#----------------------

    def find(self, substr):
        '''
        Finds a given substring within the entire document. If no such substring
          is found then return None.
 
        Parameters:
            substring to look for
        
        Return value:
            - reference to the first node of the substring found
            - None if substring is not found
        '''
        
        raise NotImplementedError
            
                
#======================


#======================
#======================
#
#    DRIVER FUNCTION
#
#======================

def main():
    # -----------------------------
    # Implement your own logic here:
    # -----------------------------
    editor = TextEditor()
    print("Welcome to DS Text Editor\n Enter commands at the prompt\n")
    while True:
        
        i=input()
        if i=="forward":
            editor.forward()
        if i=="back":
            editor.back()
        if i=="home":
            editor.home()
        if i=="end":
            editor.end()
        if i=="countCharacters":
            editor.countCharacters()
        if i=="countLines":
            editor.countLines()
        if i =="printDoc":
            editor.printDoc()
        if i=="quit":
            exit()
        else:
            try:
                l=i.split()
            except:
                print("Enter Valid Integer")
                next
            if l[0]=="goto":
                editor.goto(int(l[1]),int(l[2]))
            if l[0]=="insert":
                editor.insert(l[1])
            if l[0]=="delete":
                editor.delete(int(l[1]))
                
    # while True:
    #     editor.Goto(0,0)
    #     editor.insert("Hello comp200")
    #     editor.printDoc()
    

    

if __name__ == '__main__':
    main()
    
#======================











'''
        col_counter  = 0
        row_counter = 0
        self.temp = self.doc
        if (self.row<0 or self.col<0) or (self.row != None and self.col == None):
            return None
        
        if (row == 0) and (col ==0) :
                self.temp = self.doc.data 
                self.row = row 
                self.col = col
             
                
        


        if (row == self.row) and (col > self.col) :
                self.temp = self.doc.data 
                col_counter = 0
                while (col_counter != col) :
                    if (self.temp.next == None) :
                        new_node = Node('same col new node')
                        self.temp.next = new_node 
                        new_node.prev = self.temp 
                        new_node.next = None
                        self.temp = new_node
                       
                    else :
                        self.temp = self.temp.next
                    col_counter  += 1 
               
                self.col = col

        if (row>0) and (col>0):
            self.temp = self.doc.next
            if (self.temp.next == None):
                new_node=(None)
                self.temp.next = new_node
                new_node.prev =self.temp
                new_node.next = None
                self.temp = new_node
                self.temp.next == None
            self.temp.data = Node('created')
            self.temp=self.temp.data
            col_counter = 0
            while (col_counter != col) :
                    if (self.temp.next == None) :
                        new_node = Node('new col new node')
                        self.temp.next = new_node 
                        new_node.prev = self.temp 
                        self.temp = new_node
                    else :
                        self.temp = self.temp.next
                    col_counter  += 1 
            self.row == row
            self.col == col
        
       
        print(self.temp.data)
        return None '''