#python 3.5.2

class search():
    
    def __init__(self, searchList, item):
        self.searchList = searchList
        print( 'List: ', self.searchList )
        self.item = item 
        print('Number Search For: ', self.item)
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
                
               
    def sweep(self,direction):
        
        increment = 0
        
        if direction == 'RIGHT':
            increment = 1
            stopIndex = len(self.searchList) - 1
            
        if direction == 'LEFT':
            increment = - 1
            stopIndex = 0

        counter = self.midpoint + increment
        sweepDone = False
        
        while counter <= stopIndex and not sweepDone :
            if self.item == self.searchList [ counter ] :
                self.result.append(counter)
            else:
                sweepDone = True
            
            counter = counter + increment

    def atEnds(self):
        return self.midpoint == 1 or self.midpoint >= len(self.searchList) -2
                
    def do(self):
        
        while not (self.done or self.atEnds()) :
            self.moveMid()
            
        self.sweep('RIGHT')
            
        self.sweep('LEFT')
            
        return self.result
    
def log(line):
    print ( line )
    print ( '-'*20 + '\n' )
    

s0 = search( [5, 10, 15, 20, 25] , 5 ) 
log( s0.do() ) 

s1 = search( [5, 10, 15, 20, 25] , 10 ) 
log( s1.do() ) 

s2 = search( [5, 10, 15, 20, 25] , 15 ) 
log( s2.do() )

s3 = search( [5, 10, 15, 20, 25] , 20 ) 
log( s3.do() )

s4 = search( [5, 10, 15, 20, 25] , 25 ) 
log( s4.do() )

s5 = search( [5, 5, 10, 15, 20, 25] , 5 ) 
log( s5.do() )

s6 = search( [5, 10, 15, 20, 25, 25] , 25 ) 
log( s6.do() )

s7 = search( [5, 10, 10, 15, 20, 25, 25] , 10 ) 
log( s7.do() )


'''
OUPUT:

List:  [5, 10, 15, 20, 25]
Number Search For:  5
front : 0  midpoint : 2 back : 4
front : 0  midpoint : 1 back : 2
[0]
--------------------

List:  [5, 10, 15, 20, 25]
Number Search For:  10
front : 0  midpoint : 2 back : 4
front : 0  midpoint : 1 back : 2
[1]
--------------------

List:  [5, 10, 15, 20, 25]
Number Search For:  15
front : 0  midpoint : 2 back : 4
[2]
--------------------

List:  [5, 10, 15, 20, 25]
Number Search For:  20
front : 0  midpoint : 2 back : 4
front : 2  midpoint : 3 back : 4
[3]
--------------------

List:  [5, 10, 15, 20, 25]
Number Search For:  25
front : 0  midpoint : 2 back : 4
front : 2  midpoint : 3 back : 4
[4]
--------------------

List:  [5, 5, 10, 15, 20, 25]
Number Search For:  5
front : 0  midpoint : 2 back : 5
front : 0  midpoint : 1 back : 2
[1, 0]
--------------------

List:  [5, 10, 15, 20, 25, 25]
Number Search For:  25
front : 0  midpoint : 2 back : 5
front : 2  midpoint : 3 back : 5
front : 3  midpoint : 4 back : 5
[4, 5]
--------------------

List:  [5, 10, 10, 15, 20, 25, 25]
Number Search For:  10
front : 0  midpoint : 3 back : 6
front : 0  midpoint : 1 back : 3
[1, 2]
--------------------

'''

        

