def main() -> None:
    print("Hello from insultle!")

import pygame
import random


pygame.init()

Larghezza_Schermo = 822
Altezza_Schermo = 745

schermo = pygame.display.set_mode((Larghezza_Schermo, Altezza_Schermo)) 
pygame.display.set_caption("Insultle") 

imgSfondo = pygame.image.load("sfondoINSULTLE.jpg") #devo aggiungre il file dopo
imgSfondo = pygame.transform.scale(imgSfondo,(Larghezza_Schermo,Altezza_Schermo))

running = True
#LetteraA = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_a:
#                 LetteraA = True

ParoleComputer = ["RINCO", "SCEMO", "TONTO", "BABBO", "LENTO", "TARDO", "PIGRO", "ROZZO", "FOLLE", "MOLLE"]
ParoleAccUtente = ["acqua", "adulto", "aereo", "aglio", "aiuto", "album", "amaro", "amico", "amica", "amore", "ampio", "anima", "anno", "ansia", "apice", "aroma", "asino", "aspro", "attua", "avere", "bacio", "banca", "barca", "basso", "beato", "bella", "bello", "benda", "birra", "bocca", "bolle", "bordo", "bosco", "bravo", "breve", "bruno", "buono", "burro", "caldo", "calma", "calvo", "campo", "canto", "capra", "carne", "carro", "carta", "cassa", "cella", "censo", "cento", "certo", "cielo", "cifra", "citta", "colpa", "collo", "conto", "copra", "corda", "corpo", "corso", "costa", "crema", "cuore", "danno", "degno", "denso", "dente", "detto", "dieci", "disco", "dolce", "donna", "dorme", "dorso", "duomo", "edera", "entra", "esame", "esito", "estate", "falso", "fango", "fatta", "fatto", "ferma", "ferro", "festa", "fiore", "filo", "firma", "fisso", "fiume", "foglia", "folla", "fondo", "forno", "forse", "forte", "fossa", "frase", "freno", "frigo", "fuoco", "fuori", "gallo", "gamba", "gatto", "gente", "genio", "gesso", "gioco", "gioia", "grado", "grano", "grato", "grave", "grido", "guida", "gusto", "hotel", "idolo", "igloo", "imita", "invia", "labbro", "lampo", "largo", "latte", "leale", "legno", "lento", "libro", "lieto", "limbo", "limone", "linea", "lista", "litro", "luogo", "lusso", "madre", "magia", "mamma", "manda", "mango", "marca", "marea", "marmo", "massa", "matto", "mezzo", "miele", "misto", "molto", "mondo", "morte", "mossa", "motto", "museo", "nasce", "nervo", "nesso", "nobile", "norma", "notte", "nuovo", "nuova", "occhi", "odora", "offre", "oliva", "ombra", "opera", "orari", "ormai", "osare", "padre", "paese", "palco", "palla", "palma", "panca", "paura", "pezzo", "piano", "piede", "piena", "pieno", "pietra", "pigro", "pinna", "pista", "pizza", "porta", "posto", "prato", "preme", "primo", "prova", "pugno", "punta", "punto", "quale", "quota", "radio", "reale", "regno", "resta", "ricco", "ritmo", "rocca", "rosso", "rotta", "ruota", "ruolo", "sacco", "salto", "salvo", "santo", "scala", "scena", "scopo", "scuro", "sedia", "segno", "sella", "senno", "senso", "serio", "serra", "sesto", "sogno", "soldi", "sonno", "sopra", "sorte", "spada", "spesa", "spina", "stato", "stile", "stima", "suono", "tacco", "taglio", "tanto", "tassa", "tazza", "tempo", "tenue", "terra", "testa", "tetto", "tigre", "tondo", "torre", "torta", "trama", "treno", "trova", "tutto", "udire", "ulivo", "umano", "umile", "unico", "unire", "usare", "utile", "valle", "vanto", "vasca", "verde", "verme", "verso", "vetro", "viale", "villa", "vinci", "viola", "vista", "visto", "vitto", "volpe", "volta", "volto", "zaino", "zampa", "zebra", "zitto", "zolla", "zucca"]


# QUI CI STA IL RANDOM --->



pygame.quit()