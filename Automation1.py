import sqlite3
banco = sqlite3.connect('BDLocalization.db')
cursor = banco.cursor()
count = 0


def get_line():
    cursor.execute("SELECT * FROM localization WHERE status == '' OR status == ' '")
    for item in cursor.fetchall():
        lst = list(item)
        return lst


def contador():
    return 1

def update_bd(count):
    cursor.execute(f"UPDATE localization SET status='OK' WHERE ID = \"{count}\"")
    banco.commit()

def href():
    site = input('Digite o site: ')
    return site

def nameLogin():
    name = input('Digite o login do usuario: ')
    return name

def palavra_passe():
    senha = input('Digite a senha do usuario: ')
    return senha


from selenium import webdriver
from time import sleep

navegador = webdriver.Chrome()
lst = []
count2 = 0

for i in range(0,4):
    a = get_line()
    if count2 == 0:
        wordpress = href()
        login = nameLogin()
        password = palavra_passe()

        #Armazenando valores na lista
        lst.append(wordpress)
        lst.append(login)
        lst.append(password)


        navegador.get(wordpress + '/wp-login.php')

        sleep(5)

        login_camp = navegador.find_element_by_css_selector('#user_login')
        sleep(1)
        login_camp.send_keys(login)

        password_camp = navegador.find_element_by_css_selector('#user_pass')
        sleep(1)
        password_camp.send_keys(password)

        button_camp = navegador.find_element_by_css_selector('#wp-submit')
        button_camp.click()

        count2 = 1
    else:

        sleep(5)
        wordpress = lst[0]
        print(wordpress)
        navegador.get(wordpress + '/wp-admin/options-general.php')

        navegador.maximize_window()

        titulo_do_Site = navegador.find_element_by_css_selector('#blogname')
        sleep(1)
        titulo_do_Site.send_keys(a[1])

        titulo_do_Site = navegador.find_element_by_css_selector('#blogdescription')
        sleep(1)
        titulo_do_Site.send_keys('este site é para desenvolvimento de phyton em rio preto')
        sleep(2)
        save_button_camp = navegador.find_element_by_css_selector('#submit')
        save_button_camp.click()
        sleep(2)


        navegador.get(wordpress + '/wp-admin/admin.php?page=wpseo_local')
        sleep(2)

        endereco_Yoast = navegador.find_element_by_css_selector('#location_address')
        sleep(1)
        endereco_Yoast.send_keys(a[2])

        cidade_Yoast = navegador.find_element_by_css_selector('#location_city')
        sleep(1)
        cidade_Yoast.send_keys(a[1])

        estado_Yoast = navegador.find_element_by_css_selector('#location_state')
        sleep(1)
        estado_Yoast.send_keys(a[6])

        CEP_Yoast = navegador.find_element_by_css_selector('#location_zipcode')
        sleep(1)
        CEP_Yoast.send_keys(a[3])

        latitude_Yoast = navegador.find_element_by_css_selector('#location_coords_lat')
        sleep(1)
        latitude_Yoast.send_keys(a[4])

        longitude_Yoast = navegador.find_element_by_css_selector('#location_coords_long')
        sleep(1)
        longitude_Yoast.send_keys(a[5])

        navegador.execute_script("window.scrollBy(0,1000)", "")

        yoast_button_camp = navegador.find_element_by_css_selector('#submit')
        yoast_button_camp.click()
        count += contador()
        print(a)
        print(count)
        #Adiciona o Okay no banco de dados para não repetir a mesma cidade
        update_bd(count)