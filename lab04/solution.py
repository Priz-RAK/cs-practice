
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
    if n==0:
        sum/n=0.0
    n=len(scores)
    for i in range(n):
        sum+=scores[i]
    return sum/n

def ranking(names,scores):
    reverse_index=sorted(
        range(len(scores))
        lambda i:scores[i]
        Reverse=True
    return reverse_index

def above_average(names,scores):
    avr=average(names,scores)
    for i in range(len(scores):
        if scores[i]>avr:
    return names[i]
