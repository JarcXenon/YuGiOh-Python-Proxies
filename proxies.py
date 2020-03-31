import requests, os

def NameToCode(nom):
    lien2 = 'https://db.ygoprodeck.com/api/v6/cardinfo.php?name=' + nom
    data = requests.get(lien2).content
    txt = str(data)
    debut = txt.find('id') + 4
    fin = txt.find(',"name"')
    return(txt[debut:fin])

if not os.path.isfile('decklist.txt') and os.path.isfile('decklist.ydk'):
    data = requests.get('https://db.ygoprodeck.com/api/v6/cardinfo.php').content
    txt = str(data)
    with open('decklist.ydk') as f:
        with open('decklist.txt', 'w') as g:
            lignes = f.readlines()
            for i in lignes:
                if i[0] != '#' and i[0] != '!' and i != '\n':
                    code = i[:-1]
                    debut = txt.find(code)
                    texte = txt[debut:]
                    fin = texte.find(',"type') - 1
                    debut = texte.find('name"') + 7
                    nom = texte[debut:fin]
                    g.write(nom.replace("\\", "") + '\n')

with open('decklist.txt', 'r') as f:
    with open('cards.tex', 'w') as g:
        lignes = f.readlines()
        i = 0
        for ligne in lignes:
            if ligne[0] != '#' and ligne[0] != '!' and ligne != '\n':
                g.write('\\'+'card{' + ligne[:-1].replace(' ','_').replace('/','_') + '}\n')
                i += 1
                if i == 3:
                    g.write('\\'+'\\'+'[-0.3mm]\n')
                    i = 0
                nom = ligne[:-1]
                code = NameToCode(nom)
                jpg = nom.replace(' ','_').replace('/','_') + '.jpg'
                lien = 'https://storage.googleapis.com/ygoprodeck.com/pics/' + code + '.jpg'
                if not os.path.isfile('images/'+ jpg):
                    data = requests.get(lien).content
                    with open('images/'+ jpg, 'wb') as handle:
                        handle.write(data)

os.system('pdflatex proxies.tex')
