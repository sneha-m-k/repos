
tstr = input("enter a sentence: ")



freq = {} 

  

for i in tstr: 

    if i in freq: 

        freq[i] += 1

    else: 

        freq[i] = 1

  

print str(freq) 