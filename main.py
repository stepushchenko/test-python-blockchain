import hashlib
import json

blockchain = []
blockchainProof = "0000"


def create_hash(data):
    data = json.dumps(data, sort_keys=True)  # json to string
    data = data.encode()  # string to binary
    return hashlib.sha256(data).hexdigest()  # get hashcode


def add_first_block():
    if len(blockchain) == 0:
        block = {
            "from": "",
            "to": "",
            "amount": "",
            "hashcode": "",
            "number": ""
        }
        count = 0
        while create_hash(block)[0:4] != blockchainProof:  # wait till the hash will not be accepted
            block['number'] = count
            count += 1
        blockchain.append(block)


def add_block(client_from,client_to,amount):
    if len(blockchain) != 0:
        block = {
            "from": client_from,
            "to": client_to,
            "amount": amount,
            "hashcode": create_hash(blockchain[-1]),
            "number": ""
        }
        count = 0
        while create_hash(block)[0:4] != blockchainProof:  # wait till the hash will not be accepted
            block['number'] = count
            count += 1
        blockchain.append(block)


def validate_blockchain():
    count = 0
    for block in blockchain:
        if block['hashcode'] != "":
            expectedHashcode = create_hash(blockchain[count-1])
            actualHashcode = block['hashcode']
            if expectedHashcode == actualHashcode:
                print('Validation success')
            else:
                print('Error')
        count += 1


# examples
add_first_block()
print(blockchain)
print()

add_block("Petr","Mria",100)
print(blockchain)
print()

add_block("Mria","Andry",20)
print(blockchain)
print()

add_block("Petr","Andry",15)
print(blockchain)
print()

validate_blockchain()