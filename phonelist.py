#import sqlite3
#conn = sqlite3.connect("phone.db")

import psycopg2
conn = psycopg2.connect(
    host="localhost",
    database="phone",
    user="postgres",
    password="Bl0mm0r!")


the_list = []
print("-----Hello and welcome to the phonelist! Available commands:-----")

commands = [
    'ADD: Add a name to the list',
    'LIST: Print the list of names',
    'DELETE: Delete a name from the list',
    'QUIT: End the program',
    'SAVE: Saves the data',
    'HELP: This message will come up again' ]
for x in commands:
    print(x)




def read_phonelist(C):
    cur = C.cursor()
    cur.execute("SELECT * FROM phonelist;")
    rows = cur.fetchall()
    cur.close()
    return rows
def add_phone(C, name, phone, address):
    cur = C.cursor()
    cur.execute(f"INSERT INTO phonelist VALUES ('{name}', '{phone}', '{address} ' ); ")
    cur.close()
def delete_phone(C, name):
    cur = C.cursor()
    cur.execute(f"DELETE FROM phonelist WHERE name = '{name}';")
    cur.close()
def save_phonelist(C):
    cur = C.cursor()
    try:
        cur.execute("COMMIT;")
    except:
        print("No changes!")
    cur.close()

while True: ## REPL - Read Execute Program Loop
    cmd = input("Command: ").strip().upper()
    if cmd == "LIST":
        print(read_phonelist(conn))
    elif cmd == "ADD":
        name = input("  Name: ").strip().title()
        phone = input("  Phone: ").strip()
        address = input(" Address:").strip().title()
        add_phone(conn, name, phone, address)
    elif cmd == "DELETE":
        name = input("  Name: ").strip().title()
        delete_phone(conn, name)
    elif cmd == "REMOVE":
        print("Unknown command: REMOVE")
    elif cmd == "HELP":
        print(commands)
    elif cmd == "SAVE":
        save_phonelist(conn)
        print('SAVED')
    elif cmd == "QUIT":
        save_phonelist(conn)
        exit()
       

# import sqlite3
# conn = sqlite3.connect("phone.db")


