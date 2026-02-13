import keyring
import getpass

SERVICE_NAME = "epf"

"""
Keyring is a solution that's been proposed by AI.
Another solution would have been to store the credentials into path env
or create a .env file but we prefered that the credentials are never 
visible anywhere in the code.

Keyring uses the Windows Credential Manager to store the credentials.
The encrypting key is specific for each user and is stored in the registry.
In one hand anyone except the user can access the credentials.
In the other hand every software running under this user can access the credentials.
The most important protection here were to protect against stealing the machine.
If the machine is stolen, the credentials are not accessible while the user is not 
logged in.
"""

# Set credentials in the keyring only if the script is run directly not by importing
if __name__ == "__main__":
    email = input("Veuillez saisir votre email : ")
    keyring.set_password(SERVICE_NAME, "email", email)
    password = getpass.getpass("Veuillez saisir votre mot de passe : ")
    keyring.set_password(SERVICE_NAME, "password", password)
    print("Credentials enregistrés.")