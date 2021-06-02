import random
import re

'''
Format : XdY
'''
def lancer_des(des):
    res=[]
    des = des.split("d")
    if des[0]=='':
        des[0]='1'
    nombre_des = int(des[0])
    for i in range(nombre_des):
        k=random.randint(1,int(des[1]))
        res.append(k)
    return res


class Traits:
    def __init__(self):
        self.liste_qualites=[
        "Affinité avec les animaux",
        "Allié puissant",
        "Ambidextre",
        "Ange gardien",
        "Captivant",
        "Chanceux",
        "Constitution de fer",
        "Dur à cuire",
        "Horloge interne",
        "Meneur d’homme",
        "Nyctalope",
        "Pas de loup",
        "Rapide",
        "Résistant à l’alcool",
        "Résistant aux maladies",
        "Riche"
        ]
        
        self.liste_defauts=[
        "Âgé",
        "Amnésique",
        "Arrogant",
        "Chétif",
        "Code d’honneur",
        "Curieux",
        "Dépendant",
        "Distrait",
        "Endetté",
        "Impulsif",
        "Lâche",
        "Malade",
        "Obsédé",
        "Recherché",
        "Sceptique",
        "Timide"
        ]
        
        
        self.qualite=self.liste_qualites[sum(lancer_des("3d6"))-3]
        self.defaut=self.liste_defauts[sum(lancer_des("3d6"))-3]
        
    def __str__(self):
        res=""
        res+="Qualité : "+self.qualite+"\n"
        res+="Défaut : "+self.defaut+"\n"
        return res
    

class Competences:
    def __init__(self):
        
        self.liste_competences_generales=[
        "Athlétisme",
        "Bagarre",
        "Combat à distance",        
        "Cuisine",
        "Déguisement",
        "Démolition",        
        "Eloquence",
        "Escrime",
        "Esquive",
        "Fouille",
        "Furtivité",
        "Interrogation",        
        "Premiers soins",
        "Séduction",        
        "Vigilance",
        ]
        
        self.liste_competences_academiques =[
        "Administration",
        "Alpinisme",
        "Artisanat",
        "Botanique",
        "Bricolage",
        "Chimie",
        "Crochetage",
        "Cryptographie",
        "Electronique",
        "Equitation",
        "Histoire",
        "Informatique",
        "Jeu",
        "Langue",
        "Mécanique",
        "Médecine",
        "Navigation",
        "Pickpocket",
        "Pilotage",
        "Physique",
        "Survie",
        "Usages",
        "Zoologie"
        ]
        
        cg=random.sample(self.liste_competences_generales,10)
        cg.sort()
        self.competences_generales=cg
        
        ca=random.sample(self.liste_competences_academiques,5)
        ca.sort()
        self.competences_academiques=ca

    def get(self):
        return [self.competences_generales,self.competences_academiques]
    
    def __str__(self):
        margin="   "
        res="Compétences générales :\n"
        for c in self.competences_generales:
            res+=margin + c + "\n"
        
        res+="\nCompétences académiques :\n"
        for c in self.competences_academiques:
            res+=margin + c + "\n"
        
        return res
        

class Attributs:
    def __init__(self):
        nom_attributs_primaires=["Force","Endurance","Habileté","Agilité","Erudition","Charisme","Volonté","Perception"]
        nom_attributs_secondaires=["Vitalité","Initiative","Héroïsme","Raison"]
        [primaires, secondaires] = self.choisir_attributs_aleatoirement()
        self.primaires = dict(zip(nom_attributs_primaires, primaires))
        self.secondaires = dict(zip(nom_attributs_secondaires, secondaires))
        
    def __str__(self):
        res=""
        for key, value in self.primaires.items():
            res+=str(key)[0:3].upper()+ ' : ' + str(value) + " | "
        res+="\n"
        
        for key, value in self.secondaires.items():
            res+=str(key)[0:3].upper()+ ' : ' + str(value) + " | "
        res+="\n"
        return res
        
    def get(self):
        return [self.primaires,self.secondaires]
    
    '''
    6 points à répartir.
    Max +3 par attribut
    '''
    def choisir_attributs_aleatoirement(self):
        res_primaires =[0]*8
        res_secondaires =[0]*4
        
        # Attributs primaires 
        nombre_bonus_a_distribuer = 6
        n=len(res_primaires) # 8
        
        # p : probabilité qu'un attribut soit décrémenté
        p=0.15
        for i in range(n):
            if random.random()<p :
                res_primaires[i]-=1
                nombre_bonus_a_distribuer+=1
        
        for i in range(nombre_bonus_a_distribuer):
            k=random.randint(0,n-1)
            while(res_primaires[k]>3):
                k=random.randint(0,n-1)
            res_primaires[k]+=1
        
        # Attributs secondaires
        
        # Vitalité = 10 + End + Vol
        res_secondaires[0] = 10 + res_primaires[1]+res_primaires[6] 
        
        # Initiative = Hab + Agi + Per
        res_secondaires[1] = res_primaires[2]+res_primaires[3]+res_primaires[7]
        
        # Héroïsme = 1
        res_secondaires[2] = 1
        
        # Raison = 10 + Eru + Vol
        res_secondaires[3] = 10 +res_primaires[4] +res_primaires[6]
        
        return [res_primaires,res_secondaires]
        
        

class Personnage:
    def __init__(self, nom):
        self.nom = nom
        self.taille = random.gauss(1.75, 0.1)
        self.poids  = random.gauss(75, 10)
        self.attributs = Attributs()
        self.competences = Competences()
        self.traits = Traits()
        self.monnaie = 100+sum(lancer_des(str(random.randint(3,10))+"d6"))
        self.appliquer_traits()
        
    def appliquer_traits(self):
        qualite=self.traits.qualite
        defaut=self.traits.defaut
        
        if defaut=="Âgé":
            self.attributs.primaires["Force"]-=1
            self.attributs.primaires["Agilité"]-=1
            
        if qualite=="Rapide":
            self.attributs.secondaires["Initiative"]+=1
            
        if qualite=="Riche":
            self.monnaie += 100*sum(lancer_des("10d6"))
        
        
    def __str__(self):
        res ="Nom : "+self.nom+"   "
        res+="Taille : "+str(round(self.taille,2))+"m   "
        res+="Poids : "+str(int(self.poids))+"kg\n"
        res+="\nAttributs : \n"+str(self.attributs)+"\n"
        res+=str(self.competences)+"\n"
        res+=str(self.traits)+"\n"
        res+="Monnaie : "+str(self.monnaie)
        return res
        
        


james = Personnage("James")
print(james)

