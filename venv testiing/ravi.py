   
from flask import Flask,jsonify,request

@app.post('/item')
def create_item():
      object=request.get_json()
      key=uuid.uuid4().hex
      value={
          "name":object["name"],
          "price":object["price"]
      }
      items[key]=value

      print("the item is: ",items[key])
    #   items[uuid.uuid4().hex]=request.get_json()
      return {"massage":"item added successfully"}
       

@app.post('/item')
def create_item():
      object=request.get_json
      key=uuid.uuid4().hex
      value={
            "name":object["name"],
            "price":object["price"]
      }
      items[key]=Value
      print("the item is:",items[key])