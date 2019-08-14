import requests
from bs4 import BeautifulSoup
import re
import itertools

www = "http://aju.pl"

class Pobierator():

    def __init__(self):
        pass

    def pobierz_linki(self):
        """Metoda pobiera linki ze strony www"""
        r = requests.get(www)
        soup = BeautifulSoup(r.text, "lxml")
        links = soup.find_all("h3")
        return [link.a["href"] for link in links]

class Akapity(Pobierator):

    def __init__(self):
        pass

    def pobierz_tekst(self, link):
        """Metoda wyciąga tekst z linku"""
        self.link = link
        b = requests.get(link)
        soup_link = BeautifulSoup(b.text, "lxml")
        tekst = soup_link.find(class_="post_content")
        return tekst.get_text().replace("/xa0", "").strip("\n").split("\n")

    def obrabiacz(self, zbitka):
        """Metoda dzieli tekst na zdania z konkretnego linka i zwraca w liscie"""
        self.zbitka = self.pobierz_tekst(self.link)
        return list(itertools.chain(*[re.split(r'[!?.]\s', item.strip()) for item in self.zbitka if "})" not in item and len(item) > 1]))


class Googlator(Akapity, Pobierator):

    def __init__(self):
        pass

    def google_spany(self, zdanie):
        """Metoda bierze jedno zdanie z tekstu z linku www i zwraca spans wyszukiwania GOOGLE"""
        self.zdanie = zdanie
        r = requests.get("http://www.google.pl/search?q={0}&rlz=1C1GCEU_plPL820PL820".format(str(zdanie)))
        soup = BeautifulSoup(r.text, "lxml")
        return [soup.find_all("span", class_="r0bn4c rQMQod")]
        # return self.spans

    def span_to_text(self, googlik):
        self.spans = googlik
        googlanie = []
        for span_tag in self.spans:
            try:
                linijka = span_tag.next_sibling.string
                if "·" not in linijka or linijka[0] != " ":
                    googlanie.append(re.split(r'\s+\.+\s*', linijka.strip(" ...").strip()))
            except AttributeError:
                print('NoneType')
        return list(itertools.chain(*googlanie))


class Plagiator(Googlator):

    def __init__(self):
        pass

    def text_to_text(self, zdanie_aju, lista_google):
        self.zdanie_aju = zdanie_aju
        self.lista_google = lista_google
        for indeks in range(len(self.lista_google)):
            if zdanie_aju in self.lista_google[indeks]:
                print("ZDANIE Z AJU.PL: "+ zdanie_aju + "\n" + "ZDANIE Z GOOGLE: " + self.lista_google[indeks] + "\n" +"WYNIK: PLAGIAT DLA ZDANIA")
            else:
                print("ZDANIE Z AJU.PL: "+ zdanie_aju + "\n" + "ZDANIE Z GOOGLE: " + self.lista_google[indeks] + "\n" + "WYNIK: BRAK PLAGIATU")

if __name__ == "__main__":
    P = Pobierator()
    A = Akapity()
    G = Googlator()
    PL = Plagiator()
    lista_linkow = P.pobierz_linki()
    for item in lista_linkow:
        print("NUMER ARTYKUŁU:", lista_linkow.index(item))
        print("LINK DO ARTYKUŁU:", item)
        listy = A.obrabiacz(A.pobierz_tekst(item))
        for zdanie in listy:
            print("ZDANIE NR", listy.index(zdanie), ":", zdanie)
            szukanie = G.google_spany(zdanie)
            googlanko = G.span_to_text(szukanie)
            PL.text_to_text(zdanie, googlanko)



