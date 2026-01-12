"""
	TimeMap() Initializes the object of the data structure.
    void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
    String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".



Example 1:

Input
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output
[null, null, "bar", "bar", null, "bar2", "bar2"]
"""


class TimeMap:
	def __init__(self):
		self.map = {}

	def set(self, key: str, value: str, timestamp: int) -> None:
		if key not in self.map:
			self.map[key] = []
		self.map[key].append([timestamp, value])


	def get(self, key: str, timestamp: int) -> str:
		if key not in self.map: return ""
		keyValues = self.map[key]
		left=0
		right=len(keyValues)-1
		val = [0,""]
		while(left<=right):
			mid=left+(right-left)//2
			curr=keyValues[mid]
			if curr[0] <= timestamp:
				val=curr
				left=mid+1
			else:
				right=mid-1
		return val[1]

timeMap = TimeMap();
timeMap.set("foo", "bar", 1)
timeMap.set("foo", "bar2", 4)
print(timeMap.get("foo", 4)   )
print(timeMap.get("foo", 5))
print(timeMap.get("foo", 1))
