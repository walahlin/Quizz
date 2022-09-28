
print("Vällkomen till Python Quiz! \n ")
alla_frågor = 9
score = 0

def fråga(info_text, text1, text2, text3, text4, rätt_svar ):
    global score
    print(info_text)
    print("1", text1)
    print("2", text2)
    print("3", text3)
    print("4", text4)
    print("Skriv rätt svar: \n ")
    svar = int(input(">"))
    if(rätt_svar == svar):
        print("Rätt svar \n ")
        score += 1
        
    else:
        print("Fel")
       

fråga("Varför kallas språket så? \n ", "Namnet kommer från en reptil", "Namnet på språket kommer från BBC komediserie Monty Python's Flying Circus", "Efternamnet på skaparen är Python","Svar 2 och 3", 3)
fråga("På vilken plats kom Python i TIOBE index(språkets popularitet) 2021? \n ", "Tredje plats", "Andra plats", "Första plats","Fjarde plats", 3)
fråga("Pythons kärnfilosofi sammanfattas i dokumentet The Zen of Python PEP 203 Vilket av dessa påståenden gäller inte Pythons filosofi? \n ", "Läsbarheten räknas", "Vackert är bättre än fult", "Det bästa är fiende till det goda","Inga av de", 3)
fråga("Vad betyder 'unpythonic' i Python community? \n ", "Kod med många fel", "Kod som är svår att förstå eller läsa", "Kod som skriven på ett annat programmeringsspråk","Svar 1 + 2", 2)
fråga("Vilket av dessa program är INTE skrivet i Python? \n ", "Reddit", "Pinterest", "Adobe Photoshop","Adobe illstrator", 3)
fråga("När skapades Python? \n ", "1990", "1991", "1993","1994", 2 )
fråga("Vilken Extraherar tillägg från filnamn i Python? \n ", "Py", "Txt", "Psd", "png", 1)
fråga("Vad betyder sträng i Python? \n ", "Heltal", "Texten", "flyttal", "True", 2)
fråga("Vad är Python för typ av språk? \n ", "Lågnivå språk", "Mellanvivå språk", "Högnivå språk", "Inget av de föregående alternativen", 3)

print(" Tack för att du spelade! Ditt resultat är: ", score, "rätta svar!")