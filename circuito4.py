import schemdraw
import schemdraw.elements as elm

with schemdraw.Drawing() as d:
    d.config (fontsize= 10)
    fonteEnergia = elm.SourceV().up().label ('12 V')
    elm.Resistor().right().label('R1\n100 Ω')
    elm.Resistor().right().label('R2\n220 Ω')
    elm.Resistor().down().label('R3\n330 Ω')
    elm.Line().left().tox(fonteEnergia.start)
