from flask import Flask, render_template, request, jsonify
from sqlalchemy import create_engine, text
import os

app = Flask(__name__)

# Import the database URI from init_db module
from init_db import DATABASE_URI

engine = create_engine(DATABASE_URI)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/execute', methods=['POST'])
def execute():
    sql_query = request.form.get('query')
    try:
        with engine.connect() as connection:
            result = connection.execute(text(sql_query))
            data = [dict(row._mapping) for row in result]  # Ensures row is converted to a dictionary
            columns = result.keys()
        return jsonify({"columns": list(columns), "data": data})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
