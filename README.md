# Cyber-Security-Project
Encryption and Decryption using RSA and Digital Signature

1. Import necessary libraries:
   - `rsa`: This library provides functions for generating RSA key pairs, encryption, decryption, signing, and verification.
   - `yaml`: This library is used for working with YAML files, which are used here to store the encrypted data.

2. Define key generation and cryptographic functions:
   - `generateKeys()`: This function generates a new RSA key pair (public and private keys) of size 1024 bits and saves them in PEM format to separate files.
   - `loadKeys()`: This function reads the previously generated public and private keys from the files and returns them.
   - `encrypt(plaintext, key)`: This function takes plaintext and a public key, encrypts the plaintext, and returns the ciphertext.
   - `decrypt(ciphertext, key)`: This function takes ciphertext and a private key, decrypts the ciphertext, and returns the plaintext.
   - `sign(plaintext, key)`: This function takes plaintext and a private key, creates a digital signature, and returns it.
   - `verify(plaintext, signature, key)`: This function takes plaintext, a digital signature, and a public key, and verifies if the signature is valid for the given plaintext.

3. User input and operation selection:
   - The user is prompted to select an operation: 'Encrypt' or 'Decrypt'.

4. Encryption operation:
   - If the user chooses 'Encrypt':
     - The plaintext is read from the 'plain.txt' file.
     - New RSA key pair is generated and loaded.
     - The plaintext is signed and encrypted using the public key.
     - The ciphertext and signature are converted to hexadecimal strings.
     - The data (ciphertext and signature) is stored in a dictionary.
     - The dictionary is dumped to a 'secret.txt' file using YAML.

5. Decryption operation:
   - If the user chooses 'Decrypt':
     - The 'secret.txt' file is read, and the data is loaded from the YAML file.
     - Public and private keys are loaded.
     - Ciphertext and signature are converted from hexadecimal strings to bytes.
     - The ciphertext is decrypted using the private key.
     - Verification is performed by checking if the decrypted plaintext matches the original plaintext and if the signature is valid.
     - If decryption and verification are successful, the plaintext is printed; otherwise, an error message is printed.

Example of how to run the code:

1. Create a file named `plain.txt` with some plaintext content that you want to encrypt and decrypt.

2. Run the script in your terminal or Python environment.

3. Choose either 'Encrypt' or 'Decrypt' operation.

4. If you choose 'Encrypt', the script will generate keys, encrypt the plaintext, create a signature, and save the encrypted data to 'secret.txt'.

5. If you choose 'Decrypt', the script will read 'secret.txt', decrypt the data, verify the signature, and print the decrypted plaintext if successful.

Please note that this code is meant for educational purposes and may not cover all security considerations.
