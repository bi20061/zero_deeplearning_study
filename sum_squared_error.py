import numpy as np;

def sum_squared_error(y,t):
    return 0.5 * np.sum((y-t)**2);

#「2」を正解とする
t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0];

#例1：「2」の確率が最も高い場合（0.6）
y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
print(sum_squared_error(np.array(y), np.array(t)));

#例2：「7」の確率が最も高い場合（0.6）
y = [0.1, 0.05, 0.2, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]
print(sum_squared_error(np.array(y), np.array(t)));

