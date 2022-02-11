import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")
fig = px.pie(df, names="Country", values="InternetUsers")

fig.show()