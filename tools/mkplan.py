import markdown,re,subprocess,time
D=__import__('os').path.dirname(__import__('os').path.abspath(__file__))+'/'
md=open(D+'business-plan.md').read()
prose=md.split('## References')[0]
print('words incl tables',len(re.sub(r'[|#*\-]',' ',prose).split()),'excl tables',len(re.sub(r'[#*\-]',' ','\n'.join(l for l in prose.splitlines() if not l.startswith('|'))).split()))
md=md.replace('## References {.refs}','<div class="pb"></div>\n\n## References {.refs}').replace('## Appendix A','<div class="pb"></div>\n\n## Appendix A')
h=markdown.markdown(md,extensions=['tables','attr_list'])
html=open(D+'business-plan-template.html').read()
head=html[:html.index('</div><h2')+6]  # up to end of cover
open(''+__import__('os').path.dirname(__import__('os').path.dirname(__import__('os').path.abspath(__file__)))+'/assets/business-plan.html','w').write(head+h+'</body></html>')
from playwright.sync_api import sync_playwright
p=subprocess.Popen(['python3','-m','http.server','8793'],cwd=''+__import__('os').path.dirname(__import__('os').path.dirname(__import__('os').path.abspath(__file__)))+'',stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL);time.sleep(1)
with sync_playwright() as pw:
    b=pw.chromium.launch();pg=b.new_page();pg.goto('http://127.0.0.1:8793/assets/business-plan.html');pg.wait_for_timeout(800)
    pg.pdf(path=''+__import__('os').path.dirname(__import__('os').path.dirname(__import__('os').path.abspath(__file__)))+'/assets/stack-business-plan.pdf',format='A4',print_background=True,display_header_footer=True,header_template='<span></span>',footer_template='<div style="font-size:8px;width:100%;text-align:center;color:#8A6E5E;font-family:sans-serif">Stack business plan · <span class="pageNumber"></span> / <span class="totalPages"></span></div>',margin={'top':'22mm','bottom':'20mm','left':'20mm','right':'20mm'})
    b.close()
p.terminate()
import os;os.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/assets/business-plan.html')
