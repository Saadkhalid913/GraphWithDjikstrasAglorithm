
class priorityqueue():

    def __init__(self):
        self.data = []
    def __repr__(self):
        return str(self.data)
    def add(self, i):
        if len(self.data) == 0:
            self.data.append(i)
        else:
            for j in range(len(self.data)):
                if self.data[j][1] > i[1]:
                    self.data.insert(j, i)
                    return
            self.data.append(i)
            
    def remove(self):
        return self.data.pop(0)
    def isempty(self):
        return len(self.data) == 0

class stack():
    def __init__(self):
        self.data = []
    def __repr__(self):
        return str(self.data)
    def add(self, i):
        self.data.append(i)
    def remove(self):
        return self.data.pop()
    def isempty(self):
        return len(self.data) == 0
    def reverse(self):
        return reversed(self.data)


def ToPath(a,b,hashtable,stack):
    stack.add(b)
    if hashtable[b] == a:
        stack.add(a)
        return list(stack.reverse())
    else:
        return ToPath(a,hashtable[b], hashtable, stack)