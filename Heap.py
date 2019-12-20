class heap:
    def __init__(self, target_list,category="small"):
        if category not in {"small","big"}:
            raise Exception("Invalid category")
        self.category=category
        self.heap=target_list
        if self.heap:
            self.heapify()
    def insert(self,num):
        self.heap.append(num)
        c_index=len(self.heap)-1
        while(c_index>0):
            pop=0
            parent_index=(c_index-1)//2
            if self.category=="small":
                if self.heap[parent_index]>self.heap[c_index]:
                    pop=1
                    self.heap[parent_index],self.heap[c_index]= self.heap[c_index],self.heap[parent_index]
                    c_index=parent_index
            elif self.category=="big":
                if self.heap[parent_index]<self.heap[c_index]:
                    pop=1
                    self.heap[parent_index],self.heap[c_index]= self.heap[c_index],self.heap[parent_index]
                    c_index=parent_index
            if not pop:
                break
    def pop(self):
        num=self.heap.pop()
        self.heap[0]=num
        self.downside(0,self.category)

    def downside(self,c_index,category):
            son_left=c_index*2+1
            son_right=c_index*2+2
            if c_index>len(self.heap)-1 or son_left>len(self.heap)-1:
                return
            avai=[son_left,son_right] if son_right<len(self.heap) else [son_left]
            value=self.heap[c_index]
            if category=="small":
                change=-1
                for child in avai:
                    if value>self.heap[child]:
                        value=self.heap[child]
                        change=child
                if change!=-1:
                    self.heap[c_index],self.heap[change]=self.heap[change],self.heap[c_index]
                    self.downside(change,category)
            elif category=="big":
                change=-1
                for child in avai:
                    if value<self.heap[child]:
                        value=self.heap[child]
                        change=child
                if change!=-1:
                    self.heap[c_index],self.heap[change]=self.heap[change],self.heap[c_index]
                    self.downside(change,category)
    def heapify(self):
        for index in range(len(self.heap)//2-1,-1,-1):
            self.downside(index,self.category)
    
if __name__=="__main__":
    A=[9,12,17,30,50,20,60,65,4,49]
    my_heap=heap(A,"big")
    my_heap.insert(2)
    print(my_heap.heap)