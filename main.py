import sqlite3

def get_user_data(username):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    query = f"SELECT * FROM users WHERE username = '{username}';"
    cursor.execute(query)
    
    user_data = cursor.fetchall()
    conn.close()
    
    return user_data

# Example usage
username = input("Enter the username: ")
user_data = get_user_data(username)
print("User Data:", user_data)


from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    user_input = request.args.get('input')
    return f"<html><body><h1>{user_input}</h1></body></html>"

if __name__ == '__main__':
    app.run(debug=True)
