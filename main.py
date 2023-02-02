#This Code was Written on [Nov-18-2019] by @riishiiraz

"""
Python Program For Simple School Management
"""

import os
"""
Here os module is imported for creating folders and assecing them
"""
p=print
"""
creting an object same as print whose alias is 'p' 
"""

i=input
"""
creting an object same as input whose alias is 'i' 
"""

path=os.path.split(os.path.abspath(__file__))[0]
"""
creting an list object which contains all dirctories
"""

def wait():
    input("Press Enter To Continue ... ")

if "data" not in os.listdir(path):
    
    """
        checking for 'data' folder in the
        current directory ,if 'data' is not
        present in current directory the it
        will create a folder named 'data'
        and it will contains three
        subfolders (teachers , studets
        , punes , and a text file 'All.txt'
        which conteins all record in a list) 
    """
    
    os.mkdir(path+'\\data')
    """
        cretes the 'data' folder
    """
    
    os.mkdir(path+'\\data\\teachers')
    f=open("data\\teachers\\id.txt",'w')
    f.write("1000")
    f.close()
    
    """
        creates the 'teachers' folder and
        creates a file 'id.txt' which is
        use to generate id number for teachers
    """
    
    os.mkdir(path+'\\data\\students')
    f=open("data\\students\\id.txt",'w')
    f.write("50")
    f.close()
    
    """
        creates the 'students' folder and
        creates a file 'id.txt' which is
        use to generate id number for studets
    """
    
    os.mkdir(path+'\\data\\punes')
    f=open("data\\punes\\id.txt",'w')
    f.write("1000");f.close()
    
    """
        creates the 'punes' folder and
        creates a file 'id.txt' which is
        use to generate id number for punes
    """

    f=open(path+"\\data\\All.txt",'w')
    f.write('[[],[],[]]')
    f.close()

class teacher:
    """
        Class for teachers in which
        objects are teachers
    """
    
    def __init__(self,name=None,
                 # """ arguement for name of teacher """
                 
                 subjects=None,
                 # """ arguement for subjects of teacher """
                 
                 age=None,
                 # """ arguement for age of teacher """
                 
                 gender=None
                 # """ arguement for gender of teacher """
                 
                 ): 
        
        
        self.name=name
        """ creating an attribute for name of teacher """
        
        self.subs=subjects
        """ creating an attribute for subjects of teacher """
        
        self.age=age
        """ creating an attribute for age of teacher """
        
        self.gen=gender
        """ creating an attribute for gender of teacher """
        

    def add(self):
        """
            function for adding new teachers
        """

        """ Opening File """
        f=open("data\\teachers\\id.txt",'r')
        
        """ Ctreting attribute for id"""
        self.id=int(f.read())

        """ Closing File """
        f.close()

        """ Opening File """
        f=open("data\\teachers\\id.txt",'w')

        """ Writing File """
        f.write(str(self.id-1))

        """ Closing File """
        f.close()

        PATH = path+'\\data\\teachers\\'+str(self.id)+'.txt'
        
        """ Opening File """
        f=open(PATH,'w')
        
        #[<name>,<subs>,<id>,<age>,<Gebder>]

        """ Writing File """
        f.write(str([self.name,self.subs,self.id,self.age,self.gen]))

        """ Closing File """
        f.close()

        """ Opening File """
        f=open(path+'\\data\\All.txt')

        """  Converting String to list """
        ct=eval(f.read())

        """ Closing File """
        f.close()
        
        #[[Teachets...] , [Students...]  ,  [Punes...]]

        """ Appending data """
        ct[0].append(self.name)

        """ Opening File """
        f=open(path+'\\data\\All.txt','w')

        """ Writing File """
        f.write(str(ct))

        """ Closing File """
        f.close()

        """ Printing Notificatins """
        p("\nTeacher Added \nYour ID is %s"%self.id)
        wait()

    def info(self=None):
        
        """
            function that tells information
            of a particular teacher by entering id
        """

        ID=input("Enter ID : ")
        """ Taking ID from user """
        
        try:
            """ Exception Handling """

            """ Opening File """
            f=open(path+'\\data\\teachers\\'+str(ID)+'.txt')

            """  Converting string to list by 'eval' """
            ctnt=eval(f.read())

            """ Closig file """
            f.close()
            
        except FileNotFoundError:
            """ If file not found thats mean
            there is no teacher present from the given
            id number  """
            
            print("Teacher Not Found")

            wait()
            """ Stops the execution of the function """
            return

        head("Details (Teacher)")
        
        """ Printing Name """
        head("Name = %s"%ctnt[0])

        """ Printing Subjects """
        head("Teaching subjects = %s"%ctnt[1])

        """ Printing Id """
        head("ID = %s"%ctnt[2])

        """ Printing Age """
        head("Age = %s"%ctnt[3])

        """ Printing Gender """
        head("Gender = %s"%ctnt[4])

        wait()

        print("\n\n\n\n")

        return

class stu:

    """
        Class For Students In which
        objects are students
    """
    
    def __init__(self,
                 # """ self (object) """
                 
                 name=None,
                 # """ Object for Name """
                 
                 clas=None,
                 # """ Object for Class (students class) """
                 
                 sec=None,
                 # """ Object for Section """
                 
                 roll=None,
                 # """ Object for Roll number  """
                 
                 age=None
                 # """ Object for age """
                 
                 ):
        
        self.name=name
        """ Creating atribute for name """
        
        self.cls=clas
        """ Creating atribute for class """
         
        self.roll=roll
        """ Creating atribute for roll no. """
         
        self.sec=sec
        """ Creating atribute for section """
         
        self.age=age
        """ Creating atribute for age """
         
    def add(self):
        
        """
            function for adding new students
        """
        
        #[students \\ clas \\ sec \\ roll]
        abc =str(self.cls)
        """ Variable For class """
        
        ABC =os.listdir(path+'\\data\\students')
        """ Variable For list of directories """
        
        if abc not in ABC:
            """ if abc is not present in ABC """
            
            os.mkdir(path+'\\data\\students\\%s'%str(self.cls))

        abc= str(self.sec)
        """ Variable For Section """
        
        ABC= os.listdir(path+'\\data\\students\\%s'%str(self.cls))
        """ Variable For list of directories """
        
        if abc not in ABC:
            """ if abc is not present in ABC """
            
            os.mkdir(path+'\\data\\students\\%s\\%s'%(
                str(self.cls),str(self.sec)))

        f=open(path+'\\data\\students\\%s\\%s\\%s.txt'%(
            self.cls,self.sec,self.roll),'w')
        
        #[<Name>, <class>, <roll>, <sec> ,<age>]
        
        f.write(str([self.name
                     ,self.cls,self.roll,
                     self.sec,self.age]
                    ))
        f.close()

        f=open(path+'\\data\\All.txt')
        """ Opening file """
        
        ct=eval(f.read())
        """ converting string to list """
        
        f.close()
        """ Closing file """

        ct[1].append(self.name)
        """ Updating data """

        f=open(path+'\\data\\All.txt','w')
        """ Opening file """
        
        f.write(str(ct))
        """ Writing file """
        
        f.close()
        """ Closing file """

        print("\nStudent Added Succesfully !!")
        """ Printing Info  """

        wait()
        
    def info(self=None):
        """
            Function for printing information
            of a student by providing class
            , section , roll number
            """
        
        cls=input("Enter Class : ")
        """ Taking input from user for class """
        
        sec=input("Enter Section : ").upper()
        """ Taking input from user for Section """
        
        rol=input("Enter Roll no. : ")
        """ Taking input from user for Roll number """
        
        try:
            """
                Exception Handling
            """
            
            AbC= '\\data\\students\\%s\\%s\\%s.txt'

            """ Opening File """
            f=open(path+AbC%(cls,sec,rol))

            """ Converting string to list """
            ctnt=eval(f.read())

            """ Closing File """
            f.close()

            head("Details (Student)")

            head("Name = %s"%ctnt[0])
            """ Pritning Name of student """
            
            head("Class = %s"%ctnt[1])
            """ Pritning Class of student """
             
            head("Roll no. = %s"%ctnt[2])
            """ Pritning Roll no. of student """
             
            head("Section = %s"%ctnt[3])
            """ Pritning Section of student """
             
            head("Age = %s"%ctnt[4])
            """ Pritning Aeg of student """

            wait()
            print("\n\n\n\n")
            
        except FileNotFoundError:
            """ IF Given details Not found  """
             
            print("Not Found\n")
            wait()

def det():
    """
        Function for printing All Deatails about the School 
    """
    
    """ Opening File """
    f=open(path+'\\data\\All.txt')

    """ Converting string to list """
    C=eval(f.read())
    
    """ Closing File """
    f.close()

    head("There Are %s Students in Our School"%len(C[1]))
    """ Printing about students """
    
    head("There Are %s Teachers in Our School"%len(C[0]))
    """ Printing about teachers """
    
    head("There Are %s Punes in Our School"%len(C[2]))
    """ Printing about punes """

    wait()
    print("\n\n\n\n")


def head(label,w=40):
    """
        Function that makes design of menu by '=' sign
    """
    
    print("+"+"-"*w+"+")
    print("|"+label.center(w)+"|")
    print("+"+"-"*w+"+")

def opt():
    """
        Option for User
    """
    
    head("Home Menu")
    print("|","Enter 1 For School Details"+"\t\t |")
    print("|","Enter 2 For Teachers Details"+"\t\t |")
    print("|","Enter 3 For Adding Teachers "+"\t\t |")
    print("|","Enter 4 For Students Details"+"\t\t |")
    print("|","Enter 5 For Adding Students "+"\t\t |")
    print("|","Enter 6 For Punes Details"+"\t\t |")
    print("|","Enter 7 For Exit"+"\t\t\t |")
    print("+"+"-"*40+"+")
    print()
    
    o=input("Enter Option (1-5) : ")

    try:
        o=int (o)
    except :
        o=1000
    
    return o
    

T=teacher()
""" Creating an object for teacher """

S=stu()
""" Creating an object for students """

while True:
    
    op=opt()
    
    if op == 1:
        
        """ if option is 1 """
        det()
        
    elif op==2:
        
        """ if option is 2 """
        T.info()

    elif op==5:
        
        """ if option is 5 """
        
        name=input("Enter Name : ")
        """ Entry for name """
        
        clas=int(input("Enter Class : "))
        """ Entry for class """
        
        sec=input("Enter Section : ").upper()
        """ Entry for section """
        
        roll=int(input("Enter Roll Number : "))
        """ Entry for roll no. """
        
        age=int(input("Enter Age : "))
        """ Entry for age """

        OBJ = stu(name,clas,sec,roll,age)
        """ Creting an object by 'stu' """
        
        OBJ.add()
        """
            Calling The 'add' method
            of 'stu' for adding students
        """
        
        
    elif op==4:
        
        """ if option is 4 """
        
        S.info()
        """
            Calling The 'info' method
            of 'stu' for adding students
        """

    elif op==3:
        
        """ if option is 3 """
        
        name = input("Enter Name : ")
        sub=input("Enter teaching subjects : ")
        age=int(input("Enter Age : "))
        gen =input("Enter Gender : ")

        
        OBJ=teacher(name,sub,age,gen)
        """
            Creating An Object
            for Teacher bu 'teacher' class
        """

        OBJ.add()
        """
            Calling The 'add' method
            of 'stu' for adding teacher
        """
        
    elif op==6:
        
        """ if option is 6 """
        
        print("Sorry No details found !!")
        wait()
        
    elif op==7:
        
        """ if option is 7 """
        
        break
    else:
        head("Wrong Choice",40)
""" End OF Program """
