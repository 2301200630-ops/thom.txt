import os
from flask import Flask

app = Flask(__name__)

html_code = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Thom.💘</title>
    <link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&family=Quicksand:wght@500;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --pink-main: #ff85a1;
            --pink-soft: #fbb1bd;
            --pink-bg: #ffe5ec;
            --card-bg: #ffffff;
            --text-color: #ff477e;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            background-color: var(--pink-bg);
            background-image: 
                radial-gradient(circle at 20% 20%, #ffc2d1 0%, transparent 40%),
                radial-gradient(circle at 80% 80%, #ffb3c6 0%, transparent 40%);
            font-family: 'Quicksand', sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 1rem;
        }

        .hk-card {
            position: relative;
            background-color: var(--card-bg);
            border: 3px solid var(--pink-soft);
            padding: 2rem 1.5rem;
            border-radius: 30px;
            box-shadow: 0 15px 35px rgba(255, 133, 161, 0.25);
            max-width: 420px;
            width: 100%;
            text-align: center;
            transition: transform 0.3s ease;
        }

        .hk-card:hover {
            transform: translateY(-5px);
        }

        .btn-close {
            position: absolute;
            top: 15px;
            right: 15px;
            background: #ffe5ec;
            border: 2px solid var(--pink-soft);
            color: var(--text-color);
            padding: 5px 12px;
            border-radius: 15px;
            font-family: 'Fredoka', sans-serif;
            font-size: 0.85rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s ease;
        }

        .btn-close:hover {
            background: var(--pink-main);
            color: white;
            transform: scale(1.05);
        }

        h1 {
            color: var(--text-color);
            font-family: 'Fredoka', sans-serif;
            font-size: 2.1rem;
            margin-top: 10px;
            margin-bottom: 12px;
            text-shadow: 2px 2px 0px #ffe5ec;
        }

        p.message {
            color: #7209b7;
            font-size: 1rem;
            font-weight: 700;
            margin-bottom: 15px;
        }

        .gif-container {
            margin-top: 15px;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .gif-container img {
            max-width: 180px;
            height: auto;
            border-radius: 20px;
            filter: drop-shadow(0 5px 10px rgba(255, 133, 161, 0.3));
        }

        .footer-decor {
            margin-top: 15px;
            font-size: 1.2rem;
        }
    </style>
</head>
<body>

    <div class="hk-card" id="helloKittyMessageBox">
        <button class="btn-close" onclick="document.getElementById('helloKittyMessageBox').style.display='none'">Cerrar.</button>
        
        <h1>Mi Chulo. 💕</h1>
        
        <p class="message">Te amo mil millonessss. 💕</p>
        
        <div class="gif-container">
            <img src="https://i.ibb.co/4nWjCRdQ/hellokitty.gif" alt="Hello Kitty GIF">
        </div>

        <div class="footer-decor">
    
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
