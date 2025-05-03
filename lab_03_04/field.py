goods = [
   {'title': 'Ковер', 'price': 2000, 'color': 'green'},
   {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
]
# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}

def field(items, *args):
    try:
        assert len(args) > 0
    except: 
        print("Нет подходящих аргументов.")
        return
    if len(args) == 1:
            for i in items:
                yield i[args[0]]
    else:
        for i in range(len(items)):
            answer = {}
            flag=0
            for j in range(len(args)):
                if(args[j] in items[i]):
                    answer[args[j]] = items[i][args[j]]
            yield answer
                
def main():
    for i in field(goods, 'title'):
        print(i)
    for i in field(goods, 'title', 'price'):
        print(i)

if __name__ == "__main__":
    main()