A  = int(input()) #абонентская плаат
B  = int(input()) #количество трафика
C  = int(input()) #каждый следующий мегабайт тоит
D  = int(input()) #планирует потратить

result_sum  = A #изначально равна абонетской плате

if B >= D:
    print(A)
else:
    #если в пакете меньше трафика
    change = D - B
    print(result_sum + (change * C))
