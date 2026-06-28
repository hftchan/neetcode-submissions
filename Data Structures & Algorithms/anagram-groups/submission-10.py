class Solution:
    def isAna(self,str1, str2):
        if (set(str1) == set(str2) and len(str1) == len(str2)):
            #There is no absolute order that the listed set applies, so I need to use sorted
            listset1 = sorted(list(set(str1)))
            listset2 = sorted(list(set(str2)))
            count1= [0]*len(listset1)
            count2= [0]*len(listset2)
            for i in range(len(str1)):
                count1[listset1.index(str1[i])]+=1
                count2[listset2.index(str2[i])]+=1
            if count1 == count2:
                return True
            else:
                return False
        return False         

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_copy = strs.copy()
        groups=[]
        for i in range(len(strs)):
            #Make the group of matching, and only find its anagrams if it still exists within the unfiltered set
            temp = []
            if strs[i] in strs_copy:
                temp.append(strs[i])

                #now find all future candidates
                for j in range(i+1,len(strs)):
                    if self.isAna(strs[i], strs[j]) == True:
                        #print(strs[i], strs[j])
                        #add it if it still has not been processed
                        if strs[j] in strs_copy : 
                            temp.append(strs[j])
            #print(temp)
            #remove copies from temp
                for k in range(len(temp)):
                    if temp[k] in strs_copy:
                        strs_copy.remove(temp[k])
                    #
                if temp != []:
                    groups.append(temp)
            #print(groups)
        return groups
        