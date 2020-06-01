import os
import sys


'''
3个空瓶换一瓶
input: n个空瓶
outpu: 最终可换瓶数
'''
def demo1():
    while True:
        try:
            a = int(input())
            if a != 0:
                print(a//2)
        except:       
            break
######################################
'''
input: n以及n个随机数组成的数组
output: 去重排序后的数组
'''
def demo2():
    while True:
        try:
            n,m = int(input()),set()
            for i in range(n):
                m.add(int(input()))
            for i in sorted(m):
                print(i)
        except:
            break
########################################
'''
input: 十六进制
ouput: 十进制
'''
def hex2dec():
    while True:
        try:
            print(int(input(),16))
        except:
            break
#########################################            
'''
input: n
ouput: 数组a[n],隔二删一，输出最后一个下标
'''           
def shangshu():
    while True:
        try:
            n = int(input())
        except:
            exit()
        r = 0
        i = 2
        while i <= n:
            r = (r+3) %i
            i += 1
        print(r)

#########################################
'''
输入一个字符串，求出该字符串包含的字符集合
'''
def char():
    while True:
        try:
            res,a = "",input()
            for i in a:
                if i not in res:
                    res+=i
            print(res)
        except:
            break

##########################################
'''
sudoku
思路：深搜+剪枝
'''
def isok(mat,i,j,num):#判断填入数字 
    for row in range(0,9):#遍历列
        if mat[row][j] == num:
            return False
    for col in range(0,9):#遍历行
        if mat[i][col] == num:
            return False
    ii = i//3
    jj = j//3
    #遍历该位置所处的3*3矩阵，若该数字已出现过，则不合法
    for row in range(ii*3,ii*3+3): 
        for col in range(jj*3,jj*3+3):
            if mat[row][col] == num:
                return False
    return True

def dfs(mat,i,j):#深度优先遍历
    if i==9:#所有行已遍历完，则结束
        return mat
    if j==9:#所有列已遍历完，则进入到下一行
        return dfs(mat,i+1,0)
    flag = False#flag表示该行有需要填充的格子
    for col in range(j,9):#遍历该行的所有列，如果有值为0，则需要进行填充
        if mat[i][col]==0:
            flag = True
            isChange =False#ischange表示是否已进行填充
            for num in range(1,10):
                if isOk(mat,i,col,num):#找出1-9中能够合法填入的数字
                    isChange =True
                    mat[i][col] = num
                    tpp = dfs(mat,i,col+1)#将该位置填充后，该行的后续位置是否有解
                    if tpp == None:#如果后续位置无解，则将该位置重新置为0，未填充状态
                        isChange = False
                        mat[i][col] = 0
                        continue#尝试下一个数字
                    else:
                        return  tpp
            if isChange==False:#找不到合法数字进行填充
                return None
    if flag==False:#该行所有位置已填满，进入到下一行
        return dfs(mat,i+1,0)

def sudoku():
    while True:
        isCon = True
        mat = []
        for i in range(9):
            line = sys.stdin.readline().strip()
            if not line:
                isCon = False
                break
            line =[int(i) for i in line.split(' ')]
            mat.append(line)
        if isCon ==False:
            break
        mat = dfs(mat,0,0)
        for line in mat:
           print(' '.join(str(j) for j in line))

#####################################################
if __name__ == '__main__':
    char()
