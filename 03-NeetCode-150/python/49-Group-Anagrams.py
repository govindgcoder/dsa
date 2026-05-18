"""Given an array of strings strs, group the together. """

strs = ["a"]

def groupAnagrams(strs):
    map = {}
    for i in strs:
        key = "".join(sorted(i))
        print(key)
        if key not in map:
            map[key]=[]
        map[key].append(i)
    return list(map.values())
    
print(groupAnagrams(strs))