import sqlite3

con = sqlite3.connect("blog.db")
cur = con.cursor()
#cur.execute("create table user1(date,number,article)")
cur.execute('CREATE TABLE todo (id INT AUTO_INCREMENT,title TEXT,primary key(id))')
#####
#tt1 = ('2014-09-20','1','aaa')
#cur.execute("""insert into user1(date,number,article) values (?,?,?)""",tt1)
#
#tt2 = ('2014-09-21','2','bbba')
#cur.execute("""insert into user1(date,number,article) values (?,?,?)""",tt2)
#tt3 = ('2014-09-22','1','ccc')
#cur.execute("""insert into user1(date,number,article) values (?,?,?)""",tt3)

con.commit()
cur.close()
con.close()
