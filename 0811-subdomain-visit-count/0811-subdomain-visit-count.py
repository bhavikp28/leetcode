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
        return [f'{count} {domain}' for domain,count in counts.items()]