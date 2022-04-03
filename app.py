import json
from flight_query import FlightQueryService
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/', methods=['GET'])
def query_records():
    query = request.args.get('query').split(',')
    query = [query[i:i+2] for i in range(0, len(query), 2)]


    fqs = FlightQueryService()
    try:
        result = fqs.findFlightPath(query)
    except Exception as e:
        return str(e)
    
    return str(result)

app.run()