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

def average(scores):
    sum=0.0
    n=len(scores)
    if n==0:
        sum/n==0.0
    for i in range(n):
        sum+=scores[i]
    return round(sum/n,2)

def ranking(names,scores):
    a=[]
    reverse_index=sorted(
        range(len(scores)),
        key=lambda i:scores[i],
        reverse=True
        )
    for i in reverse_index:
        a.appendd(names[i])
    return a

def above_average(names,scores):
    avr=average(scores)
    a=[]
    for i in range(len(names)):
        if scores[i]>avr:
            a.append(names[i])
    return a
