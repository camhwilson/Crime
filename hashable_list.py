

class HashableList(list):
    #list of lists is not hashable by counter, create custom data type
    def __init__(self, val):
        #init function sorts input list upon initialization
        self.val = sorted(val)
    
    def __hash__(self):
        #make hashable
        return(hash(str(self.val)))

    def __repr__(self):
        #get clean output
        return str(self.val)

    def __eq__(self, other):
        #equality checking func
        return str(self.val) == str(other.val)
    
    def __len__(self):
        #length function
        return len(self.val)
    
    def __getitem__(self, index):
        #retrieve list elem by index
        return self.val[index]