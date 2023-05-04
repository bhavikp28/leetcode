class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counts = collections.defaultdict(int)
        ans = []
        for domain in cpdomains:
            count, dom = domain.split()
            count = int(count)
            frag = dom.split('.')
            for i in range(len(frag)):
                counts['.'.join(frag[i:])] += count
        for key,value in counts.items():
            v = str(value)
            s = ''
            s += v
            s += ' '
            s += key
            ans.append(s)
        return(ans)