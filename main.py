from flask import Flask, render_template
import platform, os
import socket, subprocess

app = Flask(__name__)
mensaje=[]


@app.route("/")
def index():
    return render_template('index.html',mensaje=['Entregable 7',' Diego Garcia'])

@app.route("/<parametro>")
def mostrar(parametro):
    if parametro=="direccion_ip":
        return render_template('index.html', mensaje=['Dirección IP', socket.gethostbyname(socket.gethostname() + ".local")]) 
    elif parametro=="hostname":
        return render_template('index.html', mensaje=['Hostname', socket.gethostname()])
    elif parametro=="reiniciar":
        if os.name == "nt":
            return render_template('index.html', mensaje=['Reboot System', subprocess.run("shutdown -r now", shell=True)])
        elif os.name == "posix":
            return render_template('index.html', mensaje=['Reboot System', subprocess.run("reboot", shell=True)])

    else:
        return render_template('index.html',mensaje=['Error','Parámetro no válido, haz clic en el menú superior'])

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
