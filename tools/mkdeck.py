D='/tmp/claude-0/-home-claude/e660ac9a-ba93-596c-b837-5a7074dfe847/scratchpad/'
sky=open(D+'sky.html').read().replace('class="ln-sky" id="lnSky"','class="sky"')
tt=open(D+'tt.html').read().replace('class="obj" id="o-tt"','class="tt"')
spk=open(D+'spk.html').read().replace('class="obj" id="o-spk"','class="spk"')
U=[40000,200000,640000];arpu=.6*10+.4*19.99
Y=[];prev=0
for u in U:
    h=u*.125;nh=(u-prev)*.125;Y.append(dict(U=u,h=h,sub=h*arpu*12,pk=nh*.4,puck=nh*.4*40,gmv=h*24,mkt=h*24*.08));prev=u
for y in Y:y['t']=y['sub']+y['puck']+y['mkt']
m=lambda v:'£%.1fm'%(v/1e6) if v>=1e6 else '£%dk'%round(v/1e3)
n=lambda v:f'{round(v):,}'
mx=max(y['t'] for y in Y)
bars=''.join(f'''<div class="col"><b>{m(y['t'])}</b><div class="stack" style="height:{y['t']/mx*100:.1f}%"><i style="background:#7FA7B7;height:{max(1.2,y['mkt']/y['t']*100):.1f}%"></i><i style="background:#EF8B2C;height:{y['puck']/y['t']*100:.1f}%"></i><i style="background:#C8452B;flex:1"></i></div><label>Year {i+1}</label></div>''' for i,y in enumerate(Y))
rows=[('People on Stack',[n(y['U']) for y in Y]),('Shared homes paying',[n(y['h']) for y in Y]),('Sharing plans',[m(y['sub']) for y in Y]),('Puck sales',[m(y['puck']) for y in Y]),('Marketplace fees',[m(y['mkt']) for y in Y])]
table='<table class="nt"><tr><th></th><th>Year 1</th><th>Year 2</th><th>Year 3</th></tr>'+''.join(f'<tr><td>{a}</td>'+''.join(f'<td>{v}</td>' for v in b)+'</tr>' for a,b in rows)+'<tr class="tot"><td>Total</td>'+''.join(f'<td>{m(y["t"])}</td>' for y in Y)+'</tr></table>'
y1=Y[0]
REC='<div class="rec"><img src="assets/vinyl.png"><img class="lab" src="assets/label.png"><img class="mono" src="assets/stack-monogram-sunset.svg"><i class="hole"></i><div class="sheen"></div></div>'
shots=['my-stack','two-decks','family','friends','marketplace']
names=['My Stack','Two decks','Family Stack','Friends','Marketplace']
S=[]
def slide(cls,body,label=''):S.append((cls,body,label))
slide('dark title',f'''<svg class="arcs" viewBox="0 0 1000 1000" preserveAspectRatio="xMidYMid slice"><g fill="none" stroke-width="12"><path d="M-60 1060 A 900 900 0 0 1 1060 -60" stroke="#E9B949"/><path d="M-60 1120 A 960 960 0 0 1 1120 -60" stroke="#EF8B2C"/><path d="M-60 1180 A 1020 1020 0 0 1 1180 -60" stroke="#C8452B"/><path d="M-60 1240 A 1080 1080 0 0 1 1240 -60" stroke="#7FA7B7"/></g></svg>
<div class="glow"></div><div class="trec">{REC}</div>
<div class="tcopy"><img class="lock" src="assets/stack-lockup-cream.svg"><h1><span>Own it.</span><em>Play it</em><em>everywhere.</em></h1><p>The vinyl and CDs on your shelf, playable on your phone, shared with your family, and sold on when you're done.</p><span class="by">Harrison Greener · Pitch deck</span></div>''')
slide('cream',f'''<div class="cp"><span class="no">01 The problem</span><h2>You own the record.<br><em>You still pay to hear it.</em></h2><p>Records and phones don't talk to each other. Own <i>The Dark Side of the Moon</i> on vinyl, and you still pay a streaming service to hear it on the bus.</p></div>
<div class="prob"><div class="it"><div class="r160">{REC}</div><span>Your records</span></div><div class="gap"><i></i><b>×</b><i></i></div><div class="it"><svg width="120" height="230" viewBox="0 0 60 120"><rect width="60" height="120" rx="12" fill="#1d110b"/><rect x="5" y="10" width="50" height="94" rx="4" fill="#F8EEDD"/><path d="M24 48l14 9-14 9z" fill="#C8452B"/></svg><span>Your phone</span></div></div>''','The problem')
slide('cream',f'''<div class="cp"><span class="no">02 The solution</span><h2>Owning the record<br><em>unlocks it everywhere.</em></h2><p>Add a record once by barcode, Discogs or the Puck, and it plays on every device, for your whole family.</p></div>
<div class="sol"><div class="r160">{REC}</div><i class="ln"></i><img src="assets/stack-monogram-sunset.svg" width="120"><i class="ln"></i><svg width="110" height="210" viewBox="0 0 60 120"><rect width="60" height="120" rx="12" fill="#1d110b"/><rect x="5" y="10" width="50" height="94" rx="4" fill="#F8EEDD"/><path d="M24 48l14 9-14 9z" fill="#2FA37A"/></svg></div>
<div class="pills"><div><b>Your collection</b><span>Browse covers, a crate or a list</span></div><div><b>Play anywhere</b><span>Every record you own, in lossless</span></div><div><b>Share it</b><span>Family, friends and the Marketplace</span></div></div>''','The solution')
slide('dark',f'''<div class="cp"><span class="no">03 The Puck</span><h2>A spin becomes<br><em>your own copy.</em></h2><p>The Puck sits between your turntable and speakers. Sound passes straight through while it records your copy in hi-res, crackle and all, and logs every play.</p></div>
<div class="flow">{tt}<i class="dash"></i><img class="puck" src="assets/puck-render.png"><i class="dash"></i>{spk}</div>
<div class="callouts"><span><b>Sound passes through</b>Untouched, to your speakers</span><span><b>Records your copy</b>Hi-res, crackle and all</span><span><b>From £30</b>Or 3 for £75</span></div>''','The Puck')
bh=[30,38,44,52,61,74,100]
slide('paper',f'''<div class="cp"><span class="no">04 The market</span><h2 class="mega">£174.4m</h2><h3><em>UK vinyl sales in 2025.</em></h3><p>Up 19.9% in a year, the highest in around 30 years. Collectors want to own music again.</p><p class="src">Sources: BPI via Dork; Express &amp; Star (2025). Bars show the trend.</p></div>
<div class="mbars">{''.join(f'<i style="height:{h}%"></i>' for h in bh)}</div>
<div class="facts"><div><b>+19.9%</b><span>growth in a year</span></div><div><b>11 years</b><span>of growth in UK recorded music</span></div></div>''','The market')
slide('cream',f'''<div class="cp"><span class="no">05 How it earns</span><h2>One loop,<br><em>four ways in.</em></h2><p>Each part feeds the next. Your own music is free; Stack earns when people share, buy a Puck or trade records.</p><p class="also">Also earning: <span>Stack Supply</span><span>Record shop partners</span></p></div>
<div class="loop"><svg viewBox="0 0 100 100"><circle cx="50" cy="50" r="38" fill="none" stroke="#EF8B2C" stroke-width=".7" stroke-dasharray="2 2.4"/></svg><div class="core">{REC}</div>
<div class="nd" style="left:50%;top:9%"><b>The Puck</b><span>Brings people in</span></div><div class="nd on" style="left:91%;top:50%"><b>Sharing plans</b><span>Keeps them</span></div><div class="nd" style="left:50%;top:91%"><b>Friends</b><span>Brings friends</span></div><div class="nd" style="left:9%;top:50%"><b>Marketplace</b><span>Keeps records moving</span></div></div>''','How it earns')
slide('dark',f'''<div class="cp"><span class="no">06 Pricing</span><h2>Your music is free.<br><em>Sharing it is what you pay for.</em></h2></div>
<div class="plans"><div class="pl"><small>Just you</small><h5>Solo</h5><b>Free</b><span>Every record you own, anywhere, in lossless, with no ads</span></div><div class="pl best"><small>2 people, one home</small><h5>Duo</h5><b>£10<i>/month</i></b><span>One shared Stack for two</span></div><div class="pl"><small>Up to 4 people</small><h5>Family</h5><b>£19.99<i>/month</i></b><span>Everyone streams everything the family owns</span></div>
<div class="pl wide"><span><b>The Puck</b> £30, 2 for £50, 3 for £75</span><span><b>Marketplace</b> 8% seller fee, payment held until it arrives</span><span><b>Stack Supply</b> clothing and record gear</span></div></div>''','Pricing')
slide('dark',f'''<div class="cp"><span class="no">07 The product</span><h2>A working app,<br><em>not a mockup.</em></h2></div>
<div class="phones">{''.join(f'<figure style="--r:{(-3,2,-1,3,-2)[i]}deg"><img src="assets/shots2/{f}.webp"><figcaption>{names[i]}</figcaption></figure>' for i,f in enumerate(shots))}</div>''','The product')
Q=[("I think this is something young people will really connect with. I’d definitely use it myself to help sell for my business.","Mike, 48, vinyl shop owner"),("The interface is so much better than other vinyl collecting apps. This is something I’d use, and I’d probably share records with my sister.","Alice, 20, freelancer"),("Why doesn’t this already exist?","Luke, 31, teacher")]
slide('cream',f'''<div class="cp"><span class="no">08 Testing</span><h2>What testers said.</h2></div><div class="quotes">{''.join(f'<blockquote><p>“{q}”</p><cite>{c}</cite></blockquote>' for q,c in Q)}</div>''','Testing')
slide('cream wide',f'''<div class="cp"><span class="no">09 Competitors</span><h2>Other apps do one thing.<br><em>Stack does all three.</em></h2></div>
<div class="grid"><svg viewBox="0 0 1000 520" preserveAspectRatio="none"><path d="M500 20V500M40 260H960" stroke="#3A2216" stroke-opacity=".25" stroke-width="2"/></svg>
<span class="ax" style="left:50%;top:-4%">Social</span><span class="ax" style="left:50%;bottom:-6%">On your own</span><span class="ax" style="left:2%;top:44%">Rent it</span><span class="ax" style="right:2%;top:44%">Own it</span>
{''.join(f'<span class="cd{" us" if u else ""}" style="left:{x}%;top:{y}%"><img src="{img}">{nm}<small>{d}</small></span>' for x,y,img,nm,d,u in [(27,30,'assets/logos/spotify.png','Spotify','Huge catalogue, you never own anything',0),(21,68,'assets/logos/applemusic.png','Apple Music','Rented, and on your own',0),(70,78,'assets/logos/discogs.png','Discogs','Great catalogue, but you can’t listen',0),(58,56,'assets/logos/bandcamp.png','Bandcamp','Physical plus digital, one shop only',0),(76,18,'assets/stack-monogram-sunset.svg','Stack','Any record you own: playable, shareable, sellable',1)])}</div>''','Competitors')
STG=[('Year 1','Manchester',40000,5000,12,'Partner record shops, students and Record Store Day'),('Year 2','The North West',200000,25000,45,'Liverpool, Leeds and Sheffield shops join'),('Year 3','The UK',640000,80000,150,'Label partnerships and the Puck in stores')]
slide('paper launch',f'''<div class="cp"><span class="no">10 Launch</span><h2>Start in Manchester,<br><em>grow from record shops.</em></h2></div>
<div class="stages">{''.join(f'<div class="stg"><small>{a}</small><h5>{b}</h5><div class="u">{c:,}</div><div class="ul">people on Stack</div><ul><li><b>{d:,}</b> shared homes</li><li><b>{e}</b> partner shops</li><li>{f}</li></ul></div>' for a,b,c,d,e,f in STG)}</div>{sky}''','Launch')
stk=[('p1',6,14,-14,150),('p6',20,58,10,130),('p3',33,10,8,140),('p7',8,70,-6,120),('p8',34,72,-10,170),('p5',42,34,16,120)]
emo=[('e1',58,20,96,'Wrapped is out!'),('e4',78,12,84,''),('e3',90,40,96,'Dropped the needle'),('e6',62,62,84,''),('e2',82,72,96,'Join me on Stack')]
slide('mk',f'''<div class="half phys">{''.join(f'<img class="stk" src="assets/stk/{a}.png" style="left:{x}%;top:{y}%;width:{w}px;transform:rotate({r}deg)">' for a,x,y,r,w in stk)}<div class="card"><small>Physical</small><h4>Out in the world</h4><ul><li>Stickers and posters in partner record shops</li><li>Record Store Day events and listening parties</li><li>The Puck on shop counters</li><li>Stack Supply clothing and tote bags</li></ul></div></div>
<div class="half dig">{''.join(f'<div class="emo" style="left:{x-50}%;top:{y}%"><img src="assets/stk/{a}.png" style="width:{w}px">{f"<span>{t}</span>" if t else ""}</div>' for a,x,y,w,t in emo)}<div class="card"><small>Digital</small><h4>On every phone</h4><ul><li>TikTok and Instagram campaigns</li><li>Music creators and DJs showing their Stacks</li><li>Shareable Stack Wrapped and Record Club picks</li><li>Invite a friend, you both get a month free</li></ul></div></div>
<div class="mkh"><span class="no">11 Marketing</span><h2>Out in the world,<br><em>and on every phone.</em></h2></div>''','Marketing')
slide('paper',f'''<div class="cp"><span class="no">12 Revenue forecast</span><h2>How Stack<br><em>makes money.</em></h2>
<div class="legend"><span><i style="background:#C8452B"></i>Sharing plans</span><span><i style="background:#EF8B2C"></i>Puck sales</span><span><i style="background:#7FA7B7"></i>Marketplace fees</span></div></div>
<div class="chart">{bars}</div><div class="tbl">{table}<p class="src">Based on the assumptions on the next page. Stack Supply and record shop commission come on top.</p></div>''','Revenue forecast')
slide('cream',f'''<div class="cp"><span class="no">12 Revenue forecast</span><h2>How Year 1<br><em>adds up.</em></h2><p>Starting from 40,000 people on Stack in Manchester.</p></div>
<div class="sums">
<div><i style="background:#C8452B"></i><b>Sharing plans</b><p>1 in 8 people share a Stack at home: {n(y1['U'])} × 12.5% = {n(y1['h'])} homes × £{arpu:.2f} a month (60% Duo at £10, 40% Family at £19.99) × 12</p><em>{m(y1['sub'])}</em></div>
<div><i style="background:#EF8B2C"></i><b>Puck sales</b><p>40% of new shared homes buy one: {n(y1['h'])} × 40% = {n(y1['pk'])} Pucks × £40 average with bundles</p><em>{m(y1['puck'])}</em></div>
<div><i style="background:#7FA7B7"></i><b>Marketplace fees</b><p>Each shared home buys about £24 of second-hand records a year: {n(y1['h'])} × £24 = {m(y1['gmv'])} sold × 8%</p><em>{m(y1['mkt'])}</em></div>
<div class="tot"><b>Year 1 total</b><p>Solo is free, so the other 87.5% of people pay nothing to play their own records.</p><em>{m(y1['t'])}</em></div></div>''','How Year 1 adds up')
R=[('Music rights','Owning a record doesn’t give you the right to stream or copy it.','Partner with labels','Many records already come with a download code. Stack becomes its home, licensed, with royalties on every play.'),('Hardware costs','Making, certifying and shipping the Puck is expensive.','Start small, keep it optional','Barcode and Discogs import work without it. The Puck launches in small batches through record shops.'),('An empty marketplace','Buyers won’t come without sellers, and the other way round.','Launch city by city','Manchester first, with partner record shops listing second-hand stock from day one.')]
slide('dark',f'''<div class="cp"><span class="no">13 Risks</span><h2>The risks,<br><em>and the answers.</em></h2></div><div class="risks">{''.join(f'<div class="rk"><div class="f"><small>Risk</small><b>{a}</b><p>{b}</p></div><div class="b"><small>Answer</small><b>{c}</b><p>{d}</p></div></div>' for a,b,c,d in R)}</div>''','Risks')
slide('dark title end',f'''<div class="glow"></div><div class="trec">{REC}</div><div class="tcopy"><h1><span>Own it.</span><em>Play it</em><em>everywhere.</em></h1><p>Try the prototype: <b>harrisongreener.github.io/stack</b><br>Pitch site: <b>harrisongreener.github.io/stackPitch</b></p><span class="by">Designed and built by Harrison Greener</span></div>''')
N=len(S)
pages=''.join(f'''<section class="s {c}"><div class="in">{b}</div><footer><span class="ft">{('<img src="assets/stack-monogram-sunset.svg">'+l) if l else ''}</span><span class="pn">{i+1} / {N}</span></footer><div class="prog"><i style="width:{(i+1)/N*100:.2f}%"></i></div></section>''' for i,(c,b,l) in enumerate(S))
CSS=open(D+'deck.css').read()
html=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Stack · Pitch deck</title><link rel="icon" href="assets/stack-monogram-sunset.svg"><style>{CSS}</style></head><body>{pages}
<script>
const S=[...document.querySelectorAll('.s')];let k=0;const fit=()=>{{const z=Math.min(innerWidth/1600,innerHeight/900);document.documentElement.style.setProperty('--z',z)}};
const go=i=>{{k=Math.max(0,Math.min(S.length-1,i));S.forEach((s,j)=>s.classList.toggle('cur',j===k));history.replaceState(null,'','#'+(k+1))}};
addEventListener('resize',fit);fit();go((+location.hash.slice(1)||1)-1);
addEventListener('keydown',e=>{{if(['ArrowRight','ArrowDown',' ','PageDown'].includes(e.key)){{e.preventDefault();go(k+1)}}if(['ArrowLeft','ArrowUp','PageUp'].includes(e.key)){{e.preventDefault();go(k-1)}}if(e.key==='Home')go(0);if(e.key==='End')go(S.length-1)}});
addEventListener('click',e=>go(k+(e.clientX<innerWidth/3?-1:1)));
</script></body></html>'''
open('/home/claude/stackpitch/deck.html','w').write(html)
print(N)
