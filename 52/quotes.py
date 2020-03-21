from flask import Flask, jsonify, abort, request

app = Flask(__name__)

quotes = [
    {
        "id": 1,
        "quote": "I'm gonna make him an offer he can't refuse.",
        "movie": "The Godfather",
    },
    {
        "id": 2,
        "quote": "Get to the choppa!",
        "movie": "Predator",
    },
    {
        "id": 3,
        "quote": "Nobody's gonna hurt anybody. We're gonna be like three little Fonzies here.",  # noqa E501
        "movie": "Pulp Fiction",
    },
]

quotes = { "id": { 
                  1: { 
                      "quote": "I'm gonna make him an offer he can't refuse.",
                      "movie": "The Godfather"
                      }, 
                  2: {
                      "quote": "Get to the choppa!",
                      "movie": "Predator"
                      }
                  }
         }


def _get_quote(qid):
    """Recommended helper"""
    data = {}
    data["quotes"] = [ 
            quote 
            for quote in quotes 
            if qid in quote.values() 
            ]
    return jsonify(data)


def _quote_exists(existing_quote):
    """Recommended helper"""
    return any(
            existing_quote == quote["id"] 
            for quote in quotes
            ) 

@app.route('/api/quotes', methods=['GET'])
def get_quotes():
    data = {}
    data["quotes"] = quotes
    return jsonify(data)

@app.route('/api/quotes/<int:qid>', methods=['GET'])
def get_quote(qid):
    if not _quote_exists(qid):
        abort(404)
    else:
        return _get_quote(qid) 

@app.route('/api/quotes', methods=['POST'])
def create_quote():
    max_id = max( [quote["id"] for quote in quotes] )
    data = request.get_json()
    if ( not all 
            (
              key in data.keys() 
              for key in ["movie", "quote"] 
              )
        ) or (
              any([data["movie"] in m["movie"] and 
                   data["quote"] in m["quote"] 
                   for m in quotes 
                  ])
        ):
        abort(400)

    new_id = max_id + 1
    data["id"] = new_id
    quotes.append(data)
    data = {"quote": data }
    return jsonify(data), 201

@app.route('/api/quotes/<int:qid>', methods=['PUT'])
def update_quote(qid):
    data = request.get_json()
    if not data:
        abort(400)
    elif not _quote_exists(qid):
        abort(404)
    for quote in quotes:
        if quote["id"] == qid:
            quote.update(data)
            updated_quote = quote
    return jsonify({"quote":updated_quote})

@app.route('/api/quotes/<int:qid>', methods=['DELETE'])
def delete_quote(qid):
    data = request.get_json()
    if not _quote_exists(qid):
        abort(404)
    for idx, quote in enumerate(quotes):
        if quote["id"] == qid:
            del quotes[idx]
    return jsonify({}), 204
     