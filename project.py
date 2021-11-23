import pandas as pd 
import plotly.express as px 

df = pd.read_csv("data.csv")
# find mean of the attempts of each student in each level

print(df.groupby(["student_id","level"])["attempt"].mean())
student_df = df.groupby(["student_id","level"],as_index=False)["attempt"].mean()
fig = px.scatter(student_df,x="student_id",y="level",color = "attempt")
fig.show()