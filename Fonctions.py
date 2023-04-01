import json
def write_json(name, content, write_type):
    # name = file name, content = content to write, write_type = "a" or "x" or "w"
    with open(name + ".json", write_type) as writing_file:
        json.dump(content, writing_file)

def read_json(name):
    # name = file name
    with open(name + ".json") as reading_file:
         my_file = json.load(reading_file)
    return my_file


def transaction(from_, amount_, to_):
    trans = read_json("transactions")
    sender = read_json(from_)
    save = sender[0]
    sender = sender[1]
    receiver = read_json(to_)
    save2 = receiver[0]
    receiver = receiver[1]
    id_ = trans[-1]
    id_ = id_["id"]
    id_ = id_ + 1
    my_trans = {"id": id_, "from": from_, "to": to_, "amount": amount_}
    sender.append(my_trans)
    history1 = [save, sender]
    receiver.append(my_trans)
    history2 = [save2, receiver]
    trans.append(my_trans)
    write_json("transactions", trans, "w")
    write_json(from_, history1, "w")    
    write_json(to_, history2, "w")
    return id_
