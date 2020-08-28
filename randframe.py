def gaussframe(x, y, names=None, chop=6,mu=None, sigma=None):
    """
    -DEPENDENCIES: pandas, random
    -gaussframe() returns a pandas.DataFrame() Object made to a given size filled with RANDOM DATA + Options.
    -gaussframe() uses random.gauss() in the background, so the entries form a NORMAL DISTRIBUTION.
    -gaussframe() helps Data Scientists with Analysis, Processing, & speeds up their understanding of Data.
    -DEFAULTS: 
            1) (mu, sigma) = (50, 25), applied to every column (See mu & sigma below)
            2) chop = 6; i.e. round to the 6th decimal place
            3) Column Names = Variable 1, Variable 2,...,Variable x (See 1.required below for x)
    ---------------------------------------------------------------------------------------------------------
    5 ORDERED ARGUMENTS (2 Required, 3 Optional):
    
    1.required) x (+int) : Number of COLUMNS
            
    2.required) y (+int) : Number of ROWS
    
    3.optional) names (list of str) : List of COLUMN NAMES of length x
    
    4.optional) chop (int or None): Positive int for ROUNDING to orders of magnitude of 10 < 1,
                                    Negative for orders > 1, None for no decimal i.e. make integer
    
    5.optional) mu (list of int or float) : List of MEANS/AVERAGES for Columns & of length x
    
    6.optional) sigma (list of +int or +float) : List of STANDARD DEVIATIONS for Columns & of length x
    ---------------------------------------------------------------------------------------------------------
    """
    #Dependencies
    from pandas import DataFrame
    from random import gauss
    
    #START Keyword Conditions for CodeBlock A:
    if names==None and mu==None and sigma==None and chop==6:
    #End Keyword Conditions for CodeBlock A:
        
        #Start CodeBlock A
        randframe = {}
        for column in range(x):
                series = []
                for row in range(y):
                    series.append(gauss(50,25))
                randframe.update({'Variable '+str(column+1):series})
        return DataFrame(data=randframe, index=list(range(1,y+1)))
        #End CodeBlock A
    
    #START Keyword Conditions for CodeBlock B:
    if names!=None and mu==None and sigma==None and chop==6:
    #END Keyword Conditions for CodeBlock B:
        
        #CodeBlock B
        randframe = {}
        for column in range(x):
                series = []
                for row in range(y):
                    series.append(gauss(50,25))
                randframe.update({names[column]:series})
        return DataFrame(data=randframe, index=list(range(1,y+1)))
        #End CodeBlock B
    
    #START Keyword Conditions for CodeBlock C:
    if mu!=None and names==None and sigma==None and chop==6:
    #END Keyword Conditions for CodeBlock C:
        
        #Start CodeBlock C
        randframe = {}
        for column in range(x):
                series = []
                for row in range(y):
                    series.append(gauss(mu[column],25))
                randframe.update({'Variable '+str(column+1):series})
        return DataFrame(data=randframe, index=list(range(1,y+1)))
        #End CodeBlock C
    
    #START Keyword Conditions for CodeBlock D:
    if mu!=None and names!=None and sigma==None and chop==6:
    #END Keyword Conditions for CodeBlock D:
        
        #Start CodeBlock D
        randframe = {}
        for column in range(x):
                series = []
                for row in range(y):
                    series.append(gauss(mu[column],25))
                randframe.update({names[column]:series})
        return DataFrame(data=randframe, index=list(range(1,y+1)))
        #End CodeBlock D
    
    #START Keyword Conditions for CodeBlock E:
    if names==None and mu==None and sigma!=None and chop==6:
    #End Keyword Conditions for CodeBlock E:
        
        #Start CodeBlock E
        randframe = {}
        for column in range(x):
                series = []
                for row in range(y):
                    series.append(gauss(50,sigma[column]))
                randframe.update({'Variable '+str(column+1):series})
        return DataFrame(data=randframe, index=list(range(1,y+1)))
        #End CodeBlock E
    
    #START Keyword Conditions for CodeBlock F:
    if names!=None and mu==None and sigma!=None and chop==6:
    #END Keyword Conditions for CodeBlock F:
        
        #CodeBlock F
        randframe = {}
        for column in range(x):
                series = []
                for row in range(y):
                    series.append(gauss(50,sigma[column]))
                randframe.update({names[column]:series})
        return DataFrame(data=randframe, index=list(range(1,y+1)))
        #End CodeBlock F
    
    #START Keyword Conditions for CodeBlock G:
    if mu!=None and names==None and sigma!=None and chop==6:
    #END Keyword Conditions for CodeBlock G:
        
        #Start CodeBlock G
        randframe = {}
        for column in range(x):
                series = []
                for row in range(y):
                    series.append(gauss(mu[column],sigma[column]))
                randframe.update({'Variable '+str(column+1):series})
        return DataFrame(data=randframe, index=list(range(1,y+1)))
        #End CodeBlock G
    
    #START Keyword Conditions for CodeBlock H:
    if mu!=None and names!=None and sigma!=None and chop==6:
    #END Keyword Conditions for CodeBlock H:
        
        #Start CodeBlock H
        randframe = {}
        for column in range(x):
                series = []
                for row in range(y):
                    series.append(gauss(mu[column],sigma[column]))
                randframe.update({names[column]:series})
        return DataFrame(data=randframe, index=list(range(1,y+1)))
        #End CodeBlock H
        
    #START Keyword Conditions for CodeBlock I:
    if names==None and mu==None and sigma==None and chop!=6:
    #End Keyword Conditions for CodeBlock I:
        
        #Start CodeBlock I
        randframe = {}
        for column in range(x):
                series = []
                for row in range(y):
                    series.append(gauss(50,25))
                series = [round(i,chop) for i in series]
                randframe.update({'Variable '+str(column+1):series})
        return DataFrame(data=randframe, index=list(range(1,y+1)))
        #End CodeBlock I
    
    #START Keyword Conditions for CodeBlock J:
    if names!=None and mu==None and sigma==None and chop!=6:
    #END Keyword Conditions for CodeBlock J:
        
        #CodeBlock J
        randframe = {}
        for column in range(x):
                series = []
                for row in range(y):
                    series.append(gauss(50,25))
                series = [round(i,chop) for i in series]
                randframe.update({names[column]:series})
        return DataFrame(data=randframe, index=list(range(1,y+1)))
        #End CodeBlock J
    
    #START Keyword Conditions for CodeBlock K:
    if mu!=None and names==None and sigma==None and chop!=6:
    #END Keyword Conditions for CodeBlock K:
        
        #Start CodeBlock K
        randframe = {}
        for column in range(x):
                series = []
                for row in range(y):
                    series.append(gauss(mu[column],25))
                series = [round(i,chop) for i in series]
                randframe.update({'Variable '+str(column+1):series})
        return DataFrame(data=randframe, index=list(range(1,y+1)))
        #End CodeBlock K
    
    #START Keyword Conditions for CodeBlock L:
    if mu!=None and names!=None and sigma==None and chop!=6:
    #END Keyword Conditions for CodeBlock L:
        
        #Start CodeBlock L
        randframe = {}
        for column in range(x):
                series = []
                for row in range(y):
                    series.append(gauss(mu[column],25))
                series = [round(i,chop) for i in series]
                randframe.update({names[column]:series})
        return DataFrame(data=randframe, index=list(range(1,y+1)))
        #End CodeBlock L
    
    #START Keyword Conditions for CodeBlock M:
    if names==None and mu==None and sigma!=None and chop!=6:
    #End Keyword Conditions for CodeBlock M:
        
        #Start CodeBlock M
        randframe = {}
        for column in range(x):
                series = []
                for row in range(y):
                    series.append(gauss(50,sigma[column]))
                series = [round(i,chop) for i in series]
                randframe.update({'Variable '+str(column+1):series})
        return DataFrame(data=randframe, index=list(range(1,y+1)))
        #End CodeBlock M
    
    #START Keyword Conditions for CodeBlock N:
    if names!=None and mu==None and sigma!=None and chop!=6:
    #END Keyword Conditions for CodeBlock N:
        
        #CodeBlock N
        randframe = {}
        for column in range(x):
                series = []
                for row in range(y):
                    series.append(gauss(50,sigma[column]))
                series = [round(i,chop) for i in series]
                randframe.update({names[column]:series})
        return DataFrame(data=randframe, index=list(range(1,y+1)))
        #End CodeBlock N
    
    #START Keyword Conditions for CodeBlock O:
    if mu!=None and names==None and sigma!=None and chop!=6:
    #END Keyword Conditions for CodeBlock O:
        
        #Start CodeBlock O
        randframe = {}
        for column in range(x):
                series = []
                for row in range(y):
                    series.append(gauss(mu[column],sigma[column]))
                series = [round(i,chop) for i in series]
                randframe.update({'Variable '+str(column+1):series})
        return DataFrame(data=randframe, index=list(range(1,y+1)))
        #End CodeBlock O
    
    #START Keyword Conditions for CodeBlock P:
    if mu!=None and names!=None and sigma!=None and chop!=6:
    #END Keyword Conditions for CodeBlock P:
        
        #Start CodeBlock P
        randframe = {}
        for column in range(x):
                series = []
                for row in range(y):
                    series.append(gauss(mu[column],sigma[column]))
                series = [round(i,chop) for i in series]
                randframe.update({names[column]:series})
        return DataFrame(data=randframe, index=list(range(1,y+1)))
        #End CodeBlock P