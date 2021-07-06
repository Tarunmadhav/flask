from flask import Flask,jsonify,request
app=Flask(__name__)
contacts=[
    {
        "id":1,
        "Name":'Raj',
        'Contact':'8824554211' ,
        "done":False,
    },
    {
       "id":2,
        "Name":'michel',
        'Contact': '98478924534',
        "done":False,
    },
]

@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"Error",
            "message":"Plz Provide Some Data To Add"
        },400)
    contact={
        'id': contacts[-1]['id'] + 1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact', ""),
        'done': False

        }
    contacts.append(contact)
    return jsonify({
            "status":"Success",
            "message":"task added successfully"
        })

if (__name__=="__main__"):
    app.run(debug=True)