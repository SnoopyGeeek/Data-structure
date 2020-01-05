# the key is to construct next array: 
#      1. The first item in the array is -1; 
#      2. The next[index] represents the maximal common prefix and suffix lengh of the pattern_string[0:index], i.e., the character on the left side of the index. For instance, ABAB the maximal common prefix and suffix length is 2 as "AB" for prefix and "AB" for suffix.
#      3. Note that for prefix and suffix, the last cha and first cha does not count in. For instance, the available prefix for "ABAB" is ["A", "AB","ABA"]; the available suffix of "ABAB" is ["B","AB","BAB"] 
#      4. You can optimize the nextGen algorithm
#      5. The complexity is O(m+n), m for searching and n for building next array.
# reference: https://blog.csdn.net/v_july_v/article/details/7041827

from collections import defaultdict
import time
import string
import random
def nextGen(pattern_string): #return a list   #prefix and suffix does not Include last and first character
    next_a=[0]*len(pattern_string)                         
    for index in range(1,len(pattern_string)):
        k=next_a[index-1]
        flag=0
        while(pattern_string[index]!=pattern_string[k] and not flag):
            if k==0:
                flag=1
            k=next_a[k-1]
        next_a[index]=k+1 if not flag else 0
    return [-1]+next_a[0:len(next_a)-1]

def KMP_first(target_string, pattern_string):  #find the first position of matching patterns
    next_a=nextGen(pattern_string)
    i=0
    j=0
    while(i<len(target_string) and j<len(pattern_string)):
        if j==-1 or target_string[i]==pattern_string[j]:
            i+=1
            j+=1
        else:
            j=next_a[j]
    if j==len(pattern_string):
        return i-j
    else:
        return -1
    
def KMP_all(target_string, pattern_string):   #find all positions of matching patterns
    ans=[]
    next_a=nextGen(pattern_string)
    i=0
    j=0
    while i<=len(target_string):
        if j==len(pattern_string):
            ans.append(i-j)
            j=0
        if i==len(target_string):
            break
        if j==-1 or target_string[i]==pattern_string[j]:
            i+=1
            j+=1
        else:
            j=next_a[j]
    return ans

def Robin_karp_find_all(target_string,pattern_string):
    if len(target_string)<len(pattern_string):
        return []
    base=100
    baseK=1
    modulo=10**9+7
    hash_s=0
    hash_p=0
    ans=[]
    for index in range(len(pattern_string)):
        hash_s=(hash_s*base+ord(target_string[index]))%modulo
        hash_p=(hash_p*base+ord(pattern_string[index]))%modulo
        baseK=(baseK*base)%modulo

    for index in range(len(target_string)-len(pattern_string)+1):
        if hash_s==hash_p and target_string[index:index+len(pattern_string)]==pattern_string:
            ans.append(index)
        if index<len(target_string)-len(pattern_string):
            hash_s=(hash_s*base-baseK*ord(target_string[index])+ord(target_string[index+len(pattern_string)])+modulo)%modulo         #important
    return ans




if __name__=="__main__":
    pattern_string1="ABCDABCE"
    pattern_string2="ABCDABDE"
    pattern_string3="DABCDABDE"
    pattern_string4="aaaaaaaaab"
    long_string=""
    for _ in range(10**6+3):
        long_string+=random.choice(string.ascii_letters)

    print(nextGen(pattern_string4))



    start=time.time()                                                #test the execution time of KMP and robin-karp
    print(KMP_all(long_string,long_string[18:26]))
    end=time.time()
    print("KMP executing time is {} s".format(end-start))


    start=time.time()
    print(Robin_karp_find_all(long_string,long_string[18:26]))
    end=time.time()
    print("Robin-karp executing time is {} s".format(end-start))