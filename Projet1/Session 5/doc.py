class Document:
    def __init__(self,titre:str,auteur:str,nbrPage:int=1)->None:
        self.__titre = titre
        self.auteur = auteur
        self.nbrPage = nbrPage

    def afficher(self):
        print('Document: ')
        print('Titre: ',self.__titre)
        print('Auteur: ',self.auteur)
        print('Nombre Page: ',self.nbrPage)

    def __str__(self)->str:
        return f"Titre: {self.__titre}, Auteur: {self.auteur} Nombre Page: {self.nbrPage}"
    
    # def getTitre(self):
    #     return(self.__titre)
    
    # def setTitre(self,titre):
    #     self.__titre=titre

    @property
    def titre(self):
        return self.__titre
    
    @titre.setter
    def titre(self,value):
        self.__titre = value


# doc1 = Documant()
# print(doc1)
# doc2 = Documant("Fille de papier","Musso",367)
# doc2.afficher()
