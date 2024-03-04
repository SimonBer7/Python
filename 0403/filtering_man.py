import numpy as np

data = np.array([0.1743, 0.2732, 0.3521, 0.4924])
filter = np.array([True, False, True, False])

nova_data = data[filter]
bigger_data = data * 1000
minus_one_data = bigger_data - 1
join_data = minus_one_data + np.array([1, 1, 1, 1])
pripraveny_filtr = data < 0.25

print(data, "\n", nova_data, "\n", bigger_data, "\n", minus_one_data, "\n", join_data, "\n", pripraveny_filtr)
