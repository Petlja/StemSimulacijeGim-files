from simanim import *

visina_bicikla_u_metrima = 1
sirina_bicikla_u_metrima = visina_bicikla_u_metrima * 1000 / 620
visina_scene_u_metrima = visina_bicikla_u_metrima * 2
sirina_scene_u_metrima = visina_scene_u_metrima * 6614 / 3000

broj_piksela_po_metru = 150

def setup(m):
    PixelsPerUnit(broj_piksela_po_metru)
    ViewBox((0, 0), sirina_scene_u_metrima, visina_scene_u_metrima)

    m.x = 0
    m.y = 0
    m.v = InputFloat(0.3, (0, 1))
    m.a = InputFloat(0.2, (0, 1))

def update(m):
    # Овде заврши изразе за промену позиције и промену брзине након протеклог времена m.dt
    deltaX = ???
    deltaV = ???
    m.x += deltaX
    m.v += deltaV

def draw(m):
    scena = Image('bicycle_background.jpg', (0, 0), sirina_scene_u_metrima, visina_scene_u_metrima)
    bicikl = Image('bicikl.png', (m.x, m.y), sirina_bicikla_u_metrima, visina_bicikla_u_metrima)
    Draw(scena, bicikl)

Run(setup, update, draw)