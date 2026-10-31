from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

def query_database(query):
    conn = sqlite3.connect('nba.db')
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    return rows

@app.route('/')
def home():
    return render_template_string('''
        <h1>Query the Database</h1>
        <form action="/query" method="post">
            SQL Query: <input type="text" name="query"><br>
            <input type="submit" value="Submit">
        </form>
    ''')

@app.route('/query', methods=['POST'])
def query():
    query = request.form['query']
    try:
        results = query_database(query)
        return render_template_string('''
            <h1>Query Results</h1>
            <table border="1">
                {% for row in results %}
                <tr>
                    {% for col in row %}
                    <td>{{ col }}</td>
                    {% endfor %}
                </tr>
                {% endfor %}
            </table>
            <br>
            <a href="/">Go Back</a>
        ''', results=results)
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == '__main__':
    app.run(debug=True)