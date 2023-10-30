import rsa
import yaml



def generateKeys():
    (publicKey, privateKey) = rsa.newkeys(1024)
    with open('All_keys/publicKey.pem', 'wb') as temp:
        temp.write(publicKey.save_pkcs1('PEM'))
    with open('All_keys/privateKey.pem', 'wb') as temp:
        temp.write(privateKey.save_pkcs1('PEM'))


def loadKeys():
    with open('All_keys/publicKey.pem', 'rb') as temp:
        publicKey = rsa.PublicKey.load_pkcs1(temp.read())
    with open('All_keys/privateKey.pem', 'rb') as temp:
        privateKey = rsa.PrivateKey.load_pkcs1(temp.read())
    return privateKey, publicKey


def encrypt(plaintext, key):
    return rsa.encrypt(plaintext.encode(), key)


def decrypt(ciphertext, key):
    try:
        return rsa.decrypt(ciphertext, key).decode()
    except:
        return False


def sign(plaintext, key):
    return rsa.sign(plaintext.encode(), key, 'SHA-256')


def verify(plaintext, signature, key):
    try:
        return rsa.verify(plaintext.encode(), signature, key,) == 'SHA-256'
    except:
        return False



operation = input('Operation (Encrypt/Decrypt) : ')

if operation == 'Encrypt':
    with open('secret.txt', 'r') as file1:
        text = file1.read()

    generateKeys()
    privateKey, publicKey = loadKeys()
    signature = sign(text, privateKey)
    ciphertext = encrypt(text, publicKey)

    # Convert binary data to a format that can be represented as a string
    ciphertext_str = ciphertext.hex()  # Convert bytes to hexadecimal string
    signature_str = signature.hex()
    # print(ciphertext_str)

    # Create a dictionary to hold the data
    data_dict = {"ciphertext": ciphertext_str, "signature": signature_str}


    with open('e.yaml', 'w') as f:
        yaml.dump(data_dict, f)


elif operation == 'Decrypt':
    try:
        with open('e.yaml', 'r') as f:
            data_dict = yaml.safe_load(f)

        privateKey, publicKey = loadKeys()

        # Convert hexadecimal strings back to bytes
        ciphertext = bytes.fromhex(data_dict["ciphertext"])
        signature = bytes.fromhex(data_dict["signature"])

        plaintext = decrypt(ciphertext, privateKey)
        verification = verify(plaintext, signature, publicKey)
        if plaintext and verification is True:
            print('Plaintext:', plaintext)
        else:
            print('Decryption failed.')

    except FileNotFoundError:
        print('No encrypted data found.')
