import time

t1 = "0          0      0   1      0    1    0      0          0         1            0        1        0       1    0            1     0     0               1   0         0      0     1  0   1   0   0      0       1    0    "
t2 = "         0       1  0         0      1         0       1       0     1    0     1    0        1         0         1       1         0  0   1      0   1         0    0     1      1     0    0     0     0           0     "
t3 = "             1          1       0        0         1               0                   1 0   0                   0   1   0   1       1  1      0 1   1           1 0    1     0     0      0   1      1   1   0         0  "
t4 = "0 1         1  0   1  1     0       0         0   1      0     0           1    0     0          1     0   0            0      0    0  1    1     0     0      1      0     0  1    1    1      1  1     0    1         0  "
t5 = " 0   0   0        0  0 0   1     1  0   0  0  1          1     0    1  0      1    0  1      0          0   1   0   0 1      1     0    0     1  0  0    0    0    0  0   0     0  1      0   0     0  1  1  1      1   1  "
t6 = "0  1  1     0   0       0    0   0        0 0 0     1 0    0  0    0     0  0    0     0   0  1    1 1    0   0      0    0  1 0    0    0   0   1 1  1 1   0     0      0    0    0    1   1     0    0   0    0  1       "

i = 0
while True:
    i += 1
    time.sleep(0.1)
    if i == 3:
        print(t1)
    elif i == 6:
        print(t2)
    elif i == 9:
        print(t3)
        i=0
    else:
        pass
          
