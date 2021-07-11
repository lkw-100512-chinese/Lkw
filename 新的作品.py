import random
dictionary = 'QWERTYUIOPASDFGHJKLZXCVBNM1234567890'
for i in range(5):
    key = []
    for j in range(5):
        a = ''
        for k in range(5):
            a += dictionary[random.randint(0, len(dictionary) - 1)]
        key.append(a)
    print('-'.join(key))