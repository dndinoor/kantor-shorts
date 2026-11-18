import math, random, subprocess, sys, os
from PIL import Image, ImageDraw, ImageFont
from multiprocessing import Pool

W, H, FPS = 1080, 1920, 30
OUT = os.path.dirname(os.path.abspath(__file__))
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # Poppins/Montserrat tidak terpasang
BG=(15,27,45); OILC=(22,49,77); OILD=(46,111,163)
ORA=(242,165,65); STE=(159,179,200); BAS=(92,107,128); HUB=(62,76,96)
SPR=(61,220,151); PRS=(232,238,245); YEL=(255,225,77); RED=(255,77,77); WHT=(255,255,255)
SCENES=[("s1",6.0,5.0),("s2",10.8,11.0),("s3",10.6,10.0),("s4",9.0,8.0),("s5",11.8,11.0),("s6",3.0,3.0)]  # nama, durasi nyata, durasi storyboard

def ease(t): t=max(0,min(1,t)); return 3*t*t-2*t**3
def lerp(a,b,t): return a+(b-a)*t
def mix(c1,c2,t): return tuple(int(lerp(c1[i],c2[i],t)) for i in range(3))
def pulse(t,a,b,c,d): return ease((t-a)/(b-a)) - ease((t-c)/(d-c))
_fc={}
def font(sz):
    sz=int(sz)
    if sz not in _fc: _fc[sz]=ImageFont.truetype(FONT,sz)
    return _fc[sz]

class Tf:
    def __init__(s,z=1.0,fx=540,fy=860): s.z,s.fx,s.fy=z,fx,fy
    def p(s,x,y): return (540+(x-s.fx)*s.z, 860+(y-s.fy)*s.z)
    def box(s,x0,y0,x1,y1):
        a=s.p(x0,y0); b=s.p(x1,y1); return [a[0],a[1],b[0],b[1]]

def rrect(d,tf,x0,y0,x1,y1,fill,r=5):
    d.rounded_rectangle(tf.box(x0,y0,x1,y1),radius=max(1,r*tf.z),fill=fill)

def arrow(d,p0,p1,col,w=14,head=36):
    ang=math.atan2(p1[1]-p0[1],p1[0]-p0[0]); L=math.hypot(p1[0]-p0[0],p1[1]-p0[1])
    b=(p1[0]-head*math.cos(ang)*0.8,p1[1]-head*math.sin(ang)*0.8)
    d.line([p0,b],fill=col,width=int(w))
    n=(-math.sin(ang),math.cos(ang))
    d.polygon([p1,(b[0]+n[0]*head*0.6,b[1]+n[1]*head*0.6),(b[0]-n[0]*head*0.6,b[1]-n[1]*head*0.6)],fill=col)

def spring(d,tf,x,y0,y1,col,n=6,wid=34):
    pts=[tf.p(x,y0)]
    for k in range(n*2):
        yy=y0+(y1-y0)*(k+0.5)/(n*2); pts.append(tf.p(x+(wid if k%2 else -wid)/2,yy))
    pts.append(tf.p(x,y1)); d.line(pts,fill=col,width=max(2,int(6*tf.z)),joint="curve")

def stack(im,tf,st,g=0.0,ex=0.0,heat=0.0,wear=0.0,hl=None,hlp=0.0,dim=False,oil=1.0,jit=0.0,t=0.0,spr_col=SPR,tick=True):
    d=ImageDraw.Draw(im,"RGBA")
    def c(base,kind=None):
        if dim and hl is not None and kind!=hl and kind!='hl_all': return mix(base,BG,0.6)
        if kind==hl and hl is not None: return mix(base,WHT,0.30*hlp)
        return base
    # oil
    if oil>0:
        top=1070-(1070-500)*oil
        d.rectangle(tf.box(125,top,955,1090),fill=OILC+(255,))
    # frame
    wallc=c(BAS,'b'); 
    rrect(d,tf,150,520,930,560,wallc); rrect(d,tf,150,520,205,1084,wallc); rrect(d,tf,875,520,930,1084,wallc)
    rrect(d,tf,150,1050,930,1084,wallc)
    if hl=='b' and hlp>0:
        for x0,x1 in((150,205),(875,930)): rrect(d,tf,x0,520,x1,1084,mix(BAS,YEL,0.8*hlp))
    rrect(d,tf,470,740,610,1050,c(HUB,'h'))
    if hl=='h' and hlp>0: rrect(d,tf,470,740,610,1050,mix(HUB,YEL,0.8*hlp))
    oc=mix(ORA,RED,heat)
    ph={'o':st['po'],'s':st['pi']}
    for i in range(8):
        kind='o' if i%2==0 else 's'
        y=724+34*i+(i-3.5)*ex-(7-i)*g
        if jit: y+=jit*math.sin(t*55+i*2.1)
        h=32.0
        if kind=='o': h-=8*wear
        yy0=y+(32-h)/2; yy1=yy0+h
        col=c(oc if kind=='o' else STE,kind)
        spans=[(205,420),(660,875)] if kind=='o' else [(250,470),(610,830)]
        for (a,b) in spans:
            rrect(d,tf,a,yy0,b,yy1,col,4)
            tabw=30
            tabc=mix(col,BG,0.28)
            if kind=='o':
                ta=(a,a+tabw) if a<540 else (b-tabw,b)
            else:
                ta=(b-tabw,b) if a<540 else (a,a+tabw)
            rrect(d,tf,ta[0],yy0,ta[1],yy1,tabc,3)
            if tick:
                L=b-a; tc=mix(col,BG,0.55)
                for k in range(-1,int(L/46)+2):
                    xx=a+((k*46+ph[kind])%(L+46))-23
                    x0=max(a+tabw*(1 if (kind=='o' and a<540) or (kind=='s' and a>540) else 0),xx)
                    x1=min(b-tabw*(0 if (kind=='o' and a<540) or (kind=='s' and a>540) else 1),xx+8)
                    if x1>x0 and (x1-x0)>1: d.rectangle(tf.box(x0,yy0+8,x1,yy1-8),fill=tc)
    py=690-8*g-4.5*ex
    rrect(d,tf,210,py,870,py+32,c(PRS),5)
    for x in (300,540,780): spring(d,tf,x,560,py,spr_col)
    # oil dots
    if oil>0:
        top=1070-(1070-500)*oil
        ov=Image.new("RGBA",im.size,(0,0,0,0)); od=ImageDraw.Draw(ov)
        rnd=random.Random(5)
        for k in range(46):
            bx=rnd.uniform(135,945); by=rnd.uniform(0,1); sp=rnd.uniform(8,22); r=rnd.uniform(3,6)
            yy=top+((by*(1090-top)-t*sp)%(1090-top)); xx=bx+8*math.sin(t*1.3+k)
            if yy>top+4:
                pp=tf.p(xx,yy); od.ellipse([pp[0]-r*tf.z,pp[1]-r*tf.z,pp[0]+r*tf.z,pp[1]+r*tf.z],fill=OILD+(150,))
        im.alpha_composite(ov)

# ---------- teks ----------
def seg_w(seg,sz):
    if seg=='ARROW': return sz*1.1
    t,col=seg[0],seg[1]; sc=seg[2] if len(seg)>2 else 1
    return font(sz*sc).getlength(t)
def draw_text(im,lines,y,size,alpha,rise=0,maxw=840):
    if alpha<=0.01: return
    # fit
    sz=size
    while sz>30 and max(sum(seg_w(s,sz) for s in ln) for ln in lines)>maxw: sz-=2
    lh=int(sz*1.28); hh=lh*len(lines)+30
    layer=Image.new("RGBA",(W,hh),(0,0,0,0)); d=ImageDraw.Draw(layer)
    mw=max(sum(seg_w(s,sz) for s in ln) for ln in lines)
    cx=490
    d.rounded_rectangle([cx-mw/2-26,2,cx+mw/2+26,hh-4],radius=26,fill=BG+(150,))
    for li,ln in enumerate(lines):
        tw=sum(seg_w(s,sz) for s in ln); x=cx-tw/2; yy=18+li*lh
        for s in ln:
            if s=='ARROW':
                a=int(sz*0.55); m=yy+sz*0.62
                d.line([(x+4,m),(x+sz*0.85,m)],fill=WHT,width=int(sz*0.12))
                d.polygon([(x+sz*1.05,m),(x+sz*0.7,m-a*0.5),(x+sz*0.7,m+a*0.5)],fill=WHT)
                x+=sz*1.1; continue
            t,col=s[0],s[1]; sc=s[2] if len(s)>2 else 1; f=font(sz*sc)
            d.text((x,yy+sz*(1-sc)*0.55),t,font=f,fill=col,stroke_width=max(3,int(sz/14)),stroke_fill=BG)
            x+=f.getlength(t)
    if alpha<1: layer.putalpha(layer.getchannel("A").point(lambda v:int(v*alpha)))
    im.alpha_composite(layer,(0,int(y+rise)))
def T(t,t0,t1,lines,y,size):  # fade in 0.25s, naik 20px, out 0.15
    return (t0,t1,lines,y,size)
def show_texts(im,tt,texts):
    for (t0,t1,lines,y,size) in texts:
        if t0<=tt<=t1:
            a=ease((tt-t0)/0.25)*ease((t1-tt)/0.15) if t1-t0>0.5 else 1
            draw_text(im,lines,y,size,a,(1-ease((tt-t0)/0.25))*20)
TOP,BOT=240,1190

# ---------- ikon ----------
def lever_icon(d,cx,cy,s,ang,col=PRS,bar=BAS):
    # tuas generik tampak samping: batang setang + tuas berputar
    d.rounded_rectangle([cx-110*s,cy+34*s,cx+110*s,cy+70*s],radius=14*s,fill=bar)
    px,py=cx-100*s,cy+10*s; L=210*s
    a=math.radians(-ang); ux,uy=math.cos(a),math.sin(a); nx,ny=-uy,ux; w=15*s
    d.polygon([(px+nx*w,py+ny*w),(px+ux*L+nx*w*0.6,py+uy*L+ny*w*0.6),(px+ux*L-nx*w*0.6,py+uy*L-ny*w*0.6),(px-nx*w,py-ny*w)],fill=col)
    d.ellipse([px-18*s,py-18*s,px+18*s,py+18*s],fill=HUB,outline=col,width=int(4*s))
def gear_icon(d,cx,cy,r,col):
    for k in range(8):
        a=k*math.pi/4
        d.polygon([(cx+math.cos(a-0.2)*r*0.8,cy+math.sin(a-0.2)*r*0.8),(cx+math.cos(a-0.15)*r*1.2,cy+math.sin(a-0.15)*r*1.2),(cx+math.cos(a+0.15)*r*1.2,cy+math.sin(a+0.15)*r*1.2),(cx+math.cos(a+0.2)*r*0.8,cy+math.sin(a+0.2)*r*0.8)],fill=col)
    d.ellipse([cx-r,cy-r,cx+r,cy+r],fill=col); d.ellipse([cx-r*0.4,cy-r*0.4,cx+r*0.4,cy+r*0.4],fill=BG)
def engine_icon(d,cx,cy,r,col,spin):
    d.rounded_rectangle([cx-r,cy-r*0.8,cx+r,cy+r*0.8],radius=14,fill=col)
    d.ellipse([cx-r*0.5,cy-r*0.5,cx+r*0.5,cy+r*0.5],fill=BG)
    a=spin; d.line([(cx,cy),(cx+math.cos(a)*r*0.45,cy+math.sin(a)*r*0.45)],fill=col,width=8)
def flow(im,t,x0,x1,y,col,alpha=1.0,broken_at=None):
    d=ImageDraw.Draw(im,"RGBA"); a=int(255*alpha)
    k=0; x=x0-((t*160)%70)
    while x<x1:
        xa=max(x,x0); xb=min(x+40,x1)
        if xb>xa:
            if broken_at is not None and xa>=broken_at: c=(*GRY,int(90*alpha))
            else: c=(*col,a)
            d.rectangle([xa,y-9,xb,y+9],fill=c)
        x+=70
    if broken_at is None: d.polygon([(x1,y),(x1-34,y-26),(x1-34,y+26)],fill=(*col,a))
GRY=(92,107,128)
def cross(d,cx,cy,r,col,w=22):
    d.line([(cx-r,cy-r),(cx+r,cy+r)],fill=col,width=w); d.line([(cx-r,cy+r),(cx+r,cy-r)],fill=col,width=w)
def check(d,cx,cy,r,col,w=24):
    d.line([(cx-r,cy),(cx-r*0.3,cy+r*0.7),(cx+r,cy-r*0.7)],fill=col,width=w,joint="curve")

# ---------- adegan ----------
def new(): return Image.new("RGBA",(W,H),BG+(255,))

def sc1(t,st,tt):
    im=new(); d=ImageDraw.Draw(im,"RGBA")
    if tt<1.5:
        ang=38*ease((tt-0.3)/0.6)
        cx,cy=540,900; s=2.4
        lever_icon(d,cx,cy,s,ang)
        # panah melengkung kuning
        px,py=cx-100*s,cy+10*s; R=215*s
        a1=math.radians(-ang-4)
        pts=[(px+R*math.cos(-math.radians(q)),py+R*math.sin(-math.radians(q))) for q in range(3,int(max(6,ang))+1,2)]
        if len(pts)>1:
            d.line(pts,fill=YEL,width=16); 
            e=pts[-1]; p=pts[-2]; arrow(d,p,(e[0]+(e[0]-p[0])*3,e[1]+(e[1]-p[1])*3),YEL,16,44)
    else:
        u=(tt-1.5)/3.5
        z=1+1.2*ease((tt-1.5)/1.5)
        gp=max(pulse(tt,2.6,3.2,3.7,4.1),pulse(tt,4.4,4.9,5.3,5.8)*1.0) if tt<5 else 0
        gp=max(pulse(tt,2.5,3.1,3.6,4.0),pulse(tt,4.2,4.7,5.0,5.0+1e-3)) if False else max(pulse(tt,2.4,3.0,3.5,3.9),pulse(tt,4.1,4.6,4.9,5.0))
        g=9*gp
        tf=Tf(z,330,722)
        stack(im,tf,st,g=g,t=tt)
        d=ImageDraw.Draw(im,"RGBA")
        cxy=tf.p(330,722-4*g); r=(46+8*math.sin(tt*9))*(0.6+0.4*min(z/2.2,1))*1.3
        if gp>0.02 or True:
            d.ellipse([cxy[0]-r,cxy[1]-r,cxy[0]+r,cxy[1]+r],outline=YEL+(int(255*min(1,(tt-2)/0.4)),),width=8)
        if tt>2.6:
            f=font(70); d.text((cxy[0]+r*0.9,cxy[1]-r*1.6),"?",font=f,fill=YEL,stroke_width=5,stroke_fill=BG)
    show_texts(im,tt,[(0.1,5.0,[[("Tarik tuas kopling...",WHT)],[("di dalam cuma gerak ",WHT),("SEGINI.",YEL,1.2)]],TOP,84)])
    return im,0,0

def sc2(t,st,tt):
    im=new()
    z=1+0.5*(1-ease(tt/2.5)) if tt<3 else 1.0
    oil=ease(tt/1.0)
    ex=14*(ease((tt-3.0)/0.8)-ease((tt-5.2)/0.8)) 
    hl=None;hlp=0;dim=False
    if 3.4<tt<5.2:
        ph=(tt-3.4)/0.9; hl='o' if int(ph)%2==0 else 's'; hlp=0.5+0.5*math.sin((ph%1)*math.pi); 
    if 6<=tt<8.5: hl='o';dim=True;hlp=1; 
    if 8.5<=tt: hl='s';dim=True;hlp=1
    k=None
    # baskets/hub flash (kuning sekali)
    if 6.8<tt<7.6: pass
    stack(im,Tf(z,540,860),st,g=0,ex=ex,hl=hl,hlp=hlp,dim=dim,oil=oil,t=tt,tick=True)
    if 6.6<tt<8.3:
        # keranjang berkedip kuning sekali (tumpuk di atas dinding)
        a=math.sin((tt-6.6)/1.7*math.pi); d=ImageDraw.Draw(im,"RGBA"); tf=Tf(z,540,860)
        for x0,x1 in((150,205),(875,930)): d.rounded_rectangle(tf.box(x0,520,x1,1084),radius=5,fill=YEL+(int(220*a),))
    if 9.1<tt<10.7:
        a=math.sin((tt-9.1)/1.6*math.pi); d=ImageDraw.Draw(im,"RGBA"); tf=Tf(z,540,860)
        d.rounded_rectangle(tf.box(470,740,610,1050),radius=5,fill=YEL+(int(220*a),))
    show_texts(im,tt,[(0.1,3.0,[[("Kopling basah",WHT)],[("(terendam oli)",(120,190,240))]],BOT,70),
        (3.1,4.6,[[("Pelat gesek",ORA)]],BOT,76),(4.6,6.0,[[("Pelat baja",STE)]],BOT,76),
        (6.0,8.5,[[("Keranjang luar",(190,205,225))]],BOT,70),(8.5,11,[[("Hub dalam",(190,205,225))]],BOT,70)])
    return im,6,6

def lever_corner(im,ang,alpha=1.0):
    ov=Image.new("RGBA",(W,H),(0,0,0,0)); d=ImageDraw.Draw(ov); lever_icon(d,200,560,1.0,ang)
    if alpha<1: ov.putalpha(ov.getchannel("A").point(lambda v:int(v*alpha)))
    im.alpha_composite(ov)

def dir_arrows(im,tf,t,alpha):
    d=ImageDraw.Draw(im,"RGBA"); a=int(255*alpha)
    for x in (420,660):
        yo=6*math.sin(t*8)
        arrow(d,tf.p(x,585+yo),tf.p(x,672+yo),SPR+(a,),max(6,int(14*tf.z)),int(34*tf.z))

def sc3(t,st,tt):
    im=new()
    g=9*(1-ease((tt-0.3)/1.0))
    z=1+0.55*(ease((tt-3.0)/0.7)-ease((tt-5.6)/0.6))
    tf=Tf(z,540,860)
    spin=6.0 if tt>6 else (3*ease(tt/6) if tt>2 else 0)
    stack(im,tf,st,g=g,t=tt)
    if tt<3.2: dir_arrows(im,tf,tt,1.0)
    d=ImageDraw.Draw(im,"RGBA")
    if 3.0<tt<6:
        a=ease((tt-3.2)/0.4)
        for i in range(8):
            y=724+34*i+16
            for x in (330,750):
                p=tf.p(x,y); s=6*tf.z
                d.polygon([(p[0]-s*1.4,p[1]-s*0.7),(p[0]+s*1.4,p[1]-s*0.7),(p[0],p[1]+s*0.8)],fill=SPR+(int(230*a),))
    lever_corner(im,38*(1-ease(tt/1.2)) if tt<1.5 else 0)
    if tt>5.8:
        a=ease((tt-6)/0.6); ov=Image.new("RGBA",(W,H),(0,0,0,0)); od=ImageDraw.Draw(ov)
        engine_icon(od,150,1115,56,PRS,tt*6); gear_icon(od,930,1115,52,PRS)
        od.text((150,1190),"mesin",font=font(34),fill=WHT,anchor="mm",stroke_width=3,stroke_fill=BG)
        od.text((920,1190),"transmisi",font=font(34),fill=WHT,anchor="mm",stroke_width=3,stroke_fill=BG)
        ov.putalpha(ov.getchannel("A").point(lambda v:int(v*a))); im.alpha_composite(ov)
        flow(im,tt,230,860,1115,YEL,a)
    show_texts(im,tt,[(0.1,10,[[("Tuas dilepas =",WHT)],[("TERHUBUNG",SPR)]],TOP,88),
        (1.2,10,[[("Pegas",SPR),'ARROW',("pelat penekan",WHT)],[('ARROW'),],][:0] or [[("Pegas",SPR),'ARROW',("penekan",WHT)],[('ARROW',),("terjepit",YEL)]][:0] or [[("Pegas",SPR),'ARROW',("pelat penekan",WHT),'ARROW',("terjepit",YEL)]],BOT+10,54)])
    return im,spin,spin

def sc4(t,st,tt):
    im=new()
    gopen=ease((tt-0.2)/1.2)
    if tt<5.5: g=10*gopen
    else: g=10*(1-pulse(tt,5.5,6.1,7.0,7.6)) if tt<7.0 else 10*ease((tt-7.0)/0.6)
    if 5.5<=tt<7.0: g=10*(1-ease((tt-5.5)/0.6))
    z=1+0.8*ease((tt-0.8)/1.7) - 0.8*ease((tt-3.6)/0.8) if tt<5 else 1.0
    tf=Tf(z,540+(330-540)*ease(min(1,(tt-0.8)/1.7))*(1-ease((tt-3.6)/0.8)) if tt<5 else 540, 860+(740-860)*ease(min(1,(tt-0.8)/1.7))*(1-ease((tt-3.6)/0.8)) if tt<5 else 860)
    spin_o=7.0 if tt>2.3 else 7*ease(tt/2.3)
    vi=spin_o*(1-min(g/10,1))
    stack(im,tf,st,g=g,t=tt,spr_col=SPR)
    d=ImageDraw.Draw(im,"RGBA")
    if 1.8<tt<4.6:
        a=ease((tt-1.8)/0.4); x=170; y0=tf.p(x,724-9*0)[1]
        pa=tf.p(x,724-7*g+0); pb=tf.p(x,724-8*g)
        # garis ukur celah antara pelat penekan dan pelat teratas
        top=tf.p(x,724-7*g); bot=tf.p(x,724-7*g-g)
        d.line([(top[0],top[1]+8),(bot[0],bot[1]-8)],fill=YEL+(int(255*a),),width=5)
        for yy in (top[1]+8,bot[1]-8): d.line([(top[0]-22,yy),(top[0]+22,yy)],fill=YEL+(int(255*a),),width=5)
    lever_corner(im,38*ease((tt-0.1)/0.6) if tt<5.5 else 38*(pulse(tt,7.0,7.6,99,100)) if tt>=7.0 else 0, 1.0) if tt<5.5 or tt>=6.9 or True else None
    if tt>3.6:
        a=ease((tt-3.8)/0.6); ov=Image.new("RGBA",(W,H),(0,0,0,0)); od=ImageDraw.Draw(ov)
        engine_icon(od,150,1115,56,PRS,tt*9); gear_icon(od,930,1115,52,mix(PRS,BG,0.25))
        ov.putalpha(ov.getchannel("A").point(lambda v:int(v*a))); im.alpha_composite(ov)
        if g>5: flow(im,tt,230,470,1115,YEL,a,None); 
        if g>5:
            dd=ImageDraw.Draw(im,"RGBA"); cross(dd,520,1115,22,RED+(int(255*a),),10)
            for x in range(590,860,60): dd.rectangle([x,1106,x+28,1124],fill=(*GRY,int(120*a)))
        else:
            flow(im,tt,230,860,1115,YEL,a)
    if tt>5.3:
        d=ImageDraw.Draw(im,"RGBA"); lab=("nyambung",SPR) if g<5 else ("putus",RED)
        d.text((540,505),lab[0],font=font(52),fill=lab[1],anchor="mm",stroke_width=5,stroke_fill=BG)
    show_texts(im,tt,[(0.1,8,[[("Tuas ditarik =",WHT)],[("TERPUTUS",RED)]],TOP,88),(1.0,8,[[("Celah cuma",WHT)],[("beberapa milimeter",YEL)]],BOT,62)])
    return im,spin_o,vi

def bike(d,ox,oy,ang,col):
    def R(x,y):
        c,s=math.cos(ang),math.sin(ang); return (ox+x*c-y*s,oy+x*s+y*c)
    for wx in (-62,62):
        p=R(wx,-36); d.ellipse([p[0]-34,p[1]-34,p[0]+34,p[1]+34],fill=col)
    d.polygon([R(x,y-36) for x,y in [(-70,-28),(-30,-32),(10,-62),(50,-66),(70,-30),(24,-18),(-60,-6)]],fill=col)

def sc5(t,st,tt):
    im=new(); d=ImageDraw.Draw(im,"RGBA")
    heat=0;wear=0;g=0;jit=0;dim=False
    if tt<1.8:
        x0,y0,x1,y1=120,1150,950,780
        d.polygon([(x0,y0),(x1,y0),(x1,y1)],fill=HUB+(255,))
        ang=math.atan2(y1-y0,x1-x0)
        for k,f in enumerate((0.25,0.5,0.75)):
            bx=x0+(x1-x0)*f; by=y0+(y1-y0)*f
            bike(d,bx,by-4,ang,BAS)
    else:
        u=(tt-4)/4
        g=1.6; jit=2
        heat=ease((tt-4)/3.5)*(1-ease((tt-9.0)/1.8)); wear=ease((tt-4)/4)
        dim=False
        stack(im,Tf(1.0,540,860),st,g=g,heat=heat,wear=min(wear,1),jit=jit,t=tt)
        d=ImageDraw.Draw(im,"RGBA")
        if tt<4: cross(d,820,540,60,RED+(255,),26)
        if 4<=tt<8:
            rnd=random.Random(int(tt*30))
            for k in range(9):
                i=rnd.randint(0,6); x=rnd.choice([rnd.uniform(250,420),rnd.uniform(660,830)]); y=724+34*i+34
                s=rnd.uniform(4,9); d.polygon([(x,y-s),(x+s,y),(x,y+s),(x-s,y)],fill=rnd.choice([RED,YEL,ORA])+(230,))
            for xb in (100,980):
                pts=[(xb+14*math.sin(yv*0.04+tt*7),yv) for yv in range(1000,640,-12)]
                d.line(pts,fill=RED+(int(220*heat),),width=9)
            # tanda silang tetap kecil
            cross(d,820,540,44,RED+(255,),20)
    if tt>=8:
        # wipe ke ikon rem / netral
        wx=int(W*ease((tt-8.0)/0.5))
        bg=Image.new("RGBA",(W,H),BG+(int(215*ease((tt-8)/0.5)),)); im.alpha_composite(bg)
        ov=Image.new("RGBA",(W,H),(0,0,0,0)); od=ImageDraw.Draw(ov)
        pl=1+0.06*math.sin(tt*8)
        # tuas rem generik
        lever_icon(od,330,860,1.4*pl,18,col=SPR,bar=BAS)
        if tt>9.2: check(od,330,1090,50,SPR)
        od.text((330,1190),"REM",font=font(54),fill=SPR,anchor="mm",stroke_width=5,stroke_fill=BG)
        if tt>9.7:
            a=ease((tt-9.7)/0.3)
            od.rounded_rectangle([650,770,830,950],radius=26,outline=SPR,width=10,fill=(22,60,50,255))
            od.text((740,860),"N",font=font(120),fill=SPR,anchor="mm")
            od.text((740,1190),"NETRAL",font=font(54),fill=SPR,anchor="mm",stroke_width=5,stroke_fill=BG)
            check(od,740,1090,50,SPR)
        crop=ov.crop((0,0,wx,H)); im.alpha_composite(crop,(0,0))
    texts=[(0.1,4.0,[[("JANGAN",RED),(" setengah",WHT)],[("kopling",WHT)]],TOP,84),
        (4.0,8.0,[[("Selip",YEL)]],BOT,76) if False else (4.0,4.9,[[("Selip",YEL)]],BOT,76),
        (4.9,5.8,[[("Selip - ",YEL),("Panas",RED)]],BOT,76),(5.8,8.0,[[("Selip - ",YEL),("Panas - ",RED),("Kampas aus",ORA)]],BOT,60),
        (8.0,11.0,[[("Pakai ",WHT),("REM",SPR),(",",WHT)],[("netral saat berhenti lama",WHT)]],TOP,70)]
    show_texts(im,tt,texts)
    return im,(9 if tt>=4 else 0),(2.5 if tt>=4 else 0)

def sc6(t,st,tt):
    im=new()
    g=7*ease((tt-1.0)/1.7)
    stack(im,Tf(1.0,540,860),st,g=g,t=tt)
    show_texts(im,tt,[(0.05,3,[[("Follow untuk",WHT)],[("bedah isi motor lainnya",WHT)]],300,72)])
    fade=ease((3.0-tt)/0.3)
    if fade<1:
        ov=Image.new("RGBA",(W,H),BG+(int(255*(1-fade)),)); im.alpha_composite(ov)
    return im,0,0

FUNCS={"s1":sc1,"s2":sc2,"s3":sc3,"s4":sc4,"s5":sc5,"s6":sc6}
def render(args):
    name,dur,orig=args
    n=int(round(dur*FPS)); fn=FUNCS[name]
    out=os.path.join(OUT,name+".mp4")
    p=subprocess.Popen(["ffmpeg","-y","-loglevel","error","-f","rawvideo","-pix_fmt","rgb24","-s",f"{W}x{H}","-r",str(FPS),"-i","-","-c:v","libx264","-pix_fmt","yuv420p","-crf","18","-preset","fast",out],stdin=subprocess.PIPE)
    st={'po':0.0,'pi':0.0}
    for f in range(n):
        t=f/FPS; tt=t*orig/dur
        im,vo,vi=fn(t,st,tt)
        st['po']+=vo; st['pi']+=vi
        if len(sys.argv)>1 and sys.argv[1]=="stills" and f in (n//4,n//2,3*n//4):
            im.convert("RGB").save(os.path.join(OUT,f"still_{name}_{f}.png"))
        p.stdin.write(im.convert("RGB").tobytes())
    p.stdin.close(); p.wait(); return name
if __name__=="__main__":
    only=[a for a in sys.argv[2:]] if len(sys.argv)>2 else None
    sc=[s for s in SCENES if not only or s[0] in only]
    with Pool(4) as pl: print(pl.map(render,sc))
