def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
print("Выберите способ считывания матрицы.")
print("Введите 1, чтобы вписать матрицу с терминала")
print("Введите 2, чтобы вписать матрицу с файла")
variant = int(input())
if variant == 1:
    print("Добрый день, дорогой пользователь \nВведи количество уравнений в системе")
    n = int(input())
    print("Спасибо, теперь вводи коэффициенты матрицы, разделяя их пробелами")
    print("Чтобы ввести нецелые числа, используй точку.")

    matrix = []
    line = []
    correcter = 0
    for i in range(n):
        correcter = 0
        line = []
        while(correcter!=1):
            k = 0
            while (k != n+1):
                a = input().split(' ')
                k = len(a)
                if k != n+1: 
                    print("вы ввели неверное количество элементов, перевведите")
            for i in range(n + 1):
                if is_number(a[i]):
                    line.append(float(a[i]))
                    correcter = 1
                else:
                    print("вы ввели не числа, перевведите строку")
                    correcter = 0
        matrix.append(line)
    print("данные приняты в обработку")
elif variant == 2:
    f = open("Файл с матрицой.txt")
    n = int(f.readline())
    matrix = []
    line = []
    correcter = 0
    for i in range(n):
        correcter = 0
        line = []
        while(correcter!=1):
            k = 0
            while (k != n+1):
                a = f.readline().split()
                k = len(a)
                if k != n+1: 
                    print("вы ввели неверное количество элементов в одну из строк, отредактируйте файл и запустите программу заново")
            for i in range(n + 1):
                if is_number(a[i]):
                    line.append(float(a[i]))
                    correcter = 1
                else:
                    print("вы ввели некоторые числа некорректоно, отредактируйте файл и запустите программу заново")
                    correcter = 0
        matrix.append(line)
    print("данные приняты в обработку")
rez = matrix    

def count(data, n):
    new_data = []
    first_elem = data[0][0]
    for i in range(n):
        if (i == 0):
            for j in range(n+1):
                data[0][j] = data[0][j]/first_elem
        else:
            firsty_elem = data[i][0]
            for j in range(n+1):
                data[i][j] = data[i][j] - data[0][j]*firsty_elem
    
    for i in range(n-1):
        line =[]
        for j in range(n):
            line.append(data[i+1][j+1])
        new_data.append(line)
    return new_data

def triangle(matrix, n, rez):
    for i in range(n-1):
        p = count(matrix, n-i)
        for k in range(n - i):
            for t in range(n - i + 1):
                rez[i+k][i+t] = matrix[k][t]
        for k in range(n-i-1):
            for t in range(n-i):
                rez[i+k+1][i+t+1] = p[k][t]
        matrix = p
    return rez
    

def determination(matrix, n):
    proizv = 1
    for i in range(n):
        proizv = proizv * matrix[i][i]
    return proizv


def answers(matrix, n):
    listik = []
    for i in range(n):
        summ = 0
        for j in range(len(listik)):
            summ += matrix[n-i-1][n-j-1]*listik[j]
        listik.append( (matrix[n-i-1][n] - summ)/matrix[n-i-1][n-len(listik)-1] )
    return listik[::-1]

def otklon(matrix, n, listik):
    razn = []
    for i in range(n):
        summ = 0
        for j in range(n):
            summ += matrix[i][j]*listik[j]
        razn.append(matrix[i][n] - summ)
    return razn

listik = answers(rez, n)
def printing(rez, n):
    print("вывод треугольной матрицы")
    for i in range(n):
        strikt = ''
        for j in range(n+1):
            strikt+= str(rez[i][j]) + ' '
        print(strikt)
    print("вывод значения определителя")
    print(determination(rez, n))
    print("Корни уравнения")
    print(answers(rez, n))
    print("Отклонения от результата")
    print(otklon(rez, n, listik))


printing(rez, n)
    
            
    
