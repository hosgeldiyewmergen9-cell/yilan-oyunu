import pygame
import random
import sys

pygame.init()

SIYAH = (0, 0, 0)
BEYAZ = (255, 255, 255)
KIRMIZI = (255, 0, 0)
YESIL = (0, 255, 0)
MAVI = (100, 100, 255)

GENISLIK = 400
YUKSEKLIK = 500
KARE_BOYUT = 20

ekran = pygame.display.set_mode((GENISLIK, YUKSEKLIK))
pygame.display.set_caption('Yilan Oyunu')
saat = pygame.time.Clock()
font = pygame.font.Font(None, 30)
buton_font = pygame.font.Font(None, 40)

def yem_olustur(yilan):
    while True:
        x = random.randint(0, (GENISLIK - KARE_BOYUT) // KARE_BOYUT) * KARE_BOYUT
        y = random.randint(0, (YUKSEKLIK - 100 - KARE_BOYUT) // KARE_BOYUT) * KARE_BOYUT
        if [x, y] not in yilan:
            return [x, y]

def buton_ciz(metin, x, y, genislik, yukseklik):
    pygame.draw.rect(ekran, MAVI, (x, y, genislik, yukseklik))
    pygame.draw.rect(ekran, BEYAZ, (x, y, genislik, yukseklik), 2)
    yazi = buton_font.render(metin, True, BEYAZ)
    ekran.blit(yazi, (x + genislik//2 - yazi.get_width()//2, y + yukseklik//2 - yazi.get_height()//2))

def buton_tikla(mouse_pos, x, y, genislik, yukseklik):
    return x <= mouse_pos[0] <= x + genislik and y <= mouse_pos[1] <= y + yukseklik

def oyun():
    yilan = [[200, 200], [180, 200], [160, 200]]
    yon = "SAG"
    yem = yem_olustur(yilan)
    skor = 0
    oyun_bitti = False
    
    while not oyun_bitti:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                
                if buton_tikla(mouse_pos, 150, 410, 100, 40) and yon != "ASAGI":
                    yon = "YUKARI"
                elif buton_tikla(mouse_pos, 150, 450, 100, 40) and yon != "YUKARI":
                    yon = "ASAGI"
                elif buton_tikla(mouse_pos, 50, 430, 90, 60) and yon != "SAG":
                    yon = "SOL"
                elif buton_tikla(mouse_pos, 260, 430, 90, 60) and yon != "SOL":
                    yon = "SAG"
        
        bas = yilan[0].copy()
        if yon == "YUKARI":
            bas[1] -= KARE_BOYUT
        elif yon == "ASAGI":
            bas[1] += KARE_BOYUT
        elif yon == "SOL":
            bas[0] -= KARE_BOYUT
        elif yon == "SAG":
            bas[0] += KARE_BOYUT
        
        yilan.insert(0, bas)
        
        if bas == yem:
            skor += 10
            yem = yem_olustur(yilan)
        else:
            yilan.pop()
        
        if bas[0] < 0 or bas[0] >= GENISLIK or bas[1] < 0 or bas[1] >= 400:
            oyun_bitti = True
        if bas in yilan[1:]:
            oyun_bitti = True
        
        ekran.fill(SIYAH)
        
        for segment in yilan:
            pygame.draw.rect(ekran, YESIL, (segment[0], segment[1], KARE_BOYUT, KARE_BOYUT))
        pygame.draw.rect(ekran, KIRMIZI, (yem[0], yem[1], KARE_BOYUT, KARE_BOYUT))
        
        skor_text = font.render(f'Skor: {skor}', True, BEYAZ)
        ekran.blit(skor_text, (10, 405))
        
        buton_ciz("↑", 150, 410, 100, 40)
        buton_ciz("↓", 150, 450, 100, 40)
        buton_ciz("←", 50, 430, 90, 60)
        buton_ciz("→", 260, 430, 90, 60)
        
        pygame.display.update()
        saat.tick(8)
    
    ekran.fill(SIYAH)
    bitti_text = font.render('OYUN BITTI!', True, KIRMIZI)
    skor_text = font.render(f'Skorunuz: {skor}', True, BEYAZ)
    ekran.blit(bitti_text, (130, 200))
    ekran.blit(skor_text, (130, 240))
    pygame.display.update()
    pygame.time.wait(3000)
    pygame.quit()

oyun()
