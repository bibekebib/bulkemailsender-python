f= open('first1.txt','x')
y = ['075']#'074','073','072','071']
b = ['bct']# 'bce', 'bme','bge','bel','bei', 'bame']
for m in y:
    for x in b:
        for i in range(48):
            if i in range (0,9):
                f.write('pas'+m+x+'00'+str(i+1)+'@wrc.edu.np\n' )
            if i in range(9,48):
                f.write('pas'+m+x+'0'+str(i+1)+'@wrc.edu.np\n' )    
    
    