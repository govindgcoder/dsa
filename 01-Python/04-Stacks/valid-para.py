def isValid(str):
   brackets = []
   mapping = {'(':')','{':'}','[':']'}
   for i in str:
      if i in mapping.keys():
         brackets.append(i)
      if i in mapping.values():
         if not brackets: return False
         curr = brackets.pop()
         if mapping[curr] != i: return False
      print(brackets)
   return True if not brackets else False

str = '{{'
print(str)
print(isValid(str))