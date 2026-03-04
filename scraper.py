# ==========================================
# PROJETO: Automated Data Extractor (Filtro: Cientista)
# ALVO: Fake Python Jobs
# ==========================================

from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import csv
import time

def iniciar_extrator_fake_jobs():
    url_do_site = "https://realpython.github.io/fake-jobs/"
    print("Iniciando o navegador...")
    
    opcoes = webdriver.ChromeOptions()
    
    driver = webdriver.Chrome(options=opcoes)
    oportunidades = [] 

    try:
        print(f"Acessando o site: {url_do_site}")
        driver.get(url_do_site)
        time.sleep(3) 
        
        xpath_cartoes = "//div[@class='card-content']"
        cartoes = driver.find_elements(By.XPATH, xpath_cartoes)
        
        print(f"Encontrei {len(cartoes)} vagas no total. Procurando por Cientistas...")

        for cartao in cartoes:
            try:
                titulo_bruto = cartao.find_element(By.XPATH, ".//h2[contains(@class, 'title')]").text
                empresa_bruta = cartao.find_element(By.XPATH, ".//h3[contains(@class, 'company')]").text
                link = cartao.find_element(By.XPATH, ".//a[text()='Apply']").get_attribute("href")
                
                titulo_limpo = re.sub(r'\s+', ' ', titulo_bruto).strip()
                empresa_limpa = re.sub(r'\s+', ' ', empresa_bruta).strip()
                titulo_minusculo = titulo_limpo.lower()
                
                if "scientist" in titulo_minusculo or "cientista" in titulo_minusculo:
                    oportunidades.append({
                        "Titulo": titulo_limpo,
                        "Empresa": empresa_limpa,
                        "Link": link
                    })
                
                
            except Exception as e:
                print(f"Aviso: Não foi possível extrair uma vaga. Erro: {e}")

    finally:
        print("Extração concluída. Fechando o navegador...")
        driver.quit()

    salvar_em_csv(oportunidades, "vagas_cientista.csv")


def salvar_em_csv(dados, nome_arquivo):
    if not dados:
        print("Poxa, nenhuma vaga com essa palavra-chave foi encontrada.")
        return

    colunas = dados[0].keys()

    with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=colunas)
        escritor.writeheader() 
        escritor.writerows(dados)
    
    print(f"🎉 SUCESSO! Encontramos {len(dados)} vagas para Cientista e salvamos em '{nome_arquivo}'.")

if __name__ == "__main__":
    iniciar_extrator_fake_jobs()