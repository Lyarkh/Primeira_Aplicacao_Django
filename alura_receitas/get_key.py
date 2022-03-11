
class GetKey:
    
    @staticmethod
    def pega_key_django():
        with open('key_django.txt', mode ='r') as arquivo_da_chave:
            chave = arquivo_da_chave.readline()
        
            return chave
    
    @staticmethod
    def pega_password_db():
        with open('key_dbserver.txt', mode ='r') as arquivo_da_chave:
            chave = arquivo_da_chave.readline()
        
            return chave
