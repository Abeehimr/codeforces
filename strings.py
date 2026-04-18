def lcp_array(s, sa):
    """
    Returns the longest common prefix (LCP) array for the string s and its suffix array sa.
    LCP[i] = length of longest common prefix of suffixes starting at sa[i] and sa[i-1].
    for banana, the suffix array is [5, 3, 1, 0, 4, 2] and the LCP array is [0, 1, 3, 0, 0, 2].
    """
    n = len(s)
    rank = [0]*n
    for i,v in enumerate(sa): rank[v] = i
    lcp = [0]*n
    k = 0
    for i in range(n):
        if rank[i] == 0: continue
        j = sa[rank[i]-1]
        while i+k<n and j+k<n and s[i+k]==s[j+k]: k+=1
        lcp[rank[i]] = k
        if k: k-=1
    return lcp

def suffix_array(s):
    """
    Returns the suffix array for the string s.
    suffix array is the array of starting indices of suffixes of s in sorted order.
        For example, for s = "banana", the suffix array is [5, 3, 1, 0, 4, 2] corresponding to the suffixes:
        5: "a"
        3: "ana"
        1: "anana"
        0: "banana"
        4: "na"
        2: "nana"
    """
    n = len(s)
    suffix_order = list(range(n))
    rank = list(map(ord, s))
    length = 1
    def sort_key(i):
        return (rank[i], rank[i + length] if (i+length<n) else -1)
    while length < n:
        suffix_order.sort(key=sort_key)
        new_rank = [0] * n
        for i in range(1, n):
            prev, cur = suffix_order[i-1], suffix_order[i]
            new_rank[cur] = new_rank[prev] + (sort_key(prev) < sort_key(cur))
        rank = new_rank
        length <<= 1
    return suffix_order

def border(s):
    """
    returns the border array for the string s
    where border[i] is the length of the longest *proper* prefix of s[:i+1] that is also a suffix of s[:i+1].
    """
    n = len(s)
    pi = [0]*n
    for i in range(1,n):
        j = pi[i-1]
        # while border exists and cur char != next char after border, try smaller border
        while j > 0 and s[i] != s[j]: j = pi[j-1]
        if s[i] == s[j]: j += 1 # if cur char == next char after border, we can extend border by 1
        pi[i] = j
    return pi

def kmp(s,t):
    """
    Returns cnt of occurrences of the string t in the string s.
    """
    pi = border(t)
    j = 0
    o = 0
    for i in range(len(s)):
        while j > 0 and s[i] != t[j]: j = pi[j-1]
        if s[i] == t[j]: j += 1
        if j == len(t):
            o += 1
            j = pi[j-1]
    return o

def zfunc(s):
    """
    Returns the Z-function for the string s
    where z[i] is the length of the longest substring of s starting at i that is also a prefix of s."""
    n = len(s)
    z = [0]*n
    l,r = 0,0
    for i in range(1,n):
        if i <= r: z[i] = min(r-i+1, z[i-l])
        while i+z[i] < n and s[z[i]] == s[i+z[i]]: z[i] += 1
        if i+z[i]-1 > r: l,r = i, i+z[i]-1
    return z

class PolynomialHash:
    def __init__(self, s: str, A = 911382323, B = 972663749):
        self.s = s
        self.A = A
        self.B = B
        self.n = len(s)
        self.h = [0] * self.n
        self.p = [0] * self.n
        self._precompute()
    
    def _precompute(self):
        """Precompute hash values and power values."""
        self.h[0] = ord(self.s[0]) % self.B
        self.p[0] = 1
        for i in range(1, self.n):
            self.p[i] = (self.p[i - 1] * self.A) % self.B
            self.h[i] = (self.h[i - 1] * self.A + ord(self.s[i])) % self.B
    
    def get_hash(self, a: int, b: int) -> int:
        """Get the hash of substring s[a...b]."""
        if a == 0:
                return self.h[b]
        return (self.h[b] - self.h[a - 1] * self.p[b - a + 1]) % self.B

sa = suffix_array("banana")
lcp = lcp_array("banana", sa)
print("Suffix Array:", sa)
print("LCP Array:", lcp)
print("Border Array:", border("banana"))
print("KMP:", kmp("banana", "a"))