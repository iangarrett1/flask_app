from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [
	{

		'name': "Ian's store",
		'items': [ 
			{
			'name': 'My Item',
			'price': 15.99
			}
		]	
	}
]

@app.route('/')
def home():
	return render_template('index.html')

#Post /store data: {name:}
@app.route('/store', methods=['POST']) # http://www.google.com/
def create_store():
	request_data = request.get_json()
	new_store = {
		'name': request_data['name'],
		'items': []
	}
	stores.append(new_store)
	return jsonify(new_store)

# GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
	# Iterate over stores
	for store in stores:
		if store['name'] ==name:
			return jsonify(store)
	return jsonify({'message': 'store not found'})
	#if the store name matches, return it
	#if none moatch, return an error message

	pass

# GET /store/
@app.route('/store')
def get_stores():
	return jsonify({'stores': stores})

#Post /store data: {name:}
@app.route('/store/<string:name>/item', methods=['POST']) # http://www.google.com/
def create_item_in_store(name):
	request_data = request.get_json()
	for store in stores:
		if store['name'] == name:
			new_item = {
				'name': request_data['name'],
				'price': request_data['price']
			}
			store['items'].append(new_item)
			return jsonify(new_item)
		return jsonify({'message': 'store not found'})

# GET /store/<string:name>
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
		for store in stores:
			if store['name'] ==name:
				return jsonify({'items': store['items']})
		return jsonify({'message': 'store not found'})

app.run(port=5000)

