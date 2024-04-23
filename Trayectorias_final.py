import numpy as np
import matplotlib.pyplot as plt

ang=10
rmay=70
xc=100
yc=100
largo=50

beta1=ang*np.pi/180  # Convertimos los ángulos a radianes 
phi1 = (180-2*ang)*np.pi/180

ang=ang*np.pi/180

r1 = rmay
xc1=xc
yc1=yc

Vh = 1   # velocidad constante de la herramienta en cm/seg
ta = 5    # tiempo de aceleración en segundos

Dr1 = np.abs(phi1)*r1

T1 = (Vh*ta + 2*Dr1)/(2*Vh)

vc1=2/(2*T1-ta)

c11=vc1/(2*ta)
c12=vc1
c13=-(vc1*ta)/2

print("Dr1 =",Dr1,"cm")
print("T1 =",T1,"seg")
print("vc1 =",vc1)

#segundo segmento
xi2 = xc-rmay * np.cos(ang)  # Posición inicial en x en cm
yi2 = yc+rmay*np.sin(ang)   # Posición inicial en y en cm
xf2 = xc-rmay * np.cos(ang)  # Posición final en x en cm
yf2 = yc+rmay*np.sin(ang) - largo # Posición final en y en cm

Dr2 = np.sqrt((xi2-xf2)**2 + (yi2-yf2)**2)
T2 = Dr2/Vh           # posibles distancias negativas
c2 = 1/T2

print("Dr2 =",Dr2,"cm")
print("T2 =",T2,"seg")

#Tercer segmento 
beta3=180*np.pi/180  # Convertimos los ángulos a radianes 
phi3 = 180*np.pi/180

rch=rmay*np.cos(ang)/4

r3 = rch
xc3=xc-3*rch
yc3=yc+rmay*np.sin(ang) - largo

Dr3 = np.abs(phi3)*r3

T3 = Dr3/Vh
c3 = 1/T3

print("Dr3 =",Dr3,"cm")
print("T3 =",T3,"seg")

#cuarto segmento
beta4=180*np.pi/180  # Convertimos los ángulos a radianes 
phi4 = 180*np.pi/180

rch=rmay*np.cos(ang)/4

r4= rch
xc4=xc-rch
yc4=yc+rmay*np.sin(ang) - largo

Dr4 = np.abs(phi4)*r4

T4 = Dr4/Vh
c4 = 1/T4

print("Dr4 =",Dr4,"cm")
print("T4 =",T4,"seg")

#quiento segmento 
beta5=180*np.pi/180  # Convertimos los ángulos a radianes 
phi5 = 180*np.pi/180

rch=rmay*np.cos(ang)/4

r5= rch
xc5=xc+rch
yc5=yc+rmay*np.sin(ang) - largo

Dr5 = np.abs(phi5)*r5

T5 = Dr5/Vh
c5 = 1/T5

print("Dr5 =",Dr5,"cm")
print("T5 =",T5,"seg")

#sexto segmento
beta6=180*np.pi/180  # Convertimos los ángulos a radianes 
phi6 = 180*np.pi/180

rch=rmay*np.cos(ang)/4

r6= rch
xc6=xc+3*rch
yc6=yc+rmay*np.sin(ang) - largo

Dr6 = np.abs(phi5)*r6

T6 = Dr6/Vh
c6 = 1/T6

print("Dr6 =",Dr6,"cm")
print("T6 =",T6,"seg")

# sestimo segmento 
xi7 = xc+rmay * np.cos(ang)  # Posición inicial en x en cm
yi7 = yc+rmay*np.sin(ang)-largo   # Posición inicial en y en cm
xf7 = xc+rmay * np.cos(ang)  # Posición final en x en cm
yf7 = yc+rmay*np.sin(ang) # Posición final en y en cm

td=5

Dr7 = np.sqrt((xi7-xf7)**2 + (yi7-yf7)**2)
T7 = (Vh*td + 2*Dr7)/(2*Vh)

vc7=2/(2*T7-td)

c71 = vc7
c72 = -vc7/(2*td)
c73 = vc7*T7/td
c74 = 1-(vc7*T7**2)/(2*td)

print("Dr7 =",Dr7,"cm")
print("T7 =",T7,"seg")

Tt=T1+T2+T3+T4+T5+T6+T7
T = np.linspace(0, Tt, 200)
s = []
x = []
y = []

for tk in T:
    if tk < ta:
        t=tk
        s1=c11*t**2
        s.append(s1)
        x.append(r1*np.cos(phi1*s1+beta1)+xc1)
        y.append(r1*np.sin(phi1*s1+beta1)+yc1)
       
    elif tk < (T1):
        t=tk
        s1=c12*t+c13
        s.append(s1)
        x.append(r1*np.cos(phi1*s1+beta1)+xc1)
        y.append(r1*np.sin(phi1*s1+beta1)+yc1)
        
    elif tk < (T1+T2):          # segundo segmento semicírculo
        t=tk-T1
        s2=c2*t
        s.append(s2)
        x.append(xi2*(1-s2)+xf2*s2)
        y.append(yi2*(1-s2)+yf2*s2)
        
    elif tk < (T1+T2+T3):   # Tercer segmento Línea recta
        t=tk-T1-T2
        s3=c3*t
        s.append(s3)
        x.append(r3*np.cos(phi3*s3+beta3)+xc3)
        y.append(r3*np.sin(phi3*s3+beta3)+yc3)
        
    elif tk < (T1+T2+T3+T4):          # Cuarto segmento semicírculo
        t=tk-T1-T2-T3
        s4=c4*t
        s.append(s4)
        x.append(r4*np.cos(phi4*s4+beta4)+xc4)
        y.append(r4*np.sin(phi4*s4+beta4)+yc4)
        
    elif tk < (T1+T2+T3+T4+T5):   # Quinto segmento Línea recta
        t=tk-T1-T2-T3-T4
        
        s5=c5*t
        s.append(s5)
        x.append(r5*np.cos(phi5*s5+beta5)+xc5)
        y.append(r5*np.sin(phi5*s5+beta5)+yc5)
        
    elif tk < (T1+T2+T3+T4+T5+T6):          # Sexto segmento semicírculo
        t=tk-T1-T2-T3-T4-T5
        
        s6=c6*t
        s.append(s6)
        x.append(r6*np.cos(phi6*s6+beta6)+xc6)
        y.append(r6*np.sin(phi6*s6+beta6)+yc6)
        
        
    elif tk < (T1+T2+T3+T4+T5+T6+T7-td):  # Octavo segmento semicírculo
        t=tk-T1-T2-T3-T4-T5-T6
        
        s71=c71*t
        s.append(s71)
        x.append(xi7*(1-s71)+xf7*s71)
        y.append(yi7*(1-s71)+yf7*s71)
        
    else:                             # Octavo segmento semicírculo 2a parte
        t=tk-T1-T2-T3-T4-T5-T6
        
        s72=c72*t**2+c73*t+c74
        s.append(s72)
        x.append(xi7*(1-s72)+xf7*s72)
        y.append(yi7*(1-s72)+yf7*s72)

# Función para dibujar un Pac-Man en las coordenadas (x, y) con un tamaño específico

ang2 = 10
rmay2 = 70
xc9 = 400
yc9 = 100
largo2 = 50

beta1=ang*np.pi/180  # Convertimos los ángulos a radianes 
phi1 = (180-2*ang)*np.pi/180

ang2=ang2*np.pi/180

r1 = rmay
xc9=xc
yc9=yc

Vh = 1   # velocidad constante de la herramienta en cm/seg
ta = 5    # tiempo de aceleración en segundos

Dr1 = np.abs(phi1)*r1

T1 = (Vh*ta + 2*Dr1)/(2*Vh)

vc1=2/(2*T1-ta)

c11=vc1/(2*ta)
c12=vc1
c13=-(vc1*ta)/2

print("Dr1 =",Dr1,"cm")
print("T1 =",T1,"seg")
print("vc1 =",vc1)

# Mod Oscar Alberto Valles Limas Instituto tecnológico de Chihuahua
fig3 = plt.figure(figsize=(8,8))
ax3=plt.axes()
xi100 = -100  #-50  # Posición inicial en x en cm
yi100 = 100#0     #50   # Posición inicial en y en cm
xf100 = -50   #-100  # Posición final en x en cm
yf100 = 150#50    #0  # Posición final en y en cm
Vh100 = 2   # velocidad constante de la herramienta en cm/seg
ta100 = 5    # tiempo de aceleración en segundos
td100 = 5 # segundos

Dr100 = np.sqrt((xi100-xf100)**2 + (yi100-yf100)**2)  # Distancia del primer segmento en cm
T100 = (Vh100*ta100 + 2*Dr100)/(2*Vh100)

vc100=2/(2*T100-ta100)

c100=vc100/(2*ta100)
c101=vc100
c103=-(vc100*ta100)/2

# Segunda trayectoria
beta200=45*np.pi/180
phi200 = 270*np.pi/180
r200 = 72
xc200=-100
yc200= 100#0

Dr200 = np.abs(phi200)*r200
T200 = Dr200/Vh100
c204 = 1/T200

#Tercera trayectoria
xi300 = -50  # Posición inicial en x en cm
yi300 = 50 #-50   # Posición inicial en y en cm
xf300 = -100  # Posición final en x en cm
yf300 = 100#0  # Posición final en y en cm

Dr300 = np.sqrt((xi300-xf300)**2 + (yi300-yf300)**2)  # Distancia del tercer segmento en cm
T300 = Dr300/Vh100
c305 = 1/T300


Tt100=T100+T200+T300
TT = np.linspace(0, Tt100, 200)
s100 = []
x100 = []
y100 = []

for tk100 in TT:
    if tk100 < ta100:
        t800=tk100
        s500=c100*t800**2
        s100.append(s500)
        x100.append(xi100*(1-s500)+xf100*s500)
        y100.append(yi100*(1-s500)+yf100*s500)
       
    elif tk100 < (T100):
        t800=tk100
        s500=c101*t800+c103 
        s100.append(s500)
        x100.append(xi100*(1-s500)+xf100*s500)
        y100.append(yi100*(1-s500)+yf100*s500)
        
    elif tk100 < (T100+T200):          # segundo segmento semicírculo
        t800=tk100-T100
        s600=c204*t800
        s100.append(s600)
        x100.append(r200*np.cos(phi200*s600+beta200)+xc200)
        y100.append(r200*np.sin(phi200*s600+beta200)+yc200)
        
    elif tk100 < (T100+T200+T300):   # Tercer segmento Línea recta
        t800=tk100-T100-T200
        s700=c305*t800
        s100.append(s700)
        x100.append(xi300*(1-s700)+xf300*s700)
        y100.append(yi300*(1-s700)+yf300*s700)
        
    else:                             
        t800=tk100-T100-T200-T300
        
        s82=c305*t800**2+c305*t800+c305
        s100.append(s700)
        x100.append(xi300*(1-s700)+xf300*s700)
        y100.append(yi300*(1-s700)+yf300*s700)

ax3.set_xlabel('Eje X')
ax3.set_ylabel('Eje Y')
ax3.set_xlim(-200,200)
ax3.set_ylim(0,200)
ax3.set_title('PAC-MAN/FANTASMA')
plt.grid()
plt.scatter(x, y, lw=1, marker = '.',color = 'r')
plt.scatter(x100, y100, lw=1, marker = '.',color = 'y')
plt.show()  # Comando para mostrar el plot (Gráfica)
