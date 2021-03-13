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
    data = (gNum, random_ids, time, status)
    sql = "insert into randomids (gNum, randomid, date, status) values (?, ?, ?, ?);"

    with sqlite3.connect(DATABASE) as con:
        try:
            con.execute(sql, data)
        except sqlite3.IntegrityError:
            pass

def add_token2(gNum, random_ids, date, status):
    # Check how random_ids is saved...
    data = (gNum, random_ids, date, status)
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


def add_test_tokens():
    add_token2("G00123321", "428a2f98d728ae22", "2020-10-30", "0")
    add_token2("G00561234", "7137449123ef65cd", "2021-02-27", "0")
    add_token2("G00654321", "b5c0fbcfec4d3b2f", "2021-01-08", "0")
    add_token2("G00615243", "e9b5dba58189dbbc", "2021-01-24", "0")
    add_token2("G00123456", "3956c25bf348b538", "2020-10-15", "0")
    add_token2("G00654321", "59f111f1b605d019", "2020-12-27", "0")
    add_token2("G00526341", "923f82a4af194f9b", "2020-12-20", "0")
    add_token2("G00654456", "ab1c5ed5da6d8118", "2020-12-16", "0")
    add_token2("G00526341", "d807aa98a3030242", "2021-02-22", "0")
    add_token2("G00654456", "12835b0145706fbe", "2020-11-15", "0")
    add_token2("G00615243", "243185be4ee4b28c", "2021-03-12", "0")
    add_token2("G00654456", "550c7dc3d5ffb4e2", "2020-11-15", "0")
    add_token2("G00123456", "72be5d74f27b896f", "2020-11-18", "0")
    add_token2("G00251436", "80deb1fe3b1696b1", "2021-01-16", "0")
    add_token2("G00561234", "9bdc06a725c71235", "2021-03-12", "0")
    add_token2("G00123321", "c19bf174cf692694", "2020-10-27", "0")
    add_token2("G00321456", "e49b69c19ef14ad2", "2020-11-07", "0")
    add_token2("G00321456", "efbe4786384f25e3", "2021-01-03", "0")
    add_token2("G00654456", "fc19dc68b8cd5b5", "2020-12-06", "0")
    add_token2("G00251436", "240ca1cc77ac9c65", "2020-11-27", "0")
    add_token2("G00654321", "2de92c6f592b0275", "2021-01-20", "0")
    add_token2("G00654456", "4a7484aa6ea6e483", "2020-11-21", "0")
    add_token2("G00654456", "5cb0a9dcbd41fbd4", "2021-01-02", "0")
    add_token2("G00321456", "76f988da831153b5", "2020-12-28", "0")
    add_token2("G00615243", "983e5152ee66dfab", "2020-11-29", "0")
    add_token2("G00123321", "a831c66d2db43210", "2020-10-18", "0")
    add_token2("G00523431", "b00327c898fb213f", "2020-11-21", "0")
    add_token2("G00526341", "bf597fc7beef0ee4", "2020-10-14", "0")
    add_token2("G00654456", "c6e00bf33da88fc2", "2021-01-16", "0")
    add_token2("G00615243", "d5a79147930aa725", "2020-12-25", "0")
    add_token2("G00654456", "6ca6351e003826f", "2021-02-20", "0")
    add_token2("G00654321", "142929670a0e6e70", "2021-02-03", "0")
    add_token2("G00526341", "27b70a8546d22ffc", "2021-02-01", "0")
    add_token2("G00162534", "2e1b21385c26c926", "2021-01-23", "0")
    add_token2("G00561234", "4d2c6dfc5ac42aed", "2020-12-05", "0")
    add_token2("G00123321", "53380d139d95b3df", "2020-10-31", "0")
    add_token2("G00526341", "650a73548baf63de", "2020-11-11", "0")
    add_token2("G00123456", "766a0abb3c77b2a8", "2021-01-06", "0")
    add_token2("G00251436", "81c2c92e47edaee6", "2020-12-27", "0")
    add_token2("G00615243", "92722c851482353b", "2021-02-05", "0")
    add_token2("G00162534", "a2bfe8a14cf10364", "2021-01-24", "0")
    add_token2("G00654456", "a81a664bbc423001", "2021-03-04", "0")
    add_token2("G00526341", "c24b8b70d0f89791", "2021-01-02", "0")
    add_token2("G00615243", "c76c51a30654be30", "2021-01-28", "0")
    add_token2("G00523431", "d192e819d6ef5218", "2020-10-12", "0")
    add_token2("G00321456", "d69906245565a910", "2020-10-10", "0")
    add_token2("G00523431", "f40e35855771202a", "2021-02-14", "0")
    add_token2("G00251436", "106aa07032bbd1b8", "2020-12-11", "0")
    add_token2("G00123456", "19a4c116b8d2d0c8", "2020-12-28", "0")
    add_token2("G00000000", "1e376c085141ab53", "2021-02-17", "0")
    add_token2("G00523431", "2748774cdf8eeb99", "2020-12-03", "0")
    add_token2("G00251436", "34b0bcb5e19b48a8", "2021-03-09", "0")
    add_token2("G00615243", "391c0cb3c5c95a63", "2020-12-05", "0")
    add_token2("G00162534", "4ed8aa4ae3418acb", "2021-02-10", "0")
    add_token2("G00456321", "5b9cca4f7763e373", "2020-11-13", "0")
    add_token2("G00654456", "682e6ff3d6b2b8a3", "2021-02-11", "0")
    add_token2("G00321456", "748f82ee5defb2fc", "2020-11-01", "0")
    add_token2("G00615243", "78a5636f43172f60", "2020-10-17", "0")
    add_token2("G00123321", "84c87814a1f0ab72", "2021-02-15", "0")
    add_token2("G00000000", "8cc702081a6439ec", "2021-01-25", "0")
    add_token2("G00654321", "90befffa23631e28", "2020-12-28", "0")
    add_token2("G00526341", "a4506cebde82bde9", "2020-12-30", "0")
    add_token2("G00251436", "bef9a3f7b2c67915", "2020-11-15", "0")
    add_token2("G00123456", "c67178f2e372532b", "2020-10-12", "0")
    add_token2("G00615243", "ca273eceea26619c", "2021-02-26", "0")
    add_token2("G00526341", "d186b8c721c0c207", "2020-11-15", "0")
    add_token2("G00456321", "eada7dd6cde0eb1e", "2020-10-27", "0")
    add_token2("G00000000", "f57d4f7fee6ed178", "2020-10-15", "0")
    add_token2("G00615243", "6f067aa72176fba", "2021-03-12", "0")
    add_token2("G00321456", "a637dc5a2c898a6", "2020-10-30", "0")
    add_token2("G00000000", "113f9804bef90dae", "2020-12-04", "0")
    add_token2("G00523431", "1b710b35131c471b", "2020-12-27", "0")
    add_token2("G00523431", "28db77f523047d84", "2020-12-22", "0")
    add_token2("G00526341", "32caab7b40c72493", "2021-01-05", "0")
    add_token2("G00456321", "3c9ebe0a15c9bebc", "2020-10-11", "0")
    add_token2("G00251436", "431d67c49c100d4c", "2020-12-29", "0")
    add_token2("G00000000", "4cc5d4becb3e42b6", "2021-02-03", "0")
    add_token2("G00654456", "597f299cfc657e2a", "2021-02-05", "0")
    add_token2("G00526341", "5fcb6fab3ad6faec", "2020-11-29", "0")
    add_token2("G00523431", "6c44198c4a475817", "2021-02-09", "0")


add_test_tokens()






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

def decryptMsg(secret_key, encrypted):
    secret_key = b64decode(secret_key)
    encrypted = encrypted.split(':')
    nonce = b64decode(encrypted[0])
    encrypted = b64decode(encrypted[1])
    box = SecretBox(secret_key)
    decrypted = box.decrypt(encrypted, nonce).decode('utf-8')

    print("Decrypted token: ", decrypted)
    return decrypted


'''Submits a token to the database.
'''
@app.route('/submit-token', methods=['POST'])
def test():
    if request.method == 'POST':
        msg = request.json
        token = str(msg['msg'])
        print("Request received:", id, token)

        # decypt
        secret_key = "5MsHBAGgmulDbS2AsX9bNY9fd5SVKd3IG5SXc9JTVic="
        decrypted = decryptMsg(secret_key, token).split(':')
        
        # Add to db
        with sqlite3.connect(DATABASE) as con:
            add_token(decrypted[0], decrypted[1])

    return "ok"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
