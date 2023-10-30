Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
myneighbours=[8,9,10]
myneighbours.append(4)
print(myneighbours)
[8, 9, 10, 4]
myneighbours.remove(4)
print(myneighbours)
[8, 9, 10]
myneighbours.append(11)
print(myneighbours)
... [8, 9, 10, 11]
... myneighbours.insert(0,7)
... print(myneighbours)
... [7, 8, 9, 10, 11]
... myneighbours.pop()
... 11
... myneighbours.pop(0)
... 7
... myneighbours.append(11)
... print(myneighbours)
... [8, 9, 10, 11]
... myneighbours.insert(0,7)
... print(myneighbours)
... [7, 8, 9, 10, 11]
... del myneighbours[0]
... print(myneighbours)
... [8, 9, 10, 11]
... myneighbours.insert(0,7)
... print(myneighbours)
... [7, 8, 9, 10, 11]
... 
... myneigh=list(myneighbours)
... print(myneigh)
... [7, 8, 9, 10, 11]
... batch.count(9)
... 0
... myneigh.count(7)
... 1
... myneigh.sort()
... print(myneigh)
... [7, 8, 9, 10, 11]
... [myneigh.sort()].reverse()
... print(myneigh)
... [7, 8, 9, 10, 11]
... myneigh.reverse()
... print(myneigh)
... [11, 10, 9, 8, 7]
... del myneighbours
... print(myneighbours)
... Traceback (most recent call last):
...   File "<pyshell#82>", line 1, in <module>
...     print(myneighbours)
... NameError: name 'myneighbours' is not defined
... myneigh.clear()
... print(myneigh)
... []
