from datetime import datetime
from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
import json
from flask_mail import Mail
with open("config.json","r") as c:
    params=json.load(c)["params"]


app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///mart.db"
app.config["SQLALCHEMY_TRACK_NOTIFCATIONS"]=False
app.config.update(
    MAIL_SERVER="smtp.gmail.com",
    MAIL_PORT="465",
    MAIL_USE_SSL=True,
    MAIL_USERNAME=params["user-id"],
    MAIL_PASSWORD=params["user-password"]
)
mail=Mail(app)
db=SQLAlchemy(app)

class Items(db.Model):
    # Sno=db.Column(db.Integer, primary_key=True,nullable=True)
    Product=db.Column(db.String(20))
    Quantity=db.Column(db.Integer,primary_key=True,unique=False)
    Subtotal=db.Column(db.Integer,primary_key=True,unique=False)
    def __repr__(self) -> str:
        return f"----{self.Product}----"

@app.route("/")
def hello_user():
    return render_template("index.html")

@app.route("/aboutus")
def about():
    return render_template('myabout.html')


@app.route("/contactus",methods=["GET","POST"])
def contact():
    if request.method=="POST":
        name1=request.form["name1"]
        email1=request.form["email1"]
        phone1=request.form["phone1"]
        subject1=request.form["subject1"]
        message1=request.form["message1"]
        mail.send_message("EnPassant Query Form",
            sender=params["user-id"],
            recipients=[email1],
            body= "hello "+ name1 +",\n" +"we will look into your query and will resolve it as soon as possible \n"  +"registered mobile number is "+phone1 +"\n subject :" +subject1 +"\n message:" + message1 +"\n Thanks for choosing us \n\n -EnPassant"
        ) 
        return render_template("mycontact.html")
    return render_template("mycontact.html")

@app.route("/fruitstore")
def fruitstore():
    allitems=Items.query.all()
    return render_template("fruits.html",allitems=allitems)

@app.route("/banana",methods=["GET", "POST"])
def banana():
    render_template("banana.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="banana",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("fruits.html",allitems=allitems)
    return render_template("banana.html")

@app.route("/apples",methods=["GET", "POST"])
def apples():
    render_template("apples.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="apple",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("fruits.html",allitems=allitems)
    return render_template("apples.html")

@app.route("/oranges",methods=["GET", "POST"])
def oranges():
    render_template("oranges.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="orange",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("fruits.html",allitems=allitems)
    return render_template("oranges.html")

@app.route("/kiwi",methods=["GET", "POST"])
def kiwi():
    render_template("kiwi.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="kiwi",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("fruits.html",allitems=allitems)
    return render_template("kiwi.html")

@app.route("/greenapple",methods=["GET", "POST"])
def greenapple():
    render_template("greenapple.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="greenapple",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("fruits.html",allitems=allitems)
    return render_template("greenapple.html")

@app.route("/pear",methods=["GET", "POST"])
def pear():
    render_template("pear.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="pear",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("fruits.html",allitems=allitems)
    return render_template("pear.html")

@app.route("/watermelon",methods=["GET", "POST"])
def watermelon():
    render_template("watermelon.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="watermelon",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("fruits.html",allitems=allitems)
    return render_template("watermelon.html")

@app.route("/pineapple",methods=["GET", "POST"])
def pineapple():
    render_template("pineapple.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="pineapple",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("fruits.html",allitems=allitems)
    return render_template("pineapple.html")

@app.route("/strawberries",methods=["GET", "POST"])
def strawberries():
    render_template("strawberries.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="strawberry",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("fruits.html",allitems=allitems)
    return render_template("strawberries.html")

@app.route("/coconut",methods=["GET","POST"])
def coconut():
    render_template("coconut.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="coconut",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("fruits.html",allitems=allitems)
    return render_template("coconut.html")

@app.route("/muskmelon",methods=["GET", "POST"])
def muskmelon():
    render_template("muskmelon.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="muskmelon",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("fruits.html",allitems=allitems)
    return render_template("muskmelon.html")

@app.route("/thaijam",methods=["GET", "POST"])
def thaijam():
    render_template("thaijam.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="thaijam",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("fruits.html",allitems=allitems)
    return render_template("thaijam.html")


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#


@app.route("/vegetablestore")
def vegetablestore():
    allitems=Items.query.all()
    return render_template("vegetables.html",allitems=allitems)

@app.route("/tomato",methods=["GET", "POST"])
def tomato():
    render_template("tomato.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="tomato",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("vegetables.html",allitems=allitems)
    return render_template("tomato.html")

@app.route("/bigtomato",methods=["GET", "POST"])
def bigtomato():
    render_template("bigtomato.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="big tomato",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("vegetables.html",allitems=allitems)
    return render_template("bigtomato.html")

@app.route("/yam",methods=["GET", "POST"])
def yam():
    render_template("yam.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="yam",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("vegetables.html",allitems=allitems)
    return render_template("yam.html")

@app.route("/cauliflower",methods=["GET", "POST"])
def cauliflower():
    render_template("cauliflower.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="cauliflower",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("vegetables.html",allitems=allitems)
    return render_template("cauliflower.html")

@app.route("/ginger",methods=["GET", "POST"])
def ginger():
    render_template("ginger.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="ginger",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("vegetables.html",allitems=allitems)
    return render_template("ginger.html")

@app.route("/lemon",methods=["GET", "POST"])
def lemon():
    render_template("lemon.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="lemon",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("vegetables.html",allitems=allitems)
    return render_template("lemon.html")

@app.route("/lemonsmall",methods=["GET", "POST"])
def lemonsmall():
    render_template("lemonsmall.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="lemonsmall",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("vegetables.html",allitems=allitems)
    return render_template("lemonsmall.html")

@app.route("/nobanana",methods=["GET", "POST"])
def nobanana():
    render_template("nobanana.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="nobanana",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("vegetables.html",allitems=allitems)
    return render_template("nobanana.html")

@app.route("/sbbrinjal",methods=["GET", "POST"])
def sbbrinjal():
    render_template("sbbrinjal.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="sbbrinjal",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("vegetables.html",allitems=allitems)
    return render_template("sbbrinjal.html")

@app.route("/smirchi",methods=["GET","POST"])
def smirchi():
    render_template("smirchi.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="smirchi",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("vegetables.html",allitems=allitems)
    return render_template("smirchi.html")

@app.route("/bittergourd",methods=["GET", "POST"])
def bittergourd():
    render_template("bittergourd.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="bittergourd",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("vegetables.html",allitems=allitems)
    return render_template("bittergourd.html")

@app.route("/cbbeans",methods=["GET", "POST"])
def cbbeans():
    render_template("cbbeans.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="cbbeans",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("vegetables.html",allitems=allitems)
    return render_template("cbbeans.html")

@app.route("/capsicum",methods=["GET", "POST"])
def capsicum():
    render_template("capsicum.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="capsicum",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("vegetables.html",allitems=allitems)
    return render_template("capsicum.html")

@app.route("/swbrinjal",methods=["GET", "POST"])
def swbrinjal():
    render_template("swbrinjal.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="swbrinjal",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("vegetables.html",allitems=allitems)
    return render_template("swbrinjal.html")

@app.route("/sbottlegourd",methods=["GET", "POST"])
def sbottlegourd():
    render_template("sbottlegourd.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="sbottlegourd",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("vegetables.html",allitems=allitems)
    return render_template("sbottlegourd.html")

@app.route("/gajar",methods=["GET", "POST"])
def gajar():
    render_template("gajar.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="gajar",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("vegetables.html",allitems=allitems)
    return render_template("gajar.html")

@app.route("/beans",methods=["GET", "POST"])
def beans():
    render_template("beans.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="beans",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("vegetables.html",allitems=allitems)
    return render_template("beans.html")

@app.route("/wtchilli",methods=["GET", "POST"])
def wtchilli():
    render_template("wtchilli.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="wtchilli",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("vegetables.html",allitems=allitems)
    return render_template("wtchilli.html")


@app.route("/orangesveg",methods=["GET", "POST"])
def orangesveg():
    render_template("orangesveg.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="orangesveg",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("vegetables.html",allitems=allitems)
    return render_template("orangesveg.html")


@app.route("/kapple",methods=["GET", "POST"])
def kapple():
    render_template("kapple.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="kapple",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("vegetables.html",allitems=allitems)
    return render_template("kapple.html")


@app.route("/lbbrinjal",methods=["GET", "POST"])
def lbbrinjal():
    render_template("lbbrinjal.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="lbbrinjal",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("vegetables.html",allitems=allitems)
    return render_template("lbbrinjal.html")


@app.route("/krchilli",methods=["GET", "POST"])
def krchilli():
    render_template("krchilli.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="krchilli",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("vegetables.html",allitems=allitems)
    return render_template("krchilli.html")


@app.route("/garlic",methods=["GET", "POST"])
def garlic():
    render_template("garlic.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="garlic",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("vegetables.html",allitems=allitems)
    return render_template("garlic.html")


@app.route("/onion",methods=["GET", "POST"])
def onion():
    render_template("onion.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="onion",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("vegetables.html",allitems=allitems)
    return render_template("onion.html")


@app.route("/potato",methods=["GET", "POST"])
def potato():
    render_template("potato.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="potato",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("vegetables.html",allitems=allitems)
    return render_template("potato.html")


@app.route("/malberries",methods=["GET", "POST"])
def malberries():
    render_template("malberries.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="malberries",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("vegetables.html",allitems=allitems)
    return render_template("malberries.html")


@app.route("/beetroot",methods=["GET", "POST"])
def beetroot():
    render_template("beetroot.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="beetroot",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("vegetables.html",allitems=allitems)
    return render_template("beetroot.html")




#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
@app.route("/bakery")
def bakery():
    allitems=Items.query.all()
    return render_template("bakery.html",allitems=allitems)

@app.route("/strawberry-cupcake",methods=["GET", "POST"])
def strawberrycupcake():
    render_template("strawberry-cupcake.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="strawberry-cupcake",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("bakery.html",allitems=allitems)
    return render_template("strawberry-cupcake.html")

@app.route("/strawberry-pastries",methods=["GET", "POST"])
def strawberrypastries():
    render_template("strawberry-pastries.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="strawberry-pastries",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("bakery.html",allitems=allitems)
    return render_template("strawberry-pastries.html")

@app.route("/butterscotch-pastries",methods=["GET", "POST"])
def butterscotchpastries():
    render_template("butterscotch-pastries.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="butterscotch-pastries",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("bakery.html",allitems=allitems)
    return render_template("butterscotch-pastries.html")

@app.route("/strawberry-vanila-pastries",methods=["GET", "POST"])
def strawberryvanilapastries():
    render_template("strawberry-vanila-pastries.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="strawberry-vanila-pastries",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("bakery.html",allitems=allitems)
    return render_template("strawberry-vanila-pastries.html")

@app.route("/strawberry-cake",methods=["GET", "POST"])
def strawberrycake():
    render_template("strawberry-cake.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="strawberry-cake",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("bakery.html",allitems=allitems)
    return render_template("strawberry-cake.html")

@app.route("/pistaachio-pastry",methods=["GET", "POST"])
def pistaachiopastry():
    render_template("pistaachio-pastry.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="pistaachio-pastry",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("bakery.html",allitems=allitems)
    return render_template("pistaachio-pastry.html")

@app.route("/croissants-choclate",methods=["GET", "POST"])
def croissantschoclate():
    render_template("croissants-choclate.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="croissants-choclate",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("bakery.html",allitems=allitems)
    return render_template("croissants-choclate.html")


@app.route("/vanila-butterscotch-pastry",methods=["GET", "POST"])
def vanilabutterscotchpastry():
    render_template("vanila-butterscotch-pastry.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="vanila-butterscotch-pastry",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("bakery.html",allitems=allitems)
    return render_template("vanila-butterscotch-pastry.html")


@app.route("/rainbow-sprinkled-strawberry-pastries",methods=["GET", "POST"])
def rainbowsprinkledstrawberrypastries():
    render_template("rainbow-sprinkled-strawberry-pastries.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="rainbow-sprinkled-strawberry-pastries",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("bakery.html",allitems=allitems)
    return render_template("rainbow-sprinkled-strawberry-pastries.html")


@app.route("/pineapple-pastries",methods=["GET", "POST"])
def pineapplepastries():
    render_template("pineapple-pastries.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="pineapple-pastries",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("bakery.html",allitems=allitems)
    return render_template("pineapple-pastries.html")


@app.route("/sweet-shot",methods=["GET", "POST"])
def sweetshot():
    render_template("sweet-shot.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="sweet-shot",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("bakery.html",allitems=allitems)
    return render_template("sweet-shot.html")


@app.route("/chef-vishwa's-special-french-cookies",methods=["GET", "POST"])
def chefvishwasspecialfrenchcookies():
    render_template("chef-vishwa's-special-french-cookies.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="chef-vishwa's-special-french-cookies",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("bakery.html",allitems=allitems)
    return render_template("chef-vishwa's-special-french-cookies.html")


@app.route("/chef-vishwa's-special-choco-cheese-shots",methods=["GET", "POST"])
def chefvishwasspecialchococheeseshots():
    render_template("chef-vishwa's-special-choco-cheese-shots.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="chef-vishwa's-special-choco-cheese-shots",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("bakery.html",allitems=allitems)
    return render_template("chef-vishwa's-special-choco-cheese-shots.html")


@app.route("/croissant",methods=["GET", "POST"])
def croissant():
    render_template("croissant.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="croissant",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("bakery.html",allitems=allitems)
    return render_template("croissant.html")


@app.route("/chocolate-cup-cake",methods=["GET", "POST"])
def chocolatecupcake():
    render_template("chocolate-cup-cake.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="chocolate-cup-cake",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("bakery.html",allitems=allitems)
    return render_template("chocolate-cup-cake.html")
# -----------------------------------------------------------------------------------------------------------------------------------
@app.route("/chef-vishwa's-special-blueberry-pie",methods=["GET", "POST"])
def chefvishwasspecialblueberrypie():
    render_template("chef-vishwa's-special-blueberry-pie.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="chef-vishwa's-special-blueberry-pie",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("bakery.html",allitems=allitems)
    return render_template("chef-vishwa's-special-blueberry-pie.html")


@app.route("/choco-pie",methods=["GET", "POST"])
def chocopie():
    render_template("choco-pie.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="choco-pie",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("bakery.html",allitems=allitems)
    return render_template("choco-pie.html")


@app.route("/choco-chip-cake",methods=["GET", "POST"])
def chocochipcake():
    render_template("choco-chip-cake.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="choco-chip-cake",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("bakery.html",allitems=allitems)
    return render_template("choco-chip-cake.html")


@app.route("/butterscotch-cake",methods=["GET", "POST"])
def butterscotchcake():
    render_template("butterscotch-cake.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="butterscotch-cake",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("bakery.html",allitems=allitems)
    return render_template("butterscotch-cake.html")


@app.route("/rainbow-sprinkled-strawberry-cupcake",methods=["GET", "POST"])
def rainbowsprinkledstrawberrycupcake():
    render_template("rainbow-sprinkled-strawberry-cupcake.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="rainbow-sprinkled-strawberry-cupcake",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("bakery.html",allitems=allitems)
    return render_template("rainbow-sprinkled-strawberry-cupcake.html")


@app.route("/chocolate-doughnuts",methods=["GET", "POST"])
def chocolatedoughnuts():
    render_template("croissachocolate-doughnutsnt.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="chocolate-doughnuts",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("bakery.html",allitems=allitems)
    return render_template("chocolate-doughnuts.html")


@app.route("/choco-strawberry-cupcake",methods=["GET", "POST"])
def chocostrawberrycupcake():
    render_template("choco-strawberry-cupcake.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="choco-strawberry-cupcake",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("bakery.html",allitems=allitems)
    return render_template("choco-strawberry-cupcake.html")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
@app.route("/snacks")
def snacks():
    allitems=Items.query.all()
    return render_template("snacks.html",allitems=allitems)

@app.route("/BRITANIA RUSK",methods=["GET", "POST"])
def BRITANIARUSK():
    render_template("BRITANIA RUSK.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="BRITANIA RUSK",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("snacks.html",allitems=allitems)
    return render_template("BRITANIA RUSK.html")


@app.route("/BRITANIA BISCUIT",methods=["GET", "POST"])
def BRITANIABISCUIT():
    render_template("BRITANIA BISCUIT.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="BRITANIA BISCUIT",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("snacks.html",allitems=allitems)
    return render_template("BRITANIA BISCUIT.html")


@app.route("/BALAJI RASGULLA",methods=["GET", "POST"])
def BALAJIRASGULLA():
    render_template("BALAJI RASGULLA.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="BALAJI RASGULLA",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("snacks.html",allitems=allitems)
    return render_template("BALAJI RASGULLA.html")


@app.route("/HALDIRAMS WHITE RASGULLA",methods=["GET", "POST"])
def HALDIRAMSWHITERASGULLA():
    render_template("HALDIRAMS WHITE RASGULLA.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="HALDIRAMS WHITE RASGULLA",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("snacks.html",allitems=allitems)
    return render_template("HALDIRAMS WHITE RASGULLA.html")


@app.route("/HALDIRAMS ELAICHI RASGULLA",methods=["GET", "POST"])
def HALDIRAMSELAICHIRASGULLA():
    render_template("HALDIRAMS ELAICHI RASGULLA.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="HALDIRAMS ELAICHI RASGULLA",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("snacks.html",allitems=allitems)
    return render_template("HALDIRAMS ELAICHI RASGULLA.html")


@app.route("/HALDIRAMS ZOR GARAM CHANA",methods=["GET", "POST"])
def HALDIRAMSZORGARAMCHANA():
    render_template("HALDIRAMS ZOR GARAM CHANA.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="HALDIRAMS ZOR GARAM CHANA",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("snacks.html",allitems=allitems)
    return render_template("HALDIRAMS ZOR GARAM CHANA.html")


@app.route("/HALDIRAMS ALL IN ONE MIXTURE",methods=["GET", "POST"])
def HALDIRAMSALLINONEMIXTURE():
    render_template("HALDIRAMS ALL IN ONE MIXTURE.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="HALDIRAMS ALL IN ONE MIXTURE",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("snacks.html",allitems=allitems)
    return render_template("HALDIRAMS ALL IN ONE MIXTURE.html")


@app.route("/HALDIRAMS  ALOO BHUJIA",methods=["GET", "POST"])
def HALDIRAMSALOOBHUJIA():
    render_template("HALDIRAMS  ALOO BHUJIA.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="HALDIRAMS  ALOO BHUJIA",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("snacks.html",allitems=allitems)
    return render_template("HALDIRAMS  ALOO BHUJIA.html")


@app.route("/HALDIRAMS KHATTA MEETA",methods=["GET", "POST"])
def HALDIRAMSKHATTAMEETA():
    render_template("HALDIRAMS KHATTA MEETA.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="HALDIRAMS KHATTA MEETA",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("snacks.html",allitems=allitems)
    return render_template("HALDIRAMS KHATTA MEETA.html")


@app.route("/HALDIRAMS MIXTURE",methods=["GET", "POST"])
def HALDIRAMSMIXTURE():
    render_template("HALDIRAMS MIXTURE.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="HALDIRAMS MIXTURE",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("snacks.html",allitems=allitems)
    return render_template("HALDIRAMS MIXTURE.html")


@app.route("/HALDIRAMS MOONG DAL",methods=["GET", "POST"])
def HALDIRAMSMOONGDAL():
    render_template("HALDIRAMS MOONG DAL.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="HALDIRAMS MOONG DAL",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("snacks.html",allitems=allitems)
    return render_template("HALDIRAMS MOONG DAL.html")


@app.route("/HALDIRAMS CHATPATA DAL",methods=["GET", "POST"])
def HALDIRAMSCHATPATADAL():
    render_template("HALDIRAMS CHATPATA DAL.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="HALDIRAMS CHATPATA DAL",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("snacks.html",allitems=allitems)
    return render_template("HALDIRAMS CHATPATA DAL.html")


@app.route("/HALDIRAMS SWEET MIXTURE",methods=["GET", "POST"])
def HALDIRAMSSWEETMIXTURE():
    render_template("HALDIRAMS SWEET MIXTURE.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="HALDIRAMS SWEET MIXTURE",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("snacks.html",allitems=allitems)
    return render_template("HALDIRAMS SWEET MIXTURE.html")


@app.route("/HALDIRAMS NAVRATAN MIXTURE",methods=["GET", "POST"])
def HALDIRAMSNAVRATANMIXTURE():
    render_template("HALDIRAMS NAVRATAN MIXTURE.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="HALDIRAMS NAVRATAN MIXTURE",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("snacks.html",allitems=allitems)
    return render_template("HALDIRAMS NAVRATAN MIXTURE.html")


@app.route("/HALDIRAMS KHATA MEETA",methods=["GET", "POST"])
def HALDIRAMSKHATAMEETA():
    render_template("HALDIRAMS KHATA MEETA.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="HALDIRAMS KHATA MEETA",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("snacks.html",allitems=allitems)
    return render_template("HALDIRAMS KHATA MEETA.html")


@app.route("/HALDIRAMS ALOO BHUJIA SMALL",methods=["GET", "POST"])
def HALDIRAMSALOOBHUJIASMALL():
    render_template("HALDIRAMS ALOO BHUJIA SMALL.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="HALDIRAMS ALOO BHUJIA SMALL",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("snacks.html",allitems=allitems)
    return render_template("HALDIRAMS ALOO BHUJIA SMALL.html")


@app.route("/HALDIRAMS  DAL BHAJI",methods=["GET", "POST"])
def HALDIRAMSDALBHAJI():
    render_template("HALDIRAMS  DAL BHAJI.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="HALDIRAMS  DAL BHAJI",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("snacks.html",allitems=allitems)
    return render_template("HALDIRAMS  DAL BHAJI.html")


@app.route("/HALDIRAMS  SPICY MIXTURE",methods=["GET", "POST"])
def HALDIRAMSSPICYMIXTURE():
    render_template("HALDIRAMS  SPICY MIXTURE.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="HALDIRAMS  SPICY MIXTURE",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("snacks.html",allitems=allitems)
    return render_template("HALDIRAMS  SPICY MIXTURE.html")


@app.route("/KRACK JACK BISCUIT SMALL",methods=["GET", "POST"])
def KRACKJACKBISCUITSMALL():
    render_template("KRACK JACK BISCUIT SMALL.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="KRACK JACK BISCUIT SMALL",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("snacks.html",allitems=allitems)
    return render_template("KRACK JACK BISCUIT SMALL.html")


@app.route("/LITTLE HEARTS",methods=["GET", "POST"])
def LITTLEHEARTS():
    render_template("LITTLE HEARTS.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="LITTLE HEARTS",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("snacks.html",allitems=allitems)
    return render_template("LITTLE HEARTS.html")


@app.route("/SUNFEAST CREAM BISCUIT",methods=["GET", "POST"])
def SUNFEASTCREAMBISCUIT():
    render_template("SUNFEAST CREAM BISCUIT.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="SUNFEAST CREAM BISCUIT",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("snacks.html",allitems=allitems)
    return render_template("SUNFEAST CREAM BISCUIT.html")


@app.route("/BRITANIA CREAM BISCUIT",methods=["GET", "POST"])
def BRITANIACREAMBISCUIT():
    render_template("BRITANIA CREAM BISCUIT.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="BRITANIA CREAM BISCUIT",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("snacks.html",allitems=allitems)
    return render_template("BRITANIA CREAM BISCUIT.html")


@app.route("/BRITANIA BLUE CREAM BISCUIT",methods=["GET", "POST"])
def BRITANIABLUECREAMBISCUIT():
    render_template("BRITANIA BLUE CREAM BISCUIT.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="BRITANIA BLUE CREAM BISCUIT",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("snacks.html",allitems=allitems)
    return render_template("BRITANIA BLUE CREAM BISCUIT.html")


@app.route("/GOODAY BUTTER BISCUIT",methods=["GET", "POST"])
def GOODAYBUTTERBISCUIT():
    render_template("GOODAY BUTTER BISCUIT.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="GOODAY BUTTER BISCUIT",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("snacks.html",allitems=allitems)
    return render_template("GOODAY BUTTER BISCUIT.html")


@app.route("/GOODAY ELAICHI BUTTER BISCUIT",methods=["GET", "POST"])
def GOODAYELAICHIBUTTERBISCUIT():
    render_template("GOODAY ELAICHI BUTTER BISCUIT.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="GOODAY ELAICHI BUTTER BISCUIT",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("snacks.html",allitems=allitems)
    return render_template("GOODAY ELAICHI BUTTER BISCUIT.html")


@app.route("/GOODAY ALMOND BUTTER BISCUIT",methods=["GET", "POST"])
def GOODAYALMONDBUTTERBISCUIT():
    render_template("GOODAY ALMOND BUTTER BISCUIT.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="GOODAY ALMOND BUTTER BISCUIT",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("snacks.html",allitems=allitems)
    return render_template("GOODAY ALMOND BUTTER BISCUIT.html")


@app.route("/PARLE 50 50",methods=["GET", "POST"])
def PARLE5050():
    render_template("PARLE 50 50.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="PARLE 50 50",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("snacks.html",allitems=allitems)
    return render_template("PARLE 50 50.html")


@app.route("/SUNFEAST ELAICHI BISCUIT",methods=["GET", "POST"])
def SUNFEASTELAICHIBISCUIT():
    render_template("SUNFEAST ELAICHI BISCUIT.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="SUNFEAST ELAICHI BISCUIT",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("snacks.html",allitems=allitems)
    return render_template("SUNFEAST ELAICHI BISCUIT.html")


@app.route("/MONACO CREAM BISCUIT",methods=["GET", "POST"])
def MONACOCREAMBISCUIT():
    render_template("MONACO CREAM BISCUIT.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="MONACO CREAM BISCUIT",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("snacks.html",allitems=allitems)
    return render_template("MONACO CREAM BISCUIT.html")


@app.route("/MONACO BISCUIT",methods=["GET", "POST"])
def MONACOBISCUIT():
    render_template("MONACO BISCUIT.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="MONACO BISCUIT",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("snacks.html",allitems=allitems)
    return render_template("MONACO BISCUIT.html")


@app.route("/HALDIRAMS SOAN PAPDI",methods=["GET", "POST"])
def HALDIRAMSSOANPAPDI():
    render_template("HALDIRAMS SOAN PAPDI.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="HALDIRAMS SOAN PAPDI",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("snacks.html",allitems=allitems)
    return render_template("HALDIRAMS SOAN PAPDI.html")


@app.route("/HALDIRAMS SOAN PAPDI ELAICHI BIG",methods=["GET", "POST"])
def HALDIRAMSSOANPAPDIELAICHIBIG():
    render_template("HALDIRAMS SOAN PAPDI ELAICHI BIG.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="HALDIRAMS SOAN PAPDI ELAICHI BIG",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("snacks.html",allitems=allitems)
    return render_template("HALDIRAMS SOAN PAPDI ELAICHI BIG.html")


@app.route("/HALDIRAMS SOAN PAPDI ELAICHI SMALL",methods=["GET", "POST"])
def HALDIRAMSSOANPAPDIELAICHISMALL():
    render_template("HALDIRAMS SOAN PAPDI ELAICHI SMALL.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="HALDIRAMS SOAN PAPDI ELAICHI SMALL",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("snacks.html",allitems=allitems)
    return render_template("HALDIRAMS SOAN PAPDI ELAICHI SMALL.html")


@app.route("/HALDIRAMS MATHRI",methods=["GET", "POST"])
def HALDIRAMSMATHRI():
    render_template("HALDIRAMS MATHRI.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="HALDIRAMS MATHRI",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("snacks.html",allitems=allitems)
    return render_template("HALDIRAMS MATHRI.html")


@app.route("/HALDIRAMS MINI SAMOSA",methods=["GET", "POST"])
def HALDIRAMSMINISAMOSA():
    render_template("HALDIRAMS MINI SAMOSA.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="HALDIRAMS MINI SAMOSA",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("snacks.html",allitems=allitems)
    return render_template("HALDIRAMS MINI SAMOSA.html")


@app.route("/HALDIRAMS BHELPURI BOX PACK",methods=["GET", "POST"])
def HALDIRAMSBHELPURIBOXPACK():
    render_template("HALDIRAMS BHELPURI BOX PACK.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="HALDIRAMS BHELPURI BOX PACK",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("snacks.html",allitems=allitems)
    return render_template("HALDIRAMS BHELPURI BOX PACK.html")


@app.route("/HALDIRAMS BHELPURI COVER PACK",methods=["GET", "POST"])
def HALDIRAMSBHELPURICOVERPACK():
    render_template("HALDIRAMS BHELPURI COVER PACK.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="HALDIRAMS BHELPURI COVER PACK",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("snacks.html",allitems=allitems)
    return render_template("HALDIRAMS BHELPURI COVER PACK.html")


@app.route("/RAJA BANANA CHIPS",methods=["GET", "POST"])
def RAJABANANACHIPS():
    render_template("RAJA BANANA CHIPS.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="RAJA BANANA CHIPS",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("snacks.html",allitems=allitems)
    return render_template("RAJA BANANA CHIPS.html")


@app.route("/HALDIRAMS ALOO CHIPS",methods=["GET", "POST"])
def HALDIRAMSALOOCHIPS():
    render_template("HALDIRAMS ALOO CHIPS.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="HALDIRAMS ALOO CHIPS",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("snacks.html",allitems=allitems)
    return render_template("HALDIRAMS ALOO CHIPS.html")


@app.route("/HALDIRAMS SOYA CHIPS",methods=["GET", "POST"])
def HALDIRAMSSOYACHIPS():
    render_template("HALDIRAMS SOYA CHIPS.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="HALDIRAMS SOYA CHIPS",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("snacks.html",allitems=allitems)
    return render_template("HALDIRAMS SOYA CHIPS.html")


@app.route("/HALDIRAMS MURKULU",methods=["GET", "POST"])
def HALDIRAMSMURKULU():
    render_template("HALDIRAMS MURKULU.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="HALDIRAMS MURKULU",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("snacks.html",allitems=allitems)
    return render_template("HALDIRAMS MURKULU.html")


@app.route("/PIZZA BASE",methods=["GET", "POST"])
def PIZZABASE():
    render_template("PIZZA BASE.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="PIZZA BASE",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("snacks.html",allitems=allitems)
    return render_template("PIZZA BASE.html")

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
@app.route("/groceries")
def groceries():
    return render_template("groceries.html")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
@app.route("/dairy")
def dairy():
    allitems=Items.query.all()
    return render_template("dairy.html",allitems=allitems)

@app.route("/AMUL MILK CHOCLATE",methods=["GET", "POST"])
def AMULMILKCHOCLATE():
    render_template("AMUL MILK CHOCLATE.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="AMUL MILK CHOCLATE",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("dairy.html",allitems=allitems)
    return render_template("AMUL MILK CHOCLATE.html")


@app.route("/AMUL DARK CHOCLATE BIG",methods=["GET", "POST"])
def AMULDARKCHOCLATEBIG():
    render_template("AMUL DARK CHOCLATE BIG.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="AMUL DARK CHOCLATE BIG",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("dairy.html",allitems=allitems)
    return render_template("AMUL DARK CHOCLATE BIG.html")


@app.route("/AMUL DARK CHOCLATE SMALL",methods=["GET", "POST"])
def AMULDARKCHOCLATESMALL():
    render_template("AMUL DARK CHOCLATE SMALL.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="AMUL DARK CHOCLATE SMALL",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("dairy.html",allitems=allitems)
    return render_template("AMUL DARK CHOCLATE SMALL.html")








@app.route("/AMUL VALENTINE SPECIAL CHOCLATE PACK",methods=["GET", "POST"])
def AMULVALENTINESPECIALCHOCLATEPACK():
    render_template("AMUL VALENTINE SPECIAL CHOCLATE PACK.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="AMUL VALENTINE SPECIAL CHOCLATE PACK",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("dairy.html",allitems=allitems)
    return render_template("AMUL VALENTINE SPECIAL CHOCLATE PACK.html")





@app.route("/AMUL SUGAR FREE CHOCLATE SMALL",methods=["GET", "POST"])
def AMULSUGARFREECHOCLATESMALL():
    render_template("AMUL SUGAR FREE CHOCLATE SMALL.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="AMUL SUGAR FREE CHOCLATE SMALL",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("dairy.html",allitems=allitems)
    return render_template("AMUL SUGAR FREE CHOCLATE SMALL.html")




@app.route("/AMUL ALMOND",methods=["GET", "POST"])
def AMULALMOND():
    render_template("AMUL ALMOND.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="AMUL ALMOND",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("dairy.html",allitems=allitems)
    return render_template("AMUL ALMOND.html")


@app.route("/AMUL GHEE",methods=["GET", "POST"])
def AMULGHEE():
    render_template("AMUL GHEE.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="AMUL GHEE",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("dairy.html",allitems=allitems)
    return render_template("AMUL GHEE.html")


@app.route("/AMUL MASTHI",methods=["GET", "POST"])
def AMULMASTHI():
    render_template("AMUL MASTHI.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="AMUL MASTHI",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("dairy.html",allitems=allitems)
    return render_template("AMUL MASTHI.html")


@app.route("/AMUL DARK PASSION",methods=["GET", "POST"])
def AMULDARKPASSION():
    render_template("AMUL DARK PASSION.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="AMUL DARK PASSION",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("dairy.html",allitems=allitems)
    return render_template("AMUL DARK PASSION.html")


@app.route("/AMUL PIZZA CHEESE BIG",methods=["GET", "POST"])
def AMULPIZZACHEESEBIG():
    render_template("AMUL PIZZA CHEESE BIG.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="AMUL PIZZA CHEESE BIG",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("dairy.html",allitems=allitems)
    return render_template("AMUL PIZZA CHEESE BIG.html")


@app.route("/AMUL PIZZA CHEESE SMALL",methods=["GET", "POST"])
def AMULPIZZACHEESESMALL():
    render_template("AMUL PIZZA CHEESE SMALL.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="AMUL PIZZA CHEESE SMALL",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("dairy.html",allitems=allitems)
    return render_template("AMUL PIZZA CHEESE SMALL.html")


@app.route("/AMUL LASSI",methods=["GET", "POST"])
def AMULLASSI():
    render_template("AMUL LASSI.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="AMUL LASSI",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("dairy.html",allitems=allitems)
    return render_template("AMUL LASSI.html")





@app.route("/AMUL CREAM",methods=["GET", "POST"])
def AMULCREAM():
    render_template("AMUL CREAM.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="AMUL CREAM",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("dairy.html",allitems=allitems)
    return render_template("AMUL CREAM.html")


@app.route("/AMUL PRO ",methods=["GET", "POST"])
def AMULPRO ():
    render_template("AMUL PRO .html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="AMUL PRO ",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("dairy.html",allitems=allitems)
    return render_template("AMUL PRO .html")


@app.route("/AMUL PRO SMALL BOTTLE",methods=["GET", "POST"])
def AMULPROSMALLBOTTLE():
    render_template("AMUL PRO SMALL BOTTLE.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="AMUL PRO SMALL BOTTLE",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("dairy.html",allitems=allitems)
    return render_template("AMUL PRO SMALL BOTTLE.html")


@app.route("/AMUL GHEE SMALL",methods=["GET", "POST"])
def AMULGHEESMALL():
    render_template("AMUL GHEE SMALL.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="AMUL GHEE SMALL",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("dairy.html",allitems=allitems)
    return render_template("AMUL GHEE SMALL.html")


@app.route("/AMUL ALMOND CHOCLATE GIFT PACK",methods=["GET", "POST"])
def AMULALMONDCHOCLATEGIFTPACK():
    render_template("AMUL ALMOND CHOCLATE GIFT PACK.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="AMUL ALMOND CHOCLATE GIFT PACK",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("dairy.html",allitems=allitems)
    return render_template("AMUL ALMOND CHOCLATE GIFT PACK.html")





@app.route("/AMUL MILK",methods=["GET", "POST"])
def AMULMILK():
    render_template("AMUL MILK.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="AMUL MILK",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("dairy.html",allitems=allitems)
    return render_template("AMUL MILK.html")


@app.route("/AMUL KOOL",methods=["GET", "POST"])
def AMULKOOL():
    render_template("AMUL KOOL.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="AMUL KOOL",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("dairy.html",allitems=allitems)
    return render_template("AMUL KOOL.html")


@app.route("/AMUL TONE MILK",methods=["GET", "POST"])
def AMULTONEMILK():
    render_template("AMUL TONE MILK.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="AMUL TONE MILK",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("dairy.html",allitems=allitems)
    return render_template("AMUL TONE MILK.html")


@app.route("/AMUL SMALL BUTTERMILK",methods=["GET", "POST"])
def AMULSMALLBUTTERMILK():
    render_template("AMUL SMALL BUTTERMILK.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="AMUL SMALL BUTTERMILK",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("dairy.html",allitems=allitems)
    return render_template("AMUL SMALL BUTTERMILK.html")


@app.route("/AMUL PEDHA",methods=["GET", "POST"])
def AMULPEDHA():
    render_template("AMUL PEDHA.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="AMUL PEDHA",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("dairy.html",allitems=allitems)
    return render_template("AMUL PEDHA.html")


@app.route("/AMUL TONE MILK SMALL PACKET",methods=["GET", "POST"])
def AMULTONEMILKSMALLPACKET():
    render_template("AMUL TONE MILK SMALL PACKET.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="AMUL TONE MILK SMALL PACKET",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("dairy.html",allitems=allitems)
    return render_template("AMUL TONE MILK SMALL PACKET.html")


@app.route("/AMUL VERY SMALL GHEE PACK",methods=["GET", "POST"])
def AMULVERYSMALLGHEEPACK():
    render_template("AMUL VERY SMALL GHEE PACK.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="AMUL VERY SMALL GHEE PACK",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("dairy.html",allitems=allitems)
    return render_template("AMUL VERY SMALL GHEE PACK.html")


@app.route("/AMUL COLD COFFEE",methods=["GET", "POST"])
def AMULCOLDCOFFEE():
    render_template("AMUL COLD COFFEE.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="AMUL COLD COFFEE",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("dairy.html",allitems=allitems)
    return render_template("AMUL COLD COFFEE.html")


@app.route("/AMUL SMALL WHOLE MILK",methods=["GET", "POST"])
def AMULSMALLWHOLEMILK():
    render_template("AMUL SMALL WHOLE MILK.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="AMUL SMALL WHOLE MILK",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("dairy.html",allitems=allitems)
    return render_template("AMUL SMALL WHOLE MILK.html")


@app.route("/AMUL BADAM MILK",methods=["GET", "POST"])
def AMULBADAMMILK():
    render_template("AMUL BADAM MILK.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="AMUL BADAM MILK",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("dairy.html",allitems=allitems)
    return render_template("AMUL BADAM MILK.html")


@app.route("/AMUL ICE CREAM ",methods=["GET", "POST"])
def AMULICECREAM ():
    render_template("AMUL ICE CREAM .html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="AMUL ICE CREAM ",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("dairy.html",allitems=allitems)
    return render_template("AMUL ICE CREAM .html")


@app.route("/DATES",methods=["GET", "POST"])
def DATES():
    render_template("DATES.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="DATES",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("dairy.html",allitems=allitems)
    return render_template("DATES.html")








#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
@app.route("/chicken")
def chicken():
    allitems=Items.query.all()
    return render_template("chicken.html",allitems=allitems)

@app.route("/FEET",methods=["GET", "POST"])
def FEET():
    render_template("FEET.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="FEET",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("chicken.html",allitems=allitems)
    return render_template("FEET.html")


@app.route("/FOREQUARTER",methods=["GET", "POST"])
def FOREQUARTER():
    render_template("FOREQUARTER.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="FOREQUARTER",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("chicken.html",allitems=allitems)
    return render_template("FOREQUARTER.html")


@app.route("/WING",methods=["GET", "POST"])
def WING():
    render_template("WING.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="WING",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("chicken.html",allitems=allitems)
    return render_template("WING.html")


@app.route("/RUMP",methods=["GET", "POST"])
def RUMP():
    render_template("RUMP.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="RUMP",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("chicken.html",allitems=allitems)
    return render_template("RUMP.html")


@app.route("/NECK",methods=["GET", "POST"])
def NECK():
    render_template("NECK.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="NECK",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("chicken.html",allitems=allitems)
    return render_template("NECK.html")


@app.route("/HEART",methods=["GET", "POST"])
def HEART():
    render_template("HEART.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="HEART",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("chicken.html",allitems=allitems)
    return render_template("HEART.html")


@app.route("/LIVER",methods=["GET", "POST"])
def LIVER():
    render_template("LIVER.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="LIVER",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("chicken.html",allitems=allitems)
    return render_template("LIVER.html")


@app.route("/GIZZARD",methods=["GET", "POST"])
def GIZZARD():
    render_template("GIZZARD.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="GIZZARD",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("chicken.html",allitems=allitems)
    return render_template("GIZZARD.html")


@app.route("/TIP",methods=["GET", "POST"])
def TIP():
    render_template("TIP.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="TIP",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("chicken.html",allitems=allitems)
    return render_template("TIP.html")


@app.route("/MID-JOINT WING",methods=["GET", "POST"])
def MIDJOINTWING():
    render_template("MID-JOINT WING.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="MID-JOINT WING",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("chicken.html",allitems=allitems)
    return render_template("MID-JOINT WING.html")


@app.route("/DRUMETTE",methods=["GET", "POST"])
def DRUMETTE():
    render_template("DRUMETTE.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="DRUMETTE",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("chicken.html",allitems=allitems)
    return render_template("DRUMETTE.html")


@app.route("/DRUMSTICK",methods=["GET", "POST"])
def DRUMSTICK():
    render_template("DRUMSTICK.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="DRUMSTICK",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("chicken.html",allitems=allitems)
    return render_template("DRUMSTICK.html")


@app.route("/BREAST",methods=["GET", "POST"])
def BREAST():
    render_template("BREAST.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="BREAST",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("chicken.html",allitems=allitems)
    return render_template("BREAST.html")


@app.route("/BREAST FILLET",methods=["GET", "POST"])
def BREASTFILLET():
    render_template("BREAST FILLET.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="BREAST FILLET",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("chicken.html",allitems=allitems)
    return render_template("BREAST FILLET.html")


@app.route("/HAM",methods=["GET", "POST"])
def HAM():
    render_template("HAM.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="HAM",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("chicken.html",allitems=allitems)
    return render_template("HAM.html")


@app.route("/THIGH",methods=["GET", "POST"])
def THIGH():
    render_template("THIGH.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="THIGH",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("chicken.html",allitems=allitems)
    return render_template("THIGH.html")


@app.route("/HINDQUARTER",methods=["GET", "POST"])
def HINDQUARTER():
    render_template("HINDQUARTER.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="HINDQUARTER",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("chicken.html",allitems=allitems)
    return render_template("HINDQUARTER.html")


@app.route("/CHICKEN FULL BODY",methods=["GET", "POST"])
def FULLBODY():
    render_template("CHICKEN FULL BODY.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="CHICKEN FULL BODY",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("chicken.html",allitems=allitems)
    return render_template("CHICKEN FULL BODY.html")


@app.route("/TURKEY EGG",methods=["GET", "POST"])
def TURKEYEGG():
    render_template("TURKEY EGG.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="TURKEY EGG",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("chicken.html",allitems=allitems)
    return render_template("TURKEY EGG.html")


@app.route("/CHICKEN EGG",methods=["GET", "POST"])
def CHICKENEGG():
    render_template("CHICKEN EGG.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="CHICKEN EGG",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("chicken.html",allitems=allitems)
    return render_template("CHICKEN EGG.html")


@app.route("/QUAIL",methods=["GET", "POST"])
def QUAIL():
    render_template("QUAIL.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="QUAIL",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("chicken.html",allitems=allitems)
    return render_template("QUAIL.html")


@app.route("/GOOSE",methods=["GET", "POST"])
def GOOSE():
    render_template("GOOSE.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="GOOSE",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("chicken.html",allitems=allitems)
    return render_template("GOOSE.html")


@app.route("/PHEASANT",methods=["GET", "POST"])
def PHEASANT():
    render_template("PHEASANT.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="PHEASANT",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("chicken.html",allitems=allitems)
    return render_template("PHEASANT.html")

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
@app.route("/mutton")
def mutton():
    allitems=Items.query.all()
    return render_template("mutton.html",allitems=allitems)

@app.route("/mutton neck",methods=["GET", "POST"])
def neck():
    render_template("mutton neck.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="mutton-neck",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("mutton.html",allitems=allitems)
    return render_template("mutton neck.html")


@app.route("/shoulder",methods=["GET", "POST"])
def shoulder():
    render_template("shoulder.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="mutton-shoulder",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("mutton.html",allitems=allitems)
    return render_template("shoulder.html")


@app.route("/ribs",methods=["GET", "POST"])
def ribs():
    render_template("ribs.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="mutton-ribs",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("mutton.html",allitems=allitems)
    return render_template("ribs.html")

@app.route("/loin",methods=["GET", "POST"])
def loin():
    render_template("loin.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="mutton-loin",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("mutton.html",allitems=allitems)
    return render_template("loin.html")


@app.route("/mutton legs",methods=["GET", "POST"])
def legs():
    render_template("mutton legs.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="mutton-legs",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("mutton.html",allitems=allitems)
    return render_template("mutton legs.html")





@app.route("/kidneys",methods=["GET", "POST"])
def kidneys():
    render_template("kidneys.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="mutton-kidneys",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("mutton.html",allitems=allitems)
    return render_template("kidneys.html")


@app.route("/mutton full body",methods=["GET", "POST"])
def muttonfullbody():
    render_template("mutton full body.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="mutton-full body",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("mutton.html",allitems=allitems)
    return render_template("mutton full body.html")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
@app.route("/fish")
def fish():
    allitems=Items.query.all()
    return render_template("fish.html",allitems=allitems)


@app.route("/head",methods=["GET", "POST"])
def head():
    render_template("head.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="fish-head",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("FISH.html",allitems=allitems)
    return render_template("head.html")


@app.route("/collar",methods=["GET", "POST"])
def collar():
    render_template("collar.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="fish-collar",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("FISH.html",allitems=allitems)
    return render_template("collar.html")


@app.route("/abdomen meat",methods=["GET", "POST"])
def abdomenmeat():
    render_template("abdomen meat.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="fish-abdomen meat",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("FISH.html",allitems=allitems)
    return render_template("abdomen meat.html")


@app.route("/back meat",methods=["GET", "POST"])
def backmeat():
    render_template("back meat.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="fish-back meat",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("FISH.html",allitems=allitems)
    return render_template("back meat.html")


@app.route("/caviar",methods=["GET", "POST"])
def caviar():
    render_template("caviar.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="fish-caviar",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("FISH.html",allitems=allitems)
    return render_template("caviar.html")


@app.route("/tail meat",methods=["GET", "POST"])
def tailmeat():
    render_template("tail meat.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="fish-tail meat",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("FISH.html",allitems=allitems)
    return render_template("tail meat.html")


@app.route("/tail",methods=["GET", "POST"])
def tail():
    render_template("tail.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="fish-tail",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("FISH.html",allitems=allitems)
    return render_template("tail.html")


@app.route("/full body",methods=["GET", "POST"])
def fullbody():
    render_template("full body.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="fish-full body",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("FISH.html",allitems=allitems)
    return render_template("full body.html")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
@app.route("/toiletries")
def toiletries():
    allitems=Items.query.all()
    return render_template("toiletries.html",allitems=allitems)



@app.route("/NIVEA ROSE BATH GEL",methods=["GET", "POST"])
def NIVEAROSEBATHGEL():
    render_template("NIVEA ROSE BATH GEL.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="NIVEA ROSE BATH GEL",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("NIVEA ROSE BATH GEL.html")


@app.route("/NIVEA LIME BATH GEL",methods=["GET", "POST"])
def NIVEALIMEBATHGEL():
    render_template("NIVEA LIME BATH GEL.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="NIVEA LIME BATH GEL",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("NIVEA LIME BATH GEL.html")


@app.route("/NIVEA LAVENDER BATH GEL",methods=["GET", "POST"])
def NIVEALAVENDERBATHGEL():
    render_template("NIVEA LAVENDER BATH GEL.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="NIVEA LAVENDER BATH GEL",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("NIVEA LAVENDER BATH GEL.html")


@app.route("/FIAMA ORANGE BATH GEL",methods=["GET", "POST"])
def FIAMAORANGEBATHGEL():
    render_template("FIAMA ORANGE BATH GEL.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="FIAMA ORANGE BATH GEL",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("FIAMA ORANGE BATH GEL.html")


@app.route("/FIAMA LAVENDER BATH GEL",methods=["GET", "POST"])
def FIAMALAVENDERBATHGEL():
    render_template("FIAMA LAVENDER BATH GEL.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="FIAMA LAVENDER BATH GEL",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("FIAMA LAVENDER BATH GEL.html")


@app.route("/FIAMA BLUE BUTTER GEL",methods=["GET", "POST"])
def FIAMABLUEBUTTERGEL():
    render_template("FIAMA BLUE BUTTER GEL.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="FIAMA BLUE BUTTER GEL",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("FIAMA BLUE BUTTER GEL.html")


@app.route("/GARNIER GREEN BATH GEL",methods=["GET", "POST"])
def GARNIERGREENBATHGEL():
    render_template("GARNIER GREEN BATH GEL.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="GARNIER GREEN BATH GEL",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("GARNIER GREEN BATH GEL.html")


@app.route("/HYGIENE BATH SOAPS",methods=["GET", "POST"])
def HYGIENEBATHSOAPS():
    render_template("HYGIENE BATH SOAPS.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="HYGIENE BATH SOAPS",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("HYGIENE BATH SOAPS.html")


@app.route("/PEARS GLYCERINE SOAP BIG PACK",methods=["GET", "POST"])
def PEARSGLYCERINESOAPBIGPACK():
    render_template("PEARS GLYCERINE SOAP BIG PACK.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="PEARS GLYCERINE SOAP BIG PACK",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("PEARS GLYCERINE SOAP BIG PACK.html")


@app.route("/PEARS GLYCERINE SOAP SMALL PACK",methods=["GET", "POST"])
def PEARSGLYCERINESOAPSMALLPACK():
    render_template("PEARS GLYCERINE SOAP SMALL PACK.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="PEARS GLYCERINE SOAP SMALL PACK",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("PEARS GLYCERINE SOAP SMALL PACK.html")


@app.route("/FIAMA DIFERENT GLYCERINE COMBO PACK",methods=["GET", "POST"])
def FIAMADIFERENTGLYCERINECOMBOPACK():
    render_template("FIAMA DIFERENT GLYCERINE COMBO PACK.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="FIAMA DIFERENT GLYCERINE COMBO PACK",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("FIAMA DIFERENT GLYCERINE COMBO PACK.html")


@app.route("/FIAMA BLACK GLYCERINE COMBO PACK",methods=["GET", "POST"])
def FIAMABLACKGLYCERINECOMBOPACK():
    render_template("FIAMA BLACK GLYCERINE COMBO PACK.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="FIAMA BLACK GLYCERINE COMBO PACK",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("FIAMA BLACK GLYCERINE COMBO PACK.html")


@app.route("/MEDISILK SHAMPOO",methods=["GET", "POST"])
def MEDISILKSHAMPOO():
    render_template("MEDISILK SHAMPOO.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="MEDISILK SHAMPOO",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("MEDISILK SHAMPOO.html")


@app.route("/CINTHOL COMBO PACK",methods=["GET", "POST"])
def CINTHOLCOMBOPACK():
    render_template("CINTHOL COMBO PACK.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="CINTHOL COMBO PACK",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("CINTHOL COMBO PACK.html")


@app.route("/SANTOOR REGULAR BIG PACK",methods=["GET", "POST"])
def SANTOORREGULARBIGPACK():
    render_template("SANTOOR REGULAR BIG PACK.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="SANTOOR REGULAR BIG PACK",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("SANTOOR REGULAR BIG PACK.html")


@app.route("/SANTOOR GOLD PACK",methods=["GET", "POST"])
def SANTOORGOLDPACK():
    render_template("SANTOOR GOLD PACK.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="SANTOOR GOLD PACK",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("SANTOOR GOLD PACK.html")


@app.route("/SANTOOR WHITE BIG PACK",methods=["GET", "POST"])
def SANTOORWHITEBIGPACK():
    render_template("SANTOOR WHITE BIG PACK.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="SANTOOR WHITE BIG PACK",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("SANTOOR WHITE BIG PACK.html")


@app.route("/SANTOOR REGULAR SMALL",methods=["GET", "POST"])
def SANTOORREGULARSMALL():
    render_template("SANTOOR REGULAR SMALL.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="SANTOOR REGULAR SMALL",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("SANTOOR REGULAR SMALL.html")


@app.route("/SANTOOR WHITE GLYCERINE",methods=["GET", "POST"])
def SANTOORWHITEGLYCERINE():
    render_template("SANTOOR WHITE GLYCERINE.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="SANTOOR WHITE GLYCERINE",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("SANTOOR WHITE GLYCERINE.html")


@app.route("/SANTOOR GOLD BIG PACK",methods=["GET", "POST"])
def SANTOORGOLDBIGPACK():
    render_template("SANTOOR GOLD BIG PACK.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="SANTOOR GOLD BIG PACK",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("SANTOOR GOLD BIG PACK.html")


@app.route("/CHARM TEA SHAMPOO",methods=["GET", "POST"])
def CHARMTEASHAMPOO():
    render_template("CHARM TEA SHAMPOO.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="CHARM TEA SHAMPOO",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("CHARM TEA SHAMPOO.html")


@app.route("/MEDIMIX GREEN SMALL PACKMEDIMIX GREEN GLYCERINE",methods=["GET", "POST"])
def MEDIMIXGREENSMALLPACKMEDIMIXGREENGLYCERINE():
    render_template("MEDIMIX GREEN SMALL PACKMEDIMIX GREEN GLYCERINE.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="MEDIMIX GREEN SMALL PACKMEDIMIX GREEN GLYCERINE",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("MEDIMIX GREEN SMALL PACKMEDIMIX GREEN GLYCERINE.html")


@app.route("/PEARS BLUE GLYCERINE SOAP BIG",methods=["GET", "POST"])
def PEARSBLUEGLYCERINESOAPBIG():
    render_template("PEARS BLUE GLYCERINE SOAP BIG.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="PEARS BLUE GLYCERINE SOAP BIG",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("PEARS BLUE GLYCERINE SOAP BIG.html")


@app.route("/MEDIMIX BLUE GLYCERINE SOAP SMALL",methods=["GET", "POST"])
def MEDIMIXBLUEGLYCERINESOAPSMALL():
    render_template("MEDIMIX BLUE GLYCERINE SOAP SMALL.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="MEDIMIX BLUE GLYCERINE SOAP SMALL",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("MEDIMIX BLUE GLYCERINE SOAP SMALL.html")


@app.route("/HIMALAYA SANDAL BIG",methods=["GET", "POST"])
def HIMALAYASANDALBIG():
    render_template("HIMALAYA SANDAL BIG.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="HIMALAYA SANDAL BIG",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("HIMALAYA SANDAL BIG.html")


@app.route("/DETTOL SMALL BLUE",methods=["GET", "POST"])
def DETTOLSMALLBLUE():
    render_template("DETTOL SMALL BLUE.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="DETTOL SMALL BLUE",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("DETTOL SMALL BLUE.html")


@app.route("/DETTOL SMALL GREEN",methods=["GET", "POST"])
def DETTOLSMALLGREEN():
    render_template("DETTOL SMALL GREEN.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="DETTOL SMALL GREEN",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("DETTOL SMALL GREEN.html")


@app.route("/CINTHOL YELLOW",methods=["GET", "POST"])
def CINTHOLYELLOW():
    render_template("CINTHOL YELLOW.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="CINTHOL YELLOW",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("CINTHOL YELLOW.html")


@app.route("/CINTHOL RED",methods=["GET", "POST"])
def CINTHOLRED():
    render_template("CINTHOL RED.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="CINTHOL RED",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("CINTHOL RED.html")


@app.route("/AYURVEDIC SOAP",methods=["GET", "POST"])
def AYURVEDICSOAP():
    render_template("AYURVEDIC SOAP.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="AYURVEDIC SOAP",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("AYURVEDIC SOAP.html")


@app.route("/PEARS YELLOW GLYCERINE",methods=["GET", "POST"])
def PEARSYELLOWGLYCERINE():
    render_template("PEARS YELLOW GLYCERINE.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="PEARS YELLOW GLYCERINE",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("PEARS YELLOW GLYCERINE.html")


@app.route("/PEARS BLUE GLYCERINE SMALL",methods=["GET", "POST"])
def PEARSBLUEGLYCERINESMALL():
    render_template("PEARS BLUE GLYCERINE SMALL.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="PEARS BLUE GLYCERINE SMALL",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("PEARS BLUE GLYCERINE SMALL.html")


@app.route("/SANTOOR WHITE 1 SOAP",methods=["GET", "POST"])
def SANTOORWHITE1SOAP():
    render_template("SANTOOR WHITE 1 SOAP.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="SANTOOR WHITE 1 SOAP",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("SANTOOR WHITE 1 SOAP.html")


@app.route("/GLYCERINE NATURAL SOAP",methods=["GET", "POST"])
def GLYCERINENATURALSOAP():
    render_template("GLYCERINE NATURAL SOAP.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="GLYCERINE NATURAL SOAP",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("GLYCERINE NATURAL SOAP.html")


@app.route("/LIRIL SOAP",methods=["GET", "POST"])
def LIRILSOAP():
    render_template("LIRIL SOAP.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="LIRIL SOAP",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("LIRIL SOAP.html")


@app.route("/DOVE SMALL",methods=["GET", "POST"])
def DOVESMALL():
    render_template("DOVE SMALL.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="DOVE SMALL",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("DOVE SMALL.html")


@app.route("/DETTOL GREEN SMALL",methods=["GET", "POST"])
def DETTOLGREENSMALL():
    render_template("DETTOL GREEN SMALL.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="DETTOL GREEN SMALL",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("DETTOL GREEN SMALL.html")


@app.route("/PEARS GREEN GLYCERINE",methods=["GET", "POST"])
def PEARSGREENGLYCERINE():
    render_template("PEARS GREEN GLYCERINE.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="PEARS GREEN GLYCERINE",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("PEARS GREEN GLYCERINE.html")


@app.route("/AWS SOAP",methods=["GET", "POST"])
def AWSSOAP():
    render_template("AWS SOAP.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="AWS SOAP",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("AWS SOAP.html")


@app.route("/SAVLON SOAP",methods=["GET", "POST"])
def SAVLONSOAP():
    render_template("SAVLON SOAP.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="SAVLON SOAP",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("SAVLON SOAP.html")


@app.route("/LUX BLUE SOAP",methods=["GET", "POST"])
def LUXBLUESOAP():
    render_template("LUX BLUE SOAP.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="LUX BLUE SOAP",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("LUX BLUE SOAP.html")





@app.route("/DOVE",methods=["GET", "POST"])
def DOVE():
    render_template("DOVE.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="DOVE",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("DOVE.html")


@app.route("/LUX GREEN",methods=["GET", "POST"])
def LUXGREEN():
    render_template("LUX GREEN.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="LUX GREEN",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("LUX GREEN.html")


@app.route("/LUX ROSE SOAP",methods=["GET", "POST"])
def LUXROSESOAP():
    render_template("LUX ROSE SOAP.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="LUX ROSE SOAP",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("LUX ROSE SOAP.html")


@app.route("/SANTOOR REGULAR BIG",methods=["GET", "POST"])
def SANTOORREGULARBIG():
    render_template("SANTOOR REGULAR BIG.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="SANTOOR REGULAR BIG",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("SANTOOR REGULAR BIG.html")


@app.route("/HIMALAYA SOAP",methods=["GET", "POST"])
def HIMALAYASOAP():
    render_template("HIMALAYA SOAP.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="HIMALAYA SOAP",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("HIMALAYA SOAP.html")


@app.route("/DOVE REGULAR BIG PACK",methods=["GET", "POST"])
def DOVEREGULARBIGPACK():
    render_template("DOVE REGULAR BIG PACK.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="DOVE REGULAR BIG PACK",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("DOVE REGULAR BIG PACK.html")


@app.route("/LUX GOLD",methods=["GET", "POST"])
def LUXGOLD():
    render_template("LUX GOLD.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="LUX GOLD",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("LUX GOLD.html")


@app.route("/LIFEBOY TURMERIC SOAP",methods=["GET", "POST"])
def LIFEBOYTURMERICSOAP():
    render_template("LIFEBOY TURMERIC SOAP.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="LIFEBOY TURMERIC SOAP",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("LIFEBOY TURMERIC SOAP.html")


@app.route("/PALM OLIVE CHERRY SHAMPOO",methods=["GET", "POST"])
def PALMOLIVECHERRYSHAMPOO():
    render_template("PALM OLIVE CHERRY SHAMPOO.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="PALM OLIVE CHERRY SHAMPOO",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("PALM OLIVE CHERRY SHAMPOO.html")


@app.route("/PALM OLIVE GOLD SHAMPOO",methods=["GET", "POST"])
def PALMOLIVEGOLDSHAMPOO():
    render_template("PALM OLIVE GOLD SHAMPOO.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="PALM OLIVE GOLD SHAMPOO",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("PALM OLIVE GOLD SHAMPOO.html")


@app.route("/SANTOOR GOLD HANDWASH",methods=["GET", "POST"])
def SANTOORGOLDHANDWASH():
    render_template("SANTOOR GOLD HANDWASH.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="SANTOOR GOLD HANDWASH",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("SANTOOR GOLD HANDWASH.html")


@app.route("/LIFEBOY HANDPUMP",methods=["GET", "POST"])
def LIFEBOYHANDPUMP():
    render_template("LIFEBOY HANDPUMP.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="LIFEBOY HANDPUMP",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("LIFEBOY HANDPUMP.html")


@app.route("/HYGIENE HANDWASH",methods=["GET", "POST"])
def HYGIENEHANDWASH():
    render_template("HYGIENE HANDWASH.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="HYGIENE HANDWASH",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("HYGIENE HANDWASH.html")


@app.route("/AYUSH SOAP",methods=["GET", "POST"])
def AYUSHSOAP():
    render_template("AYUSH SOAP.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="AYUSH SOAP",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("AYUSH SOAP.html")


@app.route("/ROSE BATH POWDER",methods=["GET", "POST"])
def ROSEBATHPOWDER():
    render_template("ROSE BATH POWDER.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="ROSE BATH POWDER",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("ROSE BATH POWDER.html")


@app.route("/ENRIQUE LIME HANDPUMP",methods=["GET", "POST"])
def ENRIQUELIMEHANDPUMP():
    render_template("ENRIQUE LIME HANDPUMP.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="ENRIQUE LIME HANDPUMP",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("ENRIQUE LIME HANDPUMP.html")


@app.route("/ENRIQUE ROSE HANDPUMP",methods=["GET", "POST"])
def ENRIQUEROSEHANDPUMP():
    render_template("ENRIQUE ROSE HANDPUMP.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="ENRIQUE ROSE HANDPUMP",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("ENRIQUE ROSE HANDPUMP.html")


@app.route("/SANTOOR SANDAL HANDPUMP",methods=["GET", "POST"])
def SANTOORSANDALHANDPUMP():
    render_template("SANTOOR SANDAL HANDPUMP.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="SANTOOR SANDAL HANDPUMP",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("SANTOOR SANDAL HANDPUMP.html")


@app.route("/SANTOOR ROSE HANDPUMP",methods=["GET", "POST"])
def SANTOORROSEHANDPUMP():
    render_template("SANTOOR ROSE HANDPUMP.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="SANTOOR ROSE HANDPUMP",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("SANTOOR ROSE HANDPUMP.html")


@app.route("/KEIN HAND SANITIZER",methods=["GET", "POST"])
def KEINHANDSANITIZER():
    render_template("KEIN HAND SANITIZER.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="KEIN HAND SANITIZER",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("KEIN HAND SANITIZER.html")


@app.route("/DETTOL HANDWIPES",methods=["GET", "POST"])
def DETTOLHANDWIPES():
    render_template("DETTOL HANDWIPES.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="DETTOL HANDWIPES",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("DETTOL HANDWIPES.html")


@app.route("/HYGEINE SANITIZER",methods=["GET", "POST"])
def HYGEINESANITIZER():
    render_template("HYGEINE SANITIZER.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="HYGEINE SANITIZER",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("HYGEINE SANITIZER.html")


@app.route("/LIFEBOY HANDSANITIZER",methods=["GET", "POST"])
def LIFEBOYHANDSANITIZER():
    render_template("LIFEBOY HANDSANITIZER.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="LIFEBOY HANDSANITIZER",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("LIFEBOY HANDSANITIZER.html")


@app.route("/LIFEBOY HANDS SANITIZER REFILL LIME",methods=["GET", "POST"])
def LIFEBOYHANDSSANITIZERREFILLLIME():
    render_template("LIFEBOY HANDS SANITIZER REFILL LIME.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="LIFEBOY HANDS SANITIZER REFILL LIME",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("LIFEBOY HANDS SANITIZER REFILL LIME.html")


@app.route("/LIFEBOY HANDS SANITIZER REFILL ROSE",methods=["GET", "POST"])
def LIFEBOYHANDSSANITIZERREFILLROSE():
    render_template("LIFEBOY HANDS SANITIZER REFILL ROSE.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="LIFEBOY HANDS SANITIZER REFILL ROSE",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("LIFEBOY HANDS SANITIZER REFILL ROSE.html")


@app.route("/FRUIT BASKET",methods=["GET", "POST"])
def FRUITBASKET():
    render_template("FRUIT BASKET.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="FRUIT BASKET",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("FRUIT BASKET.html")


@app.route("/AGARBATHI CYCLE SANDAL",methods=["GET", "POST"])
def AGARBATHICYCLESANDAL():
    render_template("AGARBATHI CYCLE SANDAL.html")
    if request.method=="POST":
        Quantity=request.form["tot_pin_requested"]
        Subtotal=request.form["tot_amount"]
        item=Items(Product="AGARBATHI CYCLE SANDAL",Quantity=Quantity,Subtotal=Subtotal)
        db.session.add(item)
        db.session.commit()
        allitems=Items.query.all()
        return render_template("toiletries.html",allitems=allitems)
    return render_template("AGARBATHI CYCLE SANDAL.html")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
@app.route("/payment",methods=["GET","POST"])
def payment():
    if request.method=="POST":
        fname=request.form["firstname"]
        email=request.form["email"]
        Mobileno=request.form["Mobileno"]
        address=request.form["address"]
        state=request.form["state"]
        mail.send_message("EnPassant delivery",
            sender=params["user-id"],
            recipients=[email],
            body="hello "+ fname +", \nyour ordered items will be delivered to the adress (" +address+","+state+")"+" ,If there is any problem ,we will contact you through your number "+Mobileno+"\n Your delivery will be given within 2 working days, we shall call you a day before your delivery reaches you."+"\nIf the given location is less than 500m to our office,you will not be charged for delivery...else,there will be delivery charges of 30 rupees \n\nThanks for choosing us :)"+"\n-EnPassant" 
        ) 
        return redirect("/cod")
    return render_template("payment.html")

@app.route("/cod")
def cod():
    return render_template("cod.html")


@app.route("/removefruit/<string:Product>",methods=["GET","POST"])
def removefruit(Product):
    item=Items.query.filter_by(Product=Product).first()
    db.session.delete(item)
    db.session.commit()
    return redirect("/fruitstore")

@app.route("/removebakery/<string:Product>",methods=["GET","POST"])
def removebakery(Product):
    item=Items.query.filter_by(Product=Product).first()
    db.session.delete(item)
    db.session.commit()
    return redirect("/bakery")

@app.route("/removevegetable/<string:Product>",methods=["GET","POST"])
def removevegetable(Product):
    item=Items.query.filter_by(Product=Product).first()
    db.session.delete(item)
    db.session.commit()
    return redirect("/vegetablestore")

@app.route("/removesnacks/<string:Product>",methods=["GET","POST"])
def removesnacks(Product):
    item=Items.query.filter_by(Product=Product).first()
    db.session.delete(item)
    db.session.commit()
    return redirect("/snacks")

@app.route("/removedairy/<string:Product>",methods=["GET","POST"])
def removedairy(Product):
    item=Items.query.filter_by(Product=Product).first()
    db.session.delete(item)
    db.session.commit()
    return redirect("/dairy")

@app.route("/removetoiletries/<string:Product>",methods=["GET","POST"])
def removetoiletries(Product):
    item=Items.query.filter_by(Product=Product).first()
    db.session.delete(item)
    db.session.commit()
    return redirect("/toiletries")

@app.route("/removechicken/<string:Product>",methods=["GET","POST"])
def removechicken(Product):
    item=Items.query.filter_by(Product=Product).first()
    db.session.delete(item)
    db.session.commit()
    return redirect("/chicken")

@app.route("/removemutton/<string:Product>",methods=["GET","POST"])
def removemutton(Product):
    item=Items.query.filter_by(Product=Product).first()
    db.session.delete(item)
    db.session.commit()
    return redirect("/mutton")

@app.route("/removefish/<string:Product>",methods=["GET","POST"])
def removefish(Product):
    item=Items.query.filter_by(Product=Product).first()
    db.session.delete(item)
    db.session.commit()
    return redirect("/fish")

if __name__ == "__main__":
    app.run(debug=True,port=8000)
