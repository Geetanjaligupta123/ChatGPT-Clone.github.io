from flask import Flask,render_template,jsonify,request
from flask_pymongo import PyMongo
app = Flask(__name__)
mongo = PyMongo(app)


app.config["MONGO_URI"] = "mongodb+srv://shravangupta563:Sapna@12@cluster0.mdmpayk.mongodb.net/chatgpt1"

@app.route('/')
def home():
    chats = mongo.db.chats.find({})
    myChats = [chat for chat in chats]
    print(chats)
    return render_template("index.html",context = {"myChats": myChats})


@app.route('/api',methods=["GET","POST"])
def qa():
    if request.method == "POST":
        print(request.json)
        question = request.json.get("question")
        chat = mongo.db.chats.find_one({"question":question})
        print(chat)
        if chat:
            data = {"result":f"{chat.answer}"}
            return jsonify(data)
        else:
            
        data ={"result":f"Answer of {question} "}
        mongo.db.chats.insert_one{"question":question,"answer":"Answer from openAi for {question}"}
        return jsonify(data)
    return render_template("index.html")
app.run(debug=True)