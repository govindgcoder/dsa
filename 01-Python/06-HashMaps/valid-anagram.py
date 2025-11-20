def check(s1, s2):
    if len(s1) != len(s2):
        print("NOT")
        return False

    def helper(fmap, s):
        for i in s:
            if i not in fmap.keys():
                fmap[i] = 1
            else:
                fmap[i] += 1

    map1 = {}
    map2 = {}
    helper(map1, s1)
    helper(map2, s2)
    return map1 == map2


s1 = "abct"
s2 = "bcta"

print(check(s1, s2))
