from flask import Flask,render_template,request,redirect,url_for
import mysql.connector
# import cgi
import random
import string

app=Flask(__name__)

mysql_config={
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'SRS'
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/connect",methods=['GET','POST'])
def connectdb():
    #/usr/local/bin/python3
    # print("Content-Type: text/html")
    # print()



    # print("<h1>Welcome to Student database.")
    # print("<br/>")
    # print("<h2>Entering random records into the database...")
    # print("<hr/>")

    # form = cgi.FieldStorage()

    def get_random_string(length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str


    def random_phone_num():
        first = str(random.randint(100, 999))
        second = str(random.randint(1, 888)).zfill(3)
        last = (str(random.randint(1, 9998)).zfill(4))
        while last in ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888']:
            last = (str(random.randint(1, 9998)).zfill(4))
        return '{}{}{}'.format(first, second, last)


    # no_of_records = int(form.getvalue("num"))
    no_of_records = 0

    if request.method=="POST":
        no_of_records=int(request.form['num'])
    # print(no_of_records)

        records=[]

        for i in range(no_of_records):
            name,phone = get_random_string(15),random_phone_num()
            records.append((name,phone))


        # print(records)

        # con = mysql.connector.connect(user="mysql",password="",host='localhost',database='SRS')
        con = mysql.connector.connect(**mysql_config)
        cur=con.cursor()
        datainserted=0
        for record in records:
            cur.execute("insert into data values(%s,%s)",record)
            datainserted+=1
        con.commit()
        message=""
        messagetag="success"
        if datainserted==no_of_records:
            message="All data are inserted successfully"
        else:
            messagetag="warning"
            message=f"Oops some error occured!!. {datainserted} data inserted while input is {no_of_records}"

        cur.close()
        con.close()
    else:
        messagetag="danger"
        message="Sething is missing!!"

    return render_template("index.html",message=message,messagetag=messagetag)

    # print("<h2>All records entered successfully")


if __name__=='__main__':
    app.run()