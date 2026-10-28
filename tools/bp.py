from playwright.sync_api import sync_playwright
import http.server,threading,functools
class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self,*a):pass
srv=http.server.ThreadingHTTPServer(('127.0.0.1',8788),functools.partial(Q,directory=''+__import__('os').path.dirname(__import__('os').path.dirname(__import__('os').path.abspath(__file__)))+''));threading.Thread(target=srv.serve_forever,daemon=True).start()
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':1600,'height':900});pg.on('pageerror',lambda e:print('ERR',e))
    pg.goto('http://127.0.0.1:8788/brand.html');pg.wait_for_timeout(2000)
    pg.pdf(path=''+__import__('os').path.dirname(__import__('os').path.dirname(__import__('os').path.abspath(__file__)))+'/assets/stack-brand-guidelines.pdf',width='1600px',height='900px',print_background=True)
    pg.set_viewport_size({'width':1440,'height':900});pg.wait_for_timeout(300)
    pg.evaluate("document.querySelectorAll('.pw')[12].scrollIntoView()");pg.wait_for_timeout(1200);pg.screenshot(path=''+__import__('os').path.dirname(__import__('os').path.abspath(__file__))+'/bw.png')
    b.close()
srv.shutdown()
