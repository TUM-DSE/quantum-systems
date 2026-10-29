import pathlib,json
root=pathlib.Path(__file__).resolve().parents[1]; out=root/'public/illustrations';out.mkdir(exist_ok=True)
blue='#003359';paper='#f7f8f5'
def line(x1,y1,x2,y2,extra=''):return f'<path d="M{x1} {y1}L{x2} {y2}" {extra}/>'
def rect(x,y,w,h,fill='none',extra=''):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" {extra}/>'
def circle(x,y,r=5,fill=paper,extra=''):return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" {extra}/>'
def path(d,extra=''):return f'<path d="{d}" {extra}/>'
def chip(x,y,w=86):
 s=rect(x,y,w,w,paper)+rect(x+18,y+18,w-36,w-36,blue)
 for i in range(5):
  z=12+i*(w-24)/4
  s+=line(x-10,y+z,x,y+z)+line(x+w,y+z,x+w+10,y+z)+line(x+z,y-10,x+z,y)+line(x+z,y+w,x+z,y+w+10)
 return s
def grid(x,y,cols=5,rows=4,gap=38,filled=()):
 s=''
 for i in range(rows):s+=line(x,y+i*gap,x+(cols-1)*gap,y+i*gap,'opacity=".22"')
 for j in range(cols):s+=line(x+j*gap,y,x+j*gap,y+(rows-1)*gap,'opacity=".22"')
 for i in range(rows):
  for j in range(cols):s+=circle(x+j*gap,y+i*gap,6,blue if (i,j) in filled else paper)
 return s
def arrow(d):return path(d,'marker-end="url(#arrow)"')
def svg(slug,body,title):
 text=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 320" width="180mm" height="96mm" role="img" aria-labelledby="title"><title id="title">{title}</title><defs><marker id="arrow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0 0 6 3 0 6Z" fill="{blue}"/></marker></defs><g id="{slug}" stroke="{blue}" stroke-width="1.6" fill="none" stroke-linejoin="round">{body}</g></svg>'
 (out/(slug+'.svg')).write_text(text+'\n')
s=grid(70,85,4,4,42,[(1,1),(2,2)])+arrow('M228 148H342')+chip(390,112,96)
svg('qtpu',s,'Hybrid tensor network and classical processor')
s=''
for y in [90,135,185,230]:
 s+=line(65,y,535,y)
 for x in [120,260,410]:s+=rect(x,y-13,26,26,paper)
s+=path('M315 55V260','stroke-dasharray="5 6"')+circle(315,90,5,blue)+circle(315,185,5,blue)
s+=arrow('M335 270H470')
svg('qvm',s,'Quantum circuit fragments and a virtual gate boundary')
s=''
for i in range(4):s+=rect(65,65+i*46,105,28,paper)+line(80,79+i*46,140,79+i*46,'opacity=".4"')
s+=path('M195 160H280V75H370M280 160H370M280 160V245H370')
for y in [43,128,213]:s+=chip(390,y,62)
svg('qos',s,'Quantum jobs and shared processing resources')
s=rect(229,113,142,94,paper)+rect(249,134,102,10,blue)+rect(249,158,66,10,blue)+rect(249,182,83,6,blue)
for x,y in [(88,75),(88,227),(470,75),(470,227)]:
 s+=circle(x,y,27,paper)+circle(x,y,9,blue)
 s+=line(x+(-27 if x>300 else 27),y,229 if x<300 else 371,138 if y<160 else 181)
svg('qonductor',s,'A scheduler linking quantum and classical resources')
s=grid(105,65,4,5,45,[(1,1),(2,2),(3,1)])+grid(357,90,3,4,45,[(1,1),(2,0)])
s+=path('M286 50V280','stroke-dasharray="4 6" opacity=".4"')
svg('eccentric',s,'Two quantum error correction code layouts')
s=grid(105,70,8,4,45,[(0,1),(1,3),(2,6),(3,5)])
s+=path('M150 70H240V115M375 160H330V205','stroke-width="3"')
svg('zero-g',s,'Sparse error events and decoder matching paths')
s=''
for x,y in [(125,47),(345,47),(125,190),(345,190)]:s+=chip(x,y,78)
s+=path('M213 86H335M213 229H335M164 135V180M384 135V180','stroke-width="3"')
svg('chipmunq',s,'Four connected quantum chiplets')
s=''
for row in range(4):
 for col in range(8):s+=rect(100+col*48,64+row*48,38,38,blue if (row,col) in [(0,0),(3,7),(2,4),(1,2)] else paper,'opacity=".9"')
s+=arrow('M120 118V183H288')+arrow('M458 183H360')
svg('harvest',s,'Logical patches and magic-state resource routes')
s=''
for row in range(4):
 for col in range(8):
  fill=blue if col==row+1 else paper
  s+=rect(100+col*48,64+row*48,38,38,fill)
s+=path('M120 133H169V181H217V229H265V277H458','stroke-width="3"')+arrow('M360 87H450')+arrow('M360 136H450')
svg('rushhour',s,'Dynamic lattice patches and a reconfigurable routing corridor')
s=rect(65,48,198,224,paper)+rect(337,48,198,224,paper)
s+=grid(95,85,4,4,45,[(0,0),(1,1),(2,2),(3,3)])+grid(370,85,4,4,45,[(0,3),(1,2),(2,1),(3,0)])
s+=arrow('M280 130H320')+arrow('M320 190H280')
svg('weaver',s,'Neutral atom arrays with programmable atom movement')
s=''
for x,y,w,h in [(65,55,190,95),(65,170,190,95),(320,55,215,210)]:s+=rect(x,y,w,h,paper)
s+=grid(92,80,5,2,30)+grid(92,195,5,2,30)+grid(350,85,5,5,36,[(0,0),(1,1),(2,2),(3,3),(4,4)])
s+=arrow('M270 100H304')+arrow('M270 215H304')
svg('multiq',s,'Independent quantum programs sharing neutral atom zones')
wave='M65 165'
for x,y in [(85,165),(98,110),(113,210),(128,125),(142,195),(157,145),(172,179),(190,158),(210,165)]:wave+=f'L{x} {y}'
s=path(wave,'stroke-width="2"')+arrow('M230 165H295')+rect(312,128,88,74,paper)+path('M400 165H450V90H520M450 165V240H520')+circle(535,90,10,blue)+circle(535,240,10)
svg('mcmit',s,'Qubit readout with conditional branch control')
s=line(85,245,290,245,'opacity=".3"')+line(85,245,85,60,'opacity=".3"')
for i in range(18):
 x=135+(i*17%53);y=105+(i*23%58);s+=circle(x,y,3,blue)
for i in range(18):
 x=207+(i*19%53);y=165+(i*29%58);s+=circle(x,y,3,paper)
s+=arrow('M310 160H370')+grid(405,103,3,4,37,[(1,1),(2,2)])
svg('oraqle',s,'Qubit-state signal clusters and an error correction code')
s=''
for i in range(5):s+=rect(58+i*24,125,14,70-(i%3)*13,blue)
s+=arrow('M198 160H246')+rect(265,105,110,110,paper)
s+=path('M375 160H420V88H465M420 160V232H465')+rect(480,58,68,60,paper)+rect(480,202,68,60,blue)
svg('mamba-readout',s,'Readout sequences with classification and refinement stages')
hero='<g opacity=".13">'+path('M35 324 300 171 570 326M35 354 300 201 570 356M35 384 300 231 570 386')+'</g>'
for cx,cy,kind in [(172,252,'classical'),(420,133,'quantum')]:
 hero+=f'<g id="{kind}-processor"><g transform="matrix(1 .55 -1 .55 {cx} {cy+16})">'+rect(-72,-72,144,144,paper)+'</g>'
 hero+=f'<g transform="matrix(1 .55 -1 .55 {cx} {cy})">'+rect(-72,-72,144,144,paper)+rect(-60,-60,120,120,paper)
 if kind=='classical':
  hero+=rect(-34,-34,68,68,blue)
  for i in range(7):
   z=-27+i*9
   hero+=line(-50,z,-37,z)+line(37,z,50,z)+line(z,-50,z,-37)+line(z,37,z,50)
 else:
  hero+=grid(-44,-44,5,5,22,[(1,1),(2,2),(3,3),(0,4)])
 hero+='</g></g>'
hero+=path('M252 298 310 331 418 269 418 229M268 289 310 313 402 260 402 220M284 280 310 295 386 251 386 211','stroke-width="2"')
hero+=circle(418,229,4,blue)+circle(402,220,4,blue)+circle(386,211,4,blue)
(out/'hero.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="180mm" height="132mm" viewBox="0 0 600 440" role="img" aria-labelledby="title"><title id="title">Classical and quantum processors linked by a shared system</title><g stroke="{blue}" stroke-width="1.4" fill="none" stroke-linejoin="round">{hero}</g></svg>\n')
