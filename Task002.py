#Задача №2
#Петя, Катя и Сережа делают из бумаги журавликов.
#Вместе они сделали S журавликов. 
#Сколько журавликов сделал каждый ребенок, если известно, что 
#Петя и Сережа сделали одинаковое количество журавликов, 
#а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

#*Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

cranes = int(input('Введите количество сделанных детьми журавликов: '))
if (cranes%6 == 0):
    print(f'Петя, Катя и Сережа сделали {cranes//6}, {cranes//6*4} и {cranes//6} журавликов соответственно.')
else:
    print('Количество журавликов не подходит под условия данной задачи.')