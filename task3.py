# Реализовать алгоритм Кана для топологической сортировки
# Пример с пошаговой работой алгоритма
# Граф: A → B → C
#       A → D

graf = {"A" : ["B", "D", 'e'],
        "B" : ["C", "D"],
        "C" : [],
        "D" : ['r'],
        'e': [],
        'r':[]}

# Шаги:
# 1. Начальные вершины без входящих рёбер: [A]
# 2. Обрабатываем A → результат [A], обновляем степени B(1→0), D(1→0)
# 3. Вершины для обработки: [B, D]
# 4. Обрабатываем B → результат [A,B], обновляем степень C(1→0)
# 5. Обрабатываем D → результат [A,B,D]
# 6. Обрабатываем C → результат [A,B,D,C]
# 7. Все вершины обработаны → сортировка завершена

def Kan(graf):
    degree={}
    line = []
    for key in graf.keys():
        degree[key]=0
    for key, val in graf.items():
        for i in val:
            degree[i]+=1

    for key, val in degree.items():
        if val==0:
            line.append(key)

    answer=[]
    while len(line)!=0:
        symbol=line[0]
        answer.append(symbol)
        line.remove(symbol)

        down_degree=graf[symbol]
        for i in down_degree:
            degree[i]-=1
        for key, val in degree.items():
            if val<=0 and key not in line and key not in answer:
                line.append(key)


    return answer

print(Kan(graf))
