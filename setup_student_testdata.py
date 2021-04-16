from flask import Flask, request, jsonify, send_file
from flask_cors import CORS

from datetime import datetime
import sqlite3

DATABASE = 'gmit.db'
CREATE_QUERY = """create table if not exists students(
                id varchar(32) unique, fname varchar(32), lname varchar(32),
                email varchar(32), programme varchar(32), year integer,
                covid_status integer);
                """


app = Flask(__name__)
CORS(app)


'''Adds to the database.
'''
def add_student(id, fname, lname, programme, year, covid_status):
    email = id + "@gmit.ie"
    # Check how random_ids is saved...
    data = (id, fname, lname, email, programme, year, covid_status)
    sql = """insert into students(id, fname, lname, email, programme, year, covid_status) 
            values (?, ?, ?, ?, ?, ?, ?);"""

    with sqlite3.connect(DATABASE) as con:
        try:
            con.execute(sql, data)
        except sqlite3.IntegrityError:
            pass

def add_test_students():
	add_student("G00400101", "Inell", "Cook", "GA484", "2", "1")
	add_student("G00400102", "Mechelle", "Guzman", "GA484", "2", "0")
	add_student("G00400103", "Nikole", "Huff", "GA182", "1", "0")
	add_student("G00400104", "Dung", "Stein", "GA787", "3", "0")
	add_student("G00400105", "Alecia", "Bullock", "GA484", "1", "0")
	add_student("G00400106", "Nikole", "Skinner", "GA484", "2", "0")
	add_student("G00400107", "Moshe", "Boyer", "GA484", "2", "0")
	add_student("G00400108", "Betty", "Skinner", "GA787", "3", "0")
	add_student("G00400109", "Marcela", "Davenport", "GA787", "1", "0")
	add_student("G00400110", "Yoko", "Davidson", "GA484", "4", "0")
	add_student("G00400111", "Veronica", "Fuller", "GA484", "2", "1")
	add_student("G00400112", "Sheri", "Hanson", "GA484", "4", "0")
	add_student("G00400113", "Naida", "Green", "GA484", "2", "0")
	add_student("G00400114", "Sheryl", "Hodges", "GA182", "2", "0")
	add_student("G00400115", "Nikole", "Vaughan", "GA182", "2", "0")
	add_student("G00400116", "Dung", "Maynard", "GA182", "3", "0")
	add_student("G00400117", "Ernie", "Nicholson", "GA182", "1", "0")
	add_student("G00400118", "Naida", "Green", "GA484", "3", "0")
	add_student("G00400119", "Alecia", "Cook", "GA182", "1", "0")
	add_student("G00400120", "Tommie", "Giles", "GA787", "4", "0")
	add_student("G00400121", "Dung", "Vaughan", "GA182", "4", "1")
	add_student("G00400122", "Kellye", "Coffey", "GA182", "4", "0")
	add_student("G00400123", "Inell", "Melendez", "GA787", "3", "0")
	add_student("G00400124", "Veronica", "Stein", "GA787", "3", "0")
	add_student("G00400125", "Tommie", "Barton", "GA182", "4", "0")
	add_student("G00400126", "Ernie", "Hanson", "GA787", "3", "0")
	add_student("G00400127", "Hedy", "Vaughan", "GA787", "4", "0")
	add_student("G00400128", "Ernest", "Cook", "GA182", "2", "0")
	add_student("G00400129", "Nana", "Landry", "GA787", "1", "0")
	add_student("G00400130", "Alecia", "Short", "GA787", "2", "0")
	add_student("G00400131", "Seymour", "Barton", "GA787", "3", "1")
	add_student("G00400132", "Clarice", "Skinner", "GA182", "2", "0")
	add_student("G00400133", "Jacki", "Acosta", "GA787", "4", "0")
	add_student("G00400134", "Gail", "Irwin", "GA182", "3", "0")
	add_student("G00400135", "Susy", "Fuller", "GA182", "3", "0")
	add_student("G00400136", "Mechelle", "Howe", "GA182", "1", "0")
	add_student("G00400137", "Moshe", "Watson", "GA182", "1", "0")
	add_student("G00400138", "Inell", "Ellison", "GA787", "2", "0")
	add_student("G00400139", "Betty", "Skinner", "GA787", "4", "0")
	add_student("G00400140", "Renaldo", "Giles", "GA182", "4", "0")
	add_student("G00400141", "Dung", "Boyer", "GA182", "2", "1")
	add_student("G00400142", "Seymour", "Brady", "GA182", "4", "0")
	add_student("G00400143", "Lue", "Benjamin", "GA182", "1", "0")
	add_student("G00400144", "Britta", "Bird", "GA484", "1", "0")
	add_student("G00400145", "Yoko", "Robles", "GA182", "2", "0")
	add_student("G00400146", "Nikole", "Coffey", "GA484", "2", "0")
	add_student("G00400147", "Suanne", "Huff", "GA182", "2", "0")
	add_student("G00400148", "Dung", "Green", "GA484", "2", "0")
	add_student("G00400149", "Katelynn", "Barton", "GA182", "4", "0")
	add_student("G00400150", "Shanda", "Cook", "GA182", "1", "0")
	add_student("G00400151", "Seymour", "Barton", "GA787", "3", "1")
	add_student("G00400152", "Tommie", "Calhoun", "GA787", "4", "0")
	add_student("G00400153", "Mechelle", "Howe", "GA182", "3", "0")
	add_student("G00400154", "Clarice", "Maynard", "GA787", "3", "0")
	add_student("G00400155", "Hildred", "Bullock", "GA484", "1", "0")
	add_student("G00400156", "Annamae", "Parks", "GA484", "4", "0")
	add_student("G00400157", "Inell", "Howe", "GA787", "4", "0")
	add_student("G00400158", "Erika", "Blanchard", "GA182", "1", "0")
	add_student("G00400159", "Sheri", "David", "GA182", "2", "0")
	add_student("G00400160", "Leonie", "Parks", "GA182", "2", "0")
	add_student("G00400161", "Moshe", "Keller", "GA787", "2", "1")
	add_student("G00400162", "Huong", "Benjamin", "GA182", "2", "0")
	add_student("G00400163", "Dung", "Guzman", "GA182", "1", "0")
	add_student("G00400164", "Erika", "Davenport", "GA787", "2", "0")
	add_student("G00400165", "Britta", "Coffey", "GA484", "1", "0")
	add_student("G00400166", "Matilda", "Rich", "GA182", "1", "0")
	add_student("G00400167", "Tommie", "Calhoun", "GA182", "1", "0")
	add_student("G00400168", "Sally", "Guzman", "GA484", "2", "0")
	add_student("G00400169", "Susy", "Blanchard", "GA182", "3", "0")
	add_student("G00400170", "Abraham", "Rich", "GA787", "2", "0")
	add_student("G00400171", "Veronica", "Keller", "GA182", "2", "1")
	add_student("G00400172", "Naida", "Daugherty", "GA787", "2", "0")
	add_student("G00400173", "Tommie", "Benjamin", "GA484", "1", "0")
	add_student("G00400174", "Frederic", "Beard", "GA182", "2", "0")
	add_student("G00400175", "Abraham", "Acosta", "GA182", "4", "0")
	add_student("G00400176", "Katelynn", "Greene", "GA182", "4", "0")
	add_student("G00400177", "Toshia", "Coffey", "GA484", "2", "0")
	add_student("G00400178", "Katelynn", "Acosta", "GA182", "4", "0")
	add_student("G00400179", "Abraham", "Schroeder", "GA182", "4", "0")
	add_student("G00400180", "Mechelle", "Small", "GA484", "3", "0")
	add_student("G00400181", "Nana", "Daugherty", "GA787", "2", "1")
	add_student("G00400182", "Reed", "Green", "GA787", "2", "0")
	add_student("G00400183", "Dung", "Acosta", "GA182", "3", "0")
	add_student("G00400184", "Sheri", "Small", "GA484", "3", "0")
	add_student("G00400185", "Yoko", "Benjamin", "GA484", "4", "0")
	add_student("G00400186", "Gail", "Boyer", "GA182", "2", "0")
	add_student("G00400187", "Joye", "Chavez", "GA787", "2", "0")
	add_student("G00400188", "Joye", "Davenport", "GA484", "3", "0")
	add_student("G00400189", "Lelia", "Blanchard", "GA182", "3", "0")
	add_student("G00400190", "Concetta", "Roach", "GA182", "2", "0")
	add_student("G00400191", "Renaldo", "Robles", "GA182", "4", "1")
	add_student("G00400192", "Frederic", "David", "GA484", "2", "0")
	add_student("G00400193", "Hedy", "Fuller", "GA484", "1", "0")
	add_student("G00400194", "Marcela", "Hodges", "GA182", "2", "0")
	add_student("G00400195", "Renaldo", "Brennan", "GA787", "4", "0")
	add_student("G00400196", "Mechelle", "Bullock", "GA484", "1", "0")
	add_student("G00400197", "Lue", "Davenport", "GA484", "2", "0")
	add_student("G00400198", "Concetta", "Brady", "GA787", "4", "0")
	add_student("G00400199", "Britta", "David", "GA182", "4", "0")
	add_student("G00400200", "Nana", "Schroeder", "GA787", "4", "0")

'''Creates the database, if it does not exist.
'''
with sqlite3.connect(DATABASE) as con:
    con.execute(CREATE_QUERY)

add_test_students()