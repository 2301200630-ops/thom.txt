import os
from flask import Flask

app = Flask(__name__)

html_code = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Thom 💘</title>
    <style>
        body {
            background-color: #ffe4e1;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
    </style>
</head>
<body>

    <div id="helloKittyMessageBox" style="position: relative; border: 2px solid #FF69B4; padding: 20px; background-color: white; border-radius: 20px; box-shadow: 0 10px 20px rgba(0,0,0,0.1); max-width: 450px; width: 90%;">
        
        <button onclick="document.getElementById('helloKittyMessageBox').style.display='none'" style="position: absolute; top: 10px; right: 10px; background: none; border: none; font-size: 16px; cursor: pointer;">Cerrar 💖</button>
        
        <h1 style="color: #FF69B4; font-family: 'Comic Sans MS', cursive, sans-serif; text-align: center; margin-top: 10px;">
            Te amo mi negro 💕
        </h1>
        
        <div style="display: flex; align-items: center; justify-content: center; margin-bottom: 10px;">
            <img src="https://upload.wikimedia.org/wikipedia/en/thumb/0/07/Hello_Kitty_logo.svg/1200px-Hello_Kitty_logo.svg.png" style="max-width: 120px; height: auto;">
        </div>
        
        <h2 style="color: #FF69B4; font-family: 'Comic Sans MS', cursive, sans-serif; margin: 0; text-align: center; font-size: 20px;">
           Nuestro experimento 💘
        </h2>
        
        <div style="text-align: center; margin-top: 15px;">
            <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbW83b3A1ZXF5ZzZ0NXFpZ3J6b3RndXNnd296bXptMXF0ODg0Z3Z4dyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/C9v8pXp09vNmM/giphy.gif" style="max-width: 140px; height: auto;" alt="Hello Kitty Gif">
        </div>
        
    </div>

</body>
</html>
"""

@app.route('/')
def home():
    return html_code

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
