student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

file = pandas.read_csv("nato_phonetic_alphabet.csv")
dict1 = {row.letter: row.code for (index, row) in file.iterrows()}
while True:
    user_input = input("Enter Name:- ").upper()
    try:
        code_name = [dict1[letter] for letter in user_input]
    except KeyError:
        print("Sorry, Only Letter in alphabet Please! ")
    else:
        break


print(code_name)
