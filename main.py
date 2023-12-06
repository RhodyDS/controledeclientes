import re
from playwright.sync_api import Page, expect, sync_playwright



sites = {
  'azul': 'https://www.azulseguros.com.br/area-restrita/',
  'mapfre': 'https://www.mapfreconnect.com.br/default.asp',
  'allianz': 'https://www.allianznet.com.br/ngx-epac/public/home',
  'porto': 'https://corretor.portoseguro.com.br/corretoronline/',
  'bradesco': 'https://wwwn.bradescoseguros.com.br/pnegocios2/wps/portal/portaldenegociosnovo/!ut/p/z1/04_Sj9CPykssy0xPLMnMz0vMAfIjo8zifdx9PA0sLYz8DJzdjAwCHcOCTdx9jQxNfE30wwkpiAJKG-AAjgZA_VGElBTkRhikOyoqAgBzNoDA/dz/d5/L2dBISEvZ0FBIS9nQSEh/',
  'tokio': 'https://ssoportais3.tokiomarine.com.br/openam/XUI/?realm=TOKIOLFR&goto=http://portalparceiros.tokiomarine.com.br/?_gl=1*79uwyt*_gcl_au*NDc5MzQxNTUwLjE2ODYwMDYzOTM.*_ga*MTAzODMxMDM0Ni4xNjg2MDA2Mzkz*_ga_M3GQZ9PQWS*MTY4OTI3Mzg4MS4yLjAuMTY4OTI3Mzg4MS42MC4wLjA.&_ga=2.14984822.1164370956.1689273882-1038310346.1686006393#login/',
  'hdi': 'https://www.hdi.com.br/hdidigital/',
  'zurich': 'https://espacoparceiros.zurich.com.br/',
  'liberty': 'https://novomeuespacocorretor.libertyseguros.com.br/dashboard',
  'alfa': 'https://wwws.alfaseguradora.com.br/Corretor/Login',
  'suhai': 'https://suhaiseguradora.com/area-corretor/',

}


corretor = {
  'lastroseg': {
    'bradesco': {
      'login': '18924189000174',
      'senha': '016592'
    },
    'porto': {
      'login': '03806124612',
      'senha': 'Seg016591@'
    },
    
    'liberty': {
      'login': '03806124612',
      'senha': 'Fredlastro016593!'
    },

    
  }
}

#### Porto
def propTransmitidas(page: Page):
  page.goto(sites['porto'])
  expect(page).to_have_title(re.compile("Porto"))

  page.get_by_role("button", name="entrar").click()
  expect(page.get("input[id='logonPrincipal']")).to_be_visible()

  page.get_by_role("input", id="logonPrincipal").fill(corretor['lastroseg']['porto']['login'])
  page.get_by_role("input", name="password").fill(corretor['lastroseg']['porto']['senha'])

  page.get_by_role("button", id="inputLogin").click()



with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    propTransmitidas(page)

    # Agora você pode realizar outras operações após o login, se necessário.

    # Fechar o navegador
    browser.close()


