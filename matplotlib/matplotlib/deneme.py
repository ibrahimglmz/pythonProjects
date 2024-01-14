import numpy as np
import matplotlib.pyplot as plt

age_list = [20, 30, 40, 50, 60, 70, 80, 90]
weight_list = [70, 60, 80, 90, 100, 120, 130, 140]

age_list_numpay = np.array(age_list)
weight_list_numpay = np.array(weight_list)


plt.title('Weight by Age')
plt.xlabel('Age')
plt.ylabel('Weight')
plt.grid(True)

plt.show()
