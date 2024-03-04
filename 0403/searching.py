import numpy as np

data = np.array([20,23,-100,-5,30,70,-18,99,81,16,45,90,-39,-82,75,0,16,91,48,0,70])


'''
Hledani zaporneho cisla
'''
negative_indices = np.where(data < 0) #ziskam indexy
negative_values = data[negative_indices]

'''
x > -10 & x < -1
'''
selected_num = np.where((data > -10) & (data < -1))
selected_val = data[selected_num]
print("Cisla v rozsahu:", selected_val)

'''
1 -50 nebo zaporny
'''
optional_num = np.where(((data >= 1) & (data <= 50)) | (data < 0))
optional_val = data[optional_num]
print("V rozsahu 1-50 nebo zaporny: ", optional_val)
