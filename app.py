from flask import Flask, request, jsonify

app = Flask(__name__)

items = {}

@app.post("/items/")
def create_item():
    item = request.get_json()

    item_id = len(items)
    items[item_id] = item

    return jsonify({
        "item_id": item_id,
        "item": item,
        "status": "created"
    }), 201


@app.delete("/items/<int:item_id>")
def delete_item(item_id):
    if item_id in items:
        del items[item_id]
        return jsonify({
            "item_id": item_id,
            "status": "deleted"
        })

    return jsonify({"error": "Item not found"}), 404


@app.put("/items/<int:item_id>")
def update_item(item_id):
    item = request.get_json()

    if item_id in items:
        items[item_id] = item
        return jsonify({
            "item_id": item_id,
            "item": item,
            "status": "updated"
        })

    return jsonify({"error": "Item not found"}), 404


@app.get("/items/<int:item_id>")
def read_item(item_id):
    if item_id in items:
        return jsonify({
            "item_id": item_id,
            "item": items[item_id]
        })

    return jsonify({"error": "Item not found"}), 404


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run(debug=True)
