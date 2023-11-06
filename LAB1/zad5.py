import re

def delete_from_string(in_string, words):
    for word in words:
       in_string = re.sub(word, "", in_string)

    return in_string

def swap_in_string(in_string, swap_dict):
    for old, new in swap_dict.items():
        in_string = re.sub(old, new, in_string)

    return in_string

swap_dict = {
    "Nic": "wszystko",
    "razy": "plus"
}


in_string = """Wisława Szymborska

Nic dwa razy

Nic dwa razy się nie zdarza
i nie zdarzy. Z tej przyczyny
zrodziliśmy się bez wprawy
i pomrzemy bez rutyny.

Choćbyśmy uczniami byli
najlepszymi w szkole świata,
nie będziemy repetować
żadnej zimy ani lata.

Żaden dzień się nie powtórzy,
nie ma dwóch podobnych nocy,
dwóch tych samych pocałunków,
dwóch jednakich spojrzeń w oczy.

Wczoraj, kiedy twoje imię
ktoś wymówił przez mnie głośno,
tak mi było, jakby róża
przez otwarte wpadła okno.

Dziś, kiedy jesteśmy razem,
odwróciłam twarz ku ścianie.
Róża? Jak wygląda róża?
Czy to kwiat? A może kamień?

Czemu ty się, zła godzino,
z niepotrzebnym mieszasz lękiem?
Jesteś – a więc musisz minąć.
Miniesz – a więc to jest piękne.

Uśmiechnięci, wpółobjęci
spróbujemy szukać zgody,
choć różnimy się od siebie
jak dwie krople czystej wody"""

out_string = delete_from_string(in_string, ["się", "byli"])
out_string = swap_in_string(out_string, swap_dict)

print(out_string)
