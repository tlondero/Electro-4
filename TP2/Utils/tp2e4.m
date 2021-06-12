%den = [1 + rc1*rc2, 1];
%num = [rf1*rc1*cc1*cc2, rf1*(cc1 + cc2), 0];

clear;
clc;

d = 0.42;
L1 = 40e-6;
L2 = 4.44e-6;
c = 47e-6;
r = 6.75;
N1 = 3;
N2 = 1;
n = N1/N2;

A_fb = [0, (1-d)*n/L1; (-1+d)*n/c, -1/r*c];
B_fb = [-d/L1; 0];

C_fb = [0, 1];
D_fb = 0;

[num, den] = ss2tf(A_fb, B_fb, C_fb, D_fb);

G = tf(num, den)
sisotool