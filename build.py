"""Générateur de la maquette Le République (Châtillon-sur-Chalaronne). Usage : python build.py <dossier-du-projet>
Contenus relevés le 13/11/2026 : Linktree (cartes PDF : formule midi et carte, tapas, boissons, glaces et gaufres),
Instagram @lerepublique118, fiche Google. Rien d'inventé : textes, photos, prix, horaires, coordonnées."""
import os
import sys
OUT = sys.argv[1] if len(sys.argv) > 1 else "."
A = 'assets/'
PH = A + 'ph/'
V = 2  # cache : incrémenter à chaque changement de CSS ou JS
TEL, TELH = '04 74 55 02 88', 'tel:0474550288'
MAIL = 'lerepublique118@gmail.com'
ADR = ('118 place de la République', '01400 Châtillon-sur-Chalaronne')
MAP = 'https://www.google.com/maps/search/?api=1&query=Le+R%C3%A9publique+118+place+de+la+R%C3%A9publique+Ch%C3%A2tillon-sur-Chalaronne'
IG = 'https://www.instagram.com/lerepublique118/'
FB = 'https://www.facebook.com/profile.php?id=61555911320949'
HOR = [('Lundi, mardi, mercredi', '6 h 30 – 15 h 30'), ('Jeudi, vendredi', '6 h 30 – 19 h'), ('Samedi', '6 h 30 – 15 h 30'), ('Dimanche', '8 h – 12 h')]
NAV = [('carte.html', 'La carte'), ('glacier.html', 'Le glacier')]


def pill(t, href, cls='', arrow='↗', ext=False):
    x = ' target="_blank" rel="noopener"' if ext else ''
    return f'<a class="pill {cls}" href="{href}"{x}><span class="r"><span>{t}</span><span>{t}</span></span><b>{arrow}</b></a>'


def tile(src, cls='', style='', alt='', par=None, lazy=True):
    p = f' data-par="{par}" style="height:118%;width:100%"' if par else ''
    return f'<figure class="tile {cls}" style="{style}"><img src="{src}" alt="{alt}"{p}{" loading=lazy" if lazy else ""}></figure>'


def logo(cls=''):
    return f'<span class="lgo {cls}" aria-hidden="true"><img src="{A}logo.png" alt=""><span><span class="wm">Le <i>République</i></span><small>Café · restaurant · glacier</small></span></span>'


def head(title, desc, cur):
    def a(h, t, cls=''):
        return f'<a href="{h}"{" class="+cls if cls else ""}{" aria-current=page" if h == cur else ""}>{t}</a>'
    items = a('index.html', 'Accueil') + ''.join(a(h, t) for h, t in NAV) + a('infos.html', 'Nous trouver', 'hl')
    return f'''<!doctype html>
<html lang="fr"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:type" content="website">
<meta name="theme-color" content="#1b241b">
<meta name="robots" content="noindex, nofollow">
<link rel="icon" href="{A}logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Great+Vibes&family=Montserrat:wght@400;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{A}style.css?v={V}">
</head><body>
<div id="bar"></div>
<header class="top">
<a class="logo" href="index.html" aria-label="Le République, accueil">{logo()}</a>
<nav class="nav" aria-label="Navigation principale"><button class="stop" type="button" aria-label="Fermer le menu"><span>MENU</span></button>{items}</nav>
<span class="side"><a class="tel" href="{TELH}" aria-label="Appeler le {TEL}"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1A17 17 0 0 1 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1z" fill="currentColor"/></svg><span>{TEL}</span></a></span>
<button class="burger" aria-label="Menu" aria-expanded="false"><i></i><i></i></button>
</header>
<main>'''


def foot():
    return f'''</main>
<footer><div class="wrap"><div class="fg">
<div>{logo('big')}<p>Café, restaurant et glacier sur la place de la République. Simple, frais et convivial !</p></div>
<div><h4 class="micro">Le République</h4><ul><li><a href="carte.html">La carte du midi</a></li><li><a href="carte.html#tapas">Les tapas</a></li><li><a href="glacier.html">Le glacier</a></li><li><a href="infos.html">Horaires et accès</a></li></ul></div>
<div><h4 class="micro">Contact</h4><ul><li><a href="{TELH}">{TEL}</a></li><li><a href="mailto:{MAIL}">{MAIL}</a></li><li><a href="{IG}" target="_blank" rel="noopener">Instagram</a></li><li><a href="{FB}" target="_blank" rel="noopener">Facebook</a></li></ul></div>
<div><h4 class="micro">Nous trouver</h4><ul><li>{ADR[0]}</li><li>{ADR[1]}</li><li>Dès 6 h 30, du lundi au samedi</li></ul></div>
</div></div>
<div class="fw" aria-hidden="true">RÉPUBLIQUE</div>
<div class="fb micro"><span class="pad">© Le République</span><span class="pad">Maquette de site · Le Génie Numérique</span></div></footer>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
<script src="https://unpkg.com/lenis@1.1.13/dist/lenis.min.js"></script>
<script src="{A}main.js?v={V}"></script></body></html>'''


def cta(t='On vous garde <em>une place ?</em>'):
    return f'''<section class="sec cta"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.6rem">Simple, frais et convivial</span><h2 class="sp">{t}</h2>
<div class="row rv">{pill('Appeler le ' + TEL, TELH, 'blue')}{pill('Nous trouver', 'infos.html', 'ghost')}</div></div></section>'''


def pagehead(crumb, h1, lead, img, img2=None, extra=''):
    t2 = tile(img2, 'small', lazy=False) if img2 else ''
    return f'''<section class="ph"><div class="wrap"><div class="crumb micro"><a href="index.html">Accueil</a> / {crumb}</div><h1 class="sp">{h1}</h1><p class="lead rv">{lead}</p>{extra}</div>{tile(img, lazy=False)}{t2}</section>'''


def gal(items):
    return '<div class="gal">' + ''.join(f'<figure class="rv" data-c="{c}" style="--d:{(i % 3) * .07}s"><img src="{PH}{k}.webp" alt="{t}" loading="lazy"><figcaption><span class="micro">{c}</span>{t}</figcaption></figure>' for i, (k, c, t) in enumerate(items)) + '</div>'


def hours():
    return ''.join(f'<span><b>{j}</b> · {h}</span>' for j, h in HOR)


def menus(lst, cls=''):
    return f'<div class="menus {cls}">' + ''.join(f'<div class="menu rv"><span class="micro mute">{s}</span><h3>{n}</h3><b>{p}</b><ul>{"".join(f"<li>{x}</li>" for x in its)}</ul></div>' for n, p, s, its in lst) + '</div>'


def carte(data, first_id=''):
    tabs = ''.join(f'<button{" class=on" if i == 0 else ""} data-f="{c}">{c}</button>' for i, (c, _) in enumerate(data))
    rows = ''.join(f'<div class="dish rv{"" if c == data[0][0] else " hide"}" data-c="{c}"><div><h3>{n}</h3>{f"<p>{d}</p>" if d else ""}</div><b>{p}</b></div>' for c, its in data for n, d, p in its)
    return f'<div class="flt" data-t=".dish">{tabs}</div><div class="dishes">{rows}</div>'


# cartes publiées sur le Linktree du République (PDF relevés le 13/11/2026)
FORMULES = [('Formule midi', '18 €', 'Du lundi au samedi', ['Entrée, plat et dessert', 'Œufs mayonnaise, rosette lyonnaise, salade de crudités ou piémontaise', 'Linguines al pesto, pêche du jour ou steack à cheval']),
            ('Formule midi', '17 €', 'Du lundi au samedi', ['Entrée et plat, ou plat et dessert', 'Crème brûlée, salade de fruits frais, faisselle d’Etrez ou tranche de gorgonzola']),
            ('Menu enfant', '13 €', 'Pour les petits', ['Boisson : sirop, oasis ou cola', 'Burger crispy ou steak haché, frites ou légumes', '2 boules de glace']),
            ('Petit-déjeuner', '8 €', 'De 7 h à 11 h, sauf le samedi', ['Boisson chaude et jus d’orange pressé', 'Croissant du boulanger', 'Beurre, confiture ou Nutella, Krisprolls'])]
CARTE = [
    ('Salades', [('César', 'Mélange de salades, filet de poulet crispy, croûtons, copeaux de parmesan et sauce César', '16 €'),
                 ('Italienne', 'Mélange de salades, jambon cru, mozza di bufala, copeaux de parmesan et tomates cerises', '16 €'),
                 ('Parisienne', 'Mélange de salades, jambon blanc truffé, comté, croûtons et œufs durs', '16 €')]),
    ('Burgers', [('Le Rep’', 'Pain burger, steak haché du boucher, œuf au plat, lard grillé, cheddar, salade, oignons crispy, sauce barbecue. Frites maison', '16 € · double 20 €'),
                 ('Le Crispy', 'Pain burger, poulet crispy, cheddar, salade, oignons rouges, tomates cerises, sauce maison. Frites maison', '16 € · double 20 €')]),
    ('Viandes', [('Bavette de veau', 'Sauce échalote, viande bovine française', '22 €'),
                 ('L’Andouillette Châtillonnaise', 'Sauce moutarde : l’excellence du terroir châtillonnais à la fraise de veau', '23 €'),
                 ('Tartare de bœuf charolais', 'Coupé au couteau, assaisonné par nos soins. 180 g ou 360 g', '20 € · 28 €'),
                 ('Carpaccio de bœuf charolais', 'Billes de mozza buratta, câpres, pesto, parmesan', '19 €')]),
    ('Tapas', [('Rosette lyonnaise', 'Et cornichons', '7 €'), ('Assiette de cochonnaille', 'Beurre et cornichons', '15 €'),
               ('Assiette mixte', 'Charcuteries et fromages', '20 €'), ('Poulet crispy', 'Et sa mayo maison', '7 €'),
               ('Bol de frites maison', '', '7 €'), ('Bol de salade', 'Et crudités', '7 €'), ('Œufs mayonnaise', '', '7 €')]),
    ('Cocktails', [('Mojito', 'Rhum, menthe, citron vert, sucre de canne, eau gazeuse', '9 €'), ('Aperol Spritz', 'Aperol, prosecco, eau gazeuse', '9 €'),
                   ('Spritz St-Germain', 'St-Germain, prosecco, eau gazeuse', '10 €'), ('Hendrick’s Basil', 'Hendrick’s, jus de citron, basilic, eau gazeuse', '10 €'),
                   ('Sans alcool', 'Mojito, planteur, piñacolada', '8 €'), ('Sangria rouge', 'Le p’tit nouveau, aussi en pichet de 1,5 L', '5 € · 25 €')]),
    ('Au comptoir', [('Café, déca', 'Allongé ou non', '1,50 €'), ('Cappuccino, chocolat chaud, thé Damman Frères', '', '3 €'),
                     ('Café ou chocolat viennois', '', '4 €'), ('Orange ou citron pressé minute', '', '4,50 €'),
                     ('Kir vin blanc', 'Crème de cassis, pêche, mûre ou châtaigne', '4 €'), ('Pelforth blonde', '25 cl · 50 cl', '3,50 € · 7 €')]),
]
COUPES = [('Dame blanche', '2 boules vanille, coulis chocolat, chantilly', '7,50 €'), ('Chocolat liégeois', 'Chocolat, vanille, coulis chocolat, chantilly', '7,50 €'),
          ('Café liégeois', 'Café, vanille, café expresso, chantilly', '7,50 €'), ('Ardéchoise', '2 boules vanille, crème de marron, chantilly', '8 €'),
          ('Bounty', '2 boules coco, coulis chocolat, chantilly', '7,50 €'), ('Snickers', 'Chocolat, vanille, cacahuètes, caramel, chantilly', '8 €'),
          ('Colonel', '2 boules citron, vodka 4 cl', '9 €'), ('After Eight', '2 boules menthe chocolat, Get 27 4 cl', '9 €'),
          ('Baileys', '2 boules café, Baileys 4 cl', '9 €'), ('Lemon', '2 boules citron, limoncello 4 cl', '9 €'), ('Reggae', '2 boules rhum-raisins, rhum ambré 4 cl', '9 €')]
SORBETS = ['fraise', 'fruits rouges', 'citron', 'abricot', 'mangue', 'fruit de la passion', 'melon', 'noix de coco', 'pêche de vigne']
CREMES = ['vanille', 'chocolat', 'café', 'caramel beurre salé', 'rhum raisins', 'menthe chocolat', 'pistache', 'nuty', 'barbe à papa', 'amarena', 'oréo', 'vanille cookie dough', 'marron', 'tiramisu']


def pages():
    P = {}
    hero_tiles = [('t1', 'huitres'), ('t2', 'spritz'), ('t3', 'glaces'), ('t4', 'salle'), ('t5', 'sylvain'), ('t6', 'givre'), ('t7', 'foiegras')]
    ht = ''.join(f'<figure class="tile {c}"><div class="fl"><div class="in"><img src="{PH}{f}.webp" alt=""></div></div></figure>' for c, f in hero_tiles)
    stack = ''.join(tile(f'{PH}{f}.webp') for f in ['assiette', 'entree', 'foiegras', 'sylvain', 'glaces', 'spritz', 'givre', 'table'])
    wall_imgs = ['huitres', 'assiette', 'salle', 'glaces', 'spritz', 'table', 'sylvain', 'foiegras', 'givre', 'entree', 'roi', 'petitdej', 'concert']
    wall = ''.join(tile(f'{PH}{wall_imgs[i % len(wall_imgs)]}.webp') for i in range(54))
    items = [('carte.html#formules', '01', 'Le café', 'Dès 6 h 30. Petit-déjeuner à 8 €, de 7 h à 11 h.', 'petitdej', 'Sauf le samedi'),
             ('carte.html', '02', 'Le midi', 'Formule à 17 € ou 18 €, salades, burgers, viandes charolaises.', 'assiette', 'Lundi au samedi'),
             ('carte.html#tapas', '03', 'Les tapas', 'Cochonnaille, assiette mixte, poulet crispy, frites maison.', 'huitres', 'À partager'),
             ('glacier.html', '04', 'Le glacier', 'Coupes, gaufres et milk-shakes. Vingt-trois parfums.', 'glaces', 'Glacier')]
    pl = ''.join(f'<a href="{h}"><span class="micro mute">{n}</span><span class="nm">{t}</span><span class="d">{d}<b>{b}</b></span></a>' for h, n, t, d, _, b in items)
    prev = ''.join(tile(f'{PH}{it[4]}.webp', 'on' if i == 0 else '') for i, it in enumerate(items))
    track = ''.join(f'<figure class="tile"><img src="{PH}{f}.webp" alt="{l}" loading="lazy"><span class="tag">{l}</span></figure>' for f, l in [
        ('assiette', 'Le midi'), ('entree', 'En entrée'), ('huitres', 'Samedi, jour de marché'), ('spritz', 'Aperol Spritz'), ('glaces', 'Le glacier'), ('sylvain', 'La tarte de Sylvain')])
    steps = [('Le matin', 'Café au comptoir dès 6 h 30.'),
             ('Le midi', 'Formule du lundi au samedi.'),
             ('L’après-midi', 'Une glace en terrasse.'),
             ('Le dimanche', 'L’apéro, de 8 h à midi.')]
    st = ''.join(f'<div class="stp"><div class="n">{i + 1}</div><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(steps))
    mq = ''.join(f'<span>{x}</span>' for x in ['Café', 'Restaurant', 'Glacier', 'Tapas', 'Cocktails', 'Terrasse', 'Formule midi'] * 2)

    P['index.html'] = head('Le République — Café, restaurant, glacier à Châtillon-sur-Chalaronne', 'Le République, café, restaurant et glacier au 118 place de la République à Châtillon-sur-Chalaronne : formule midi, tapas, glaces. 04 74 55 02 88.', 'index.html') + f'''
<section class="hero">
<div class="cap micro c1"><b>Simple, frais</b>et convivial !</div>
<div class="cap micro c2"><b>Café · restaurant</b>glacier</div>
<div class="cap micro c3"><b>Place de la République</b>dès 6 h 30</div>
<div class="go">{pill('Voir la carte', 'carte.html')}</div>
{ht}
<p class="para">Café, restaurant et glacier, au cœur de Châtillon.</p>
<h1 class="word">RÉPUBLIQUE</h1>
<div class="scrollhint micro"><i></i>Défiler</div>
</section>

<div class="mq" aria-hidden="true"><div>{mq}</div></div>

<section class="sec"><div class="wrap fin"><div><span class="micro mute" style="display:block;margin-bottom:1.4rem">Bienvenue</span><h2 class="sp">Sur la place, <em>du matin au soir</em></h2>
<p class="lead rv" style="margin:1.4rem 0 2rem">Le café au comptoir dès 6 h 30, la formule du midi, les tapas à partager, une glace en terrasse. Le samedi, jour de marché : huîtres fraîches et le p’tit blanc.</p>
<ul class="checks rv" style="margin-bottom:2rem"><li><span><b>Le midi</b>, du lundi au samedi.</span></li><li><span><b>Le dimanche matin</b>, l’apéro de 8 h à midi.</span></li><li><span><b>La terrasse</b>, sur la place de la République.</span></li></ul>{pill('Horaires et accès', 'infos.html', 'blue')}</div>{tile(PH + 'huitres.webp', '', par=8, alt='La terrasse du République, huîtres du samedi')}</div></section>

<section class="story"><span class="micro mute m3">Notre cuisine</span>
<h2><span class="w">Simple,</span> <span class="w">frais</span> <span class="w">et</span> <span class="w"><em>convivial</em></span></h2>
<div class="stack">{stack}</div>
<p class="micro mute m1">Viandes charolaises, frites maison.</p><span class="micro mute m2">Du lundi au samedi</span></section>

<section class="wall"><div class="grid">{wall}</div><div class="mid"><span class="micro mute">Formule midi</span><h2>Dès <em>17 €</em></h2>{pill('Voir la carte', 'carte.html', 'blue')}</div></section>

<section class="sec" id="services"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.4rem">Du matin au soir</span><h2 class="sp" style="margin-bottom:clamp(2rem,5vw,4rem)">Une envie <em>de quoi ?</em></h2>
<div class="plist">{pl}</div></div><div class="prev">{prev}</div></section>

<section class="hz"><div class="pin"><div class="wrap top2"><div><span class="micro mute" style="display:block;margin-bottom:1.2rem">À table</span><h2>Au Rep’, <em>on partage</em></h2></div>{pill('La carte', 'carte.html')}</div>
<div class="track">{track}</div></div></section>

<section class="sec"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.4rem">Ils en parlent</span><h2 class="sp">Une adresse <em>de la place</em></h2>
<div class="cnt rv"><div><b data-to="338">0</b><span>avis sur Google, note de 4,2 sur 5</span></div><div><b data-to="1068">0</b><span>abonnés sur Facebook</span></div><div><b data-to="23">0</b><span>parfums de sorbets et crèmes glacées</span></div></div>
<p class="note" style="margin-top:1.4rem">Chiffres relevés en novembre 2026, à confirmer avec le République.</p></div></section>

<section class="sec" style="padding-top:0"><div class="wrap fin"><div><span class="micro mute" style="display:block;margin-bottom:1.4rem">Fait maison</span><h2 class="sp">La tarte <em>de Sylvain</em></h2>
<p class="lead rv" style="margin:1.4rem 0 2rem">Notre Sylvain pose les pieds en cuisine et les mains dans les pommes : une tarte faite avec amour, passion et beaucoup de rigolade.</p>{pill('Les desserts', 'glacier.html', 'blue')}</div>{tile(PH + 'sylvain.webp', '', par=8, alt='Sylvain et sa tarte aux pommes')}</div></section>

<section class="sec" style="padding-top:0"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.4rem">Votre journée</span><h2 class="sp">Toujours <em>une bonne raison</em></h2><div class="steps">{st}</div></div></section>
{cta()}''' + foot()

    P['carte.html'] = head('La carte — Le République, Châtillon-sur-Chalaronne', 'Formule midi à 17 € et 18 €, salades, burgers, viandes charolaises, andouillette châtillonnaise, tapas et cocktails au République.', 'carte.html') + pagehead('La carte', 'La carte <em>du République</em>', 'Simple, frais et convivial ! La formule du midi, les salades, les burgers, les viandes charolaises et les tapas à partager.', PH + 'assiette.webp', PH + 'entree.webp') + f'''
<section class="sec" id="formules"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.2rem">Nos formules</span><h2 class="sp" style="margin-bottom:clamp(2rem,5vw,3.4rem)">Midi et matin, <em>à petit prix</em></h2>{menus(FORMULES, 'm4')}</div></section>
<section class="sec" style="padding-top:0" id="tapas"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.2rem">À la carte</span><h2 class="sp" style="margin-bottom:2rem">Choisissez <em>votre envie</em></h2>
{carte(CARTE)}
<p class="note" style="margin-top:2rem">Burgers et viandes accompagnés de frites maison (ou légumes et salade pour les viandes). Prix nets, service et sourire compris. Chèques non acceptés. Carte relevée sur les documents du République, à confirmer avec le restaurant.</p></div></section>''' + cta() + foot()

    chips = lambda L: '<div class="chips rv">' + ''.join(f'<span class="tag">{x}</span>' for x in L) + '</div>'
    GL = [('1 boule', '3 €', 'Compose ta coupe', ['Sorbet ou crème glacée, au choix']),
          ('2 boules', '5,50 €', 'Compose ta coupe', ['Deux parfums au choix']),
          ('3 boules', '7,50 €', 'Compose ta coupe', ['Trois parfums au choix']),
          ('Milk-shake de Roméo', '7 €', 'Nouveau', ['Glace et lait mixés', 'Parfum au choix'])]
    GF = [('Gaufre', 'Nature ou sucre', '3,50 €'), ('Nutella ou crème de marron', 'Sur la gaufre ou la coupe', '1,50 €'), ('Coulis', 'Chocolat maison, caramel maison, fruits rouges', '1 €'),
          ('Éclats', 'Chamallows, oréo, smarties, cacahuètes', '1 €'), ('Boule de glace', 'Sur la gaufre : sorbet ou crème glacée', '2,50 €'), ('Chantilly maison', '', '1,50 €')]
    P['glacier.html'] = head('Le glacier — Le République, Châtillon-sur-Chalaronne', 'Le glacier du République : coupes de 1 à 3 boules, coupes glacées et digestives, gaufres, milk-shakes. Neuf sorbets et quatorze crèmes glacées.', 'glacier.html') + pagehead('Le glacier', 'Une glace <em>en terrasse</em>', 'Des sorbets aux plus gourmandes, en passant par les nouveautés et les incontournables : composez votre coupe.', PH + 'glaces.webp', PH + 'givre.webp') + f'''
<section class="sec"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.2rem">Compose ta coupe</span><h2 class="sp" style="margin-bottom:clamp(2rem,5vw,3.4rem)">Une, deux <em>ou trois boules</em></h2>{menus(GL, 'm4')}</div></section>
<section class="sec" style="padding-top:0"><div class="wrap split"><div><span class="micro mute" style="display:block;margin-bottom:1.2rem">Les parfums</span><h2 class="sp">Vingt-trois <em>parfums</em></h2></div>
<div><h3 class="micro mute" style="margin-bottom:1rem">Sorbets</h3>{chips(SORBETS)}<h3 class="micro mute" style="margin:2rem 0 1rem">Crèmes glacées</h3>{chips(CREMES)}</div></div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.2rem">Coupes glacées et digestives</span><h2 class="sp" style="margin-bottom:2rem">Les <em>gourmandes</em></h2>
<div class="dishes">{"".join(f'<div class="dish rv"><div><h3>{n}</h3><p>{d}</p></div><b>{p}</b></div>' for n, d, p in COUPES)}</div></div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.2rem">Nouveau</span><h2 class="sp" style="margin-bottom:2rem">Compose <em>ta gaufre</em></h2>
<div class="dishes">{"".join(f'<div class="dish rv"><div><h3>{n}</h3>{f"<p>{d}</p>" if d else ""}</div><b>{p}</b></div>' for n, d, p in GF)}</div>
<p class="note" style="margin-top:2rem">Desserts : crème brûlée, salade de fruits frais, faisselle d’Etrez et son coulis, 5,50 €. Carte d’été relevée sur les documents du République, à confirmer avec le restaurant.</p></div></section>''' + cta('Une petite <em>douceur ?</em>') + foot()

    P['infos.html'] = head('Nous trouver — Le République, Châtillon-sur-Chalaronne', f'Le République, 118 place de la République, Châtillon-sur-Chalaronne. Ouvert dès 6 h 30 du lundi au samedi, le dimanche de 8 h à midi. {TEL}.', 'infos.html') + pagehead('Nous trouver', 'Sur la place, <em>au centre</em>', 'Au 118 place de la République, à Châtillon-sur-Chalaronne. Côté bar, on vous accueille dès 6 h 30 du lundi au samedi, et dès 8 h le dimanche.', PH + 'huitres.webp', PH + 'salle.webp') + f'''
<section class="sec"><div class="wrap split"><div><span class="micro mute" style="display:block;margin-bottom:1.2rem">Horaires</span><h2 class="sp">Ouvert <em>tous les jours</em></h2>
<div class="hor rv">{hours()}<span class="micro">Restauration le midi, du lundi au samedi. Horaires à confirmer avec le République.</span></div></div>
<div><span class="micro mute" style="display:block;margin-bottom:1.2rem">Contact</span><h2 class="sp">Un appel <em>suffit</em></h2>
<div class="hor rv"><span><b>Téléphone</b> · <a href="{TELH}">{TEL}</a></span><span><b>E-mail</b> · <a href="mailto:{MAIL}">{MAIL}</a></span><span><b>Adresse</b> · {ADR[0]}, {ADR[1]}</span></div>
<div class="row rv" style="margin-top:2rem">{pill('Appeler', TELH, 'blue')}{pill('Itinéraire', MAP, 'ghost', ext=True)}</div></div></div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.2rem">Nos nouvelles</span><h2 class="sp" style="margin-bottom:clamp(2rem,5vw,3.4rem)">La vie <em>du Rep’</em></h2>
<div class="flt" data-t=".gal figure"><button class="on" data-f="*">Tout</button><button data-f="À table">À table</button><button data-f="Nouvelles">Les nouvelles</button></div>
{gal([('salle', 'Nouvelles', 'La salle'), ('assiette', 'À table', 'Le midi'), ('huitres', 'Nouvelles', 'Samedi : marché et huîtres'), ('spritz', 'À table', 'Nos cocktails sont de retour'), ('petitdej', 'Nouvelles', 'Le petit-déjeuner à 8 €'), ('foiegras', 'À table', 'Foie gras au grué de cacao'), ('sylvain', 'Nouvelles', 'Sylvain, pâtissier'), ('glaces', 'À table', 'Les glaces'), ('concert', 'Nouvelles', 'La Isla Band en live'), ('givre', 'À table', 'Les cocktails givrés'), ('roi', 'Nouvelles', 'Et si le roi était en cuisine ?'), ('entree', 'À table', 'En entrée'), ('table', 'Nouvelles', 'Votre table vous attend')])}</div></section>''' + cta() + foot()
    return P


for k, v in pages().items():
    open(os.path.join(OUT, k), 'w', encoding='utf-8').write(v)
print('ok')
