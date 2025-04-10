### Put and delete - HTTP verbs
### Working with API's - Json
### Flask API

from flask import Flask, jsonify, request

app = Flask(__name__)

# Initial data with my todo list

items = [
    {"id": 1, "name":"Item1", "description1":"This is item1"},
    {"id": 2, "name":"Item2", "description":"This is item2"}
]

@app.route('/')
def home():
    return "Welcome to the SAmple TO DO List App!"

## Get : Retrive all the items in the list

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

## Get : Retrive a specific item by id

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id']== item_id), None)
    if item is None:
        return jsonify({'Error':'Item not found!'})
    return jsonify(item)

## Post : Create a new task

@app.route('/items', methods = ['POST'])
def create_item():
    if not request.json or 'name' not in request.json:
        return jsonify({'Erroe':'Item not found'})
    new_item = {
        'id' : items[-1]['id']+1 if items else 1,
        'name' : request.json['name'],
        'decription' : request.json['description']
    }

    items.append(new_item)
    return jsonify(new_item)

## PUT : update an existing item

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({'Error':'Item not found!'})
    item['name'] = request.json.get('name', item['name'])
    item['description'] = request.json.get('description', item['description'])
    return jsonify(item)

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({'result':'Item Deleted!'})

if __name__ == '__main__':
    app.run(debug=True)
