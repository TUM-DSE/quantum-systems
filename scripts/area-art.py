from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'public' / 'illustrations'
BLUE = '#003359'
PAPER = '#f7f8f5'


def line(x1, y1, x2, y2, opacity=1, width=1.4):
    return f'<path d="M{x1} {y1}L{x2} {y2}" opacity="{opacity}" stroke-width="{width}"/>'


def path(d, width=1.4, opacity=1):
    return f'<path d="{d}" opacity="{opacity}" stroke-width="{width}"/>'


def rect(x, y, w, h, fill=PAPER, opacity=1, width=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" opacity="{opacity}" stroke-width="{width}"/>'


def circle(x, y, r=4, fill=PAPER, opacity=1, width=1.4):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" opacity="{opacity}" stroke-width="{width}"/>'


def plane(cx, cy, body, name):
    return f'<g id="{name}" transform="matrix(1 .55 -1 .55 {cx} {cy})">{body}</g>'


def tile(cx, cy, size, body, name, depth=12):
    half = size / 2
    lower = plane(cx, cy + depth, rect(-half, -half, size, size), f'{name}-base')
    upper = plane(cx, cy, rect(-half, -half, size, size) + rect(-half+10, -half+10, size-20, size-20) + body, name)
    return lower + upper


def grid(start=-50, n=6, step=20, filled=(), opacity=.55):
    s = ''
    for i in range(n):
        s += line(start, start+i*step, start+(n-1)*step, start+i*step, .18, 1)
        s += line(start+i*step, start, start+i*step, start+(n-1)*step, .18, 1)
    for row in range(n):
        for col in range(n):
            s += circle(start+col*step, start+row*step, 3.5, BLUE if (row,col) in filled else PAPER, 1 if (row,col) in filled else opacity, 1.1)
    return s


def save(slug, title, body):
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="180mm" height="108mm" viewBox="0 0 600 360" role="img" aria-labelledby="title"><title id="title">{escape(title)}</title><g id="{slug}" stroke="{BLUE}" stroke-width="1.4" fill="none" stroke-linejoin="round" stroke-linecap="round">{body}</g></svg>'
    (OUT / f'{slug}.svg').write_text(svg+'\n')


cpu = rect(-29,-29,58,58,BLUE)
for i in range(7):
    z=-24+i*8
    cpu += line(-44,z,-32,z)+line(32,z,44,z)+line(z,-44,z,-32)+line(z,32,z,44)
quantum = grid(-40,5,20,[(1,1),(2,2),(3,3),(0,4)])
s = tile(405,112,130,quantum,'quantum-processor')
s += tile(175,218,130,cpu,'classical-processor')
s += path('M248 261L302 291L408 230V196M264 252L302 273L392 222V187M280 243L302 255L376 213V178',2)
for x,y in [(408,196),(392,187),(376,178)]:
    s += circle(x,y,3.2,BLUE)
save('area-hybrid','Classical and quantum processors connected by shared execution paths',s)

s = tile(300,232,142,grid(filled=[(2,1),(3,4)]),'syndrome-layer-1',8)
s += tile(300,180,142,grid(filled=[(1,2),(4,4)]),'syndrome-layer-2',8)
top = grid(filled=[(1,1),(2,3),(3,4),(4,2)])
top += path('M-30 -30H10V-10M30 10V30H-10',3.2)
for x,y in [(-30,-30),(10,-10),(30,10),(-10,30)]:
    top += circle(x,y,4.8,BLUE)
s += tile(300,128,142,top,'decoding-layer',8)
save('area-error-correction','Layered syndrome lattices with highlighted decoder matching paths',s)

patches = ''
for row in range(6):
    for col in range(6):
        filled=(row,col) in [(0,1),(1,4),(3,2),(4,0),(5,4)]
        patches += rect(-81+col*28,-81+row*28,22,22,BLUE if filled else PAPER,1 if filled else .4,1.1)
patches += path('M-28 -85V-28H28V56H84',3)
patches += path('M-86 28H0V84',2.3,.65)
s = tile(355,145,200,patches,'logical-patch-layout')
factory = rect(-22,-22,44,44,BLUE)
factory += rect(-16,-16,12,12,PAPER)+rect(4,4,12,12,PAPER)
s += tile(130,222,88,factory,'resource-factory')
s += path('M174 246L218 270L279 236V214M162 253L218 284L293 243V222',2)
s += circle(279,214,3,BLUE)+circle(293,222,3,BLUE)
save('area-compilation','Logical patches and routing lanes connected to a resource-state factory',s)

atoms = ''
empty={(0,3),(3,5),(4,1)}
for row in range(6):
    for col in range(6):
        x,y=-60+col*24,-60+row*24
        atoms += circle(x,y,6,'none',.25,1)
        if (row,col) not in empty:
            atoms += circle(x,y,2.9,BLUE,.7,1)
atoms += path('M-36 -36C-55 -70 -4 -92 12 -60',2)
atoms += path('M12 12C22 42 64 48 60 12',2)
atoms += path('M-12 36C-8 62 -51 70 -36 36',2)
for x,y in [(-36,-36),(12,12),(-12,36)]:
    atoms += circle(x,y,4.5,BLUE)
atoms += line(36,-12,60,-12,1,3)
atoms += circle(36,-12,4.5,BLUE)+circle(60,-12,4.5,BLUE)
s = tile(300,185,174,atoms,'atom-array',9)
s += plane(300,185,path('M-100 -70V70M100 -70V70',2,.5),'transport-rails')
save('area-neutral-atoms','An atom array with transport trajectories and an interacting atom pair',s)

resonator=path('M-38 -34H26V-20H-26V-6H26V8H-26V22H26V36H-38',2)
resonator+=rect(31,-28,10,56,BLUE)
s=tile(182,130,126,resonator,'readout-resonator')
controller=rect(-28,-28,56,56,BLUE)
for i in range(5):
    y=-22+i*11
    controller+=line(-46,y,-31,y)+line(31,y,46,y)
s+=tile(420,228,126,controller,'feedback-controller')
s+=path('M250 166L286 186L300 178L316 203L329 188L342 216L354 209',2.2)
s+=path('M237 173L286 201L300 193L316 218L329 203L342 231L354 224',1.5,.45)
s+=path('M363 272L308 304L202 246V214',1.5)
s+=circle(202,214,3,BLUE)
save('area-readout','Qubit readout hardware connected to a classical feedback controller',s)
