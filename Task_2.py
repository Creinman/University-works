from urllib.request  import urlopen as url
from pathlib import Path as pth
import re
from scipy.special import spherical_jn as jn, spherical_yn as yn
import numpy as np
import matplotlib.pyplot as plt

variant = 9 
C=300000000
PI=3.1415926535

file = pth('./taskfile.txt')
if not file.exists():
  txt = url('https://jenyay.net/uploads/Student/Modelling/task_02.txt').read()
f0 = file.open('wb')
f0.write(txt)
f0.close()

if file.exists():
  f1 = file.open()
lines = [x for x in f1]
p = re.compile(r'[0-9\.\-e]+')
m = p.findall(lines[variant-1])
print(m[1:])
f1.close()

D = float(m[1])
fmin = float(m[2])
fmax = float(m[3])
f = np.linspace(fmin, fmax, 400)
r = D/2

def nxc(n, x):
  return complex(jn(n, x), yn(n,x))

def nxul(n, x):
  upr_n = x * jn(n-1, x) - n*jn(n, x)
  lwr_n = x * nxc(n-1, x) - n * nxc(n, x)
  return upr_n / lwr_n

def nxd(n, x):
  return jn(n, x) / nxc(n, x) 

def fsig(x):
  lm = C/ x 
  k = 2*PI/lm
  kr = k*r
  Sum = 0+0j
  for i in range(1, 40):
  Sum += ((-1) ** i) * (i + 1/2) * (nxul(i, kr) - nxd(i, kr))
  return ((lm**2) / PI) * (np.abs(Sum)**2) 

sig = [fsig(x) for x in f]
p = pth('results')
result = p / 'task_02_307b_Zhuravlev_9.txt'
if not p.exists():
  p.mkdir(exist_ok = True)
if p.exists():
  with result.open('w') as fl:
    i = 0
    for x in f:
      fl.write('%20f   %.20f\n' % (x, sig[i]))
      i += 1
a = 4
ftst = C*a / (2*PI*r)
stst = fsig(ftst)/(PI*r*r)
l = 2*PI*r*ftst/C
plt.plot(f/1e9, sig)
plt.xlabel('f, ГГц')
plt.ylabel('$\sig, м^2$')
plt.grid()
plt.show()
print(l, stst)
