import random
import string

logo = '''
████████╗ ██████╗ ██╗  ██╗██╗ ██████╗
╚══██╔══╝██╔═══██╗╚██╗██╔╝██║██╔════╝
   ██║   ██║   ██║ ╚███╔╝ ██║██║     
   ██║   ██║   ██║ ██╔██╗ ██║██║     
   ██║   ╚██████╔╝██╔╝ ██╗██║╚██████╗
   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝ ╚═════╝
                                     
'''

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def create_password_list(password_length, num_passwords):
    passwords = [generate_password(password_length) for _ in range(num_passwords)]
    return passwords

def save_passwords_to_file(passwords):
    file_name = "passwords.txt"
    with open(file_name, "w") as file:
        for password in passwords:
            file.write(password + "\n")
    print("Passwords saved to", file_name)

# Hear logo color green
logo = "\033[92m" + logo + "\033[0m"

print(logo)

information = {
    "Admin": "SAGOR",
    "WhatsApp": "01831018711",
    "Github": "TOXIC-SAGOR",
    "Version": "0.1"
}

# white border 
for key, value in information.items():
    print("\033[97m╔═════════════════════════════════════════════════╗\033[0m")
    print("\033[97m║\033[94m{}\033[97m:\033[91m{:<40}\033[97m║\033[0m".format(key, value))
    print("\033[97m╚═════════════════════════════════════════════════╝\033[0m")

password_length = int(input("PASSWORD LENGTH: "))
num_passwords = int(input("HOW MANY PASSWORD DO YOU WANT: "))
passwords = create_password_list(password_length, num_passwords)

print("\nGenerated Passwords:")
for password in passwords:
    print(password)

save_passwords_to_file(passwords)
