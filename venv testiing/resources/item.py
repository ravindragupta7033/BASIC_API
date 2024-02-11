from flask import Flask ,request
import uuid
from db import items
from flask.views import MethodView
from flask_smorest import Blueprint


app=Flask(__name__)  

blp=Blueprint("items",__name__,description="operations on items")


  
@blp.route("/item") 
class Item(MethodView):
   def get(self):
      id=request.args.get('id')
      if id==None:
         return {"items":items}
      id=request.args.get('id')
      try:
         return items[id]
      except KeyError:
         return {"massage":"item does't found"} 
  

   def put(self):
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

   def post(self):
    request_data=request.get_json()
    if "name" not in request_data or "price" not in request_data:
        return {"massage":" 'name' and 'price' must included in body"}
    items[uuid.uuid4().hex]=request_data    
    return {"massage":"item added succesfully"}  

   def delete(self):
     
    item_id=request.args.get('id')
    if item_id ==None:
      return{"massage":"given id doesn't found"}
    
    if item_id in items:
        items.pop(item_id)
        return {"massage":"item removed succesfully"}
    return {"message":"item not found"}

app.run(port=5000)

 



