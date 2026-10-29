#!/usr/bin/env python3
# Genera las 4 paginas de oferta (upsell/downsell) del paquete PERRO.
# El widget de Hotmart se pega en widgets/<slug>.html (si existe) dentro del bloque de botones.
import os, html

BASE = os.path.dirname(os.path.abspath(__file__))

OFFERS = [
    dict(slug="perro-upsell-1", img="img/p5.jpg", bar="¡Espera! Tu pedido está casi listo",
         title="Enséñale las 6 órdenes que harán su vida más fácil y segura",
         product="Educa en positivo: plan de 8 semanas",
         intro="Un plan de 8 semanas para enseñar a tu perro <b>sentado, tumbado, quieto, ven, pasear sin tirar y déjalo</b>, solo con premios y sin castigos.",
         items=["Objetivo claro para cada semana", "Paso a paso de cada orden", "Consejos y errores que debes evitar",
                "Plan para marcar cada sesión", "Prueba final, tabla de progreso y diploma"],
         pages="PDF de 24 páginas", price="27"),
    dict(slug="perro-upsell-2", img="img/p6.jpg", bar="¡Una última sorpresa para vosotros!",
         title="Más de 15 juegos para cansarlo, relajarlo y divertiros sin salir de casa",
         product="El perro feliz en casa",
         intro="Juegos de <b>olfato, rompecabezas de comida, movimiento y calma</b>, hechos con cosas que ya tienes en casa. Ideal para días de lluvia o de poco paseo.",
         items=["Juegos de olfato y rompecabezas de comida", "Juegos de movimiento", "Juegos para aprender el nombre de sus juguetes",
                "Juegos de calma para antes de dormir", "Programa de 4 semanas y plan semanal"],
         pages="PDF de 16 páginas", price="19"),
    dict(slug="perro-upsell-3", img="img/p7.jpg", bar="Antes de terminar…",
         title="5 minutos al día para relajarle y reforzar vuestro vínculo",
         product="Masajes y bienestar",
         intro="Tres técnicas básicas y <b>seis rutinas paso a paso</b> para que tu perro se relaje con tus manos, también si ya es mayor.",
         items=["Cuerpo entero, cabeza y orejas, espalda y patas", "Rutina de calma antes de dormir", "Rutina especial para perros mayores",
                "Señales para saber si le gusta", "Cuándo no hay que masajear"],
         pages="PDF de 16 páginas", price="17"),
    dict(slug="perro-downsell", img="img/p8.jpg", bar="¿Prefieres empezar por lo básico?",
         title="Las 4 órdenes que más le protegen, en solo 14 días",
         product="Las 4 órdenes esenciales en 14 días",
         intro="<b>Sentado, quieto, ven y déjalo</b>, en sesiones de 5 minutos y solo con premios. Las órdenes que pueden evitarle un susto en la calle.",
         items=["Calendario de 14 días", "Sesiones cortas de 5 minutos", "Solo con premios, sin castigos",
                "Prueba final", "Diploma para tu perro"],
         pages="PDF de 15 páginas", price="9"),
    dict(slug="gato-upsell-1", img="img/g5.jpg", bar="¡Espera! Tu pedido está casi listo",
         title="Convierte tu casa en el paraíso de tu gato",
         product="Gato feliz de interior",
         intro="Los gatos de interior necesitan <b>cazar, trepar, rascar y comer con reto</b> para estar tranquilos y felices. Esta guía te enseña cómo dárselo en casa, sin obras ni gastos grandes.",
         items=["Los 5 pilares de un gato feliz en casa", "Juego de caza paso a paso", "Alturas y rascadores: dónde y cómo",
                "Comer pensando: comederos con reto", "Plan de 4 semanas"],
         pages="PDF de 18 páginas", price="27"),
    dict(slug="gato-upsell-2", img="img/g6.jpg", bar="¡Una última sorpresa para vosotros!",
         title="Adiós al pis fuera del arenero y a los muebles arañados",
         product="Adiós a los problemas de arenero y arañazos",
         intro="Por qué hace pis fuera o rasca tus muebles, y <b>cómo solucionarlo con cariño y sin castigos</b>.",
         items=["Cómo es el arenero ideal", "Limpieza que sí funciona", "Qué hacer si hace pis fuera",
                "Rascadores que de verdad usa", "Cómo proteger tus muebles"],
         pages="PDF de 17 páginas", price="19"),
    dict(slug="gato-upsell-3", img="img/g7.jpg", bar="Antes de terminar…",
         title="Presenta un nuevo gato (o un perro) sin peleas",
         product="Un nuevo compañero en casa",
         intro="Si alguna vez quieres traer otro animal, esta guía te lleva <b>paso a paso</b> para que la convivencia empiece bien.",
         items=["Qué preparar antes de que llegue", "Intercambio de olores", "Primeras miradas y primeros encuentros",
                "Gato y perro: cómo presentarlos", "Señales de que vais bien"],
         pages="PDF de 17 páginas", price="17"),
    dict(slug="gato-downsell", img="img/g8.jpg", bar="¿Prefieres empezar por algo sencillo?",
         title="10 minutos al día para un gato más feliz y tranquilo",
         product="10 juegos de caza en 10 minutos",
         intro="Diez juegos con <b>cosas que ya tienes en casa</b>, paso a paso y sin gastar dinero.",
         items=["10 juegos de caza explicados", "Hechos con cosas de casa", "Paso a paso y seguros",
                "Plan de 2 semanas", "Más unido a ti cada día"],
         pages="PDF de 18 páginas", price="9"),
]

PAW = ('<svg viewBox="0 0 64 64" aria-hidden="true"><g fill="currentColor"><ellipse cx="32" cy="42" rx="13" ry="11"/>'
       '<ellipse cx="15" cy="27" rx="6" ry="8"/><ellipse cx="49" cy="27" rx="6" ry="8"/>'
       '<ellipse cx="24" cy="15" rx="5.5" ry="7.5"/><ellipse cx="40" cy="15" rx="5.5" ry="7.5"/></g></svg>')

TPL = """<!doctype html>
<html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex">
<title>{product} · Oferta especial</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,700&family=Nunito:wght@400;600;700&display=swap" rel="stylesheet">
<style>
:root{{--cream:#fbf5ec;--card:#fffdf9;--brown:#5b3a22;--text:#3d2a1c;--muted:#7a6352;--orange:#e88a3c;--orange-d:#c96f24;--line:#ecdcc6}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--cream);color:var(--text);font:18px/1.6 Nunito,system-ui,sans-serif;overflow-x:hidden}}
.bar{{background:var(--brown);color:#fff;text-align:center;padding:12px 16px;font-weight:700;font-size:17px}}
.wrap{{max-width:620px;margin:0 auto;padding:22px 16px 40px;position:relative}}
.paws{{position:absolute;inset:0;pointer-events:none;color:var(--orange);opacity:.08;overflow:hidden}}
.paws svg{{position:absolute;width:46px}}
h1{{font-family:Fraunces,Georgia,serif;font-size:30px;line-height:1.2;color:var(--brown);text-align:center;margin:8px 0 18px}}
.card{{background:var(--card);border:1px solid var(--line);border-radius:22px;padding:22px;box-shadow:0 10px 30px rgba(91,58,34,.08);position:relative}}
.cover{{display:block;width:72%;max-width:300px;margin:0 auto 16px;border-radius:16px;box-shadow:0 12px 26px rgba(91,58,34,.22)}}
.tag{{display:inline-block;background:#fdebd9;color:var(--orange-d);font-weight:700;font-size:14px;padding:4px 12px;border-radius:99px}}
h2{{font-family:Fraunces,Georgia,serif;font-size:23px;color:var(--brown);margin:10px 0 6px}}
ul{{list-style:none;padding:0;margin:16px 0}}
li{{padding:8px 0 8px 34px;position:relative;border-bottom:1px dashed var(--line)}}
li:last-child{{border-bottom:0}}
li::before{{content:"✓";position:absolute;left:2px;top:9px;width:22px;height:22px;border-radius:50%;background:var(--orange);color:#fff;font-size:14px;font-weight:700;line-height:22px;text-align:center}}
.price{{text-align:center;margin:20px 0 6px}}
.price b{{font-family:Fraunces,Georgia,serif;font-size:46px;color:var(--orange-d)}}
.price small{{display:block;color:var(--muted);font-size:15px}}
.buy{{margin:18px 0 6px;min-height:60px}}
.note{{text-align:center;font-size:15px;color:var(--muted);margin-top:14px}}
.guar{{display:flex;gap:12px;align-items:center;background:#f6ecdf;border-radius:16px;padding:14px 16px;margin-top:18px;font-size:16px}}
.guar span{{font-size:28px}}
footer{{text-align:center;font-size:13px;color:var(--muted);margin-top:26px}}
</style></head>
<body>
<div class="bar">{bar}</div>
<div class="wrap">
  <div class="paws">{paws}</div>
  <h1>{title}</h1>
  <div class="card">
    <img class="cover" src="{img}" alt="Portada de {product}" width="300" height="300">
    <span class="tag">Oferta solo para ti, ahora</span>
    <h2>{product}</h2>
    <p>{intro}</p>
    <ul>{items}</ul>
    <div class="price"><b>{price} €</b><small>Pago único · {pages} · Descarga inmediata</small></div>
    <div class="buy" id="comprar">
{widget}
    </div>
    <p class="note">Se añade a tu compra con un clic, sin volver a meter la tarjeta.</p>
    <div class="guar"><span>🛡️</span><div><b>Garantía de 7 días.</b> Si no te convence, te devolvemos el dinero.</div></div>
  </div>
  <footer>Ediciones Faro Claro · Pago seguro procesado por Hotmart</footer>
</div>
</body></html>
"""

def paws():
    spots = [(4, 8, -20), (86, 18, 15), (10, 52, 25), (84, 64, -10), (6, 88, 10), (88, 92, -25)]
    return "".join(f'<span style="position:absolute;left:{x}%;top:{y}%;transform:rotate({r}deg);display:block;width:46px">{PAW}</span>'
                   for x, y, r in spots)

def main():
    for o in OFFERS:
        wfile = os.path.join(BASE, "widgets", o["slug"] + ".html")
        widget = open(wfile, encoding="utf-8").read() if os.path.exists(wfile) else "<!-- WIDGET HOTMART -->"
        page = TPL.format(bar=html.escape(o["bar"]), title=html.escape(o["title"]), product=html.escape(o["product"]),
                          intro=o["intro"], items="".join(f"<li>{html.escape(i)}</li>" for i in o["items"]),
                          price=o["price"], pages=o["pages"], img=o["img"], widget=widget, paws=paws())
        os.makedirs(os.path.join(BASE, "site", "img"), exist_ok=True)
        open(os.path.join(BASE, "site", o["slug"] + ".html"), "w", encoding="utf-8").write(page)
    print("ok")

if __name__ == "__main__":
    main()
