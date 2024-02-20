import sqlite3
class Data():

    def create_table_main():
        create_main=sqlite3.connect("data.db")
        cur=create_main.cursor()
        cur.execute("CREATE TABLE info(name ,number,age ,mony ,mony_ ,state,diagnos,doctor,room,ch_ill )")
        create_main.commit()

    def insert_data(name ,number,age ,mony ,mony_ ,state,diagnos,doctor,room,ch_ill):
        data=[name ,number,age ,mony ,mony_ ,state,diagnos,doctor,room,ch_ill]
        conect=sqlite3.connect("data.db")
        cur=conect.cursor()
        cur.execute("INSERT INTO info VALUES(?,?,?,?,?,?,?,?,?,?)",data)
        conect.commit()

    def select_data(number):
        num=[number]
        conect=sqlite3.connect("data.db")
        cur=conect.cursor()
        data= cur.execute("SELECT * FROM info WHERE number=?",num)
        return data.fetchall()







 

