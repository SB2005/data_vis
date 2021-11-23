import pandas as pd 
import statistics as st 
import plotly.graph_objects as go 

df = pd.read_csv("data.csv")
print(df)

print(df.groupby("level")["attempt"].mean())

student_df = df.loc[df["student_id"] == "TRL_987"]
print(student_df.groupby("level")["attempt"].mean())

df_list = df.values.tolist()
print(df_list[0:3])
l_4 = []
l_3 = []
l_2 = []
l_1 = []
for row in df_list:
    if(row[1] == "Level 4"):
        l_4.append(row[2])
    if(row[1] == "Level 3"):
        l_3.append(row[2])
    if(row[1] == "Level 2"):
        l_2.append(row[2])
    if(row[1] == "Level 1"):
        l_1.append(row[2])

m_4 = st.mean(l_4)
m_3 = st.mean(l_3)
m_2 = st.mean(l_2)
m_1 = st.mean(l_1)

print(m_4,m_3,m_2,m_1)

fig = go.Figure(go.Bar(x = df.groupby("level")["attempt"].mean(),y = ["Level 1","Level 2","Level 3","Level 4"],orientation = "h"))
fig.show()

fig1 = go.Figure(go.Bar(x = student_df.groupby("level")["attempt"].mean(),y = ["Level 1","Level 2","Level 3","Level 4"],orientation = "h"))
fig1.show()