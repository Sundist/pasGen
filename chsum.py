import random



def topla(param):
    k = 0
    p = 0
    n = 0

    for i in param:
        n = n+ int(i)
    print('{} basamak toplamı -> {}'.format(len(param),n))
          
    for i in param[0:-1]:
        k = k+ int(i)
        #print(k)
    s = str(k)
    print('basamak-1 toplamı:',s)
    print('son hane:',param[-1])
    
    for j in s:
        p = p + int(j)
        #print(p)
    return str(p)


while True:
    pin = random.randrange(0,99999999)
    print('PİN:',pin)
    mak = str(pin)
    print('Basamak sayısı:',len(mak))
    if topla(mak) == mak[-1]:
        print('Buldum!!',mak)
        break
       
        
