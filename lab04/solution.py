names =  ["Аня", "Боря", "Вика"]
scores = [7.0,   9.0,    9.0]

def winner(names,scores):
    max=-100.0
    winname=''
    for i in range(len(scores)):
        if scores[i]>max:
            max=scores[i]
            winname=names[i]
    return winname

def average(names,scores):
    sum=0.0
    n=len(scores)
    avr=sum/n
    if n==0:
        avr=0.0
    for i in range(n):
        sum+=scores[i]
    return avr

def ranking(names,scores):
    a=[]
    reverse_index=sorted(
        range(len(scores)),
        lambda i:scores[i],
        Reverse=True
        )
    for i in revers_index:
        a.appendd(names[i])
    return a

def above_average(names,scores):
    avr=average(names,scores)
    a=[]
    for i in range(len(scores)):
        if scores[i]>avr:
            a.append(names[i])
    return a
