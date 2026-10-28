from playwright.sync_api import sync_playwright
import http.server,threading,functools
class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self,*a):pass
srv=http.server.ThreadingHTTPServer(('127.0.0.1',8789),functools.partial(Q,directory=''+__import__('os').path.dirname(__import__('os').path.dirname(__import__('os').path.abspath(__file__)))+''));threading.Thread(target=srv.serve_forever,daemon=True).start()
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':1600,'height':900});pg.emulate_media(media='print')
    pg.goto('http://127.0.0.1:8789/brand.html');pg.wait_for_timeout(1500)
    r=pg.evaluate("""[...document.querySelectorAll('.pg')].map((g,i)=>{const hd=g.querySelector('.hd');if(!hd)return null;const H=hd.getBoundingClientRect();
     const out=[];[...g.querySelector('.in').children].forEach(c=>{if(c===hd||getComputedStyle(c).display==='none')return;const R=c.getBoundingClientRect();
      const ox=Math.min(H.right,R.right)-Math.max(H.left,R.left);if(ox<=0)return;const gap=R.top-H.bottom;if(gap<48&&R.bottom>H.top)out.push(c.className.baseVal??c.className, Math.round(gap))});
     const f=g.querySelector('footer');let fb=null;if(f){const F=f.getBoundingClientRect();[...g.querySelector('.in').children].forEach(c=>{const R=c.getBoundingClientRect();if(R.height&&F.top-R.bottom<24&&R.bottom<=F.bottom+400&&getComputedStyle(c).display!=='none')fb=(fb||'')+' '+(c.className.baseVal??c.className)+':'+Math.round(F.top-R.bottom)})}
     return [i+1,out,fb]})""")
    for x in r:
        if x and (x[1] or x[2]):print(x)
    b.close()
srv.shutdown()
