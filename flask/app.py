from flask import Flask,render_template,url_for,redirect,request,flash
from flask_mysqldb import MySQL

app=Flask(__name__)

#mysql connection

app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]="root"
app.config["MYSQL_DB"]="dhinakar"
app.config["MYSQL_CURSORCLASS"]="DictCursor"
mysql=MySQL(app)


#Loading Home Page
@app.route("/")
def home ():
    con=mysql.connection.cursor()
    sql="SELECT * FROM users"
    con.execute(sql)
    res=con.fetchall()
    return render_template("home.html",datas=res)

#New User
@app.route("/addusers",methods=['GET','POST'])
def addusers():
    if request.method=='POST':
        name=request.form['name']
        age=request.form['age']
        city=request.form['city']
        con=mysql.connection.cursor()
        sql="insert into users(name,city,age) value (%s,%s,%s)"
        con.execute(sql,[name,city,age])
        mysql.connection.commit()
        con.close()
        flash('User Detail Added')
        return redirect(url_for("home"))
    return render_template("add users.html")

#update User
@app.route("/editUser/<string:id>",methods=['GET','POST'])

def editUser(id):
    con=mysql.connection.cursor()

    if request.method=='POST':
        name=request.form['name']
        age=request.form['age']
        city=request.form['city']
        sql="Update users set Name=%s,City=%s,Age=%s where ID=%s"
        con.execute(sql,[name,city,age,id])
        mysql.connection.commit()
        con.close()
        flash('User Detail Updated')
        return redirect(url_for("home"))
        con=mysql.connection.cursor()

        
        
    sql="SELECT * FROM users where ID=%s"
    con.execute(sql,[id])
    res=con.fetchone()
     
    return render_template("edit user.html",datas=res)

#DELETE USER
@app.route("/deleteUser/<string:id>",methods=['GET','POST'])
def deleteUser(id):
     con=mysql.connection.cursor()
     sql="Delete from Users where (ID = %s) "
     con.execute(sql,[id])
     mysql.connection.commit()
     con.close()
     flash('User Detail Deleted')
     return redirect(url_for("home"))

    
if(__name__=='__main__'):
    app.secret_key="abc123"
    app.run(debug=True)


