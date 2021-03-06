#1. Merge sort
def MergeSort(array):
    temp=[0]*len(array)                #new a temp list to store temporary result in the merge process
    def sort(a,left,right,temp):
        if left<right:
            mid=(left+right)//2 
            sort(a,left,mid,temp)        #sort the left  side
            sort(a,mid+1,right,temp)     #sort the right side 
            merge(a,left,mid,right,temp)    # merge the left side and right side together
    def merge(ar,left,mid,right,temp):
        i=left
        j=mid+1
        tmp_p=0
        while(i<=mid and j<=right):
            if ar[i]<=ar[j]:
                temp[tmp_p]=ar[i]
                i+=1
            else:
                temp[tmp_p]=ar[j]
                j+=1
            tmp_p+=1
        while(i<=mid):
            temp[tmp_p]=ar[i]
            i+=1
            tmp_p+=1
        while(j<=right):
            temp[tmp_p]=ar[j]
            j+=1
            tmp_p+=1
        for index in range(right-left+1):
            ar[left+index]=temp[index]
    sort(array,0,len(array)-1,temp)


#2. One-diemensional poset problem----  calculate the number of reverse order pairs(ROP)
# The basic idea is to split into left and right part, then calculate ROP of the left and right and sort them, the sum=left+right+mergeresult
# reference: https://blog.csdn.net/DERRANTCM/article/details/46761051
def CDQReverOrderCal(array):
    temp=[0]*len(array)

    def CDQ(ar,left,right,temp):
        if left<right:
            mid=(left+right)//2
            leftside=CDQ(ar,left,mid,temp)           #reverse order pair number in the left side
            rightside=CDQ(ar,mid+1,right,temp)       #reverse order pair number in the right side
            middle=merge(ar,left,mid,right,temp)     # newly generated reverse order pair between left and right side
            return leftside+rightside+middle
        else:
            return 0
    def merge(ar,left,mid,right,temp):
        p=mid
        q=right
        tmp_p=len(temp)-1
        count=0
        while(p>=left and q>=mid+1):
            if ar[p]>ar[q]:
                count+=q-mid                   #important, if left pointed value greater than the right pointed value, then the reverse order pair number is the from right pointer to the head of the right part.
                temp[tmp_p]=ar[p]
                p-=1
            else:
                temp[tmp_p]=ar[q]
                q-=1
            tmp_p-=1
        while p>=left:
            temp[tmp_p]=ar[p]
            tmp_p-=1
            p-=1
        while q>=mid+1:
            temp[tmp_p]=ar[q]
            tmp_p-=1
            q-=1
        ar[left:right+1]=temp[tmp_p+1:]
        return count
    return CDQ(array,0,len(array)-1,temp)
            
#3. Two-diemensional poset problem----  CDQ divide and conquer algorithm
#def CDQ(left,right):
#   if left==right:
#       return
#   mid=(L+R)//2
#   CDQ(left,mid)
#   CDQ(mid+1,right)
#   Handling the influence of left CDQ to the right part


#4. Binary indexed tree 树状数组   reference: https://blog.csdn.net/Yaokai_AssultMaster/article/details/79492190

class BinaryIndexTree:
    def __init__(self,inputlist):
        self.ori=inputlist
        self.bit=self.construct_tree(self.ori)   #binary index tree
    def construct_tree(self,input):
        ans=[0]+input
        for index in range(1,len(ans)):
            next=index+(index&(-index))
            if next<len(ans):
                ans[next]=ans[next]+ans[index]
        return ans
    def prefixsum(self,idx):         # the top idx sum
        current=idx
        ans=0
        while(current>0):
            ans+=self.bit[current]
            current=current-(current&(-current))
        return ans
    def update(self,idx,value):       #change idx index of origin to value     
        difference=value-self.bit[idx+1]       
        current=idx+1
        while current<len(self.bit):
            self.bit[current]+=difference
            current=current+(current&(-current))
    def rangesum(self,idx1,idx2):
        return self.prefixsum(idx2)-self.prefixsum(idx1)

#5. Segmentation tree 线段树 

if __name__=="__main__":
    array=[6,9,1,12,4,8,28,0]
    array2=[7,5,6,4]
    array3=[6, 5, 4, 3, 2, 1]
    BITarray=[1,7,3,0,7,8,3,2,6,2,1,1,4,5]
    arrayBit=[1,7,3,0,5,8,3,2,6,2,1,1,4,5]
    #MergeSort(array)
    #print(array)
    #print(CDQReverOrderCal(array3))
    Bit=BinaryIndexTree(arrayBit)
    print(Bit.bit)
    Bit.update(4,7)
    print(Bit.bit)
