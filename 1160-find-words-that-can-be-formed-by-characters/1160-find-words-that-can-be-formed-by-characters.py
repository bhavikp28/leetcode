class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        hmap = collections.defaultdict(int)
        for i in chars:
            hmap[i] += 1
        ans = []
        for word in words:
            hmap2 = collections.defaultdict(int)
            count = 0
            for letter in word:
                hmap2[letter] +=1
                if hmap[letter] >= hmap2[letter]:
                    count += 1
            if count == len(word):
                ans.append(word)
        total = 0
        for i in ans:
            for a in i:
                total += 1
        return total