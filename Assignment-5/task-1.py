dict = {'Alice':85,'Dharmaya':90,'Anita':80,'Riya':89,'Hiren':80}

name = input("Enter the student's name: ").capitalize()

if name not in dict.keys():
    print('Student not found.')
else:
    print("{}'s marks: {}".format(name,dict[name]))