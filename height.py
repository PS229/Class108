import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv("hw.csv")
fig = ff.create_distplot([df["Height"].tolist()], ["Height"], show_hist=False)
fig.show()