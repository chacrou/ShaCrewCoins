from tkinter.messagebox import YES
import scratchattach as scratch3
import Fonctions as f

session = scratch3.Session(".eJxVj0trwzAQhP-Lzq1rybIl59bkUEqhAVNoexKrh235Ibm2TCCl_70S5JLTLt_sDLO_aN_M6mA26IBOPajV7-gBCdhDL5IkrI5KzUlV8CKPUjBbUN6PNjkufh2NvjdIUKNxyZWYccEqCNa77CZsWWOW6QaPt-OY6-MSTUQqXBNdQl7XlCnNpWaKYllJDoYW5HAtxfBSkJ_j-ePU5Mp2b8P5Sy-i-XyNMZPvrHu0S0rCJMOYZiSOmqaSE7huhy41b9cI9BCBF8HO5updws-zWWO1p3dzEd_xufvXetj6eFTyClRJgQGj0NaYt5pw0IrlhWmlxpppzGSVo79_3q5xlw:1pSYz9:LaYT1p_uAAaNgEydXPeX4MWjRCY", username="Chacrou") #replace with your session_id and username
conn = session.connect_cloud("829566680") #replace with your project id
client = scratch3.CloudRequests(conn)

#Just to check the server status
@client.request
def avaible():
    return 'The server isn\'t down'


@client.request
def get_balance(argument1, argument2):
    if  argument2 == 'scc':
        my_balance = f.read_json(argument1)
        my_balance = my_balance[0]
        my_balance = my_balance["balance"]
        return my_balance
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
