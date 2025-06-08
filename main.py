from tkinter.messagebox import YES
import scratchattach as scratch3
import Fonctions as f

session = scratch3.Session("session_id", username="username") #replace with your session_id and username
conn = session.connect_cloud("805013764") #replace with your project id
client = scratch3.CloudRequests(conn)
print('ShaCrewCoins')

#Just to check the server status
@client.request
def avaible():
    return 'The server isn\'t down'

@client.request
def name(argument1):
    verif_user = f.read_json("utilisateur")
    verif_user = argument1 in verif_user
    if verif_user == False:
        print('firstco')
        connexions = f.read_json("utilisateur")
        connexions.append(argument1)
        f.write_json("utilisateur", connexions, "w")
        user_content = [{"balance":100},[]]
        f.write_json(argument1, user_content, "x")
    return 'Ok' #send back to the Scratch project

@client.request
def find(argument1):
    verif_user = f.read_json("utilisateur")
    dest = argument1 in verif_user
    if dest == True:
        return 'yes'
    if dest == False:
        return 'User_not_found'
    
@client.request
def give(argument1, argument2):
    somme = int(argument1)
    my_file = f.read_json(argument2)
    save = my_file[1]
    balance = my_file[0]
    balance = balance["balance"]
    balance = balance + somme
    my_file = [{"balance":balance}, save]
    f.write_json(argument2, my_file, "w")
    return 'Good'

@client.request
def gave(argument1, argument2):
    my_file = f.read_json(argument2)
    balance = my_file[0]
    balance = balance["balance"]
    save = my_file[1]
    somme = int(argument1)
    if balance < somme:
        return 'no'
    balance = balance - somme
    my_file = [{"balance":balance}, save]
    f.write_json(argument2, my_file, "w")
    return ('Yes')

@client.request
def transaction(argument1, argument2):
    who = 0
    from_ = ''
    to_ = ''
    for chars in argument1:
        if who == 1:
            to_ = to_ + chars
        if who == 0:
            if chars != ';':
                from_ = from_ + chars
            else:
                who = 1
    amount = int(argument2)
    f.transaction(from_, amount, to_)
    return 'yes'

@client.request
def balance(argument1):
    my_balance = f.read_json(argument1)
    my_balance = my_balance[0]
    my_balance = my_balance["balance"]
    return my_balance
@client.request
def trans_check(argument1):
    trans = f.read_json("transactions")
    trans = trans[argument1]
    return trans
@client.event
def on_ready():
    print("Request handler is running")
client.run()
