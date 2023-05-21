import pandas as pd
kid = pd.read_csv("mercer_ml\products(kid cloth)_1684669288097.csv")
women = pd.read_csv("mercer_ml\products(women cloth)_1684669305548.csv")
men = pd.read_csv("mercer_ml\products(men cloth)_1684669083782.csv")
# print(kid.columns)
df1 = pd.DataFrame(columns = ["name","link"])
name = []
link = []
for i in range(len(kid)):
    name.append(kid["title"][i])
    link.append(kid["url"][i])
print(len(kid))
for i in range(len(women)):
    name.append(women["title"][i])
    link.append(women["url"][i])
print(len(women))
for i in range(len(men)):
    name.append(men["title"][i])
    link.append(men["url"][i])
print(len(men))

df1["name"] = name
df1["link"] = link

df1.to_csv("amazon.csv")