import flask
from flask_expects_json import expects_json, expects_parameter


if __name__ == "__main__":

    app = flask.Flask(__name__)

    body_schema = {
        "type": "object",
        "properties": {
            "price": {"type": "number"},
            "name": {"type": "string"},
        },
        "required": ["price"]
    }

    parameter_name_schema = {
        "type": "string",
        "enum": ["Barak","Omri"]
    }

    parameter_last_schema = {
        "type": "string",
        "enum": ["Rozenkvit","Levi"]
    }

    @app.route('/schema')
    @expects_parameter(schema=parameter_name_schema, name="name", required=False)
    @expects_parameter(schema=parameter_last_schema, name="last", required=False)
    @expects_json(schema=body_schema)

    def schema():
        i=0
    
        return {'happy':1}
    
    client = app.test_client()
    response = client.get('/schema?age=1',
                            data='{"name": "Eggs", "price": 34.99}',
                            content_type='application/json')
    

    print(response)