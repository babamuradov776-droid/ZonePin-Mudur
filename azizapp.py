import os
from flask import Flask, render_template_string, request

app = Flask(__name__)

# Ürünler listesi
urunler = [
    {"ad": "60 UC", "fiyat": "35 TL", "icon": "💰"},
    {"ad": "325 UC", "fiyat": "212.49 TL", "icon": "💰"},
    {"ad": "660 UC", "fiyat": "419.18 TL", "icon": "💰"},
    {"ad": "1800 UC", "fiyat": "1150 TL", "icon": "💰"},
    {"ad": "3850 UC", "fiyat": "2143.20 TL", "icon": "💰"},
    {"ad": "8100 UC", "fiyat": "4258.02 TL", "icon": "💰"},
    {"ad": "16200 UC", "fiyat": "8724.92 TL", "icon": "💰"},
    {"ad": "40500 UC", "fiyat": "18500 TL", "icon": "💰"},
    {"ad": "81000 UC", "fiyat": "35000 TL", "icon": "💰"},
    {"ad": "Royale Pass", "fiyat": "450 TL", "icon": "🎫"},
    {"ad": "Prime Plus", "fiyat": "320 TL", "icon": "👑"}
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ZONEPIN GLOBAL</title>
    <style>
        body { background:#0a0a0a; color:#fff; font-family: sans-serif; margin:0; }
        .nav { display:flex; justify-content:space-between; align-items:center; padding:15px; border-bottom:1px solid #333; }
        .login-btn { background:#00ffaa; color:#000; padding:6px 15px; border-radius:5px; font-weight:bold; text-decoration:none; font-size:13px; }
        .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; padding: 10px; }
        .card { background: #151515; border-radius: 10px; padding: 15px; text-align: center; border: 1px solid #333; }
        .icon { font-size: 25px; margin-bottom: 8px; }
        .ad { font-weight: bold; font-size: 13px; margin-bottom: 5px; }
        .fiyat { color: #00ffaa; font-weight: bold; font-size: 14px; margin-bottom: 10px; }
        .btn { background: #00ffaa; border: none; color: #000; padding: 8px; width: 100%; border-radius: 5px; font-weight: bold; cursor: pointer; }
    </style>
</head>
<body>
    <div class="nav">
        <h2 style="margin:0; color:#00ffaa;">🛡️ ZONEPIN</h2>
        <a href="/login" class="login-btn">GİRİŞ YAP</a>
    </div>
    <div class="grid">
        {% for u in urunler %}
        <div class="card">
            <div class="icon">{{ u.icon }}</div>
            <div class="ad">{{ u.ad }}</div>
            <div class="fiyat">{{ u.fiyat }}</div>
            <form action="/sepet" method="GET">
                <input type="hidden" name="urun" value="{{ u.ad }}">
                <button type="submit" class="btn">SEPETE EKLE</button>
            </form>
        </div>
        {% endfor %}
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, urunler=urunler)

@app.route('/login')
def login():
    return "<body style='background:#0a0a0a; color:#fff; text-align:center; padding-top:50px;'><h1>Giriş Sayfası</h1><a href='/' style='color:#00ffaa;'>Ana Sayfaya Dön</a></body>"

@app.route('/sepet')
def sepet():
    urun = request.args.get('urun')
    return f"<body style='background:#0a0a0a; color:#fff; text-align:center; padding-top:50px;'><h1>{urun} sepete eklendi!</h1><a href='/' style='color:#00ffaa;'>Devam Et</a></body>"

if __name__ == '__main__':
    # Sunucu (Render/Heroku) portunu otomatik bulur
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
