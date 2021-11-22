print('Welkom bij de aanmeldprogramma! Beantwoord deze vragen!')
Leeftijd = int(input('Hoe oud bent u? '))
if Leeftijd >= 16:
    Flexibel = input('Bent u iemand die meer altijd hetzelfde doet, of iemand die zich kan aanpassen aan de situatie? '
                     'Hetzelfe/Aanpassen ')
    if Flexibel == "Aanpassen":
        Positief = input('Bent u positief in het leven of somber? Positief/Somber ')
        if Positief == "Positief":
            Doorzettend = input(
                'Stopt u na een paar keer proberen, of bent u een echte doorzetter? Stoppen/Doorzetter ')
            if Doorzettend == "Doorzetter":
                print('Nou dat u deze vragen beantwoord heeft.')
            else:
                print('Sorry, u kunt geen teamlid worden!')
                quit()
        else:
            print('Sorry, u kunt geen teamlid worden!')
            quit()
    else:
        print('Sorry, u kunt geen teamlid worden!')
        quit()

else:
    print('Sorry, u kunt geen teamlid worden!')
    quit()


def start():
    Keuze = input('Voor welke teamlid wilt u de aanmeldprogramma doen? Kies uit Beer, Vos, Bever of Uil. ')
    if Keuze == "Beer":
        print('Dus u wilt de beer uit het team zijn, dan moet u wel sterk zijn!')
        Sterk = int(input('U bent heel sterk als u meer dan 120 kg kan drukken. Hoeveel kilo kunt u drukken? '))
        if Sterk >= 120:
            print('Zo! Dat is wel heel veel! Nu de tweede vraag.')
            Sterk1 = int(input('U bent heel sterk als u 5 houten planken tegelijk kan kapot slaan. Hoeveel houten '
                               'planken kunt u in een keer kapot slaan? '))
            if Sterk1 >= 5:
                print('Gefeliciteerd! U bent aangenomen als de Beer van het team!')
            elif Sterk1 < 5:
                NSterk = input(
                    'Helaas bent u niet sterk genoeg om de Beer van het team te zijn. Als u een ander rol wilt '
                    'kiezen, type dan: Start ')
                if NSterk == "Start":
                    start()
                else:
                    quit()
        elif Sterk < 120:
            NSterk = input(
                'Helaas bent u niet sterk genoeg om de Beer van het team te zijn. Als u een ander rol wilt kiezen, '
                'type dan: Start ')
            if NSterk == "Start":
                start()
            else:
                quit()
    elif Keuze == "Vos":
        print("Dus u wilt de Vos van het team zijn, dan moet u weel heel slim zijn!")
        IQ = int(input('Om de Vos te zijn moet u minimaal een IQ hebben van 120, wat is uw IQ? '))
        if IQ >= 120:
            print('Zo slim als een vos dus!')
            Vangen = int(
                input('Een Vos wilt altijd snel zijn, dus het moet niet lang bezig zijn. Hoelang duurt het voor '
                      'u om een kastje in elkaar te zetten? '))
            if Vangen >= 300:
                print('Gefeliciteerd! U bent aangenomen als de Vos van het team!')
            else:
                NVangen = input(
                    'Helaas bent u niet snel genoeg om de Vos van het team te zijn. Als u een ander rol wilt kiezen, '
                    'type dan: Start ')
                if NVangen == "Start":
                    start()
                else:
                    quit()
        else:
            NSlim = input(
                'Helaas bent u niet slim genoeg om de Vos van het team te zijn. Als u een ander rol wilt kiezen, '
                'type dan: Start ')
            if NSlim == "Start":
                start()
            else:
                quit()
    elif Keuze == "Bever":
        print('Dus u wilt de Bever van het team zijn, dan moet u wel handig zijn!')
        Springen = int(
            input('Je bent handig als je ver kunt springen natuurlijk. Hoe ver kunt u springen? (In meters) '))
        if Springen >= 3:
            print('Nou, dat is pas ver!')
            Vuur = int(input('Je bent handig als je snel vuur kunt maken met een vuursteen en hooi. Hoeveel seconden '
                             'duurt het voor u om vuur te maken met deze 2 materialen? '))
            if Vuur <= 60:
                print('Gefeliciteerd! U bent aangenomen als de Bever van het team!')
            else:
                NVuur = input(
                    'Helaas bent u niet handig genoeg om de Bever van het team te zijn.. Als u een ander rol wilt '
                    'kiezen, type dan: Start ')
                if NVuur == "Start":
                    start()
                else:
                    quit()
        else:
            NVuur = input(
                'Helaas bent u niet handig genoeg om de Bever van het team te zijn.. Als u een ander rol wilt '
                'kiezen, type dan: Start ')
            if NVuur == "Start":
                start()
            else:
                quit()
    else:
        print('Dus u wilt de Uil van het team zijn, dan moet u heel veel kennis hebben!')
        Herken = int(input('Hoeveel eetbare paddestoelen kunt u herkennen? '))
        if Herken >= 5:
            print('Nou, dat is er pas veel!')
            Kruiden = int(input('Hoeveel giftige kruiden kunt u herkennen? '))
            if Kruiden >= 10:
                Water = input('Kunt u drinkbare water maken/herkennen? Ja/Nee ')
                if Water == "Ja":
                    Tent = input('Kunt u van hout en allemaal andere materialen een tent maken? Ja/Nee ')
                    if Tent == "Ja":
                        print('Gefeliciteerd! U bent aangenomen als de Uil van het team!')
                    else:
                        NTent = input(
                            'Helaas heeft u niet genoeg kennis om de Uil van het team te zijn.. Als u '
                            'een ander rol wilt kiezen, type dan: Start')
                        if NTent == "Start":
                            start()
                        else:
                            quit()
                else:
                    NWater = input(
                        'Helaas heeft u niet genoeg kennis om de Uil van het team te zijn.. Als u '
                        'een ander rol wilt kiezen, type dan: Start')
                    if NWater == "Start":
                        start()
                    else:
                        quit()
            else:
                NKruiden = input(
                    'Helaas kunt u niet genoeg giftige kruiden herkennen om de Uil van het team te zijn.. Als u '
                    'een ander rol wilt kiezen, type dan: Start')
                if NKruiden == "Start":
                    start()
                else:
                    quit()
        else:
            NHerken = input('Helaas kunt u niet genoeg paddestoelen herkennen om de Uil van het team te zijn.. Als u '
                            'een ander rol wilt kiezen, type dan: Start')
            if NHerken == "Start":
                start()
            else:
                quit()


start()
