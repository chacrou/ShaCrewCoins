from tkinter.messagebox import YES
import scratchattach as scratch3
import Fonctions as f

session = scratch3.Session("", username="Chacrou") #replace with your session_id and username
conn = session.connect_cloud("829566680") #replace with your project id
client = scratch3.CloudRequests(conn)

#Just to check the server status
@client.request
def avaible():
    return 'The server isn\'t down'


@client.request
def get_balance(argument1, argument2):
    if  argument2 == 'scc':
        users = f.read_json("utilisateur")
        user = argument1 in users
        if user == True:
            my_balance = f.read_json(argument1)
            my_balance = my_balance[0]
            my_balance = my_balance["balance"]
            return my_balance
        else:
            return 'You need to use to ShaCrewCoins'
@client.request

def set_balance(argument1, argument2):
    n = 0
    who = ''
    to = ''
    for chars in argument1:
        if n == 1:
            to = to + chars
        if n == 0:
            if chars != ';':
                who = who + chars
            else:
                n = 1
    if to == 'scc':    
        my_file = f.read_json(who)
        balance = my_file[0]
        balance = balance["balance"]
        save = my_file[1]
        somme = int(argument2)
        if balance < somme:
            return 'no'
        balance = balance + somme
        my_file = [{"balance":balance}, save]
        f.write_json(who, my_file, "w")
        return ('Good')

client.run()
