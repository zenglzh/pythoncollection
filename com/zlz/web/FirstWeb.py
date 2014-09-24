import web
import sqlite3
        
urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

class hello:        
    def GET(self, name):
        con = sqlite3.connect("blog.db")
        cur = con.cursor()
        cur.execute('select * from user1')
        for row in cur:
            print row
        cur.close()
        con.close()
        
if __name__ == "__main__":
    app.run()