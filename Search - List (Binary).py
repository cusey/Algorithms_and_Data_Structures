#python 3.5.2

class search():
    
    def __init__(self, searchList, item):
        self.searchList = searchList 
        self.item = item 
        self.front = 0
        self.back = len (searchList) -1 
        self.midpoint = self.mid()
        self.result = []
        self.done = False
        
    def mid(self):
        return ((self.back - self.front) // 2) + self.front
    
    def moveMid(self):
            self.midpoint = self.mid()
        
            print('front :',self.front,' midpoint :',  self.midpoint, 'back :', self.back) 
        
            if self.searchList[self.midpoint] > self.item:
                self.back = self.midpoint
            elif self.searchList[self.midpoint] < self.item:
                self.front = self.midpoint
            elif self.searchList[self.midpoint] == self.item:
                self.done = True
                self.result.append(self.midpoint)
                
               
    def sweep(self):
         
        #Left Sweep
        counter = self.midpoint -1
            
        while self.item == self.searchList [ counter ] and counter <= 0:
            self.result.append(counter)
            counter = counter -1
            
        #Right Sweep
        counter = self.midpoint +1
            
        while self.item == self.searchList [ counter ] and counter >= len(self.searchList) :
            self.result.append(counter)
            counter = counter +1
            
            
    
                
    def atEnds(self):
        return self.midpoint == 1 or self.midpoint >= len(self.searchList) -2
                
    def do(self):
        
        while not (self.done or self.atEnds()) :
            self.moveMid()
            
        self.sweep()
            
        return self.result

s0 = search( [5, 10, 15, 20, 25] , 5 ) 

print ( s0.do() ) 

        
s1 = search( [5, 10, 15, 20, 25] , 10 ) 

print ( s1.do() ) 

s2 = search( [5, 10, 15, 20, 25] , 15 ) 

print ( s2.do() )

s3 = search( [5, 10, 15, 20, 25] , 20 ) 

print ( s3.do() )

s4 = search( [5, 10, 15, 20, 25] , 25 ) 

print ( s4.do() )