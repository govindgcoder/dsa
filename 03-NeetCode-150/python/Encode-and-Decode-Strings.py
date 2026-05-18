inputArr = ["neet","code","love","you"]

def encode(arr):
    res = ""
    for i in arr:
        res+=str(len(i))+"."+i
    return res

def decode(s):
    res = []
    currstr=""
    readstr = 0
    count = 0
    curr = 0
    for i in s:
        if not readstr :
            val = ord(i)-ord('0')
            if 0<=val<=9:
                curr=curr*10+val
            if i=='.':
                if curr==0:
                    res.append("")
                else:
                    readstr=1
        else:
            currstr+=i
            count+=1
            if count==curr:
                readstr=0
                res.append(currstr)
                currstr=""
                count=0
                curr = 0
    return res

print(encode(inputArr))
print(decode(encode(inputArr)))
