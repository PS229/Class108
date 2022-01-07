import random
import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd
dicerolls = []
count = []
for x in range(0,1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    sum = dice1 + dice2
    dicerolls.append(sum)
    count.append(x)
fig = px.bar(x = dicerolls, y = count)
fig.show()