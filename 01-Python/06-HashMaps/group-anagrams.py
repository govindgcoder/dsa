def groupAnagrams(strs):
    buckets = {}
    for ag in strs:
        chars = [_ for _ in ag]
        chars.sort()
        key = tuple(chars)
        if key in buckets:
            buckets[key].append(ag)
        else:
            buckets[key] = [ag]
    return list(buckets.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(groupAnagrams(strs))
