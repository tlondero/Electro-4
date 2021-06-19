clear;
clc;
R=70;
C=47e-6;
RL=0.0016;
RC=0.0016;
L=40e-6;
d=0.3;
n=3;

A_on = [[(-RL/L), 0];[0, -(1/(C*(R+RC)))]];
B_on = [-1/L;0];
C_on= [0, R/(R+RC)];
D_on=0;

A_off = [[(n^2*RC*R)/(L*(R-RC)), (n*R/(L*(R-RC)))];[-(n*R/(C*(R-RC))), -(1/(C*(R-RC)))]];
B_off= [0;0];
C_off= [n*R*RC/(R-RC), R/(R-RC)];
D_off=0;
A=A_on*d + A_off*(1-d)
B=B_on*d + B_off*(1-d)
C=C_on*d + C_off*(1-d)
D=D_on*d + D_off*(1-d)
system=ss(A,B,C,D)
pzplot(system)
step(system)
[num,den]=ss2tf(A,B,C,D)
G=tf(num,den)
sisotool