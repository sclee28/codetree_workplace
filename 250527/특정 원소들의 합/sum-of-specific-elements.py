arr_2nd = [ 
    list(map(int, input().split()))
    for i in range(4)
]

ans = []

for i in range(4):
    for j in range(i):
        ans.append(arr_2nd[i][j])

    
    

print(sum(ans))