from ast import keyword
from multiprocessing.sharedctypes import Value


dict = {
    "fname" : "Fidel",
    "lname" : "Munywoki",
    "Role" : "Engineer"
}

output = [dict[value] for value in dict]
print(output)