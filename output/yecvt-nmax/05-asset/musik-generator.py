import numpy as np, wave, sys
sr=44100; bpm=100; beat=60/bpm; T=38.0
n=int(sr*T); L=np.zeros(n); R=np.zeros(n)
def hz(m): return 440*2**((m-69)/12)
chords=[[57,60,64],[53,57,60],[48,52,55],[55,59,62]]  # Am F C G
bar=4*beat
def add(buf,t0,sig,g):
    i=int(t0*sr); e=min(n,i+len(sig))
    if i<n: buf[i:e]+=sig[:e-i]*g
rng=np.random.default_rng(1)
for b in range(int(T/bar)+1):
    ch=chords[b%4]; t0=b*bar
    # pad
    tt=np.arange(int(bar*1.15*sr))/sr
    env=np.minimum(tt/0.5,1)*np.exp(-np.maximum(tt-bar,0)*8)
    pad=sum(np.sin(2*np.pi*hz(m)*tt)+0.4*np.sin(2*np.pi*hz(m)*2*tt) for m in ch)*env/6
    add(L,t0,pad,0.5); add(R,t0,pad,0.5)
    # bass
    tb=np.arange(int(beat*2*sr))/sr
    bs=np.sin(2*np.pi*hz(ch[0]-12)*tb)*np.exp(-tb*2.5)*np.minimum(tb/0.01,1)
    for k in (0,2): add(L,t0+k*beat,bs,0.35); add(R,t0+k*beat,bs,0.35)
    # arpeggio pluck on 8ths
    for k in range(8):
        m=ch[[0,1,2,1,0,1,2,1][k]]+12
        tp=np.arange(int(0.5*sr))/sr
        p=(np.sin(2*np.pi*hz(m)*tp)+0.3*np.sin(2*np.pi*hz(m)*2*tp))*np.exp(-tp*7)*np.minimum(tp/0.004,1)
        pan=0.3+0.4*(k%2)
        add(L,t0+k*beat/2,p,0.18*(1-pan)*2); add(R,t0+k*beat/2,p,0.18*pan*2)
    # soft hat
    for k in range(8):
        th=np.arange(int(0.05*sr))/sr
        h=rng.standard_normal(len(th))*np.exp(-th*70)
        add(L,t0+k*beat/2+beat/4*0,h,0.03*(1 if k%2 else .5)); add(R,t0+k*beat/2,h,0.03*(1 if k%2 else .5))
m=np.stack([L,R],1)
m/=np.abs(m).max(); m*=0.8
f=np.minimum(np.arange(n)/(sr*1.5),1)*np.minimum((n-np.arange(n))/(sr*2.5),1)
m*=f[:,None]
w=wave.open(sys.argv[1],'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(sr)
w.writeframes((m*32767).astype('<i2').tobytes()); w.close()
