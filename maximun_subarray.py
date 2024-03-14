

#Listas de prueba
prove_list = [-2,1,-3,4,-1,2,1,-5,4]
list1 = [5,-4,3,-2,1,4]

#Versión de prueba
"""
sum_max = 0

for i in range(len(prove_list)):
    for j in range(i, len(prove_list)):
        
        current_sum = sum(prove_list[i:j+1])
        print(prove_list[i:j+1])
        #print(current_sum)
    
        if current_sum > sum_max:
            sum_max = current_sum
            best_list = prove_list[i:j+1]
            
print(sum_max)
print(best_list)
"""

# Como función
def maximun_sum(list):
    sum_max = 0

    for i in range(len(list)):
        for j in range(i, len(list)):
            
            current_sum = sum(list[i:j+1])
            #print(list[i:j+1])
            #print(current_sum)
        
            if current_sum > sum_max:
                sum_max = current_sum
                best_list = list[i:j+1]
    
    print(best_list)
    print(sum_max)

maximun_sum(list1)
