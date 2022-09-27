print("välkomen till Python frågor")

def fråga(info_text, text1, text2, text3, text4, rätt_svar):
    print(info_text)
    print("1", text1)
    print("2", text2)
    print("3", text3)
    print("3", text4)
    print("Skriv rätt svar:")
    svar = int(input())
    if(rätt_svar == svar):
        print("rätt svar")
    else:
        print("Fel")

fråga("Varför kallas språket så?", "Namnet kommer från en reptil", "Namnet på språket kommer från BBC komediserie Monty Python's Flying Circus", "Efternamnet på skaparen är Python","Svar 2 och 3", 3)
fråga("Var är Python i TIOBE 2021-ränkingen?", "Tredje plats", "Andra plats", "Första plats","Fjarde plats", 3)
fråga("Pythons kärnfilosofi sammanfattas i dokumentet The Zen of Python PEP 203 Vilket av dessa påståenden gäller inte Pythons filosofi?", "Läsbarheten räknas", "Vackert är bättre än fult", "Det bästa är fiende till det goda","Inga av de", 3)
fråga("Vad betyder 'unpythonic' i Python community?", "Kod med många fel", "Kod som är svår att förstå eller läsa", "Kod som skriven på ett annat programmeringsspråk","Svar 1 + 2", 2)
fråga("Vilket av dessa program är INTE skrivet i Python?", "Reddit", "Pinterest", "Adobe Photoshop","Adobe illstrator", 3)
fråga("Uppträdde första gången?", "1990", "1991", "1993","1994", 2 )
fråga("Vilken Extraherar tillägg från filnamn i Python?", "Py", "Txt", "Psd", "png", 1)
fråga("Vad betyder sträng i Python", "Heltal", "Texten", "flyttal", 2)
fråga("Vad betyder 'unpythonic' i Python community?", "Kod med många fel", "Kod som är svår att förstå eller läsa", "Kod som skriven på ett annat programmeringsspråk", "Svar 1 och 2", 2)
fråga("varfår kallas språket så?", "Namnet kommer från en reptil", "Namnet på språket kommer från BBC komediserie Monty Pythons Flying Circus", "Efternamnet på skaparen är Python", "vet ej", 2)