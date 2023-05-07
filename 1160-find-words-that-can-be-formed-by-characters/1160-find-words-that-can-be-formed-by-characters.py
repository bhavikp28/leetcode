class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        hmap = collections.defaultdict(int)
        hmap = collections.defaultdict(int)
        for i in chars:
            hmap[i] += 1
        count = 0
        for word in words:
            goodword = True
            hmap2 = collections.defaultdict(int)
            for letter in word:
                hmap2[letter] +=1
                if hmap[letter] >= hmap2[letter]:
                    pass
                else:
                    goodword = False
            if goodword == True:
                count += len(word)
        return(count)        