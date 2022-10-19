
def dados_gasolina(mes_inicial, mes_final):
    
    #Importa bibliotecas
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.support.select import Select
    from selenium.webdriver.common.by import By
    import time
    
    #Ano e mes de pesquisa
 
    pesquisa_inicial = "Etanol + Gasolina Comum - "+mes_inicial+"/2022"
    pesquisa_final = "Etanol + Gasolina Comum - "+mes_final+"/2022"
    pesquisa_gasolina = [pesquisa_inicial, pesquisa_final]   
        
    #Inicia o Chrome com caminho dos arquivos
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": r"C:\Users\oliver.rospendowski\Desktop\Estudo\EstudoPython\output"}
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=options)
    
            
    #Baixa os arquivos com base na informação de periodo
    driver.maximize_window()
    teste = driver.get("http://127.0.0.1:5500/index.html")
    
    site_gov = driver.get("https://dados.gov.br/dataset/serie-historica-de-precos-de-combustiveis-por-revenda")
    pesquisa = driver.find_elements(By.CLASS_NAME, "heading")

    for primeira_pesquisa in pesquisa:
        primeira_pesquisa
        
        if pesquisa_inicial in primeira_pesquisa.text:
            primeira_pesquisa.click()
            break 

    site_gov_download = driver.find_elements(By.CLASS_NAME, "actions")

    for e in site_gov_download:
        print(" Localizado " + pesquisa_inicial)
        
    time.sleep(2)    
    site_gov_download[0].click()

    site_gov = driver.get("https://dados.gov.br/dataset/serie-historica-de-precos-de-combustiveis-por-revenda")
    pesquisa = driver.find_elements(By.CLASS_NAME, "heading")

    for segunda_pesquisa in pesquisa:
        segunda_pesquisa
        
        if pesquisa_final in segunda_pesquisa.text:
            segunda_pesquisa.click()
            break 

    site_gov_download = driver.find_elements(By.CLASS_NAME, "actions")

    for e in site_gov_download:
        print(" Localizado " + pesquisa_final)
        
    time.sleep(2)    
    site_gov_download[0].click()
    time.sleep(20) 
    driver.quit()
        
    driver.quit()