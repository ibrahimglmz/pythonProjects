import  pandas as pd
import  numpy as np

my_dict1 = {"Name": ["ibrahim", "hasan", "eray","serhat"],
            "sports": ["basketball", "football", "tennis", "running"],
            "colories": [100, 200, 300, 400]
            }
my_frame = pd.DataFrame(my_dict1)

my_dict2 = {"Name": ["abraham", "house", "baylan","serkan"],
            "sports": ["basketball", "football", "tennis", "running"],
            "colories": [200, 300, 600, 430]
            }
my_frame2 = pd.DataFrame(my_dict2)
toplam = pd.concat([my_frame, my_frame2])
print(toplam)
