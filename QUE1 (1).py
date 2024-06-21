# SET operations
'''
    Objectives: 
        Create a class SET. Create member functions to perform the following SET
        operations:
        1) is member: check whether an element belongs to the set or not and return
        value as true/false.
        2) powerset: list all the elements of the power set of a set .
        3) subset: Check whether one set is a subset of the other or not.
        4) union and Intersection of two Sets.
        5) complement: Assume Universal Set as per the input elements from the user.
        6) set Difference and Symmetric Difference between two sets.
        7) cartesian Product of Sets.
        Write a menu driven program to perform the above functions on an instance of the
        SET class.
'''
import numpy as np


class SET :


    def __init__(self, myset):
        pSET = np.array([])
        for i in myset:
            if i not in pSET:
                pSET = np.append(pSET,i)
        self.myset = np.array(pSET)

#  ismembre : checks whether an element belongs to the given set or not. returns value as true/ false  


    def ismember(self,item):

        if item in self.myset:
            return True

        else:


            return False

#    union  of two Sets.
    def union(self, setB):


        uSET = np.array([])


        for i in np.concatenate((self.myset,setB.myset)):

            if i not in uSET:


                uSET = np.hstack((uSET,i))
        return uSET

# and Intersection
    def intersection(self,setB):


        interSET = np.array([])

        for i in np.concatenate((self.myset,setB.myset)):


            if (i in self.myset)and(i in setB.myset) and (i not in interSET):


                interSET = np.hstack((interSET,i))
        return interSET

#  set Difference  between two sets.
    def differ(self,setB):


        diffSET = np.array([])


        for i in  np.concatenate((self.myset,setB.myset)):


            if (i in self.myset) and (i not in self.intersection( setB)) and (i not in diffSET) :


                diffSET = np.hstack((diffSET,i))

        return (diffSET)

#  and Symmetric Difference
    def symDiff(self,setB):


        symDset = SET(self.union(setB)).differ(SET(self.intersection(setB)))


        return (symDset)
#   powerset: list all the elements of the power set of a set .
    def powerSET(self):
        pwrSET = np.array([])

        size = len(self.myset)
        def bincov(size):
            arr = np.array([])
            for i in range(2**size):
                val = bin(i)[2:]
                while len(val)< size:
                    val = "0"+val
                arr = np.hstack((arr,val))
            return arr
        
        for j in bincov(size):
            element = np.array([])
            
            count = 0
            for k in j :

                if k != '0':
                    element = np.hstack((self.myset[count], element))
                count+=1
            
            pwrSET = np.append(pwrSET,str(element))
        
        return pwrSET

            




#   subset: Check whether one set is a subset of the other or not.
    def subset(self,setB):

        flagList = np.array([])

        for i in setB.myset:

            flag = None

            if i in self.myset:

                flag = True
                
            else: 

                flag = False

            flagList = np.hstack((flagList,np.array([flag])))
        if False in flagList:
            return f"{setB.myset} is NOT a subset of {self.myset}."
        else:
            return  f"{setB.myset} is a subset of {self.myset}."

    
# Cartesian Product
    def cartProd(self,setB):
        
        cpSET  = np.zeros((1,2))       # created an array: [[0,0]] so that when adding more sets to it,  doesn't show dimension mismatch ERROR
        for i in self.myset:
            for j in setB.myset:
                buff = [i,j]
                cpSET = np.concatenate((cpSET,[buff]))
        return cpSET[1:]        # removing the set[0,0] from 0th which was created to facilitate the concatenation above 

        







while True:
    # ----------------------: MENU :----------------------
    print("SET operations:")
    print(
    "\t1) ismember: check whether an element belongs to the set or not and return value as true/false."
    , "\t2) powerset: list all the elements of the power set of a set ."
    , "\t3) subset: Check whether one set is a subset of the other or not."
    ,"\t4) Union of two Sets. "
    ,"\t5) Intersection of two Sets."
    ,"\t6) set Difference between two sets."
    ,"\t7) Symmetric Difference between two sets."
    ,"\t8) cartesian Product of Sets.", sep="\n")

    choice = int(input("Enter your choice:\t"))

    while(choice not in (1,2,3,4,5,6,7,8)):
        print("\tInvalid INPUT!","\tPlease recheck and ENTER AGAIN",sep="\n")
        choice = int(input("Enter your choice:\t"))
    else:
        
        s1 = [eval(i) for i in input("Enter setA: ").split(',') ]
        setA = SET(s1)
        if choice==1:
            ele = eval(input("Enter an element: ") )
            
            print(setA.ismember(ele))
        elif choice==2:
            print("Power Set: ")
            print(setA.powerSET())
        elif choice==3:
            s2 = [eval(i) for i in input("Enter subset: ").split(',')]
            setB = SET(s2)
            print(setA.subset(setB))

        elif choice==4:
            s2 = [eval(i) for i in input("Enter setB: ").split(',')]
            setB = SET(s2)
            print("Union:")
            print(setA.union(setB))
        elif choice==5:
            s2 = [eval(i) for i in input("Enter setB: ").split(',')]
            setB = SET(s2)
            print("Intersection:")
            print(setA.intersection(setB))
        
        elif choice==6:
            s2 = [eval(i) for i in input("Enter setB: ").split(',')]
            setB = SET(s2)
            print("SET Difference:")
            print(setA.differ(setB))
        elif choice==7:
            s2 = [eval(i) for i in input("Enter setB: ").split(',')]
            setB = SET(s2)
            print("Symmetric Difference:")
            print(setA.symDiff(setB))
        elif choice==8:
            s2 = [eval(i) for i in input("Enter setB: ").split(',')]
            setB = SET(s2)
            print("Cartesian product: ")
            print(setA.cartProd(setB))
        