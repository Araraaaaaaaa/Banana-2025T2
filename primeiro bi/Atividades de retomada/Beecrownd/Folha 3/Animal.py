'''https://www.beecrowd.com.br/repository/UOJ_1049.html'''

animal = []
for i in range(3):
    animal.append(input())
match animal[0]:
    case "vertebrado":
        match animal[1]:
            case "ave":
                match animal[2]:
                    case "carnivoro":
                        print("Aguia")
                    case "onivoro":
                        print("Pomba")
            case "mamifero":
                match animal[2]:
                    case "onivoro":
                        print("Homem")
                    case "herbivoro":
                        print("Vaca")
    case "invertebrado":
        match animal[1]:
            case "inseto":
                match animal[2]:
                    case "hematofago":
                        print("Pulga")
                    case "herbivoro":
                        print("Lagarta")
            case "analideo":
                match animal[2]:
                    case "hematofago":
                        print("Sanguessuga")
                    case "onivoro":
                        print("Minhoca")
