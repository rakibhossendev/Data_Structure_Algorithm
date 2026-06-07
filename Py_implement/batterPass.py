password = "unsophisticated"

def betterPassword(password):
    list_password = list(password)
    upper_password = list_password[0].upper()
    list_password.append(0)
    list_password[0] = upper_password

    

    n = len(list_password)
    i = 0
    while i < n:

        if list_password[i] == "s":
            list_password[i] = "$"
        
        if list_password[i] == "i":
            list_password[i] = "!"

        if list_password[i] == "o":
            list_password[i] = '()'

        i += 1
    list_password[-1] = '.'

    current_password = "".join(list_password)
    print(current_password)

betterPassword(password)