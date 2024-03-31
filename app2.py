# flask --app app2 run
from flask import Flask, request
import subprocess

app = Flask(__name__)

# уязвимость OS Command Injection
# @app.route("/dns")
# def dns_lookup():
#     hostname = request.values.get("hostname")
#     cmd = "nslookup " + hostname
#     output = subprocess.check_output(cmd, shell=True, text=True)

#     return output


# решение против вышеуказанной уязвимости
@app.route("/dns")
def dns_lookup():
    hostname = request.values.get("hostname")
    cmd = ["nslookup", hostname]
    output = subprocess.run(cmd, capture_output=True, text=True).stdout
    return output


if __name__ == "main":
    app.run(debug=True)
