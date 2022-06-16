import webbrowser
import requests
import sys
from bs4 import BeautifulSoup
import smtplib
import time
from playsound import playsound
from colorama import Fore, Back, Style
from colorama import init

init()  # włączenie coloramy - do kolorowania tekstu w konsoli

# Podanie loginu i hasła do poczty email, hasło jednorazowe, generowane przez google
Email = 'INSERT YOUR EMAIL ADDRESS HERE'
Haslo = 'INSERT PASSWORD FOR YOUR EMAIL HERE'

# Lista linków do śledzenia
linki = [                                 
'https://www.elnino-parfum.pl/thierry-mugler-a-men-pure-wood-woda-toaletowa-dla-mezczyzn-100-ml-tester/',                      
'https://www.elnino-parfum.pl/thierry-mugler-a-men-pure-havane-woda-toaletowa-dla-mezczyzn-100-ml-tester/',                     
'https://www.elnino-parfum.pl/thierry-mugler-a-men-pure-tonka-woda-toaletowa-dla-mezczyzn-100-ml-tester/',                      
'https://www.elnino-parfum.pl/hugo-boss-boss-bottled-intense-woda-perfumowana-dla-mezczyzn-100-ml/',                              
'https://www.elnino-parfum.pl/thierry-mugler-a-men-ultra-zest-woda-toaletowa-dla-mezczyzn-100-ml-tester/',                  
'https://www.elnino-parfum.pl/van-cleef-arpels-midnight-in-paris-pour-homme-woda-toaletowa-dla-mezczyzn-125-ml-tester/',               
'https://www.elnino-parfum.pl/van-cleef-arpels-midnight-in-paris-pour-homme-woda-toaletowa-dla-mezczyzn-40-ml-tester/',                
'https://www.elnino-parfum.pl/christian-dior-dior-homme-parfum-perfumy-dla-mezczyzn-75-ml-tester/',                                     
'https://www.elnino-parfum.pl/bvlgari-aqva-amara-woda-toaletowa-dla-mezczyzn-100-ml-tester/',                                          
'https://www.elnino-parfum.pl/amouage-reflection-man-woda-perfumowana-dla-mezczyzn-100-ml-tester/',                                  
'https://www.elnino-parfum.pl/amouage-jubilation-xxv-for-man-woda-perfumowana-dla-mezczyzn-100-ml-tester/',                             
'https://www.elnino-parfum.pl/jean-paul-gaultier-kokorico-woda-toaletowa-dla-mezczyzn-100-ml-tester/',                                  
'https://www.elnino-parfum.pl/guerlain-l-homme-ideal-woda-perfumowana-dla-mezczyzn-100-ml-tester/',                                     
'https://www.elnino-parfum.pl/guerlain-l-homme-ideal-l-intense-woda-perfumowana-dla-mezczyzn-100-ml-tester/',                          
'https://www.elnino-parfum.pl/guerlain-habit-rouge-dress-code-2018-woda-perfumowana-dla-mezczyzn-100-ml-tester/',                       
'https://www.elnino-parfum.pl/prada-luna-rossa-extreme-woda-perfumowana-dla-mezczyzn-100-ml-tester/',                                   
'https://www.elnino-parfum.pl/prada-luna-rossa-extreme-woda-perfumowana-dla-mezczyzn-100-ml/',                                          
'https://www.elnino-parfum.pl/prada-luna-rossa-extreme-woda-perfumowana-dla-mezczyzn-50-ml/',                                     
'https://www.elnino-parfum.pl/creed-aventus-cologne-woda-perfumowana-dla-mezczyzn-100-ml-tester/',      
'https://www.elnino-parfum.pl/prada-luna-rossa-extreme-woda-perfumowana-dla-mezczyzn-50-ml-tester/',                                    
'https://www.elnino-parfum.pl/prada-luna-rossa-sport-woda-toaletowa-dla-mezczyzn-100-ml-tester/',                                       
'https://www.elnino-parfum.pl/prada-l-homme-intense-woda-perfumowana-dla-mezczyzn-100-ml-tester/',                                                
'https://www.elnino-parfum.pl/christian-dior-jules-2016-woda-toaletowa-dla-mezczyzn-100-ml-tester/',                                               
'https://www.elnino-parfum.pl/tom-ford-fucking-fabulous-woda-perfumowana-30-ml/',                                             
'https://www.elnino-parfum.pl/chanel-platinum-egoiste-pour-homme-woda-toaletowa-dla-mezczyzn-100-ml-tester/',          
'https://www.elnino-parfum.pl/paco-rabanne-1-million-prive-woda-perfumowana-dla-mezczyzn-100-ml-tester/'                                       
]

# STWORZENIE AGENTA NA PODSTAWIE WLASNEJ PRZEGLADARKI
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/95.0.4638.69 Safari/537.36'}


# Funkcja wysyłająca maila na podane adresy wraz z informacją o dostępności danego produktu w sklepie.
def WyslijMaila(nazwa, URL):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()  # Sprawdzenie tożsamości
        server.starttls()  # Szyfrowanie połączenia
        server.ehlo()
        server.login(Email, Haslo)
        subject = nazwa + " jest dostepny w sprzedazy!"
        body = "Sprawdz link do produktu: \n\n" + URL
        msg = f"From: (ADD YOUR NAME HERE )\nSubject: {subject}\n\n{body}"
        server.sendmail(
            'PUT SENDER ADDRESS HERE',
            ["RECIVE_ADDRESS_1", "RECIVE_ADDRESS_2"],
            msg
        )

        print("Wiadomosc zostala wyslana")
        server.quit()
    except:
        print("Nie mozna wyslac wiadomosci e-mail")


# Odtworzenie pliku dźwiękowego
def OdpalDzwiek():
    try:
        playsound('/notify.wav')
    except:
        print("Blad odpalania pliku dzwiekowego")


# Wyświetlenie strony w nowej karcie przeglądarki
def WyswietlStrone(URL):
    try:
        webbrowser.open(URL, new=2)
    except:
        print("Nie mozna otworzyc strony internetowej")


# Funkcja sprawdzająca dostępność na podstawie analizy kodu źródłowego strony
def SprawdzenieDostepnosci(URL):
    try:
        # Wczytanie strony
        Strona = requests.get(URL, headers=headers, timeout=10)
        # Parsowanie strony
        soup = BeautifulSoup(Strona.content, 'html.parser')
        # Sprawdzenie dostępnosci i wypisanie statusu
        dostepnosc = str(soup.find(itemprop="availability"))
        # Sprawdzenie nazwy produktu
        nazwa = soup.find('h1', class_="ProductInfo-title", itemprop="name").text.strip().partition('\n')[0]
        SprawdzenieDostepnosci.item = nazwa
        # Sprawdzenie ceny produktu
        cena = soup.find(class_="ProductRow-prices u-pl--none u-pr--none").text.strip().partition('\n')[0]
        SprawdzenieDostepnosci.wartosc = cena
        czas = time.localtime()
        SprawdzenieDostepnosci.czas = czas
        # Analiza atrybutu "availability" w celu określenia dostępności produktu
        if (dostepnosc == '<link href="http://schema.org/InStock" itemprop="availability"/>'):
            SprawdzenieDostepnosci.variable = True
        else:
            SprawdzenieDostepnosci.variable = False
    except:
        print("Blad sieci")
        time.sleep(15)


# Utworzenie flag dostepnosci produktow
flagaDostepnosci = []
for i in range(len(linki)):

    flagaDostepnosci.append(1)
# Wykonywanie pętli głównej programu w nieskończonej pętli
while (True):
    global flagaDostepnosc
    dlugosc_listy = len(linki)
    try:
        for i in range(dlugosc_listy):
            SprawdzenieDostepnosci(linki[i])
            if (SprawdzenieDostepnosci.variable == True) and (flagaDostepnosci[i] == 1):
                with open('dostepnosc.txt', 'a') as f:
                    print(str(SprawdzenieDostepnosci.czas.tm_hour).strip() + ":" + str(
                        SprawdzenieDostepnosci.czas.tm_min).strip() + ":" + str(
                        SprawdzenieDostepnosci.czas.tm_sec).strip() + "  " + SprawdzenieDostepnosci.item + " DOSTEPNY " + "w cenie: " + SprawdzenieDostepnosci.wartosc,
                          file=f)
                print(str(SprawdzenieDostepnosci.czas.tm_hour).strip() + ":" + str(
                    SprawdzenieDostepnosci.czas.tm_min).strip() + ":" + str(
                    SprawdzenieDostepnosci.czas.tm_sec).strip() + "  " + SprawdzenieDostepnosci.item + Fore.GREEN + " DOSTEPNY " + Style.RESET_ALL + "w cenie: " + SprawdzenieDostepnosci.wartosc)
                WyslijMaila(SprawdzenieDostepnosci.item, linki[i])
                OdpalDzwiek()
                WyswietlStrone(linki[i])
                flagaDostepnosci[i] = 2
            elif (SprawdzenieDostepnosci.variable == True) and (flagaDostepnosci[i] == 2):
                with open('dostepnosc.txt', 'a') as f:
                    print(str(SprawdzenieDostepnosci.czas.tm_hour).strip() + ":" + str(
                        SprawdzenieDostepnosci.czas.tm_min).strip() + ":" + str(
                        SprawdzenieDostepnosci.czas.tm_sec).strip() + "  " + SprawdzenieDostepnosci.item + " DOSTEPNY " + "w cenie: " + SprawdzenieDostepnosci.wartosc,
                          file=f)
                print(str(SprawdzenieDostepnosci.czas.tm_hour).strip() + ":" + str(
                    SprawdzenieDostepnosci.czas.tm_min).strip() + ":" + str(
                    SprawdzenieDostepnosci.czas.tm_sec).strip() + "  " + SprawdzenieDostepnosci.item + Fore.GREEN + " DOSTEPNY " + Style.RESET_ALL + "w cenie: " + SprawdzenieDostepnosci.wartosc)
            else:
                print(str(SprawdzenieDostepnosci.czas.tm_hour).strip() + ":" + str(
                    SprawdzenieDostepnosci.czas.tm_min).strip() + ":" + str(
                    SprawdzenieDostepnosci.czas.tm_sec).strip() + "  " + SprawdzenieDostepnosci.item + Fore.RED + " NIEDOSTEPNY " + Style.RESET_ALL)
            time.sleep(1)
    except:
        print("KONCZENIE PRACY PROGRAMU....")
        sys.exit(0)




