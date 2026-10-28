import json
arpu=.6*10+.4*19.99
QU=[3000,7000,12000,18000, 30000,50000,70000,90000, 130000,170000,220000,280000]  # average people per quarter
fixed=[(86250+30000+15000)/4]*4+[(198950+80000+35000)/4]*4+[(348450+300000+70000)/4]*4
def model(hm=1.0,att=.4):
    rows=[];prev=1000*.125*hm   # pilot ends with ~1,000 people
    for i,u in enumerate(QU):
        h=u*.125*hm; nh=max(h-prev,0); prev=h
        sub=h*arpu*3; pk=nh*att; puck=pk*40; gmv=h*6; mk=gmv*.08
        rev=sub+puck+mk; rights=sub*2/3; puckc=pk*1.5*24
        pay=h*3*(14*.015+.2)+pk*(40*.015+.2)+gmv*.015+gmv/20*.2; host=u*.10*3
        cost=rights+puckc+pay+host+fixed[i]
        rows.append(dict(u=u,h=h,sub=sub,puck=puck,mkt=mk,rev=rev,rights=rights,puckc=puckc,other=pay+host,fixed=fixed[i],cost=cost,net=rev-cost))
    return rows
R=model()
Y=[]
for y in range(3):
    q=R[y*4:y*4+4];t={k:sum(r[k] for r in q) for k in q[0]};t['u']=t['u']/4;t['h']=t['h']/4;Y.append(t)
for t in Y:print({k:round(v) for k,v in t.items()})
cash=-30000;C=[('Pilot',-30000,cash)]
for i,r in enumerate(R[:8]):cash+=r['net'];C.append((f'Y{i//4+1} Q{i%4+1}',round(r['net']),round(cash)))
for c in C:print(c)
for nm,hm,att in[('bad',.5,.2),('good',1.5,.4)]:
    r=model(hm,att);print(nm,[round(sum(x['net'] for x in r[y*4:y*4+4])) for y in range(3)])
json.dump(dict(Y=Y,C=C,R=R),open(''+__import__('os').path.dirname(__import__('os').path.abspath(__file__))+'/fin3.json','w'))
