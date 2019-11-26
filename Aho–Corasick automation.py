import collections
class TrieNode:
    def __init__(self):
        self.children=collections.defaultdict(TrieNode)
        self.isWord=False
        self.fail=None
        self.str=None          #store the string on this node if it is a termination of a word; void otherwise

class Trie:
    def __init__(self):
        self.root=TrieNode()
    def insert(self,word):
        cur=self.root
        for w in word:
            cur=cur.children[w]
        cur.isWord=True                # whether is word or not
        cur.str=word                   #store the word string

    def search(self,word):
        cur=self.root
        for w in word:
            cur=cur.children.get(w)
            if not cur:
                return False
        return cur.isWord

class ACautomation:
    def __init__(self,pattern_list):
        self.trie=Trie()
        self.target=pattern_list
        for w in pattern_list:
            self.trie.insert(w)
    def failGen(self):                #generate fail links for the Trie nodes
        queue=collections.deque()
        root=self.trie.root
        for key in root.children:   #push all children nodes of the root into the queue; set their fail link to the root.
            queue.append(root.children[key])
            root.children[key].fail=root
        while(queue):              #BFS to iterate over all nodes in the Trie to set fail links
            node=queue.popleft()
            failto=node.fail
            for key in node.children:
                while failto and key not in failto.children:       #while failto is not none, iterate over failto until (key in failto.children)
                    failto=failto.fail
                node.children[key].fail=failto.children[key] if failto else root
                queue.append(node.children[key])
    def find_single(self,target_string):   #find postitions of existing patterns from a single string
        cur=self.trie.root
        root=self.trie.root
        index=0
        result=collections.defaultdict(list)     #result occurence of the patterns
        while(index<len(target_string)):
            if cur.isWord:                        #if current pos isWord==True
                result[cur.str].append(index-len(cur.str))
            if cur!=root and cur.fail.isWord:     #if current pos.fail. isword==True, avoid getting break
                result[cur.fail.str].append(index-len(cur.fail.str))
            while cur!=None:
                if target_string[index] in cur.children:
                    cur=cur.children[target_string[index]]
                    break
                else:
                    cur=cur.fail
            if cur==None:
                cur=root
            index+=1
        return result


if __name__=="__main__":
    pattern_list=["abcdef","abhab","bcd","cde","cdfkcdf"]        #some pattern strings
    target_string="bcabcdebcedfabcdefababkabhabk"
    ACmachine=ACautomation(pattern_list)
    ACmachine.failGen()
    print(ACmachine.find_single(target_string))