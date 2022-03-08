
class GetKey:
    
    @staticmethod
    def pega_key():
        with open('key_django.txt', mode ='r') as arquivo_da_chave:
            chave = arquivo_da_chave.readline()
        
            return chave