contacts = {

    "Fidel" : 667777,
    "Tech" : 67776,
    "Tech2" : 67776,
    "Success" : 5556

}


contacts['Tish'] = 67779
print(contacts)

#reverse look up

def caller_id(caller_number):
    for name, num in contacts.items():
        print(name, num)
        if num == caller_number:
            return name + " found matching " + str(num) 
        

    


print(caller_id(67776))
