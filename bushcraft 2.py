BPrijs = float(input('Wat is de prijs van de Diesel? '))  # 1.67
Km = 244
Benzine = 12
PPrijs = 8
Personen = 5
PRepen = 8
PRPrijs = float(input('Wat is de prijs voor een pakje pemmican-repen? '))  # 3.45
VPlakken = 15
VPrijs = float(input('Wat is de prijs van een vijgenplak? '))  # 1.24
SBrtollen = 2
SBRPrijs = float(input('Wat is de prijs van de scheepsbiscuit rol? '))  # 2.67
FireS = 2
FSPrijs = float(input('Wat is de prijs van een firesteel? '))  # 3.26
Lucifer = 5
LPrijs = float(input('Wat is de prijs van een pakje lucifers? '))  # 0.21
VuurS = 4
VSPrijs = float(input('Wat is de prijs van een originele vuursteen? '))  # 2.23
STouw = 10
STPrijs = float(input('Wat is de prijs van een sisaltouw per 2 meter? '))  # 0.59
Berekening = (Km / Benzine * BPrijs + PPrijs * Personen) * 2
Berekening1 = PRepen * PRPrijs + VPlakken * VPrijs + SBrollen * SBRPrijs + FireS * FSPrijs + Lucifer * LPrijs + VuurS * VSPrijs + STouw * STPrijs
print('De prijs van de rit is:', round(Berekening, 2))
print('De prijs van alle benodigdheden is:', Berekening1)
Totaal = Berekening + Berekening1
print('De totale prijs is: €', round(Totaal, 2))
