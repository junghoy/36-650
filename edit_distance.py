
def edit_distance(s1, s2):
    #Make case insensitive by converting all strings into lower-case
    s1 = s1.lower()
    s2 = s2.lower()

    #Construct table that displays DAG
    dag = {}

    #Horizontal movement represents insertion
    #Vertical movement represents deletion
    #Diagnoal movement represents copy & substitution
    for i in range(len(s1)+1): 
        dag[i,0]=i
    for j in range(len(s2)+1): 
        dag[0,j]=j    
    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            cost = None
            if s1[i-1] == s2[j-1]:
                cost = 0
            else: 
                cost = 1
            dag[i,j] = min(dag[i, j-1]+1, dag[i-1, j]+1, cost+dag[i-1, j-1])

    return dag[i,j]


