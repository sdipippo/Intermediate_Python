'''
Fun with Passwords
'''

passwords = {}

### Plain Text :-( #################

def store_password(username, password):
    passwords[username] = password

def check_password(username, password):
    return passwords[username] == password

###  Encrypted Passwords #################
###  Encryption is reversible, hashing is not #####

def store_password(username, password):
    passwords[username] = password.encode('rot-13')

def check_password(username, password):
    return passwords[username].decode('rot-13') == password

###  Hashed Passwords #################
###  Hashing is a one-way transformation and more secure
###  Breakable the more cores you have. You can figure out
###  what value hashes to the password hash using this method
###  The "hash" keyword in Python was not designed for security

def store_password(username, password):
    passwords[username] = hash(password)

def check_password(username, password):
    return passwords[username] == hash(password)

###  Cryptographically secure hash! #################
###  MD5 still has security weaknesses and you can literally
### Google the hash to get the password

import md5

def store_password(username, password):
    passwords[username] = md5.new(password).hexdigest()

def check_password(username, password):
    return passwords[username] == md5.new(password).hexdigest()

###  MODERN Cryptographically secure hash! #################

import hashlib

def store_password(username, password):
    passwords[username] = hashlib.sha512(password).hexdigest()
                                         
def check_password(username, password):
    return passwords[username] == hashlib.sha512(password).hexdigest()

### HACKER SECTION #############
### Rainbow Table Attack #######

rainbow = {} # hashode as key: known password as value

with open('data/common_passwords.txt') as f:
    for line in f:
        password = line.split(',')[0]
        hashcode = hashlib.sha512(password).hexdigest()
        rainbow[hashcode] = password

def attack(passwords):
    for username, hashcode in passwords.items():
        if hashcode in rainbow:
            print 'Gotcha! {}: {}'.format(username, rainbow[hashcode])


###  MODERN Cryptographically secure hash! #################
### Add some SALT ###########################
### This renders rainbow tables useless since you are adding
### The user's password to the salt value
### But with today's hardware, GPUs can literally create
### all possible hashes less than x characters to beat this
            
import hashlib, random, string

alphabet = string.ascii_letters + string.digits + string.punctuation
def good_password(n=20):
    return ''.join(random.choice(alphabet) for i in range(n))

salt = good_password()
# should be per-user and stored with the user's hashcode

def store_password(username, password):
    passwords[username] = hashlib.sha512(password + salt).hexdigest()
                                         
def check_password(username, password):
    return passwords[username] == hashlib.sha512(password).hexdigest()





###  Slow things down #################
### This technique makes it take more time / tries to hack
### Making it more expensive for the attacker to do it

            
import hashlib, random, string

alphabet = string.ascii_letters + string.digits + string.punctuation
def good_password(n=20):
    return ''.join(random.choice(alphabet) for i in range(n))

repeats = 100000
salt = good_password()
# should be per-user and stored with the user's hashcode

def slowhash(password):
    hashcode = hashlib.sha512(password + salt).hexdigest()
    for i in range(repeats):
        hashcode = hashlib.sha512(hashcode).hexdigest()
    return hashcode

#Correct: use hashlib.pbkdf2_hmac as a best practice

def store_password(username, password):
    passwords[username] = slowhash(password)
                                         
def check_password(username, password):
    return passwords[username] == slowhash(password)




######### TEST ########################
if __name__ == '__main__':
    store_password('admin', 'cisco123')
    print check_password('admin', 'cisco123')
    print check_password('admin', 'cisco')

    crummy_passwords = '''
    password superman cisco michael cristina admin
    root god dog asdf qwerty mustang 1234 bobby
    '''.split()
    for i, password in enumerate(crummy_passwords):
        username = 'User{:}'.format(i)
        store_password(username, password)
    print passwords

    attack(passwords)

    
