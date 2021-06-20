%den = [1 + rc1*rc2, 1];
%num = [rf1*rc1*cc1*cc2, rf1*(cc1 + cc2), 0];

clear;
clc;

d = 0.3;
L1 = 40e-6;
Rl = 0.001;%0.008;
Rc = 0.001;
C = 47e-6;
R = 6.75;
N1 = 3;
N2 = 1;
n = N1/N2;

A_fb = [-d * Rl / L1 + (1 - d) * n ^ 2 * Rc * R / (R - Rc) / L1 (1 - d) * n * R / (R - Rc) / L1; -(1 - d) * n * R / (R - Rc) / C -d / (R + Rc) / C - (1 - d) / (R + Rc) / C;];
B_fb = [-d / L1 0; 0 0;];

C_fb = [(1 - d) * n * R * Rc / (R - Rc) d * R / (R + Rc) + (1 - d) * R / (R - Rc);];
D_fb = [0, 0];

[num, den] = ss2tf(A_fb, B_fb, C_fb, D_fb, 1);

G = tf(num, den);

%Realimentador

Rc1 = 10e3;
Rf = 1e3;
Cc1 = 10e-9;
Cc2 = 1e-6;

Cnum = [Rc1*Cc1, 1];
Cden = [Rf*Rc1*Cc1*Cc2, Rf*(Cc1 + Cc2), 0];
Cden2 = [Rf*Rc1*Cc1*Cc2, Rf*Cc1, 0];

C = tf(Cnum, Cden);
C2 = tf(Cnum, Cden2);

%sisotool

% h = bodeplot(IOTransfer_r2y); setoptions(h,'FreqUnits','Hz');