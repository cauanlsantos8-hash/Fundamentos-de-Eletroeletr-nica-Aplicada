import schemdraw
import schemdraw.elements as elm

with schemdraw.Drawing() as d:
    d.config(fontsize=10)
    bat = elm.BatteryCell().up().label('6V').color('blue').linewidth(3).flip().scale(2)
    elm.Switch(action="close").right().label('S1').color('pink').linewidth(3)
    elm.Lamp().down().label('L1').color('blue').fill('pink').linewidth(3)
    elm.Line().left().color('pink').linewidth(3).linestyle('--')
