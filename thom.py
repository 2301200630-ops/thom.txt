import os
from flask import Flask

app = Flask(__name__)

# AQUÍ VA TODO TU CÓDIGO ORIGINAL
from IPython.display import HTML, display
import json

versos = [
    "Antes de que te despidas y decidas dejar todo esto en la nada",
    "Antes que finjas amarme y luego me digas que lo nuestro no es na",
    "Te voy a decir que lo hago solo para ver como brilla esa mirada",
    "pero da igual :("
]

versos_json = json.dumps(versos)

html_code = """
<!DOCTYPE html>
<html>
<head>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Varela+Round&display=swap');
        body {
            font-family: 'Varela Round', sans-serif;
            background: #ffe4e1;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
        }
        .box {
            background: white;
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
            text-align: center;
            max-width: 80%;
            animation: bounceIn 1s ease;
        }
        @keyframes bounceIn {
            0% { opacity: 0; transform: scale(0.3); }
            70% { opacity: 1; transform: scale(1.05); }
            100% { transform: scale(1); }
        }
        h2 { color: #ff6b81; min-height: 60px; }
        button {
            background: #ff6b81;
            color: white;
            border: none;
            padding: 12px 24px;
            font-size: 16px;
            border-radius: 25px;
            cursor: pointer;
            transition: 0.3s;
        }
        button:hover { background: #ff4757; transform: scale(1.05); }
    </style>
</head>
<body>
    <div class="box">
        <h2 id="verso">❤️ Presiona el botón para empezar...</h2>
        <button id="btn" onclick="siguienteVerso()">Siguiente verso</button>
    </div>

    <script>
        var versos = """ + versos_json + """;
        var index = 0;
        function siguienteVerso() {
            if(index < versos.length) {
                document.getElementById('verso').innerText = versos[index];
                index++;
            } else {
                document.getElementById('verso').innerText = "Te amo mi negro ❤️";
                document.getElementById('btn').style.display = 'none';
            }
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return html_code

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
