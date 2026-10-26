import schemdraw
import schemdraw.elements as eln

with schemdraw.Drawing() as d:
  eln.Resistor().right().label ('R1\n330 Ω')
  eln.Line().down()
  eln.LED().left().label('LED1')
  eln.SourceV().label('SV')
