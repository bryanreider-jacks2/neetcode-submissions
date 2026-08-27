class TimeMap:

    def __init__(self):
        self.store = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        values = self.store[key]
        l, r = 0, len(values) - 1
        result = ""

        while l <= r:
            m = (l + r) // 2
            
            if values[m][0] <= timestamp:
                result = values[m][1]
                l = m + 1
            else:
                r = m - 1
        return result

'''
self.store = {
    alice : [(1, "happy"), (3, "sad")]
}

values = [(1, "happy"), (3, "sad")]
l,r = 2,1
m = 1
timestamp = 3
result = "sad"
'''


