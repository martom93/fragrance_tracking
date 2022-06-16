import webbrowser
import requests
import sys
from bs4 import BeautifulSoup
import smtplib
import time
from playsound import playsound
from colorama import Fore, Back, Style
from colorama import init

#################### DANE WEJŚCIOWE ####################################
Email = 'ADRES@ NADAWCY'
Haslo = 'HASŁO'
Odbiorca1 = 'ADRES1@'
Odbiorca2 = 'ADRES2@' #opcjonalnie
Nadawca = 'IMIE I NAZWISKO'  #Nazwa nadawcy wiadomości email
########################################################################

init()  # włączenie coloramy - do kolorowania tekstu w konsoli

#Odpalenie pliku z linkami i zapisanie kazdego linku do tablicy
plik = open("linki.txt", "r")
linki = []
for line in plik:
    line_strip = line.strip()
    linki.append(line_strip)

# STWORZENIE AGENTA NA PODSTAWIE WLASNEJ PRZEGLADARKI
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/95.0.4638.69 Safari/537.36'}


# Funkcja wysyłająca maila na podane adresy wraz z informacją o dostępności danego produktu w sklepie.
def WyslijMaila(nazwa, URL):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)  #Port SMTP dla Gmaila
        server.ehlo()  # Sprawdzenie tożsamości
        server.starttls()  # Szyfrowanie połączenia
        server.ehlo()
        server.login(Email, Haslo)
        subject = nazwa + " jest dostepny w sprzedazy!"
        body = "Sprawdz link do produktu: \n\n" + URL
        msg = f"From: {Nadawca}\nSubject: {subject}\n\n{body}"
        server.sendmail(Email, [Odbiorca1, Odbiorca2], msg)

        print("Wiadomosc zostala wyslana")
        server.quit()
    except ValueError:
        print("Nie mozna wyslac wiadomosci e-mail")


# Odtworzenie pliku dźwiękowego
def OdpalDzwiek():
    try:
        playsound('notify.wav')
    except ValueError:
        print("Blad odpalania pliku dzwiekowego")


# Wyświetlenie strony w nowej karcie przeglądarki
def WyswietlStrone(URL):
    try:
        webbrowser.open(URL, new=2)
    except ValueError:
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
    except ValueError:
        print("Blad sieci")
        time.sleep(15)

# Utworzenie flag dostepnosci produktow
flagaDostepnosci = [1 for each in linki]

# Wykonywanie pętli głównej programu w nieskończonej pętli
while (True):
    global flagaDostepnosc
    dlugosc_listy = len(linki)
    try:
        for i in range(dlugosc_listy):
            SprawdzenieDostepnosci(linki[i])
            czas = (f"{SprawdzenieDostepnosci.czas.tm_hour}:{SprawdzenieDostepnosci.czas.tm_min}:{SprawdzenieDostepnosci.czas.tm_sec}")

            if (SprawdzenieDostepnosci.variable == True) and (flagaDostepnosci[i] == 1):
                print(f"{czas} {SprawdzenieDostepnosci.item} {Fore.GREEN}DOSTEPNY{Style.RESET_ALL} w cenie: {SprawdzenieDostepnosci.wartosc}")
                WyslijMaila(SprawdzenieDostepnosci.item, linki[i])
                OdpalDzwiek()
                WyswietlStrone(linki[i])
                flagaDostepnosci[i] = 2
            elif (SprawdzenieDostepnosci.variable == True) and (flagaDostepnosci[i] == 2):
                print(f"{czas}  {SprawdzenieDostepnosci.item}{Fore.GREEN} DOSTEPNY{Style.RESET_ALL} w cenie: {SprawdzenieDostepnosci.wartosc}")
            else:
                print(f"{czas} {SprawdzenieDostepnosci.item} {Fore.RED}NIEDOSTEPNY{Style.RESET_ALL} ")
            time.sleep(1)
    except ValueError:
        print("KONCZENIE PRACY PROGRAMU....")
        sys.exit(0)




