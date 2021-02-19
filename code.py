# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 12:14:25 2021

@author: armand
"""


#initiation de mon tableau de données
"""
    chaque entrée de mon tableau tabData correspondra à un tableau
    imbriqué, qui contiendra le type de viewMode, le nombre d'occurence 
    qui se suivent et un autre tableau imbriqué qui contiendra la liste 
    des niveaux de zoom
    
    exemple :
        tabData = [
            'standard', 4, ['19', '12', '14'],
            ]
"""
tabData = []

# readlines me permet de lire le contenu de mon fichier
file = open('data.txt', 'r')
Lines = file.readlines()

PreviousViewMode = ".";
CurrentViewMode = "";

indice = 0;


# permet de parcourir chaque ligne de mon fichier
for line in Lines:
    
    # permet de verifier si la ligne correspond au format d'une tuile
    if line.find("/map/1.0/slab/") != -1 :
        
        # me permet de découper ma chaine pour récupérer ce qui m'interesse 
        splitLine = line.split('/map/1.0/slab/')
        splitLine2 = splitLine[1].split("/");
        
        #permet de recupérer le view mode de la ligne
        CurrentViewMode = splitLine2[0]
        
        """ 
            me permet de savoir si le view mode précedent est similaire
            au viewmode actuel, ainsi je peux savoir si elles se suivent ou
            pas
        """ 
        if PreviousViewMode == CurrentViewMode :
            
            # tabData[indice-1][1] permet d'accéder au nbr d'occurence du viewmode indice-1 
            tabData[indice-1][1]+=1;
            
            # permet de savoir si le niveau de zoom actuel, n'a pas encore été ajouté dans mon tableau de niveaux de zoom
            # du view mode indice - 1
            
            # splitLine2[2] contient le niveau de zoom
            if splitLine2[2] not in tabData[indice-1][2] :
                tabData[indice-1][2].append(splitLine2[2])
        # permet d'ajouter un nouvel élément dans mon tableau tabData
        # splitLine2[2] contient le niveau de zoom
        else :
            tabData.append([CurrentViewMode,1,[splitLine2[2]]])
            PreviousViewMode = CurrentViewMode
            indice+=1;
            
for i in range( len(tabData) ) :
    
    listZoom = ",".join([str(element) for element in tabData[i][2]])
    print(tabData[i][0]+"\t"+str(tabData[i][1])+"\t"+" {} \n".format(str(listZoom)))