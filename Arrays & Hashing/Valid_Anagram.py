s = "fe"
t = "ja"
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1  # frequency of each character as it's added
    for char in t:
        freq[char] = freq.get(char, 0) - 1  # frequency of each character as it's removed

    for cnt in freq.values():
        if cnt != 0:
            return False
    return True

ans = isAnagram(s, t)
print(ans)
