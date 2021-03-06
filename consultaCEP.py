import requests
import json
import PySimpleGUI as sg

class TelaPython:    
    def __init__(self):        
        layout = [
                [sg.Text('CEP'), sg.Input(size = (15,0), key='CEP'), sg.Button('Buscar')],
                [sg.Output(size=(40,10))]
        ]        
        self.tela = sg.Window('Busca de CEP',layout)
        
    def consultacep(self,cep):        
        url = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        if url.status_code == 200:
        	print('------- Serviço disponível -------')        	
        elif url.status_code == 400:
        	print('------- Serviço indisponível -------')        	
        endereco = url.json()
        return endereco

    def start_window(self):        
        while True:            
            self.button , self.values = self.tela.Read()    
            try:                
                valores = self.consultacep(self.values['CEP'])
                for k, v in valores.items():
                    print(k.upper() , ':' ,v)                    
            except:                
                print('--- Erro, função não definida! ---')               

sg.theme('DarkAmber')
jnl = TelaPython()
jnl.start_window()

while True:    
    event, values = jnl.read()    
    if event == sg.WIN_CLOSED: 
        break
    
jnl.close()
