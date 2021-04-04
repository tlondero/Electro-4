time = out.get('logsout').getElement('id').Values.Time;

id = out.get('logsout').getElement('id').Values.Data;
il = out.get('logsout').getElement('il').Values.Data;
vtrig = out.get('logsout').getElement('vtrig').Values.Data;
vo = out.get('logsout').getElement('vo').Values.Data;
vl = out.get('logsout').getElement('vl').Values.Data;

d = [time , id];
save('id.mat', 'd');

d = [time , il];
save('il.mat', 'd');

d = [time , vl];
save('vl.mat', 'd');

d = [time , vo];
save('vo.mat', 'd');

d = [time , vtrig];
save('vtrig.mat', 'd');