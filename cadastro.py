import pyautogui
import time
import pandas

# Pausa entre todos os comandos
pyautogui.PAUSE=0.7

# Comando para verificar a posição do mouse
# print(pyautogui.position())

# Variaveis
link= "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
email= "fabiane.c.badaz@gmail.com"
senha="teste"

# Entrar no navegador
pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")

# Entrar no site
pyautogui.write(link)
pyautogui.press("enter")

# Tempo para o site carregar
time.sleep(5)

# E-mail
pyautogui.click(x=2351, y=218)
pyautogui.write(email)
pyautogui.press("tab")

# Senha
pyautogui.write(senha)
pyautogui.click(x=2361, y=377)

# Importação da base de dados
tabela = pandas.read_csv("produtos.csv")

for linha in tabela.index:
  pyautogui.press("enter")
  pyautogui.scroll(5000)
  pyautogui.click(x=2207, y=98   )
  for coluna in tabela.columns:
    dado=tabela.loc[linha,coluna]
    if not pandas.isna(dado):
      pyautogui.write(str(dado))
    pyautogui.press("tab")
    
