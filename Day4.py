"""
正常的人耳能夠聽到最微弱的聲音叫作「聽覺閾」為 20 個微巴斯卡 (縮寫為 μPa) 
以聲壓 20μPa 定義為 0 分貝，表示 V0 為 20μPa，其餘聲壓為 V1(微巴斯卡)
例如將 V1 帶入 200μPa，V0 為 20μPa，可以得到 20GdB。
"""
import numpy as np

#1.正常的談話的聲壓為20000微巴斯卡，請問多少分貝?
v0 = 20*10**-6
v1 = 20000*10**-6#(μ=10^-6)
Gdb = 20*np.log10(np.divide(v1, v0))
print(' answer1 Gdb = ',Gdb)


#2.30分貝的聲壓會是50分貝的幾倍?
#[db = 20*log10(V1/V0)]→[db/20 = log10(V1/V0)]→[10^(db/20) = V1/V0]→[V1 = 10^(db/20)*v0] 
db_30 = 30
db_50 = 50
V_30 = 10**(db_30/20)*v0
V_50 = 10**(db_50/20)*v0
print('\n','answer2 gain = ',V_30/V_50)


"""[簡答題]"""
# 1.請問下列程式碼，運算結果分別為何？
 
a = np.array( [20,30,40,50] )
b = np.array( [1,2,3,4] ) 
c = 1
d = np.array( [1] )
e = np.array( [1,2] ) 
print('\n',a + a)
print(a + b)
print(a + c)
print(a + d)
# print(a + e)ValueError: operands could not be broadcast together with shapes (4,) (2,)


#2. 如何在不用迴圈的情況下計算 (A+B)*(-A/2) ？那用迴圈怎麼做？
A = np.ones(3)*1
B = np.ones(3)*2
print((A + B) * (-A / 2))

#3. 請問如何計算「1x6 的單位矩陣」和「6x1 的單位矩陣」的內積和外積？
A1 = np.ones((1,6))
B1 = np.ones((6,1))
print(A1 * B1)
print(A1 @ B1)