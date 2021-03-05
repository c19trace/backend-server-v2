from flask import Flask, request, jsonify, send_file
from flask_cors import CORS

from datetime import datetime
import sqlite3

from base64 import b64decode, b64encode
from nacl.secret import SecretBox
from nacl.public import PrivateKey

API_KEY = "test123" 
DATABASE = 'exposed_random_ids.db'
CREATE_QUERY = """create table if not exists
                randomids (id integer primary key autoincrement,
                gNum varchar(32) not null, randomid varchar(32) not null unique,
                date date, status integer);
                """


app = Flask(__name__)
CORS(app)

'''Adds to the database.
'''
def add_token(gNum, random_ids):
    time = datetime.now().strftime("%Y-%m-%d") 
    status = 0
    # Check how random_ids is saved...
    print(gNum)
    print(random_ids)
    data = (gNum, random_ids, time, status)
    sql = "insert into randomids (gNum, randomid, date, status) values (?, ?, ?, ?);"

    with sqlite3.connect(DATABASE) as con:
        try:
            con.execute(sql, data)
        except sqlite3.IntegrityError:
            pass


'''Creates the database, if it does not exist.
'''
with sqlite3.connect(DATABASE) as con:
    con.execute(CREATE_QUERY)

#add_random_ids([(124,), (125,)])

'''Updates the status of a token.
'''
@app.route('/update-status', methods=['POST'])
def update_status():
    if request.method == 'POST':
        msg = request.json
        data = (msg['status'], msg['id'])
        sql = """update randomids set status = ? where id = ?;"""

        with sqlite3.connect(DATABASE) as con:
            cur = con.cursor()
            cur.execute(sql, data)

    return "ok"
    
'''Returns all of tokens stored in the database.
'''
@app.route('/get-tokens')
def tokens():
    sql = 'select * from randomids'
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    all_tokens = cur.execute(sql).fetchall()
    return jsonify(all_tokens)

'''Returns the exposed tokens from the database
'''
@app.route('/get-exposure-list')
def exposures():
    sql = "select randomid from randomids where status = 1;"
    with sqlite3.connect(DATABASE) as con:
        cur = con.cursor()
        cur.execute(sql)
        results = '\n'.join([r[0] for r in cur.fetchall()])
        return results
        

# Terminal... unused.
@app.route('/submit-exposure-list', methods=['GET'])
def submit_list():
    data = request.form

    if data.get("key") != API_KEY:
        return "bad key"

    random_ids = data.get("randomids").split(",")
    random_ids = [(i, ) for i in random_ids]

    with sqlite3.connect(DATABASE) as con:
        add_token(random_ids)

    return "ok"


#===============

# Decryption... unused
def decryptMsg(secret_key, encrypted):
    secret_key = b64decode(secret_key)
    encrypted = encrypted.split(':')
    nonce = b64decode(encrypted[0])
    encrypted = b64decode(encrypted[1])
    box = SecretBox(secret_key)
    decrypted = box.decrypt(encrypted, nonce).decode('utf-8')

    print("Decrypted token: ", decrypted)


'''Submits a token to the database.
'''
@app.route('/submit-token', methods=['POST'])
def test():
    if request.method == 'POST':
        msg = request.json
        token = str(msg['token'])
        id = str(msg['id'])
        print("Request received:", id, token)

        with sqlite3.connect(DATABASE) as con:
            add_token(id, token)

        #decryptMsg(secret_key, msg)

    return "ok"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
