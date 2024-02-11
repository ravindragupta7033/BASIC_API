from flask import Flask,request,jsonify

from db import items
import uuid

app=Flask(__name__)


         #get all items of cafe http://127.0.0.1:5000/grt-items

@app.get('/items')
def get_all_items():
    return {"items":items}     # return {"items":list(items.values())}[for get only values not id]


         #get a single item from cafe items http://127.0.0.1:5000/items/___
@app.get('/item')
def get_item():
    id=request.args.get('id')
    try:
       return items[id]
    except KeyError:
       return {"massage":"item does't found"} 
    

                                              #create single item in items of  menu
@app.post('/item')
def add_item():
    request_data=request.get_json()
    if "name" not in request_data or "price" not in request_data:
        return {"massage":" 'name' and 'price' must included in body"}
    items[uuid.uuid4().hex]=request_data    
    return {"massage":"item added succesfully"}  

# other way to item in items
# @app.post('/item')
# def create_item():
#       object=request.get_json()
#       key=uuid.uuid4().hex
#       value={
#           "name":object["name"],
#           "price":object["price"]
#       }
#       items[key]=value

#       print("the item is: ",items[key])
#     #   items[uuid.uuid4().hex]=request.get_json()
#       return {"massage":"item added successfully"}

                               #update the item in menu by using put methods http://127.0.0.1:5000/______

@app.put('/item')
def update_item():
     id=request.args.get('id')
     if id ==None:
      return{"massage":"given id doesn't found"}
     

     if id in items.keys():
        request_data=request.get_json()
        if "name" not in request_data or "price" not in request_data:
           return {"massage":" 'name' and 'price' must included in body"}
        items[id] =request_data
        return {"massage":"item updated succesfully"}
     return {"massage":"invalid id's"}
#delete the item from menu

@app.delete('/item')
def delete_item():
     
    item_id=request.args.get('id')
    if item_id ==None:
      return{"massage":"given id doesn't found"}
    
    if item_id in items:
        items.pop(item_id)
        return {"massage":"item removed succesfully"}
    return {"message":"item not found"}

app.run(port=5000)