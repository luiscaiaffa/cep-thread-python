#lfa

from pprint import pprint 
import requests
import threading
import json

class CepThread(threading.Thread):
    def __init__(self,cep,):
        self.value = None
        self.cep = cep
        threading.Thread.__init__(self)

    def headers(self):
        return {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Token token=TOKEN AQUI' # cadastro no site cepaberto
        }

    def run(self):
        try:
            cep = self.cep.replace( "-", "" )
            url = 'http://www.cepaberto.com/api/v2/ceps.json?cep=%s' %(cep)
            response = requests.get(url, headers=self.headers())
            self.value = json.loads(response.content.decode('utf-8'))
        except Exception as error:
            raise

    

cep = CepThread('25845-002')
cep.start()
cep.join()
pprint (cep.value)