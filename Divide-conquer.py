#1. Merge sort
def MergeSort(array):
    temp=[0]*len(array)
    def sort(a,left,right,temp):
        if left<right:
            mid=(left+right)//2
            sort(a,left,mid,temp)
            sort(a,mid+1,right,temp)
            merge(a,left,mid,right,temp)
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

if __name__=="__main__":
    array=[6,9,1,12,4,8,28,0]
    MergeSort(array)
    print(array)
