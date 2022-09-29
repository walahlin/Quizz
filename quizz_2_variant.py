from Question import Question

#skapar en lista med alla frågor
frågor = [
"Varför kallas språket så? \n (a) Namnet kommer från en reptil \n (b) Namnet på språket kommer från BBC komediserie Monty Python's Flying Circus \n (c) Efternamnet på skaparen är Python \n (d) Svar 2 och 3 \n \n  ",
"På vilken plats kom Python i TIOBE index(språkets popularitet) 2021? \n (a) Tredje plats \n (b) Andra plats \n (c) Första plats \n (d) Fjarde plats  \n \n ",
"Pythons kärnfilosofi sammanfattas i dokumentet The Zen of Python PEP 203. Vilket av dessa påståenden gäller inte Pythons filosofi? \n (a) Läsbarheten räknas  \n (b) Vackert är bättre än fult \n (c) Det bästa är fiende till det goda  \n (d) Inga av de \n \n ",
"Vad betyder 'unpythonic' i Python community? \n (a) Kod med många fel \n (b) Kod som är svår att förstå eller läsa \n (c) Kod som skriven på ett annat programmeringsspråk  \n (d) Svar 1 + 2  \n \n ",
"Vilket av dessa program är INTE skrivet i Python? \n (a) Reddit \n (b) Pinterest \n (c) Adobe Photoshop \n (d) Sims 4  \n \n ",
"När skapades Python? \n (a) 1990 \n (b) 1991 \n (c) 1993 \n (d) 1994  \n \n ",
"Vilken Extraherar tillägg från filnamn i Python? \n (a) Py \n (b) Txt \n (c) Psd \n (d) png   \n \n ",
"Vad betyder sträng i Python? \n (a) Heltal  \n (b) Texten  \n (c) flyttal  \n (d) True  \n \n ",
"Vad är Python för typ av språk?  \n (a) Lågnivå språk  \n (b) Mellanvivå språk  \n (c) Högnivå språk  \n (d) Inget av de föregående alternativen  \n \n ",
"Vad heter skaparen av Python?  \n (a) Guido Van Rossum  \n (b) James Gosling  \n (c) David Flanagan \n (d) Yukihiro Matsumoto  \n \n "
]


#i en annan fil skapade class Question med funktion

#skapar en ny lista med rätta svar som använder class Question
Questions = [
    Question(frågor[0], "b"),
    Question(frågor[1], "c"),
    Question(frågor[2], "c"),
    Question(frågor[3], "b"),
    Question(frågor[4], "c"),
    Question(frågor[5], "b"),
    Question(frågor[6], "a"),
    Question(frågor[7], "b"),
    Question(frågor[8], "c"),
    Question(frågor[9], "a")
]
 #funktion som frågår användaren
def run_quiz(frågor):
    score = 0 
    for question in Questions:
        svar = input(question.fråga) #sparar svar
        if svar == question.svar:  #om det stämmer då +1
            print("-----------------------")
            score +=1
        else:
            print("Fel svar :( \n")
            print("-----------------------")
        print("Du har " + str(score) + " rätta svar från " + str(len(Questions)))
        print("-----------------------")
    print("Tack för att du spelade Quiz!")

run_quiz(Questions)