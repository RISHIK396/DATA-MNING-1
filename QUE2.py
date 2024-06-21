# Relations 

""""
OBJECTIVEs:
    Create a class RELATION, use Matrix notation to represent a relation. Include
    member functions to check if the relation is 
        Reflexive, 
        Symmetric, 
        Anti-symmetric,
        Transitive. 
    Using these functions check whether the given relation is: 
        Equivalence
        or Partial Order relation 
        or None
"""
import numpy as np 

class RELEATION:
    def __init__(self,relmat):
        self.relmat  = relmat
# reflexive 
    def reflexive(self):
        tDiag = np.eye(self.relmat.shape[0], dtype=bool) # gives a identity diagonal matrix in bool
        princDiag = self.relmat[tDiag]        # gives the principal diagonal
        if np.all(princDiag == 1):
            return True
        else: 
            return False
# symmetric
    def symmetric(self):
        if self.relmat == self.relmat.T:
            return True
        return False

# Anti- Symmetric
    def antiSymm(self):
        
        for i in range(self.relmat.shape[0]):
            for j in range(self.relmat.shape[1]):
                if (i != j) and (self.relmat[i][j]) == 1 and (self.relmat[j][i]) == 1:
                    return False
        return True
# transitive
    def transitive(self):
        for i in range(self.relmat.shape[0]):
            for j in range(self.relmat.shape[1]):
                for k in range(self.relmat[0]):
                    if self.relmat[i][j] == 1 and self.relmat[j][k] == 1 and self.relmat[i][k] != 1:
                        return False
        return True
# relation TYPE
    def relTYPE(self):
        if self.reflexive() and self.symmetric() and self.transitive():
            print( "Relation is Equivalance.")
        elif self.reflexive() and self.antiSymm() and self.transitive():
            print( "Relation is Partial Order.")
        else:
            print("NONE\n",'Nither Equivalance Nor Partial Order.')
        return ''



        
