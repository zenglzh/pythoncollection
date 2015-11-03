# encoding= utr-8
# 现在有一个包含N个元素的元组或者是序列，怎样将它里面的值解压后同时赋值给N个变量？
data = ['ACME', 43, 93.2, (2012, 12, 21)]
name, shares, price, (year, mon, day) = data

# 如果一个可迭代对象的元素个数超过变量个数时，会出现”太多解压值”的异常。 那么怎样才能从这个可迭代对象中解压出N个元素出来？
def avg(first, *rest): 
    return (first + sum(rest)) // (1 + len(rest))

def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)

record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = user_record

#1.3 保留最后N个元素:在迭代操作或者其他操作的时候，怎样只保留最后有限几个元素的历史记录？
from collections import deque

def search(lines,pattern,history=5):
    previous_lines = deque(maxlen=history)
    for li in lines:
        if pattern in li:
            yield li,previous_lines
        previous_lines.append(line)
# Example use on a file
if __name__ == '__main__':
    with open(r'somefile.txt') as f:
        for line,prevines in search(f,'Python',5):
            for pline in prevlines:
                print(pline,end='')
            print(line,end='')
            print('-'* 20)

# 怎样从一个集合中获得最大或者最小的N个元素列表？
            
import heapq
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums)) # Prints [42, 37, 23]
print(heapq.nsmallest(3, nums)) # Prints [-4, 1, 2]

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])

# 怎样实现一个按优先级排序的队列？ 并且在这个队列上面每次pop操作总是返回优先级最高的那个元素


class PriorityQueue:
    
    def __init__(self):
        self._queue=[]
        self._index = 0
        
    def push(self,item,priority):
        heapq.heappush(self._queue,(-priority,self._index,item))
        self._index+=1

    def pop(self):
        return heapq.heapqpop(self._queue)[-1]

class Item:
    def __init__(self,name):
        self.name= name
        
    def __repr__(self):
        return 'Item({!r})'.format(self.name)

q = PriorityQueue()
# 1.6 字典中的键映射多个值

from collection import defaultdict
d = default(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)

# 1.7 字典排序
from collections import OrderdDict

def orderd_dict():
    d = OrderDict()
    d['foo'] = 1
    d['fbar'] = 2
    d['spa'] = 3
    
import  json
json.dumps(d)
    
# 怎样在数据字典中执行一些计算操作(比如求最小值、最大值、排序等等)？
    
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

min_price = min(zip(prices.values(), prices.keys()))
# min_price is (10.75, 'FB')
max_price = max(zip(prices.values(), prices.keys()))
# max_price is (612.78, 'AAPL')

# 1.9 查找两字典的相同点
a = {
    'x' : 1,
    'y' : 2,
    'z' : 3
}

b = {
    'w' : 10,
    'x' : 11,
    'y' : 2
}
# Find keys in common
a.keys() & b.keys() # { 'x', 'y' }
# Find keys in a that are not in b
a.keys() - b.keys() # { 'z' }
# Find (key,value) pairs in common
a.items() & b.items() # { ('y', 2) }

# 1.10 删除序列相同元素并保持顺序
#列上的值都是hashable类型
def dedupe(items):
    seen = Set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

# 如果你想消除元素不可哈希(比如dict类型)的序列中重复元素
def dedupeno(items,key = None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)




















