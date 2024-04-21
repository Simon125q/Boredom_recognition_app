

class MaxSizeQueue:
    def __init__(self, maxSize: int) -> None:
        self.currSize: int = 0
        self.maxSize: int = maxSize
        self.elements: list = list()

    def __len__(self) -> int:
        return len(self.elements)

    def add(self, data: any) -> None:
        if self.currSize >= self.maxSize:
            self.elements.pop(0)
            self.elements.append(data)
        else:
            self.elements.append(data)
            self.currSize += 1

    def getMax(self, elemBack: int = 0) -> tuple[any, float]:
        data = list()
        if elemBack >= self.currSize or elemBack == 0:
            data = self.elements
        else:
            data = self.elements[self.currSize - elemBack:]

        vals = [(x, data.count(x)) for x in set(data)]
        print(sorted(vals, key=lambda x: x[1]))
        max_val = max(vals, key = lambda x: x[1])
        return (max_val[0], round(max_val[1]/len(data), 3))


if __name__ == "__main__":
    myQueue = MaxSizeQueue(100)
    x = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'aa', 'aa', 'aa']
    y = [a + c for a in x for c in x]
    y.append('ffff')
    
    for x in y:
        myQueue.add(x)

    print(myQueue.getMax())
