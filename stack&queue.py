books=[]
books.append("Learn c")
books.append("Learn java")
books.append("Learn c++")
print (books)

books.pop()
print("now the top book is:",books[-1])
books.pop()
print("now the top book is:",books[-1])
books.pop()
if not books:
    print("no books left")

# Queue
from collections import deque
school=deque(["sallu","jahod","jannat","sajib"])
print(school)
school.popleft()
print(school)
school.popleft()
school.popleft()
if not school:
    print("no persion left")