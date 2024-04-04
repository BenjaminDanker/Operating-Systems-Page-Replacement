import random
from queue import Queue

FRAMES = 4

# Least recently used algorithm
def LRUpaging(pageReference):
    pageTable = set()
    pageDict = {}
    faults = 0
    
    for num, c in enumerate(pageReference):
        # if the page number is not already in the page frame
        if c not in pageTable:
            
            # if page frame is not full
            if len(pageTable) < FRAMES:
                pageTable.add(c)
                
                # add recently used index to hash table
                pageDict[c] = num
                
                faults += 1
            else:
                recentIndex = float('inf')
                
                # set pageNum equal to least recently used index
                for d in pageTable:
                    if pageDict[d] < recentIndex:
                        recentIndex = pageDict[d]
                        pageNum = d
                        
                pageTable.remove(pageNum)
                pageTable.add(pageReference[num])
                
                pageDict[c] = num

                faults += 1
                
        print("pageTable: ", pageTable, " faults: ", faults)
                
# used to predict the most likely page number not be used soon
def predict(pageTable, pageReference, index):
    res = -1
    farthest = index
    
    for num, c in enumerate(pageTable):
        j = 0
        for j in range(index, len(pageReference)):
            if c == pageReference[j]:
                if j > farthest:
                    farthest = j
                    res = num
                break
            
        if j == len(pageReference):
            return num
        
    if res == -1:
        return 0
    else:
        return res

# Optimal algorithm
def optimalPaging(pageReference):
    pageTable = set()
    faults = 0
    
    for num, c in enumerate(pageReference):
        # if the page number is not already in the page frame
        if c not in pageTable:
            # if page frame is not full
            if len(pageTable) < FRAMES:
                pageTable.add(c)
                
                faults += 1
            else:
                # get predicted index
                predictedIndex = predict(pageTable, pageReference, num+1)
                try:
                    pageTable.remove(pageReference[predictedIndex])
                    pageTable.add(c)
                except KeyError:
                    pass
                
                faults +=1

        print("pageTable: ", pageTable, " faults: ", faults)

# First in first out algorithm
def FIFOpaging(pageReference):
    que = Queue()
    pageTable = set()
    faults = 0
    
    for c in pageReference:
        # if the page number is not already in the page frame
        if c not in pageTable:    
            # if page frame is not full
            if len(pageTable) < FRAMES:
                # add page number
                pageTable.add(c)
                que.put(c)
                
                faults += 1
        
            else:
                # get first page number
                pageNum = que.queue[0]
                que.get()
                
                # remove page number
                pageTable.remove(pageNum)
                
                # add page number
                pageTable.add(c)
                que.put(c)
                
                faults += 1
         
        print("pageTable: ", pageTable, " faults: ", faults)

def main():
    # info
    print("Page reference range is 1-5")
    print("Number of frames is 4")
    
    # get reference array length
    print("Enter page reference array length")
    inp = input()
    
    # create reference array
    pageReference = []
    for i in range(int(inp)):
        ran = random.randint(1,5)
        pageReference.append(ran)
        
    # print reference array
    print("Page reference array: ")
    print(pageReference)

    
    # call each paging algorithm
    print("\nLeast Recent Used Algorithm: ")
    print("Time Complexity O(n) ")
    LRUpaging([7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2] )
    
    print("\nOptimal Algorithm: ")
    print("Time Complexity O(4n) ")
    optimalPaging(pageReference)
    
    print("\nFIFO Algorithm: ")
    print("Time Complexity O(n)")
    FIFOpaging(pageReference)


if __name__ == "__main__":
    main()