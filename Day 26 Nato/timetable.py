import pandas

time_table = {
    "Monday": {
        "MFC": 2,
        "Python": 3,
        "CIR": 3
    },
    "Tuesday": {
        "AI": 3,
        "AVP": 2,
        "DSA": 3
    },
    "Wednesday": {
        "Python": 1,
        "ICN": 4,
        "OS": 3
    },
    "Thursday": {
        "ICN": 1,
        "BIO": 1,
        "MFC": 1,
        "OS": 2,
        "Gita": 1,
        "AI": 1
    },
    "Friday": {
        "DSA": 2,
        "BIO": 1,
        "AI": 1,
        "Gita": 1,
        "MFC": 3
    }
}
# print(time_table)
df = pandas.DataFrame(time_table)

# Monday = 10
# Tuesday = 11
# Wednesday = 10
# Thursday = 11
# Friday = 10

df = df * 10
df["Sum of Classes"] = df.sum(axis=1)
print(df)