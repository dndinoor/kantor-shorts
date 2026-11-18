import numpy as np, wave
sr=44100; D=51.2; n=int(sr*D); t=np.arange(n)/sr
rng=np.random.default_rng(7)
# pad: Am9-ish chord, detuned sines, slow tremolo
notes=[110.0,164.81,220.0,261.63,329.63,246.94]
pad=np.zeros(n)
for i,f in enumerate(notes):
    for d in (-0.4,0.4):
        pad+=np.sin(2*np.pi*(f+d)*t+i)*(0.6+0.4*np.sin(2*np.pi*(0.07+0.013*i)*t+i))/ (1+0.3*i)
pad/=np.abs(pad).max()
# soft pulse bass-like gentle beat 90bpm
beat=np.zeros(n); bp=60/90
for k in range(int(D/bp)):
    s=int(k*bp*sr); L=int(0.25*sr); tt=np.arange(L)/sr
    beat[s:s+L]+=np.sin(2*np.pi*(55+25*np.exp(-tt*30))*tt)*np.exp(-tt*14)*(1 if k%2==0 else .6)
music=pad*0.8+beat*0.25
env=np.minimum(1,np.minimum(t/2.0,(D-t)/3.0)); music*=env
# whooshes at scene cuts
sw=np.zeros(n)
for c in [6,16.8,27.4,36.4,48.2]:
    L=int(0.7*sr); noise=rng.standard_normal(L); tt=np.arange(L)/sr
    # crude sweeping lowpass via cumulative filter
    out=np.zeros(L); y=0
    for i in range(L):
        a=0.02+0.5*(i/L)**2; y+=a*(noise[i]-y); out[i]=y
    out*=np.sin(np.pi*tt/0.7)**2
    s=int((c-0.5)*sr); sw[s:s+L]+=out/np.abs(out).max()
# click when clutch pulls/releases (~ start of s3 and s4 content)
for c in [18.0,28.5]:
    s=int(c*sr);L=int(.05*sr);tt=np.arange(L)/sr
    sw[s:s+L]+=np.sin(2*np.pi*1800*tt)*np.exp(-tt*120)*0.8
def wr(name,x):
    x=x/np.abs(x).max()*0.9
    w=wave.open(name,'wb');w.setnchannels(1);w.setsampwidth(2);w.setframerate(sr)
    w.writeframes((x*32767).astype('<i2').tobytes());w.close()
wr('music.wav',music); wr('sfx.wav',sw)
