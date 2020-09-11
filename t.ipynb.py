# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
a = 1
b = 2
print(a + b)

# %%
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))
plt.show()

# %%
data = {"key": {"subkey": "value", "foo": "bar"}}
print(data)