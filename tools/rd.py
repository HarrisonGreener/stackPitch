from playwright.sync_api import sync_playwright
import http.server,threading,functools,sys
D=sys.argv[1]
class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self,*a):pass
srv=http.server.ThreadingHTTPServer(('127.0.0.1',8786),functools.partial(Q,directory=''+__import__('os').path.dirname(__import__('os').path.dirname(__import__('os').path.abspath(__file__)))+''));threading.Thread(target=srv.serve_forever,daemon=True).start()
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':1600,'height':900});pg.on('pageerror',lambda e:print('ERR',e))
    pg.goto('http://127.0.0.1:8786/deck.html');pg.wait_for_timeout(1500)
    pg.pdf(path=''+__import__('os').path.dirname(__import__('os').path.dirname(__import__('os').path.abspath(__file__)))+'/assets/stack-pitch-deck.pdf',width='1600px',height='900px',print_background=True)
    b.close()
srv.shutdown()
