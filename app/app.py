from flask import Flask, request, Response, jsonify
import json
from utils import valid_date, build_summary

def create_app():
    '''
    Construct app
    '''
    app = Flask(__name__)

    @app.route('/')
    def home():
        return "ok"
    
    @app.route('/get_summary', methods=["GET"])
    def get_summary():
        date = request.args.get('date')
        if valid_date(date):
            return jsonify(build_summary(date))
        
        else:
            return Response("Date is in the wrong format, please retry with YYYY-MM-DD", status=400)

    return app


if __name__ == "__main__":
    app = create_app()