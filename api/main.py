from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/reinforcements/<id>', methods=['GET'])
def get_reinforcement(id):
    # Get the current time
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Print the <id> and the time
    print(f"ID: {id}, Time: {current_time}")
    
    # Return a response
    return f"Received request for reinforcement ID: {id} at {current_time}"

if __name__ == '__main__':
    app.run(port=80)
