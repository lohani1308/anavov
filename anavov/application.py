from flask import *
import sqlite3 as sq
app=Flask(__name__)

app.database="anavov.db"

@app.route('/')
def index():
    return render_template("login.html")
#============================================================================================================
@app.route('/product-add')
def product_add():
    return render_template("add-product.html")
#============================================================================================
@app.route('/prod',methods=['POST'])
def add():
    name = request.form["name"]
    desc = request.form["description"]
    date = request.form["expire_date"]
    stock=request.form["stock"]
    conn = sq.connect("anavov.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO product VALUES (?,?,?,?)", [name,desc,date,stock])
    conn.commit()
    conn.close()
    return render_template("index.html")

#=============================================================================================================
@app.route('/signup')
def signup():
    return render_template("signup.html")
#====================================================================================================
@app.route('/sign',methods=['POST'])
def input():
    name = request.form["username"]
    passw = request.form["password"]
    phone=request.form["phone"]
    conn = sq.connect("anavov.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO first VALUES (?,?,?)", [name, phone,passw])
    conn.commit()
    conn.close()
    return render_template("signup.html")
#=============================================================================================================
@app.route('/login',methods=['POST'])
def login():
    username=request.form['username']
    password=request.form['password']
    conn=sq.connect("anavov.db")
    cursor=conn.cursor()
    cursor.execute("select * from first where email=(?) and password=(?)",[username,password])
    if cursor.fetchone():
        session['ml']=username
        return redirect(url_for("landing"))
    else:
        msg="sry not valid username or password"
        return render_template("login.html",msg=msg)
#================================================================================================================
@app.route('/landing')
def landing():
    if 'ml' in session:
        return render_template('index.html')
    else:
        return redirect("/")

#==============================================================================================


app.run(debug=True)