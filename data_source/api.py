from flask import Flask, jsonify

app = Flask(__name__)

metrics_data = {
	"object1": {
		"size" : 10,
		"weight": 5,
		"status" : "0",
		"quantity": 20
		},
	"object2": {
                "size" : 8,
                "weight": 3,
                "status" : "1",
                "quantity": 15
                },
	"object3": {
                "size" : 12,
                "weight": 7,
                "status" : "2",
                "quantity": 25
                }
}

@app.route("/get_metrics/<string:object_id>", methods=["GET"])

def get_metrics(object_id):
	if object_id in metrics_data:
		return jsonify(metrics_data[object_id])
	else:
		return jsonify({"error":"Object not found"}), 404

if __name__ == "__main__":
	app.run(debug=True, port=9001)


