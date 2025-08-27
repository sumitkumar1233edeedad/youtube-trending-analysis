import numpy as np
import pandas as pd
import matplotlib.pyplot as mtl

x = np.array((1, 2, 3, 4, 8))
y = np.array((10, 20, 30, 20, 50))

df = pd.DataFrame({
    'name':x,
    'age':y,
})
print(df)
x = df['name']
y = df['age']

mtl.bar(x, y, color = 'gray',label='x,y')
mtl.plot(x, y, color= 'black', linestyle='--', linewidth=2, marker='o')
mtl.xlabel('len')
mtl.ylabel('wight')
mtl.title('tool work checking')
mtl.show()