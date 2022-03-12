# Given an array of words and an array of sentences, determine which words are anagrams of each other. 
# Calculate how many sentences can be created by replacing any word with one of its anagrams, 
# Example wordSet = ['listen' 'silent, 'it', ' is',tinscel] 
# sentence = "listen it is silent"
# Determine that listen is an anagram of silent. Those two words can be replaced with their anagrams. 
# The four sentences that can be created are: • listen it is silent • listen it is listen • silent it is silent • silent it is listen​

def solution(sentences,wordSet):
    hm = {}
    ans = 0
    
    # loop through the wordSet to check the anagrams
    for word in wordSet:
        word = ''.join(sorted(word))
        if word not in hm:
            hm[word] = 1
        else:
            hm[word] += 1
    
    print(hm)
    
    for sentence in sentences:
        currWay = 1
        for word in sentence.split():
            word = ''.join(sorted(word))
            if word in hm:
                currWay *= hm[word]
        ans += currWay
    print(ans)
    return ans
    
solution(["listen it is silent", "listen to the teacher"], ["listen", "silent", "it", "is", "netsil"])
solution([],["listen", "silent", "it", "is", "netsil"])
solution(["today is friday"], ["listen", "silent", "it", "is", "netsil"])
