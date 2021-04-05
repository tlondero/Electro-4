clear;
clc;
name = 'ideal_vo.mat';
path = 'C:\Users\Usuario\Documents\GitHub\Electro-IV\TP1\Ejercicio 2\Matlab\';
load(strcat(path, name));
d = [data.Time , data.data];
save(name, 'd');