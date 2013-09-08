def editDistance(x, y):
    m = len(x)
    n = len(y)

    # print 'Distanza da "' + x +'" a "' + y + '":'

    cost = {}
    cost['copy'] = 0     #Costo per la copia
    cost['replace'] = 1  #Costo per la sostituzione
    cost['twiddle'] = 1  #Costo per lo scambio
    cost['delete'] = 3   #Costo per la cancellazione
    cost['insert'] = 1   #Costo per l'inserimento

    c = [range(n + 1)] * (m + 1)

    for i in range(m + 1):
        c[i] = range(i,i + n + 1)



    for i in range(1,m +1):
        for j in range(1,n +1):
            if x[i-1] == y[j-1]:
                c[i][j] = minimum(c[i-1][j] + cost['delete'], c[i][j-1] + cost['insert'], c[i-1][j-1] + cost['copy'])
          
            elif (i>=2 and j>=2 and x[i-1] == y[j-2] and x[i-2] == y[j-1]):
                c[i][j] = minimum((c[i-2][j-2] + cost['twiddle']),(c[i][j-1] + cost['delete']), (c[i-1][j] + cost['insert']))
          
            else:
                c[i][j] = minimum(c[i][j-1] + cost['insert'], c[i-1][j] + cost['delete'], c[i-1][j-1] + cost['replace'])


    # for i in range(m+1):
    #    print c[i]

    #  print 'Costo:  ',c[m][n]

    return c[m][n]
    

def minimum(x, y, z):
    m = x
    if y < m:
        m = y
    if z < m:
        m = z
    return m
