
# https://leetcode.com/discuss/interview-question/1799446/Mercari-Inc-Software-Engineer-(New-Graduate-Position)-Hiring-Test-2022
def solution(arr,x):
    # [0,1,2,1,3]
    hm = []
    ansArr = list()
    for i in range (len(arr)):
        for j in range (len(arr)): 
            if j not in hm and (i == arr[j] or (arr[j] != 0 and x != 0 and arr[j] >= x and (arr[j] % x == i or arr[j] % x == 0))) or (i != 0 and i % x == arr[j]):
                hm.append(j)
                ansArr.append(i)
                break



    print(ansArr)
    for i in range(len(ansArr)):
        if i not in ansArr:
            print(i)
            return i
    print(len(ansArr))
    return len(ansArr)
solution([0,1,2,1,3],3) # 5
solution([1,1,1,1], 2) # 0
solution([3,4,5],1) # 3 
solution([777, 999, 333], 4) # 0
solution([222, 444, 666], 9) # 1
solution([3, 1, 4,5 ], 3) # 3
solution([0, 1, 2, 3, 5, 6, 7],9) # 4
