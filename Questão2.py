rows = input("Quantas linhas você quer? ")
rows = int(rows)

for row in range(rows,0,-1):
    for colunas in range(1,row+1):
        print(colunas,end="")
    print()