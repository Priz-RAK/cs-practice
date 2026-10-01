porog=float(input())
n=int(input())
schet_oshibok=0
previshenie=0
max_new=-10**10
sum=0
schet_ne_oshibok=0
for i in range(n):
    new=input()
    if new=='error':
        schet_oshibok+=1
    else:
        ne_oshibka=float(new)
        if ne_oshibka>porog:
            previshenie+=1
        if ne_oshibka>max_new:
            max_new=ne_oshibka
        sum+=ne_oshibka
        schet_ne_oshibok+=1

print(n)
print(schet_oshibok)
print(previshenie)
print(f'{max_new:.1f}')
print(f'{sum/schet_ne_oshibok:.1f}')
