import pandas as pd
import numpy as np
import matplotlib as plt

dates = pd.date_range('2000-01-01',periods=1000)

ts =pd.Series(np.random.randn(1000),index=dates)

ts = ts.cumsum()
ts.plot()
