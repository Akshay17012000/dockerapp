from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
import pymongo

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')

try:
    client = pymongo.MongoClient(MONGO_URI)
    db = client.test
    collection = db['flask']
    print("Database connection successful!") # Added line
except pymongo.errors.ConnectionFailure as e:
    print(f"Could not connect to MongoDB: {e}")
    exit(1) # Exit if connection fails, preventing further execution.

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    try:
        form_data = dict(request.json)
        print(f"Received JSON data: {form_data}") # Add this line
        collection.insert_one(form_data)
        return 'Data submitted successfully!'
    except Exception as e:
        print(f"Error submitting data: {e}")
        return jsonify({'error': 'An error occurred during submission.'}), 500

@app.route('/view')
def view():
    data = collection.find()
    data = list(data)

    for item in data:
        print(item)
        del item['_id']

    data = {
        'data': data
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)

