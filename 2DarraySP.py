#===================================
#===================================
# Name   : 
# Roll no: 
# Section: 
# Date   : 
#===================================
#===================================

class Spreadsheet:
    storage = [] # to preserve the previous values of cursor's location
    storage_two = []    
    def __init__(self):
        '''
        Predefined member variables. 
        
        WARNING:DO NOT MODIFY THE FOLLOWING VARIABLES
        '''
        self.sheet = None   # 2D array of values
        self.rows = 0       
        self.cols = 0
        self.cursor=[0,0]   # cursor's current position
        self.selction = [None, None, None, None]
        
        #======================
        # Insert your Member
        #   variables here (if any):
        #----------------------
        
        
        #======================
        
#======================
    def CreateSheet(self, rows, cols):
        '''
        Creates a new 2 dimensional array assigned
          to the self.sheet member variable.
        Initialize the 2D array with 'None' type.
 
        Parameters:
            rows --> total number of rows in this spreadsheet
            cols --> total number of cols in this spreadsheet
        
        Return value:
            None
        '''

        print('''
        
        1) ___________CreateSheet Method ___________ ''')


        
        self.rows = rows 
        self.cols = cols 
        self.sheet  = [   # >>>>>>Empty array
                        ]
        for i in range(rows):  #Loop for rows 
            
            initialised_rows  = []         #Empty rows of the 2-D array 
            
            for j in range(cols):   #Fill rows with self.cols number of elements 
        
                initialised_rows.append('')                         
            
            self.sheet.append(initialised_rows)
        print (self.sheet)
#======================

#======================
    def Goto(self, row, col):
        '''
        Moves the cursor to the location indicated by the 
          row and col parameters
 
        Parameters:
            row --> row number to move to
            col --> column number to move to
        
        Return value:
            None
        '''
        
        print('''
        
        2) _______________Goto Method ___________________''')


        self.cursor[0] , self.cursor[-1] = row , col
        print(self.cursor)
        return None
#======================

#======================        
    def Insert(self, val):
        '''
        Inserts value at the position indicated by the cursor.
 
        Parameters:
            val --> value to be inserted at the cursor location
        
        Return value:
            None
        '''
        
        print('''
        
        3) _______________Insert Method ___________________''')

        self.sheet[self.cursor[0]][self.cursor[-1]] = val
        
        print  (self.sheet)
        return None 
#======================

#======================        
    def Delete(self):
        '''
        Deletes a value from the position indicated by the cursor.
 
        Parameters:
            None
        
        Return value:
            None
        '''

        print('''
        4)_______________Delete Method ___________________''')
        self.sheet[self.cursor[0]][self.cursor[1]] = None  #Setting the giving coordinates of sheet to None 

#======================

#======================    
    def ReadVal(self):
        '''
        Prints the value from the position indicated by the cursor.
 
        Parameters:
            None
        
        Return value:
            value stored at the cursor location 

        '''
        
        print (f'''
        5) _______________ReadVal Method ___________________

            Read Value at {self.cursor} is :''' )

        return self.sheet[self.cursor[0]][self.cursor[-1]] #Gives values at given coordinates 


#======================

#======================    


    def Select(self,row, col):   
        '''
        Selects values between the position indicated in arguments with row and col and the position indicated by the cursor
 
        Parameters:
            row --> Row number to be selected 
            col --> Column number to be selected
        
        Return value:
            None
        '''

        print('''
        
        6) _______________Goto Method ___________________''')
        

        

        Spreadsheet.storage.append(row)
        Spreadsheet.storage.append(col)
        Spreadsheet.storage_two.append(self.cursor[0])
        Spreadsheet.storage_two.append(self.cursor[-1])
    
        
        '''if self.cursor[0] >= row and self.cursor[-1] >= col:  #CASE I : 
                                                              # if given point is right 
                                                              # above or behind the point of cursor
            row , col = self.cursor[0] , self.cursor[-1]
            self.cursor  = Spreadsheet.storage '''

        if self.cursor[0]>row and self.cursor[-1]>col :   # CASE II:
                                                          # if given point's row and column values are 
                                                          # smaller than cursor's row and column values  

            row , col = self.cursor[0] , self.cursor[-1]
            self.cursor  = Spreadsheet.storage




        if self.cursor[0]<row and self.cursor[-1]>col:   # CASE III :
                                                        # If cursor's row value is smaller
                                                        # the given row value but column value 
                                                        # greater than the given column value 
            Spreadsheet.storage_two  = [self.cursor[0] , self.cursor[-1]]
            self.cursor[0] , self.cursor[-1] = self.cursor[0] ,  col 
            row  , col  = row  , Spreadsheet.storage_two[-1]
            

        x = [self.sheet[i][self.cursor[-1]:col+1] for i in range(self.cursor[0],row+1)]
        self.selection  = [j for i in x for j in i]
        print (self.selection)
#======================

#======================        
    def GetSelection(self):
        '''
        Returns a tuple with current selecion cooridnates
        Parameters:
            None
        
        Return value:
            Returns a tuple with row and column of the selection:
                position 1 of the tuple indicates the stating row of the selection
                position 2 of the tuple indicates the stating col of the selection
                position 3 of the tuple indicates the ending row of the selection
                position 4 of the tuple indicates the ending col of the selection
            
            Example: (1,1,3,4)
        '''
        
        print('''
        
        7) _______________GetSelection Method ___________________''')

        return (tuple([Spreadsheet.storage_two[0] ,Spreadsheet.storage_two[-1] , 
                    Spreadsheet.storage[0] , Spreadsheet.storage[-1]]))
#======================

#======================        
    def Sum(self,row,col):
        '''
        Stores the sum of the values in the current selection at the position indicated in arguments
        Parameters:
            row --> Row number to store the sum
            col --> Column number to store the sum
        
        Return value:
            None
        '''
        
        print('''
        
        8) _______________Sum Method ___________________''')
        
        add = 0    # add variable initialised 
        for i in self.selection : # Loop to iterate over the integers in the selected region of sheet 
            add+=i  # add all the integers to the initialised add variable 
        self.sheet[row][col] = add 
        
        return None 
        
#======================

#======================    
    def Mul(self,row,col):
        '''
        Stores the product of the values in the current selection at the position indicated in arguments
        Parameters:
            row --> Row number to store the product
            col --> Column number to store the product
        
        Return value:
            None
        '''   
             
        print('''
        
        9) _______________Mul Method ___________________''')
        prod = 1   # variable set to 1 and not 0 so that the 
                    #incoming selected integers do not result as 0 when multiplied 


        for i in self.selection: # Loop to iterate over all the selected region
            prod = prod*i  # Multiplying all values selected and storing to prod
        self.sheet[row][col] = prod #Storing the resultant value to the desired cell of sheet

        return None 

#======================

#======================        
    def Avg(self,row,col):
        '''
        Stores the average of the values in the current selection at the position indicated in arguments
        Parameters:
            row --> Row number to store the average
            col --> Column number to store the average
        
        Return value:
            None
        '''
           
        print('''
        
        10) _______________Avg Method ___________________''')
        add = 0
        for i in self.selection :
            add+=i 
        self.sheet[row][col] = add/len(self.selection) #sum of selected vals divided by number of selected vals 

        return None
#======================

#======================
    def Max(self,row, col):
        '''
        Stores the maximum of the values in the current selection at the position indicated in arguments
        Parameters:
            row --> Row number to store the maximum
            col --> Column number to store the maximum
        
        Return value:
            None
        '''        
        
        print('''


        11) _______________Max Method ___________________''')

        self.sheet[row][col] = max(self.selection) # maximum integer of all the selected values 
#======================

#======================
    def PrintSheet(self):
        '''
        Prints the sheet in a human readable from
        Parameters:
            None
        Return value:
            None    

        Note: This is an example output your values will differ
        PrintSheet()
        row/col:    0   1   2   3   4
            0       
            1   
            2           10               
            3                   12
            4 
        '''
        
        print('''
        
        12) _______________PrintSheet Method ___________________''')
        
        for i in range(len(self.sheet[0])):
            print ('    ',f'|{i}|' , end = '   ')
        print('\n')
        for j in range(len(self.sheet)):
            print(f'|{j}|','',(str(self.sheet[j][0:]))
                                .replace('[','').
                                replace(']','').
                                replace(',','        '))
            print('')

        return None 
            
#======================

            
#======================
#======================
#    BONUS
#======================
    def Undo(self):
        '''
        Undoes the previous action by user.
 
        Parameters:
            None
        
        Return value:
            None 

        '''
        
        raise NotImplementedError

#----------------------

    def Redo(self):
        '''
        Redoes the previous action undone by user.
 
        Parameters:
            None
        
        Return value:
            None 

        '''
        
        raise NotImplementedError

#----------------------

    def Save(self, fileName):
        '''
        Saves the spreadsheet to a file with name given as Parameter
 
        Parameters:
            fileName
        
        Return value:
            None 

        '''
        
        print('''
        
        15)_______________Save Method ___________________''')

        with open(fileName , 'w' ) as f:
            
            for i in self.sheet:
                 
                
                f.write(str(i).replace('[' , '').replace(']','').replace(',','  ')) 
                f.write('\n')

#----------------------

    def Load(self, fileName):
        '''
        Loads the spreadsheet from a file with name given as Parameter
 
        Parameters:
            fileName
        
        Return value:
            None 

        '''
        
        print('''
        16) _________________ Load Method __________________ ''')
        
        
        with open(fileName ,'r') as f:
            lines = [int(line.split(' ')) for line in f]
            

        for i in lines:
            for j in i:
                if j=='' or j== ':':
                    i.remove(j)
                if j.isnumeric() != False:
                    i.remove(j)
        print(lines)
                
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
    #sheet = Spreadsheet()
    # sheet.CreateSheet(5,5)
    #
    # while True:
    #     sheet.Goto(2,2)
    #     sheet.insert(4)
    #     sheet.Print() 
    
    print("Welcome to DS SpreadSheet Program")
    print("")
    print("Enter commands at the prompt")
    sheet = Spreadsheet()
    
    input1 = input()
    r=input1.split()
    b=(r[0])
    c=int(r[1])
    d=int(r[2])
    if b=="CreateSheet":
        sheet.CreateSheet(c,d)
        print("Sheet successfully created")
    else:
        print("error")
    while True:
        input2=input()
        r=input2.split()
        
        if r[0]=="Goto": 
            c=int(r[1])
            d=int(r[2])
            sheet.Goto(c,d)
        if r[0]=="Insert": 
            c=int(r[1])
            sheet.Insert(c)
        if r[0]=="Delete":
            sheet.Delete
        if r[0]=="ReadVal": 
            sheet.ReadVal() 
        if r[0]=="Select":
            c=int(r[1])
            d=int(r[2])
            sheet.Select(c,d)
        if r[0]=="GetSelection":
            print(sheet.GetSelection())
        if r[0]=="Sum":
            c=int(r[1])
            d=int(r[2])
            sheet.Sum(c,d) 
        if r[0]=="Mul":
            c=int(r[1])
            d=int(r[2])
            sheet.Mul(c,d)
        if r[0]=="Avg":
            c=int(r[1])
            d=int(r[2])
            sheet.Avg(c,d)
        if r[0]=="Max":
            c=int(r[1])
            d=int(r[2])
            sheet.Max(c,d)
        if r[0]=="PrintSheet":
            sheet.PrintSheet()
        if r[0]=="Save":
            c=str(r[1])
            sheet.Save(c)
            








if __name__ == '__main__':
    main()    







    
    
    
#======================


