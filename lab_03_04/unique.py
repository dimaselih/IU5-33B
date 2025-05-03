# Итератор для удаления дубликатов
from gen_random import gen_random
class Unique(object):
    def __init__(self, items, **kwargs):
        self.answer=[]
        self.index=0
        try:
            if kwargs["ignore_case"] == True:
                try:
                    for i in range(len(items)):
                        items[i]=items[i].lower()
                except:
                    pass
                for i in items:
                    if not i in self.answer:
                        self.answer.append(i)
            else:
                for i in items:
                    if not i in self.answer:
                        self.answer.append(i)
        except:
            for i in items:
                if not i in self.answer:
                    self.answer.append(i)
        
        

    def __next__(self):
        if self.index < len(self.answer):
            result = self.answer[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

    def __iter__(self):
        return self
    
def main():
    data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    
    for i in Unique(data):
        print(i,end = ' ')
    print()

    data = gen_random(10, 1, 3)
    for i in Unique(data):
        print(i,end = ' ')
    print()

    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    for i in Unique(data):
        print(i,end = ' ')
    print()
    for i in Unique(data, ignore_case=True):
        print(i,end = ' ')
    print()

if __name__ == "__main__":
    main()