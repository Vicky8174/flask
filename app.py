from flask import Flask
import os
import datetime
import psutil

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Set full name
    full_name = "Vicky Jha"

    # Get system username safely
    system_username = os.getenv("USER") or os.getenv("USERNAME") or "Unknown"

    # Get server time in IST
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)

    # Get top 10 processes
    top_output = "\n".join([f"{p.info['pid']} {p.info['name']}" for p in psutil.process_iter(['pid', 'name'])][:10])

    # Format the response
    return f"""
    <h1>System Information</h1>
    <p><b>Name:</b> {full_name}</p>
    <p><b>Username:</b> {system_username}</p>
    <p><b>Server Time (IST):</b> {ist_time.strftime("%Y-%m-%d %H:%M:%S")}</p>
    <h2>Top Processes:</h2>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
