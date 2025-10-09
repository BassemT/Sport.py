print("Welcome to sport.py. Here you can watch any sports schedule, final scores, lineups, and more!")
sport = input("What sport would you like to watch? We have Football, Basketball, and Volleyball: ").lower()

if sport == "football":
    Football = input("Which league would you like to watch? We have Premier League, La Liga, and Bundesliga: ").lower()
elif sport == "basketball":
    Basketball = input("Which league would you like to watch? We have NBA, EuroLeague, and CBA: ").lower()
elif sport == "volleyball":
    Volleyball = input("Which league would you like to watch? We have AVP, FIVB, and NCAA: ").lower()
else:
    print("Error code 404 not found X(")

if Football == "Premier League":
    print("Manchester United vs Liverpool, 5 PM, Saturday", "Final Score: 2-1", "Lineups: Manchester United - De Gea, Maguire, Fernandes; Liverpool - Alisson, Van Dijk, Salah")
elif Football == "la Liga":
    print("Real Madrid vs Barcelona, 8 PM, Sunday", "Final Score: 3-2", "Lineups: Real Madrid - Courtois, Ramos, Benzema; Barcelona - Ter Stegen, Pique, Messi")
elif Football == "bundesliga":
    print("Bayern Munich vs Borussia Dortmund, 6PM, Saturday", "Final Score: 4-2", "Lineups: Bayern Munich - Neuer, Alaba, Lewandowski; Borussia Dortmund - Hitz, Hummels, Haaland")
elif Basketball == "NBA":
    print("Lakers vs Celtics, 7 PM, Friday", "Final Score: 110-105", "Lineups: Lakers - LeBron, Davis, Westbrook; Celtics - Tatum, Brown, Walker")
elif Basketball == "Euro League":
    print("CSKA Moscow vs Fenerbahce, 9 PM, Saturday", "Final Score: 85-80", "Lineups: CSKA Moscow - Clyburn, Hackett, Hines; Fenerbahce - De Colo, Vesely, Sloukas")
elif Basketball == "CBA":
    print("Guangdong vs Liaoning, 7 PM, Sunday", "Final Score: 98-95", "Lineups: Guangdong - Yi, Zhou, Marsh; Liaoning - Han, Fogg, Zhang")
elif Volleyball == "AVP":
    print("Dalhausser/Day vs Gibb/Rosenthal, 3 PM, Saturday", "Final Score: 21-18, 19-21, 15-13", "Lineups: Dalhausser/Day - Dalhausser, Day; Gibb/Rosenthal - Gibb, Rosenthal")
elif Volleyball == "FIVB": 
    print("Italy vs Brazil, 6 PM, Sunday", "Final Score: 3-2", "Lineups: Italy - Juantorena, Zaytsev, Lanza; Brazil - Bruno, Lucarelli, Wallace")
elif Volleyball == "NCAA":
    print("Texas vs UCLA, 8 PM, Friday", "Final Score: 3-1", "Lineups: Texas - Tuiasosopo, Sander, Smith; UCLA - Anderson, Johnson, Lee")
else:
    print("Error code 404 not found X(")

print("Thank you for using the sports.py program. Enjoy your day!")

