from flask import Flask, render_template, request
import mysql.connector
import random
import string
import math
import random as rd
import getname as gn


app = Flask(__name__)

# Configure the MySQL connection
mysql_config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'aiclass'
}

# Home page


@app.route("/")
def home():
    return render_template("home.html")

# function for generating contact number


def gen_number():
    number = ''.join(str(rd.randint(0, 9)) for _ in range(10))
    return number


# function for generating name
def gen_name(length):
    letters = string.ascii_lowercase
    name = ''.join(random.choice(letters) for _ in range(length))
    return name


def data_percent(data, total):
    if data == 0 or total == 0:
        return float(0)
    percent = data/total
    data_perct = '{:.2f}'.format(percent*100.00)
    return data_perct

# Data Insertion


@app.route("/insert", methods=['GET', 'POST'])
def insertdata():

    data_insert = 0
    datacreated = 0
    datainserted = 0
    if request.method == "POST":
        data_insert = int(request.form['data-insert'])
        datas = []
        for _ in range(data_insert):
            name, contact = gn.gen_name(), "+91 " + gen_number()
            datas.append((name, contact))

        datacreated = len(datas)
        # dbcont = mysql.connector.connect(user="mysql",password="",host='localhost',database='SRS')
        dbcont = mysql.connector.connect(**mysql_config)
        cur = dbcont.cursor()
        for record in datas:
            cur.execute("insert into datatable values(%s,%s)", record)
            datainserted += 1
        dbcont.commit()
        message = ""
        messagetag = "success"
        if datainserted == data_insert or datainserted == datacreated:
            message = f"{data_percent(datainserted,datacreated)}% data inserted successfully"
        else:
            messagetag = "warning"
            message = f"Oops some error occured!!. {data_percent(datainserted,datacreated)}% data inserted."

        cur.close()
        dbcont.close()
    else:
        messagetag = "danger"
        message = "Sething is missing!!"

    return render_template("home.html", message=message, messagetag=messagetag)

# Show data from database


@app.route("/data")
def showdata():
    # Get the current page number from the query string
    page = request.args.get('page', default=1, type=int)

    # Connect to the MySQL database and retrieve the data for the current page
    dbcont = mysql.connector.connect(**mysql_config)
    cursor = dbcont.cursor()
    rows_per_page = 9
    offset = (page - 1) * rows_per_page
    limit = rows_per_page
    query = f"SELECT * FROM datatable LIMIT {limit} OFFSET {offset}"
    cursor.execute(query)
    data = cursor.fetchall()

    # Calculate the total number of rows and pages
    query = "SELECT COUNT(*) FROM datatable"
    cursor.execute(query)
    total_rows = cursor.fetchone()[0]
    total_pages = math.ceil(total_rows / rows_per_page)

    # Close the cursor and database connection
    cursor.close()
    dbcont.close()
    # print(data)
    # print(page)
    # print(total_pages)
    # for ds in data:
    #     print(ds[0])
    # Render the HTML template with the datas and pagination variables
    return render_template("data.html", data=data, page=page, pages=total_pages)


# Main function
if __name__ == '__main__':
    app.run(debug=True)
