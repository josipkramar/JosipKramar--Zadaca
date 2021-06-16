def rekurzija(n):
    if len(n)==1:
         return n
    else:
         return rekurzija(n[1::]) + n[0]
