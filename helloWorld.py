"""
Create a list of tuples from the folowing datastructure {‘a’: ‘Alpha’, ‘b’ : ‘Beta’, ‘g’: ‘Gamma’}
"""
############################# Assignment 1
Directors = {"Benny", "Hans", "Tine", "Mille", "Torben", "Troels", "Søren"}
Management = {"Tine", "Trunte", "Rane"}
Employees = {"Niels", "Anna", "Tine", "Ole", "Trunte", "Bent", "Rane", "Allan", "Stine", "Claus", "James", "Lars"}

print(Directors - Employees)
# Answer : {'Torben', 'Mille', 'Hans', 'Troels', 'Benny', 'Søren'}
print(Directors & Employees)
# Answer : {'Tine'}
print(len(Directors & Management))
# Answer : 1
print(Management <= Employees)
# Answer : True
print(Directors <= Management)
# Answer : False
print(Directors & Employees & Management)
# Answer : {'Tine'}
print(Employees.difference(Directors, Management))
print(Employees - Directors - Management)
# Answer : {'Stine', 'Anna', 'Ole', 'Allan', 'James', 'Lars', 'Niels', 'Claus', 'Bent'}
############################# Assignment 2
minTuble = (('a', 'Alpha'), ('b','Beta'), ('g', 'Gamma'))
print(minTuble)
############################# Assignment 3
set1 = {'a', 'e', 'i', 'o', 'u', 'y'}
set2 = {'a', 'e', 'i', 'o', 'u', 'y', 'æ', 'ø', 'å'}
print(sorted(set1.union(set2)))
print(sorted(set1 | set2))

print(set1 ^ set2)
print(set1.symmetric_difference(set2))

print(set1-set2)
print(set1.difference(set2))
print(set2 - set1)
print(set2.difference(set1))

print(set1 & set2)
print(set1.isdisjoint(set2))
############################# Assignment 4
monthDictionary = {
    'JAN': 1,
    'FEB': 2,
    'MAR': 3,
    'APR': 4,
    'MAY': 5,
    'JUN': 6,
    'JUL': 7,
    'AUG': 8,
    'SEP': 9,
    'OCT': 10,
    'NOV': 11,
    'DEC': 12
}
def reformDate(date):

    day, month, year = date.split('-')

    monthNumber = monthDictionary[month]
    finalYear = "19" + year
    return (int(finalYear),monthNumber, int(day))

date = "8-MAR-20"
print(reformDate(date))
############################# Assignment 5
invited = {'John', 'Alice', 'Bob', 'Eve', 'Chris', 'David', 'Hannah', 'Irene', 'James', 'Lucy', 'Michael', 'Nora'}
responded = {'Zara', 'Alice', 'Eve', 'Michael', 'Nora', 'Tim', 'Ryan', 'Wendy', 'Vincent', 'Ulysses', 'Sam', 'Ron'}

invitedButNotRSVP = invited - responded
print("These are the people who were invited but haven't RSVP: ", invitedButNotRSVP)
notInvitedButRSVP = responded - invited
print("These are the pople who RSVP but weren't invited: ", notInvitedButRSVP)
invitedAndRSVP = invited & responded
print("These are the people who RSVP and were invited: ", invitedAndRSVP)
############################# Assignment 6

studentsDictionary = {
    'Mathias': 100,
    'Marcus': 50,
    'Jannick': 10,
    'Ham Der': 60,
    'Mai': 80,
    'Julie': 75,
    'Hende Der': 40
}

def upgradeGrades(studentsDictionary):
    studentsDictionary['Marcus']= 90
    studentsDictionary['Julie']=100

    for student, grade in studentsDictionary.items():
        if grade > 85:
            print(student, grade)


upgradeGrades(studentsDictionary)


