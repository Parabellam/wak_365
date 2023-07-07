import os
import pyautogui
import time
import sys
from pynput import keyboard
import threading

# Obtener las dimensiones de la pantalla
screen_width, screen_height = pyautogui.size()

# Definir los límites del área de búsqueda para la mitad de la pantalla hacia abajo
abajo_region = (0, screen_height // 2, screen_width, screen_height // 2)

# Definir los límites del área de búsqueda para la mitad de la pantalla hacia arriba
arriba_region = (0, 0, screen_width, screen_height // 2)

img_unica = { # imagen unica punto apoyo p1
    "cofre": os.path.join("imgs_programa","cofre.png"),
}

apoyo_p2_1= { # apoyo p2
    "img_apoyo_p2_1": os.path.join("imgs_programa","img_apoyo_p2_1.png"),
    "img_apoyo_p2_11": os.path.join("imgs_programa","img_apoyo_p2_11.png"),
}
apoyo_p2_2= { # apoyo p2
    "img_apoyo_p2_2": os.path.join("imgs_programa","img_apoyo_p2_2.png"),
}
apoyo_p2_3= { # apoyo p2
    "img_apoyo_p2_3": os.path.join("imgs_programa","img_apoyo_p2_3.png"),
}
apoyo_p2_4= { # apoyo p2
    "img_apoyo_p2_4": os.path.join("imgs_programa","img_apoyo_p2_4.png"),
}
apoyo_p2_5= { # apoyo p2
    "img_apoyo_p2_5": os.path.join("imgs_programa","img_apoyo_p2_5.png"),
}

apoyo_p3_1= { # apoyo p3
    "img_apoyo_p3_1": os.path.join("imgs_programa","img_apoyo_p3_1.png"),
}
apoyo_p3_2= { # apoyo p3
    "img_apoyo_p3_2": os.path.join("imgs_programa","img_apoyo_p3_2.png"),
}
apoyo_p3_3= { # apoyo p3
    "img_apoyo_p3_3": os.path.join("imgs_programa","img_apoyo_p3_3.png"),
}

apoyo_p4_1= { # apoyo p4
    "img_apoyo_p4_1": os.path.join("imgs_programa","img_apoyo_p4_1.png"),
    "img_apoyo_p4_11": os.path.join("imgs_programa","img_apoyo_p4_11.png"),
}
apoyo_p4_2= { # apoyo p4
    "img_apoyo_p4_2": os.path.join("imgs_programa","img_apoyo_p4_2.png"),
    "img_apoyo_p4_x": os.path.join("imgs_programa","img_apoyo_p4_x.png"),
}
apoyo_p4_3= { # apoyo p4
    "img_apoyo_p4_3": os.path.join("imgs_programa","img_apoyo_p4_3.png"),
    "img_apoyo_p4_33": os.path.join("imgs_programa","img_apoyo_p4_33.png"),
    "img_apoyo_p4_333": os.path.join("imgs_programa","img_apoyo_p4_333.png"),
    "img_apoyo_p4_3333": os.path.join("imgs_programa","img_apoyo_p4_3333.png"),
}

apoyo_p5_1= { # apoyo p5
    "img_apoyo_p5_1": os.path.join("imgs_programa","img_apoyo_p5_1.png"),
    "img_apoyo_p5_11": os.path.join("imgs_programa","img_apoyo_p5_11.png"),
    "img_apoyo_p5_111": os.path.join("imgs_programa","img_apoyo_p5_111.png"),
}
apoyo_p5_2= { # apoyo p5
    "img_apoyo_p5_2": os.path.join("imgs_programa","img_apoyo_p5_2.png"),
    "img_apoyo_p5_22": os.path.join("imgs_programa","img_apoyo_p5_22.png"),
    "img_apoyo_p5_222": os.path.join("imgs_programa","img_apoyo_p5_222.png"),
}
apoyo_p5_3= { # apoyo p5
    "img_apoyo_p5_3": os.path.join("imgs_programa","img_apoyo_p5_3.png"),
    "img_apoyo_p5_33": os.path.join("imgs_programa","img_apoyo_p5_33.png"),
    "img_apoyo_p5_333": os.path.join("imgs_programa","img_apoyo_p5_333.png"),
    "img_apoyo_p5_3333": os.path.join("imgs_programa","img_apoyo_p5_3333.png"),
}
apoyo_p5_4= { # apoyo p5
    "img_apoyo_p5_4": os.path.join("imgs_programa","img_apoyo_p5_4.png"),
    "img_apoyo_p5_44": os.path.join("imgs_programa","img_apoyo_p5_44.png"),
    "img_apoyo_p5_33": os.path.join("imgs_programa","img_apoyo_p5_33.png"), # Comparte algunas con el 3, no hay problema
    "img_apoyo_p5_333": os.path.join("imgs_programa","img_apoyo_p5_333.png"),
}

img_p1_temporal = { # imagen p1 temporales Sacro
    "p11": os.path.join("imgs_temporales","p11.png"),
    "p12": os.path.join("imgs_temporales","p12.png"),
    "p13": os.path.join("imgs_temporales","p13.png"),
    "p14": os.path.join("imgs_temporales","p14.png"),
    "p15": os.path.join("imgs_temporales","p15.png"),
    "p16": os.path.join("imgs_temporales","p16.png"),
    "p17": os.path.join("imgs_temporales","p17.png"),
    "p18": os.path.join("imgs_temporales","p18.png"),
    "p19": os.path.join("imgs_temporales","p19.png"),
    "p110": os.path.join("imgs_temporales","p110.png"),
}

img_p2_temporal = { # imagen temporales p2 panda
    "p21": os.path.join("imgs_temporales","p21.png"),
    "p22": os.path.join("imgs_temporales","p22.png"),
    "p23": os.path.join("imgs_temporales","p23.png"),
    "p24": os.path.join("imgs_temporales","p24.png"),
    "p25": os.path.join("imgs_temporales","p25.png"),
    "p26": os.path.join("imgs_temporales","p26.png"),
    "p27": os.path.join("imgs_temporales","p27.png"),
    "p28": os.path.join("imgs_temporales","p28.png"),
    "p29": os.path.join("imgs_temporales","p29.png"),
    "p210": os.path.join("imgs_temporales","p210.png"),
    "p211": os.path.join("imgs_temporales","p211.png"),
    "p212": os.path.join("imgs_temporales","p212.png"),
}

img_p3_temporal = { # imagen p3 temporales ZOBAL
    "p31": os.path.join("imgs_temporales","p31.png"),
    "p32": os.path.join("imgs_temporales","p32.png"),
    "p33": os.path.join("imgs_temporales","p33.png"),
    "p34": os.path.join("imgs_temporales","p34.png"),
    "p35": os.path.join("imgs_temporales","p35.png"),
    "p36": os.path.join("imgs_temporales","p36.png"),
}

img_p4_temporal = { # imagen p4 temporales BRAKMAR OCRA
    "p41": os.path.join("imgs_temporales","p41.png"),
    "p42": os.path.join("imgs_temporales","p42.png"),
    "p43": os.path.join("imgs_temporales","p43.png"),
    "p44": os.path.join("imgs_temporales","p44.png"),
}

img_p5_temporal = { # imagen p5 temporales AMAKNA OSAMODA
    "p51": os.path.join("imgs_temporales","p51.png"),
    "p52": os.path.join("imgs_temporales","p52.png"),
    "p53": os.path.join("imgs_temporales","p53.png"),
    "p54": os.path.join("imgs_temporales","p54.png"),
    "p55": os.path.join("imgs_temporales","p55.png"),
    "p56": os.path.join("imgs_temporales","p56.png"),
    "p57": os.path.join("imgs_temporales","p57.png"),
    "p58": os.path.join("imgs_temporales","p58.png"),
    "p59": os.path.join("imgs_temporales","p59.png"),
    "p510": os.path.join("imgs_temporales","p510.png"),
    "p511": os.path.join("imgs_temporales","p511.png"),
    "p512": os.path.join("imgs_temporales","p512.png"),
}

logeo_img = { # imagen logeando
    "logeo1": os.path.join("imgs_programa","logeo1.png"),
    "logeo2": os.path.join("imgs_programa","logeo2.png"),
    "logeo3": os.path.join("imgs_programa","logeo3.png"),
    "logeo4": os.path.join("imgs_programa","logeo4.png"),
    "logeo5": os.path.join("imgs_programa","logeo5.png"),
    "logeo6": os.path.join("imgs_programa","logeo6.png"),
}

deslogeo_img = { # imagen deslogeo
    "deslogeo1":os.path.join("imgs_programa", "deslogeo1.png"),
    "deslogeo2": os.path.join("imgs_programa","deslogeo2.png"),
    "deslogeo3": os.path.join("imgs_programa","deslogeo3.png"),
    "deslogeo4": os.path.join("imgs_programa","deslogeo4.png"),
    "deslogeo5": os.path.join("imgs_programa","deslogeo5.png"),
}

deslogeosi_img={ # Botón "Sí" al deslogear
    "deslogeo1si":os.path.join("imgs_programa", "deslogeo1si.png"),
    "deslogeo2si": os.path.join("imgs_programa","deslogeo2si.png"),
    "deslogeo3si": os.path.join("imgs_programa","deslogeo3si.png"),
    "deslogeo4si": os.path.join("imgs_programa","deslogeo4si.png"),
}

deslogeo_carga_img={
    "deslogeo33": os.path.join("imgs_programa","deslogeo33.png"),
    "deslogeo44": os.path.join("imgs_programa","deslogeo44.png"),
    "deslogeo55": os.path.join("imgs_programa","deslogeo55.png"),
    "deslogeo66": os.path.join("imgs_programa","deslogeo66.png"),
    "deslogeo77": os.path.join("imgs_programa","deslogeo77.png"),
}

minarboton_img={ # Botón minar
    "minar1": os.path.join("imgs_programa", "minar1.png"),
    "minar2": os.path.join("imgs_programa", "minar2.png"),
    "minar3": os.path.join("imgs_programa", "minar3.png"),
}

print("------------------------INICIO-------------------------------------------------------")
print("3 segundos... iniciando... espere confirmación")
time.sleep(3)
print("------------------------NOTAS-------------------------------------------------------")
print("Las imágenes proporcionadas para el reconocimiento de cada personaje, no debe estar el personaje seleccionado")
print("Para iniciar, ubiquese en el menú de seleccionar personaje y de un solo click en el último personaje")

print("------------------------COMIENZO-------------------------------------------------------")

print("INGRESE EL NÚMERO DE PERSONAJES:")
np = int(input("=>"))  # Convierte np en un entero

print("----------------------------------------------------------------------------------------:")

print("5 segundos, vaya al juego")
time.sleep(5)  # Esperar

pyautogui.FAILSAFE=False

#  "p1": "p1.png" - "p2": "p2.png" - "p3": "p3.png" - asi se guarda cada img en el diccionario
image_dicts = {}
for i in range(1, np + 1):
    image_key = f"p{i}"
    image_path = f"p{i}.png"
    image_dicts[image_key] = image_path

positions = {}

for image_nameX99, image_pathX99 in image_dicts.items(): # Buscar imágen
    location = None
    while location is None: # Buscar la imagen continuamente hasta encontrarla
        location = pyautogui.locateOnScreen(image_pathX99, confidence=0.8)

    if location: # imagen encontrada
        position = pyautogui.center(location)
        positions[image_nameX99] = position

def deslogeo():
    max_attempts = 3 # Máximo de veces que busca la imagen
    attempts = 0 # Inicializa las veces
    process_counter = 0
    max_process_repeats = 50

    pyautogui.press('esc')  # Presiona la tecla Esc
    time.sleep(1) # Tiempo que tarda pisando la tecla
    cambiar_personaje_encontrado = False
    start_time = time.time()  # Obtener el tiempo de inicio

    while not cambiar_personaje_encontrado:
        pyautogui.moveTo(0, 0)
        for _, image_pathXX in deslogeo_img.items():  # Buscar imágen de CAMBIAR DE PERSONAJE
            locationdeslogeo_img = pyautogui.locateOnScreen(image_pathXX, confidence=0.9)

            if locationdeslogeo_img:
                center = pyautogui.center(locationdeslogeo_img)
                time.sleep(0.5)  # Esperar
                pyautogui.doubleClick(center)  # Realiza un doble clic en la posición center
                cambiar_personaje_encontrado = True
                time.sleep(1)  # Esperar
                break  # Salir del bucle for

        elapsed_time = time.time() - start_time  # Calcular el tiempo transcurrido

        if elapsed_time >= 6:  # Si han pasado 6 segundos y no se ha encontrado la imagen
            pyautogui.press('esc')  # Presionar la tecla Esc
            time.sleep(1)  # Tiempo que tarda pisando la tecla
            start_time = time.time()  # Reiniciar el tiempo de inicio para buscar la imagen nuevamente

    deslogeo_si_encontrado = False
    while not deslogeo_si_encontrado:
        pyautogui.moveTo(0, 0)
        for _, image_pathX3 in deslogeosi_img.items():  # Buscar imágen de deslogeo SI
            locationdeslogeosi_img = pyautogui.locateOnScreen(image_pathX3, confidence=0.9)

            if locationdeslogeosi_img:
                center = pyautogui.center(locationdeslogeosi_img)
                time.sleep(7)  # Esperar
                pyautogui.doubleClick(center)  # Realiza un doble clic en la posición center
                deslogeo_si_encontrado = True
                break  # Salir del bucle for
            else:
                print("NO se ha encontrado la imagen SI deslogeo<---")

    while attempts < max_attempts:
        for _, image_pathX4 in deslogeo_carga_img.items(): # Buscar imágen de deslogeo_carga
            location = pyautogui.locateOnScreen(image_pathX4, confidence=0.9)

            if location:
                time.sleep(4)  # Espera 4 segundos antes de repetir el proceso
                attempts = 0  # Reinicia el contador de intentos
            else:
                attempts += 1
                time.sleep(1)

        # Verifica si el proceso se ha repetido 50 veces
        if process_counter >= max_process_repeats:
            sys.exit()

        # Incrementa el contador de procesos
        process_counter += 1
    time.sleep(1.8)
    pyautogui.moveTo(366, 508)
    # Desplazar el mouse hacia arriba 10 "clics"
    pyautogui.scroll(180)
    time.sleep(1.5)
    pyautogui.scroll(180)
    pass
def logeo(position):
    max_attempts = 4 # Máximo de veces que busca la imagen
    attempts = 0 # Inicializa las veces
    process_counter = 0
    max_process_repeats = 50
    encontrado=0
    verificacion=0
    time.sleep(3)
    print("Logeo: despues de time.sleep 3")

    while encontrado==0:
        print("Logeo: entra en el while encontrado")
        if(encontrado==1):
            break
        while attempts < max_attempts:
            print("Logeo: entra en el while attempts")
            if(encontrado==1):
                break
            for _, image_pathAS in logeo_img.items(): # Buscar imágen de logeo_img
                locationlogeo_img = pyautogui.locateOnScreen(image_pathAS, confidence=1)
                if(encontrado==1):
                    break
                if locationlogeo_img:
                    print("Logeo: entra en el if locationlogeo_img")
                    encontrado=0
                    time.sleep(2)  # Espera 2 segundos antes de repetir el proceso
                    attempts = 0  # Reinicia el contador de intentos
                    # Incrementa el contador de procesos
                    process_counter += 1
                    
                else:
                    print("Logeo: entra en el else locationlogeo_img")
                    attempts += 1
                    if(attempts>=4):
                        encontrado=1
                    time.sleep(1.5)
                    if(process_counter>49):
                        encontrado=1
                        break

            # Verifica si el proceso se ha repetido 50 veces
            if process_counter >= max_process_repeats:
                verificacion=1
                pyautogui.click(1353, 13)# Cerrar juego y abrir
                time.sleep(2)
                pyautogui.click(646, 406)
                time.sleep(5)
                pyautogui.click(1124, 748)
                time.sleep(3)
                pyautogui.rightClick(1144, 705)
                time.sleep(3)
                pyautogui.click(889, 271)
                time.sleep(10)
                pyautogui.click(270, 349)
                time.sleep(25)
                pyautogui.doubleClick(683, 352)
                time.sleep(0.2)
                pyautogui.doubleClick(683, 352)
                time.sleep(10)
                pyautogui.doubleClick(position)
    # Verifica si el proceso se ha repetido 50 veces
    if(verificacion==0 and process_counter >= max_process_repeats):
        if process_counter >= max_process_repeats:
            verificacion=1
            pyautogui.click(1353, 13)# Cerrar juego y abrir
            time.sleep(2)
            pyautogui.click(646, 406)
            time.sleep(5)
            pyautogui.click(1124, 748)
            time.sleep(3)
            pyautogui.rightClick(1144, 705)
            time.sleep(3)
            pyautogui.click(889, 271)
            time.sleep(10)
            pyautogui.click(270, 349)
            time.sleep(25)
            pyautogui.doubleClick(683, 352)
            time.sleep(0.2)
            pyautogui.doubleClick(683, 352)
            time.sleep(10)
            pyautogui.doubleClick(position)

    time.sleep(2.5)
    pass
#-------------------------------------------------------------------------------------------------------
#P11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
def action_for_p1(position):
    logeo(position)
    pyautogui.rightClick(1026, 372)
    encontradas=0
    pyautogui.moveTo(0, 0)
    time.sleep(0.2)
    for _, image_path228Q in minarboton_img.items(): # Buscar botón minar
        locationminarboton_img5Q=None
        locationminarboton_img5Q = pyautogui.locateOnScreen(image_path228Q, confidence=0.9)
        if locationminarboton_img5Q:
            encontradas+=1
            center = pyautogui.center(locationminarboton_img5Q)
            del locationminarboton_img5Q
            pyautogui.click(center)
            time.sleep(5.2) # Tiempo que tarda en llegar y minar
            pyautogui.rightClick(251, 283)
            pyautogui.moveTo(0, 0)
            time.sleep(0.2)
            for _, image_path228QR in minarboton_img.items(): # Buscar botón minar
                locationminarboton_img5QR=None
                locationminarboton_img5QR = pyautogui.locateOnScreen(image_path228QR, confidence=0.9)
                time.sleep(0.2)
                if locationminarboton_img5QR:
                    encontradas+=1
                    center = pyautogui.center(locationminarboton_img5QR)
                    del locationminarboton_img5QR
                    pyautogui.click(center)
                    time.sleep(4.1) # Tiempo que tarda en llegar y minar
                    pyautogui.click(205, 283)

    pyautogui.rightClick(554, 304)
    pyautogui.moveTo(0, 0)
    encontradas=0
    time.sleep(0.2)
    for _, image_path228QQ in minarboton_img.items(): # Buscar botón minar
        locationminarboton_img5QQ=None
        locationminarboton_img5QQ = pyautogui.locateOnScreen(image_path228QQ, confidence=0.9)
        time.sleep(0.2)
        if locationminarboton_img5QQ:
            encontradas+=1
            center = pyautogui.center(locationminarboton_img5QQ)
            del locationminarboton_img5QQ
            pyautogui.click(center)
            time.sleep(4.1) # Tiempo que tarda en llegar y minar

    contador=0
    encontradas=0
    no_encontro_nada=0
    pyautogui.moveTo(0, 0)
    time.sleep(0.3)
    for _, image_path11X in img_p1_temporal.items(): # Buscar filón
        if contador>=25 or encontradas>=5:
            break
        mina881X=None
        mina881X = pyautogui.locateOnScreen(image_path11X, confidence=0.9, grayscale=True)
        time.sleep(0.2)
        if mina881X:
            center1X = pyautogui.center(mina881X)
            pyautogui.rightClick(center1X)
            del mina881X
            pyautogui.moveTo(0, 0)
            time.sleep(0.3)
            for _, image_path227X in minarboton_img.items(): # Buscar botón minar
                locationminarboton_img5=None
                locationminarboton_img5 = pyautogui.locateOnScreen(image_path227X, confidence=0.9, region=abajo_region)
                time.sleep(0.2)
                if locationminarboton_img5:
                    encontradas+=1
                    center = pyautogui.center(locationminarboton_img5)
                    del locationminarboton_img5
                    pyautogui.click(center)
                    time.sleep(6) # Tiempo que tarda en llegar y minar
                    no_encontro_nada=1
        contador+=1
    contador=0
    encontradas=0
    no_encontro_nada=0
    pyautogui.moveTo(0, 0)
    time.sleep(0.3)
    while contador<25:
        if contador>=25:
            print("if contador>=25:")
            break
        for _, image_path11 in img_p1_temporal.items(): # Buscar filón
            if contador>=25 and encontradas>=5:
                print("if contador>=25 and encontradas>=5:")
                break
            mina881=None
            mina881 = pyautogui.locateOnScreen(image_path11, confidence=0.9, grayscale=True)
            time.sleep(0.2)
            if mina881:
                print("if mina881:")
                center1 = pyautogui.center(mina881)
                pyautogui.rightClick(center1)
                del mina881
                pyautogui.moveTo(0, 0)
                time.sleep(0.3)
                for _, image_path227 in minarboton_img.items(): # Buscar botón minar
                    locationminarboton_img5=None
                    locationminarboton_img5 = pyautogui.locateOnScreen(image_path227, confidence=0.9)
                    time.sleep(0.2)
                    if locationminarboton_img5:
                        encontradas+=1
                        center = pyautogui.center(locationminarboton_img5)
                        del locationminarboton_img5
                        pyautogui.click(center)
                        time.sleep(6.2) # Tiempo que tarda en llegar y minar
                        no_encontro_nada=1
            contador+=1
    for _, image_path228QRS in minarboton_img.items(): # Buscar botón minar
        locationminarboton_img5QRS=None
        locationminarboton_img5QRS = pyautogui.locateOnScreen(image_path228QRS, confidence=0.9)
        time.sleep(0.2)
        if locationminarboton_img5QRS:
            encontradas+=1
            center = pyautogui.center(locationminarboton_img5QRS)
            del locationminarboton_img5QRS
            pyautogui.click(center)
            time.sleep(4.1) # Tiempo que tarda en llegar y minar
    if(no_encontro_nada==1):
        foundX=False
        pyautogui.moveTo(0, 0)
        time.sleep(0.3)
        for _, image_path in img_unica.items():
            if foundX:
                break
            loc_unica = pyautogui.locateOnScreen(image_path, confidence=0.75)
            if loc_unica:
                foundX=True
                center = pyautogui.center(loc_unica)
                pyautogui.click(center)
                time.sleep(4)
    deslogeo()
    pass
#P22222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
def action_for_p2(position):
    logeo(position)

    pyautogui.rightClick(725, 599)
    pyautogui.moveTo(0, 0)
    time.sleep(0.2)
    for _, image_path228Q in minarboton_img.items(): # Buscar botón minar
        locationminarboton_img5Q=None
        locationminarboton_img5Q = pyautogui.locateOnScreen(image_path228Q, confidence=0.9)
        if locationminarboton_img5Q:
            center = pyautogui.center(locationminarboton_img5Q)
            del locationminarboton_img5Q
            pyautogui.click(center)
            time.sleep(5.4) # Tiempo que tarda en llegar y minar
            pyautogui.rightClick(167, 63)
            pyautogui.moveTo(0, 0)
            time.sleep(0.2)
            for _, image_path228QR in minarboton_img.items(): # Buscar botón minar
                locationminarboton_img5QR=None
                locationminarboton_img5QR = pyautogui.locateOnScreen(image_path228QR, confidence=0.9)
                if locationminarboton_img5QR:
                    center = pyautogui.center(locationminarboton_img5QR)
                    del locationminarboton_img5QR
                    pyautogui.click(center)
                    time.sleep(7) # Tiempo que tarda en llegar y minar
                    pyautogui.click(1158, 458)

    pyautogui.rightClick(166, 277)
    pyautogui.moveTo(0, 0)
    time.sleep(0.2)
    for _, image_path228QQ in minarboton_img.items(): # Buscar botón minar
        locationminarboton_img5QQ=None
        locationminarboton_img5QQ = pyautogui.locateOnScreen(image_path228QQ, confidence=0.9)
        time.sleep(0.2)
        if locationminarboton_img5QQ:
            center = pyautogui.center(locationminarboton_img5QQ)
            del locationminarboton_img5QQ
            pyautogui.click(center)
            time.sleep(4.4) # Tiempo que tarda en llegar y minar


    contador=0
    encontradas=0
    while contador<=20 and encontradas<=5:
        if contador>=20 or encontradas>=5:
            print("break 306")
            break
        for _, image_path12Q in img_p2_temporal.items(): # Buscar filón
            if contador>=20 or encontradas>=5:
                print("break 310")
                break
            minaQ=None
            minaQ = pyautogui.locateOnScreen(image_path12Q, confidence=0.9, region=abajo_region, grayscale=True)
            time.sleep(0.2)
            if minaQ:
                contador+=1
                center1 = pyautogui.center(minaQ)
                del minaQ
                pyautogui.rightClick(center1)
                for _, image_path228 in minarboton_img.items(): # Buscar botón minar
                    locationminarboton_img5 = pyautogui.locateOnScreen(image_path228, confidence=0.9)
                    time.sleep(0.2)
                    if locationminarboton_img5:
                        encontradas+=1
                        center = pyautogui.center(locationminarboton_img5)
                        pyautogui.click(center)
                        time.sleep(6.2) # Tiempo que tarda en llegar y minar
            else:
                contador+=1
    contador=0
    encontradas=0
    while contador<=20 and encontradas<=5:
        if contador>=20 or encontradas>=5:
            print("break 306")
            break
        for _, image_path12 in img_p2_temporal.items(): # Buscar filón
            if contador>=20 or encontradas>=5:
                print("break 310")
                break
            mina=None
            mina = pyautogui.locateOnScreen(image_path12, confidence=0.9, grayscale=True)
            time.sleep(0.2)
            if mina:
                contador+=1
                center1 = pyautogui.center(mina)
                del mina
                pyautogui.rightClick(center1)
                for _, image_path228 in minarboton_img.items(): # Buscar botón minar
                    locationminarboton_img5 = pyautogui.locateOnScreen(image_path228, confidence=0.9)
                    time.sleep(0.2)
                    if locationminarboton_img5:
                        encontradas+=1
                        center = pyautogui.center(locationminarboton_img5)
                        pyautogui.click(center)
                        time.sleep(6.2) # Tiempo que tarda en llegar y minar
            else:
                contador+=1
    contador=0
    encontradas=0
    buscando_apoyo=0
    while contador<=3:
        if buscando_apoyo>=5:
            break
        pyautogui.moveTo(0, 0)
        time.sleep(0.3)
        for _, image_path13 in apoyo_p2_1.items(): # Buscar punto apoyo 1
            if buscando_apoyo>=5:
                print("break 328")
                break
            mina2=None
            mina2 = pyautogui.locateOnScreen(image_path13, confidence=0.9, grayscale=True)
            time.sleep(0.2)
            if mina2:
                contador=4
                center1 = pyautogui.center(mina2)
                del mina2
                pyautogui.click(center1)
                time.sleep(3.2)
            else:
                contador+=1
                buscando_apoyo+=1
                if(buscando_apoyo==2):
                    pyautogui.click(x=472,y=486) # Moverse para intentar buscar punto apoyo 1 abajo izq
                    time.sleep(2)
                if(buscando_apoyo==3):
                    pyautogui.click(x=900,y=275) # Moverse para intentar buscar punto apoyo 1 arriba derecha
                    time.sleep(2)
                    pyautogui.click(x=900,y=275) # Moverse para intentar buscar punto apoyo 1 arriba derecha
                    time.sleep(2)
    encontradas=0
    buscando_apoyo=0
    contador=0
    while contador<=3:
        if buscando_apoyo>=5:
            break
        pyautogui.moveTo(0, 0)
        time.sleep(0.3)
        for _, image_path14 in apoyo_p2_2.items(): # Buscar punto apoyo 2
            if buscando_apoyo>=5:
                print("break 350")
                break
            mina25=None
            mina25 = pyautogui.locateOnScreen(image_path14, confidence=0.9, grayscale=True)
            time.sleep(0.2)
            if mina25:
                contador=4
                center1 = pyautogui.center(mina25)
                del mina25
                pyautogui.click(center1)
                time.sleep(3.2)
            else:
                contador+=1
                buscando_apoyo+=1
                if(buscando_apoyo==2):
                    pyautogui.click(x=472,y=486) # Moverse para intentar buscar punto apoyo 2 abajo izq
                    time.sleep(2)
                if(buscando_apoyo==3):
                    pyautogui.click(x=900,y=275) # Moverse para intentar buscar punto apoyo 2 arriba derecha
                    time.sleep(2)
                    pyautogui.click(x=900,y=275) # Moverse para intentar buscar punto apoyo 2 arriba derecha
                    time.sleep(2)
    contador=0
    encontradas=0
    while contador<=20 and encontradas<=5:
        if contador>=20 or encontradas>=5:
            print("break 373")
            break
        for _, image_path15 in img_p2_temporal.items(): # Buscar filón
            if contador>=20 or encontradas>=5:
                print("break 373")
                break
            mina4=None
            mina4 = pyautogui.locateOnScreen(image_path15, confidence=0.9, grayscale=True)
            time.sleep(0.2)
            if mina4:
                contador+=1
                print("Antes de buscar apoyo 3 del break 397 ENTRA IF DE MINA4")
                center1 = pyautogui.center(mina4)
                del mina4
                pyautogui.rightClick(center1)
                for _, image_path277 in minarboton_img.items(): # Buscar botón minar
                    locationminarboton_img5 = pyautogui.locateOnScreen(image_path277, confidence=0.9)
                    time.sleep(0.2)
                    if locationminarboton_img5:
                        encontradas+=1
                        center = pyautogui.center(locationminarboton_img5)
                        pyautogui.click(center)
                        time.sleep(6.2) # Tiempo que tarda en llegar y minar
            else:
                contador+=1
                print("Antes de buscar apoyo 3 del break 397 ELSEEEE")

    print("Antes de buscar apoyo 3 del break 397")
    encontradas=0
    buscando_apoyo=0
    encontrado=0
    contador=0
    while contador<=3:
        if buscando_apoyo>=5:
            break
        pyautogui.moveTo(0, 0)
        time.sleep(0.3)
        for _, image_path16 in apoyo_p2_3.items(): # Buscar punto apoyo 3
            if buscando_apoyo>=5:
                print("break 397")
                break
            mina111=None
            mina111 = pyautogui.locateOnScreen(image_path16, confidence=0.9, grayscale=True)
            time.sleep(0.2)
            if mina111:
                contador=4
                print("Encontró punto de apoyo 3")
                center1 = pyautogui.center(mina111)
                del mina111
                pyautogui.click(center1)
                time.sleep(3)
                encontrado=1
            else:
                contador+=1
                print("NO Encontró punto de apoyo 3")
                buscando_apoyo+=1
                if(buscando_apoyo==2):
                    pyautogui.click(x=472,y=486) # Moverse para intentar buscar punto apoyo 3 abajo izq
                    time.sleep(2)
                if(buscando_apoyo==3):
                    pyautogui.click(x=900,y=275) # Moverse para intentar buscar punto apoyo 3 arriba derecha
                    time.sleep(2)
                    pyautogui.click(x=900,y=275) # Moverse para intentar buscar punto apoyo 3 arriba derecha
                    time.sleep(2)

    encontradas=0
    buscando_apoyo=0
    if(encontrado!=1):
        contador=0
        while contador<=3:
            if buscando_apoyo>=5:
                break
            pyautogui.moveTo(0, 0)
            time.sleep(0.3)
            for _, image_path17 in apoyo_p2_2.items(): # Buscar punto apoyo 2
                if buscando_apoyo>=5:
                    print("break 422")
                    break
                mina12=None
                mina12 = pyautogui.locateOnScreen(image_path17, confidence=0.9, grayscale=True)
                time.sleep(0.2)
                if mina12:
                    contador=4
                    print("Encontró punto de apoyo 2")
                    center1 = pyautogui.center(mina12)
                    del mina12
                    pyautogui.click(center1)
                    time.sleep(3.2)
                else:
                    contador+=1
                    print("NO Encontró punto de apoyo 2")
                    buscando_apoyo+=1
                    if(buscando_apoyo==2):
                        pyautogui.click(x=472,y=486) # Moverse para intentar buscar punto apoyo 2 abajo izq
                        time.sleep(2)
                    if(buscando_apoyo==3):
                        pyautogui.click(x=900,y=275) # Moverse para intentar buscar punto apoyo 2 arriba derecha
                        time.sleep(2)
                        pyautogui.click(x=900,y=275) # Moverse para intentar buscar punto apoyo 2 arriba derecha
                        time.sleep(2)
        contador=0
        encontradas=0
        buscando_apoyo=0
        while contador<=3:
            if buscando_apoyo>=5:
                break
            pyautogui.moveTo(0, 0)
            time.sleep(0.3)
            for _, image_path18 in apoyo_p2_3.items(): # Buscar punto apoyo 3
                if buscando_apoyo>=5:
                    print("break 445")
                    break
                mina13=None
                mina13 = pyautogui.locateOnScreen(image_path18, confidence=0.9, grayscale=True)
                time.sleep(0.2)
                if mina13:
                    contador=4
                    encontrado=1
                    center1 = pyautogui.center(mina13)
                    del mina13
                    pyautogui.click(center1)
                    time.sleep(2.8)
                else:
                    contador+=1
                    buscando_apoyo+=1
                    if(buscando_apoyo==2):
                        pyautogui.click(x=472,y=486) # Moverse para intentar buscar punto apoyo 3 abajo izq
                        time.sleep(2)
                    if(buscando_apoyo==3):
                        pyautogui.click(x=900,y=275) # Moverse para intentar buscar punto apoyo 3 arriba derecha
                        time.sleep(2)
                        pyautogui.click(x=900,y=275) # Moverse para intentar buscar punto apoyo 3 arriba derecha
                        time.sleep(2)
    if(encontrado==1):
        contador=0
        encontradas=0
        while contador<=10 and encontradas<=2:
            if contador>=10 or encontradas>=2:
                print("break 470")
                break
            for _, image_path19 in img_p2_temporal.items(): # Buscar filón
                if contador>=10 or encontradas>=2:
                    print("break 470")
                    break
                mina5=None
                mina5 = pyautogui.locateOnScreen(image_path19, confidence=0.9, grayscale=True)
                time.sleep(0.2)
                if mina5:
                    contador+=1
                    center1 = pyautogui.center(mina5)
                    del mina5
                    pyautogui.rightClick(center1)
                    for _, image_path278 in minarboton_img.items(): # Buscar botón minar
                        locationminarboton_img5 = pyautogui.locateOnScreen(image_path278, confidence=0.9)
                        time.sleep(0.2)
                        if locationminarboton_img5:
                            encontradas+=1
                            center = pyautogui.center(locationminarboton_img5)
                            pyautogui.click(center)
                            time.sleep(6.2) # Tiempo que tarda en llegar y minar
                            
                else:
                    contador+=1
    contador=0
    encontradas=0
    buscando_apoyo=0
    encontrado=0
    while contador<=3:
        if buscando_apoyo>=5:
            break
        pyautogui.moveTo(0, 0)
        time.sleep(0.3)
        for _, image_path112 in apoyo_p2_4.items(): # Buscar punto apoyo 4
            
            if buscando_apoyo>=5:
                print("break 493")
                break
            mina8=None
            mina8 = pyautogui.locateOnScreen(image_path112, confidence=0.9, grayscale=True)
            time.sleep(0.2)
            if mina8:
                contador=4
                print("Encontró punto de apoyo 4")
                encontrado=1
                center1 = pyautogui.center(mina8)
                del mina8
                pyautogui.click(center1)
                time.sleep(3.2)
            else:
                contador+=1
                print("NO Encontró punto de apoyo 4")
                buscando_apoyo+=1
                if(buscando_apoyo==2):
                    pyautogui.click(x=472,y=486) # Moverse para intentar buscar punto apoyo 4 abajo izq
                    time.sleep(2)
                if(buscando_apoyo==3):
                    pyautogui.click(x=900,y=275) # Moverse para intentar buscar punto apoyo 4 arriba derecha
                    time.sleep(2)
                    pyautogui.click(x=900,y=275) # Moverse para intentar buscar punto apoyo 4 arriba derecha
                    time.sleep(2)
    if(encontrado!=1):
        contador=0
        encontradas=0
        buscando_apoyo=0
        encontrado=0
        while contador<=3:
            if buscando_apoyo>=5:
                break
            pyautogui.moveTo(0, 0)
            time.sleep(0.3)
            for _, image_path113 in apoyo_p2_3.items(): # Buscar punto apoyo 3
                
                if buscando_apoyo>=5:
                    print("break 520")
                    break
                mina6=None
                mina6 = pyautogui.locateOnScreen(image_path113, confidence=0.9, grayscale=True)
                time.sleep(0.2)
                if mina6:
                    contador=4
                    encontrado=1
                    center1 = pyautogui.center(mina6)
                    del mina6
                    pyautogui.click(center1)
                    time.sleep(3.2)
                else:
                    contador+=1
                    buscando_apoyo+=1
                    if(buscando_apoyo==2):
                        pyautogui.click(x=472,y=486) # Moverse para intentar buscar punto apoyo 3 abajo izq
                        time.sleep(2)
                    if(buscando_apoyo==3):
                        pyautogui.click(x=900,y=275) # Moverse para intentar buscar punto apoyo 3 arriba derecha
                        time.sleep(2)
                        pyautogui.click(x=900,y=275) # Moverse para intentar buscar punto apoyo 3 arriba derecha
                        time.sleep(2)
        contador=0
        encontradas=0
        buscando_apoyo=0
        encontrado=0
        while contador<=3:
            if buscando_apoyo>=5:
                break
            pyautogui.moveTo(0, 0)
            time.sleep(0.3)
            for _, image_path114 in apoyo_p2_4.items(): # Buscar punto apoyo 4
                
                if buscando_apoyo>=5:
                    print("break 546")
                    break
                mina15=None
                mina15 = pyautogui.locateOnScreen(image_path114, confidence=0.9, grayscale=True)
                time.sleep(0.2)
                if mina15:
                    contador=4
                    encontrado=1
                    center1 = pyautogui.center(mina15)
                    del mina15
                    pyautogui.click(center1)
                    time.sleep(3.2)
                else:
                    contador+=1
                    buscando_apoyo+=1
                    if(buscando_apoyo==2):
                        pyautogui.click(x=472,y=486) # Moverse para intentar buscar punto apoyo 4 abajo izq
                        time.sleep(2)
                    if(buscando_apoyo==3):
                        pyautogui.click(x=900,y=275) # Moverse para intentar buscar punto apoyo 4 arriba derecha
                        time.sleep(2)
                        pyautogui.click(x=900,y=275) # Moverse para intentar buscar punto apoyo 4 arriba derecha
                        time.sleep(2)
    if(encontrado==1):
        contador=0
        encontradas=0
        while contador<=20 and encontradas<=4:
            if contador>=20 or encontradas>=4:
                print("break 571")
                break
            for _, image_path115 in img_p2_temporal.items(): # Buscar filón
                if contador>=20 or encontradas>=4:
                    print("break 571")
                    break
                mina9=None
                mina9 = pyautogui.locateOnScreen(image_path115, confidence=0.9, grayscale=True)
                time.sleep(0.2)
                if mina9:
                    contador+=1
                    center1 = pyautogui.center(mina9)
                    del mina9
                    pyautogui.rightClick(center1)
                    for _, image_path279 in minarboton_img.items(): # Buscar botón minar
                        locationminarboton_img5 = pyautogui.locateOnScreen(image_path279, confidence=0.9)
                        time.sleep(0.2)
                        if locationminarboton_img5:
                            encontradas+=1
                            center = pyautogui.center(locationminarboton_img5)
                            pyautogui.click(center)
                            time.sleep(6.2) # Tiempo que tarda en llegar y minar
                            
                else:
                    contador+=1
    contador=0
    encontradas=0
    buscando_apoyo=0
    encontrado=0
    while contador<=3:
        if buscando_apoyo>=5:
            break
        pyautogui.moveTo(0, 0)
        time.sleep(0.3)
        for _, image_path116 in apoyo_p2_5.items(): # Buscar punto apoyo 5
            
            if buscando_apoyo>=5:
                print("break 594")
                break
            mina16=None
            mina16 = pyautogui.locateOnScreen(image_path116, confidence=0.9, grayscale=True)
            time.sleep(0.2)
            if mina16:
                contador=4
                print("Encontró punto de apoyo 5")
                encontrado=1
                center1 = pyautogui.center(mina16)
                del mina16
                pyautogui.click(center1)
                time.sleep(3.2)
                
            else:
                contador+=1
                print("NO Encontró punto de apoyo 5")
                buscando_apoyo+=1
                if(buscando_apoyo==2):
                    pyautogui.click(x=472,y=486) # Moverse para intentar buscar punto apoyo 5 abajo izq
                    time.sleep(2)
                if(buscando_apoyo==3):
                    pyautogui.click(x=900,y=275) # Moverse para intentar buscar punto apoyo 5 arriba derecha
                    time.sleep(2)
                    pyautogui.click(x=900,y=275) # Moverse para intentar buscar punto apoyo 5 arriba derecha
                    time.sleep(2)
    if(encontrado!=1):
        contador=0
        encontradas=0
        buscando_apoyo=0
        encontrado=0
        while contador<=3:
            if buscando_apoyo>=5:
                break
            pyautogui.moveTo(0, 0)
            time.sleep(0.3)
            for _, image_path117 in apoyo_p2_4.items(): # Buscar punto apoyo 4
                
                if buscando_apoyo>=5:
                    print("break 621")
                    break
                mina17=None
                mina17 = pyautogui.locateOnScreen(image_path117, confidence=0.9, grayscale=True)
                time.sleep(0.2)
                if mina17:
                    contador=4
                    encontrado=1
                    center1 = pyautogui.center(mina17)
                    del mina17
                    pyautogui.click(center1)
                    time.sleep(3.2)
                else:
                    contador+=1
                    buscando_apoyo+=1
                    if(buscando_apoyo==2):
                        pyautogui.click(x=472,y=486) # Moverse para intentar buscar punto apoyo 4 abajo izq
                        time.sleep(2)
                    if(buscando_apoyo==3):
                        pyautogui.click(x=900,y=275) # Moverse para intentar buscar punto apoyo 4 arriba derecha
                        time.sleep(2)
                        pyautogui.click(x=900,y=275) # Moverse para intentar buscar punto apoyo 4 arriba derecha
                        time.sleep(2)
        contador=0
        encontradas=0
        buscando_apoyo=0
        encontrado=0
        while contador<=3:
            if buscando_apoyo>=5:
                break
            pyautogui.moveTo(0, 0)
            time.sleep(0.3)
            for _, image_path118 in apoyo_p2_5.items(): # Buscar punto apoyo 5
                
                if buscando_apoyo>=5:
                    print("break 647")
                    break
                mina18=None
                mina18 = pyautogui.locateOnScreen(image_path118, confidence=0.9, grayscale=True)
                time.sleep(0.2)
                if mina18:
                    contador=4
                    encontrado=1
                    center1 = pyautogui.center(mina18)
                    del mina18
                    pyautogui.click(center1)
                    time.sleep(3)
                else:
                    contador+=1
                    buscando_apoyo+=1
                    if(buscando_apoyo==2):
                        pyautogui.click(x=472,y=486) # Moverse para intentar buscar punto apoyo 5 abajo izq
                        time.sleep(2)
                    if(buscando_apoyo==3):
                        pyautogui.click(x=900,y=275) # Moverse para intentar buscar punto apoyo 5 arriba derecha
                        time.sleep(2)
                        pyautogui.click(x=900,y=275) # Moverse para intentar buscar punto apoyo 5 arriba derecha
                        time.sleep(2)
    if(encontrado==1):
        contador=0
        encontradas=0
        while contador<=15 and encontradas<=3:
            if contador>=15 or encontradas>=3:
                print("break 672")
                break
            for _, image_path119 in img_p2_temporal.items(): # Buscar filón
                if contador>=15 or encontradas>=3:
                    print("break 672")
                    break
                mina19=None
                mina19 = pyautogui.locateOnScreen(image_path119, confidence=0.9, grayscale=True)
                time.sleep(0.2)
                if mina19:
                    contador+=1
                    center1 = pyautogui.center(mina19)
                    del mina19
                    pyautogui.rightClick(center1)
                    for _, image_path280 in minarboton_img.items(): # Buscar botón minar
                        locationminarboton_img5 = pyautogui.locateOnScreen(image_path280, confidence=0.9)
                        time.sleep(0.2)
                        if locationminarboton_img5:
                            encontradas+=1
                            center = pyautogui.center(locationminarboton_img5)
                            pyautogui.click(center)
                            time.sleep(6.2) # Tiempo que tarda en llegar y minar
                            
                else:
                    contador+=1
    if(encontrado!=1):
        contador=0
        encontradas=0
        while contador<=15 and encontradas<=3:
            if contador>=15 or encontradas>=3:
                print("break 672")
                break
            for _, image_path119 in img_p2_temporal.items(): # Buscar filón
                if contador>=15 or encontradas>=3:
                    print("break 672")
                    break
                mina19=None
                mina19 = pyautogui.locateOnScreen(image_path119, confidence=0.9, grayscale=True)
                time.sleep(0.2)
                if mina19:
                    contador+=1
                    center1 = pyautogui.center(mina19)
                    del mina19
                    pyautogui.rightClick(center1)
                    for _, image_path280 in minarboton_img.items(): # Buscar botón minar
                        locationminarboton_img5 = pyautogui.locateOnScreen(image_path280, confidence=0.9)
                        time.sleep(0.2)
                        if locationminarboton_img5:
                            encontradas+=1
                            center = pyautogui.center(locationminarboton_img5)
                            pyautogui.click(center)
                            time.sleep(6.2) # Tiempo que tarda en llegar y minar
                            
                else:
                    contador+=1
    if(encontrado!=1):
        pyautogui.click(x=900,y=487) # Moverse de último recurso 5 abajo derecha
        time.sleep(2.2)
        contador=0
        encontradas=0
        while contador<=15 and encontradas<=3:
            if contador>=15 or encontradas>=3:
                print("break 672")
                break
            for _, image_path119 in img_p2_temporal.items(): # Buscar filón
                if contador>=15 or encontradas>=3:
                    print("break 672")
                    break
                mina19=None
                mina19 = pyautogui.locateOnScreen(image_path119, confidence=0.9, grayscale=True)
                time.sleep(0.2)
                if mina19:
                    contador+=1
                    center1 = pyautogui.center(mina19)
                    del mina19
                    pyautogui.rightClick(center1)
                    for _, image_path280 in minarboton_img.items(): # Buscar botón minar
                        locationminarboton_img5 = pyautogui.locateOnScreen(image_path280, confidence=0.9)
                        time.sleep(0.2)
                        if locationminarboton_img5:
                            encontradas+=1
                            center = pyautogui.center(locationminarboton_img5)
                            pyautogui.click(center)
                            time.sleep(5.5) # Tiempo que tarda en llegar y minar
                            
                else:
                    contador+=1
    contador=0
    encontradas=0
    buscando_apoyo=0
    encontrado=0
    while contador<=3:
        if buscando_apoyo>=5:
            break
        pyautogui.moveTo(0, 0)
        time.sleep(0.3)
        for _, image_path120 in apoyo_p2_5.items(): # Buscar punto apoyo 5
            if buscando_apoyo>=5:
                print("break 696")
                break
            mina20=None
            mina20 = pyautogui.locateOnScreen(image_path120, confidence=0.9, grayscale=True)
            time.sleep(0.2)
            if mina20:
                contador=4
                encontrado=1
                center1 = pyautogui.center(mina20)
                del mina20
                pyautogui.click(center1)
                time.sleep(3.2)
            else:
                contador+=1
                buscando_apoyo+=1
                if(buscando_apoyo==2):
                    pyautogui.click(x=472,y=486) # Moverse para intentar buscar punto apoyo 5 abajo izq
                    time.sleep(2)
                if(buscando_apoyo==3):
                    pyautogui.click(x=900,y=275) # Moverse para intentar buscar punto apoyo 5 arriba derecha
                    time.sleep(2)
                    pyautogui.click(x=900,y=275) # Moverse para intentar buscar punto apoyo 5 arriba derecha
                    time.sleep(2)
                if(buscando_apoyo==4):
                    pyautogui.click(x=814,y=444)
                    time.sleep(1.3)
                    pyautogui.click(x=558,y=317)
                    time.sleep(1.3)
                    pyautogui.click(x=386,y=529)
                    time.sleep(3)
                    pyautogui.click(x=386,y=529)
                    time.sleep(3)
                    pyautogui.click(x=386,y=529)
                    time.sleep(3)
                    pyautogui.click(x=386,y=529)
                    time.sleep(3)
                    pyautogui.click(x=386,y=529)
                    time.sleep(1)

    contador=0
    encontradas=0
    buscando_apoyo=0
    encontrado=0
    while contador<=3:
        if buscando_apoyo>=5:
            break
        pyautogui.moveTo(0, 0)
        time.sleep(0.3)
        for _, image_path121 in apoyo_p2_4.items(): # Buscar punto apoyo 4
            if buscando_apoyo>=5:
                print("break 723")
                break
            mina21=None
            mina21 = pyautogui.locateOnScreen(image_path121, confidence=0.9, grayscale=True)
            time.sleep(0.2)
            if mina21:
                contador=4
                encontrado=1
                center1 = pyautogui.center(mina21)
                del mina21
                pyautogui.click(center1)
                time.sleep(3.2)
            else:
                contador+=1
                buscando_apoyo+=1
                if(buscando_apoyo==2):
                    pyautogui.click(x=472,y=486) # Moverse para intentar buscar punto apoyo 4 abajo izq
                    time.sleep(2)
                if(buscando_apoyo==3):
                    pyautogui.click(x=900,y=275) # Moverse para intentar buscar punto apoyo 4 arriba derecha
                    time.sleep(1.7)
                    pyautogui.click(x=900,y=275) # Moverse para intentar buscar punto apoyo 4 arriba derecha
                    time.sleep(2)
                if(buscando_apoyo==4):
                    pyautogui.click(x=814,y=444)
                    time.sleep(1.3)
                    pyautogui.click(x=558,y=317)
                    time.sleep(1.3)
                    pyautogui.click(x=386,y=529)
                    time.sleep(3)
                    pyautogui.click(x=386,y=529)
                    time.sleep(3)
                    pyautogui.click(x=386,y=529)
                    time.sleep(3)
                    pyautogui.click(x=386,y=529)
                    time.sleep(3)

    contador=0
    encontradas=0
    buscando_apoyo=0
    encontrado=0
    while contador<=3:
        if buscando_apoyo>=5:
            break
        pyautogui.moveTo(0, 0)
        time.sleep(0.3)
        for _, image_path122 in apoyo_p2_3.items(): # Buscar punto apoyo 3
            if buscando_apoyo>=5:
                print("break 751")
                break
            mina22=None
            mina22 = pyautogui.locateOnScreen(image_path122, confidence=0.9, grayscale=True)
            time.sleep(0.2)
            if mina22:
                contador=4
                encontrado=1
                center1 = pyautogui.center(mina22)
                del mina22
                pyautogui.click(center1)
                time.sleep(3.2)
                
            else:
                contador+=1
                buscando_apoyo+=1
                if(buscando_apoyo==2):
                    pyautogui.click(x=472,y=486) # Moverse para intentar buscar punto apoyo 3 abajo izq
                    time.sleep(2)
                if(buscando_apoyo==3):
                    pyautogui.click(x=900,y=275) # Moverse para intentar buscar punto apoyo 3 arriba derecha
                    time.sleep(1.7)
                    pyautogui.click(x=900,y=275) # Moverse para intentar buscar punto apoyo 3 arriba derecha
                    time.sleep(2)
                if(buscando_apoyo==4):
                    pyautogui.click(x=814,y=444)
                    time.sleep(1.3)
                    pyautogui.click(x=558,y=317)
                    time.sleep(1.3)
                    pyautogui.click(x=386,y=529)
                    time.sleep(3)
                    pyautogui.click(x=386,y=529)
                    time.sleep(3)
                    pyautogui.click(x=386,y=529)
                    time.sleep(3)
    contador=0
    encontradas=0
    buscando_apoyo=0
    encontrado=0
    while contador<=3:
        if buscando_apoyo>=5:
            break
        pyautogui.moveTo(0, 0)
        time.sleep(0.3)
        for _, image_path123 in apoyo_p2_2.items(): # Buscar punto apoyo 2
            if buscando_apoyo>=5:
                print("break 778")
                break
            mina14=None
            mina14 = pyautogui.locateOnScreen(image_path123, confidence=0.9, grayscale=True)
            time.sleep(0.2)
            if mina14:
                contador=4
                encontrado=1
                center1 = pyautogui.center(mina14)
                del mina14
                pyautogui.click(center1)
                time.sleep(3.1)
                
            else:
                contador+=1
                buscando_apoyo+=1
                if(buscando_apoyo==2):
                    pyautogui.click(x=472,y=486) # Moverse para intentar buscar punto apoyo 2 abajo izq
                    time.sleep(2)
                if(buscando_apoyo==3):
                    pyautogui.click(x=900,y=275) # Moverse para intentar buscar punto apoyo 2 arriba derecha
                    time.sleep(1.7)
                    pyautogui.click(x=900,y=275) # Moverse para intentar buscar punto apoyo 2 arriba derecha
                    time.sleep(2)
                if(buscando_apoyo==4):
                    pyautogui.click(x=814,y=444)
                    time.sleep(1.3)
                    pyautogui.click(x=558,y=317)
                    time.sleep(1.3)
                    pyautogui.click(x=386,y=529)
                    time.sleep(3)
                    pyautogui.click(x=386,y=529)
                    time.sleep(3)
    contador=0
    encontradas=0
    buscando_apoyo=0
    encontrado=0
    while contador<=3:
        if buscando_apoyo>=5:
            break
        pyautogui.moveTo(0, 0)
        time.sleep(0.3)
        for _, image_path124 in apoyo_p2_1.items(): # Buscar punto apoyo 1
            if buscando_apoyo>=5:
                print("break 805")
                break
            mina23=None
            mina23 = pyautogui.locateOnScreen(image_path124, confidence=0.9, grayscale=True)
            time.sleep(0.2)
            if mina23:
                contador=4
                encontrado=1
                center1 = pyautogui.center(mina23)
                del mina23
                pyautogui.click(center1)
                pyautogui.click(center1)
            else:
                contador+=1
                buscando_apoyo+=1
                if(buscando_apoyo==2):
                    pyautogui.click(x=472,y=486) # Moverse para intentar buscar punto apoyo 1 abajo izq
                    time.sleep(1.9)
                if(buscando_apoyo==3):
                    pyautogui.click(x=900,y=275) # Moverse para intentar buscar punto apoyo 1 arriba derecha
                    time.sleep(1.7)
                    pyautogui.click(x=900,y=275) # Moverse para intentar buscar punto apoyo 1 arriba derecha
                    time.sleep(1.9)
                if(buscando_apoyo==4):
                    pyautogui.click(x=814,y=444)
                    time.sleep(1.3)

    if(encontrado!=1):
        print("Algo salió mal. No volvió al punto de inicio PUNTO DE APOYO 1")


    deslogeo()
    
    pass
#P3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
def action_for_p3(position): # El 3 pasa a ser el Zobal
    logeo(position)
    pyautogui.rightClick(939, 579)
    encontradas=0
    pyautogui.moveTo(0, 0)
    time.sleep(0.2)
    for _, image_path228Q in minarboton_img.items(): # Buscar botón minar
        if(encontradas==4):
            break
        locationminarboton_img5Q = pyautogui.locateOnScreen(image_path228Q, confidence=0.9)
        if locationminarboton_img5Q:
            encontradas+=1
            center = pyautogui.center(locationminarboton_img5Q)
            pyautogui.click(center)
            time.sleep(5.6) # Tiempo que tarda en llegar y minar
            pyautogui.rightClick(943, 193)
            pyautogui.moveTo(0, 0)
            time.sleep(0.2)
            for _, image_path228QR in minarboton_img.items(): # Buscar botón minar
                if(encontradas==4):
                    break
                locationminarboton_img5QR = pyautogui.locateOnScreen(image_path228QR, confidence=0.9)
                time.sleep(0.2)
                if locationminarboton_img5QR:
                    encontradas+=1
                    center = pyautogui.center(locationminarboton_img5QR)
                    pyautogui.click(center)
                    time.sleep(5.6) # Tiempo que tarda en llegar y minar
                    pyautogui.click(205, 283)
                else:
                    if(encontradas==3):
                        encontradas=4
                        break

    pyautogui.rightClick(1157, 385)
    pyautogui.moveTo(0, 0)
    encontradas=0
    time.sleep(0.2)
    for _, image_path228QQ in minarboton_img.items(): # Buscar botón minar
        if(encontradas==3):
            break
        locationminarboton_img5QQ = pyautogui.locateOnScreen(image_path228QQ, confidence=0.9)
        time.sleep(0.2)
        if locationminarboton_img5QQ:
            encontradas+=1
            center = pyautogui.center(locationminarboton_img5QQ)
            pyautogui.click(center)
            time.sleep(5.7) # Tiempo que tarda en llegar y minar
            pyautogui.click(205, 283)
        else:
            if(encontradas==2):
                encontradas=3
                break

    contador=0
    encontradas=0
    while contador<=16 and encontradas<=4:
        if contador>=16 or encontradas>=4:
            print("break 306")
            break
        pyautogui.moveTo(0, 0)
        time.sleep(0.3)
        for _, image_path12Q in img_p3_temporal.items(): # Buscar filón
            if contador>=16 or encontradas>=4:
                print("break 310")
                break
            minaQ=None
            minaQ = pyautogui.locateOnScreen(image_path12Q, confidence=0.9, region=abajo_region, grayscale=True)
            time.sleep(0.2)
            if minaQ:
                contador+=1
                center1 = pyautogui.center(minaQ)
                del minaQ
                pyautogui.rightClick(center1)
                pyautogui.moveTo(0, 0)
                time.sleep(0.3)
                for _, image_path228 in minarboton_img.items(): # Buscar botón minar
                    locationminarboton_img5 = pyautogui.locateOnScreen(image_path228, confidence=0.9)
                    time.sleep(0.2)
                    if locationminarboton_img5:
                        encontradas+=1
                        center = pyautogui.center(locationminarboton_img5)
                        pyautogui.click(center)
                        time.sleep(6.2) # Tiempo que tarda en llegar y minar
            else:
                contador+=1
    contador=0
    encontradas=0
    while contador<=16 and encontradas<=4:
        if contador>=16 or encontradas>=4:
            print("break 306")
            break
        pyautogui.moveTo(0, 0)
        time.sleep(0.3)
        for _, image_path12 in img_p3_temporal.items(): # Buscar filón
            if contador>=16 or encontradas>=4:
                print("break 310")
                break
            mina=None
            mina = pyautogui.locateOnScreen(image_path12, confidence=0.9, grayscale=True)
            time.sleep(0.2)
            if mina:
                contador+=1
                center1 = pyautogui.center(mina)
                del mina
                pyautogui.rightClick(center1)
                pyautogui.moveTo(0, 0)
                time.sleep(0.3)
                for _, image_path228 in minarboton_img.items(): # Buscar botón minar
                    locationminarboton_img5 = pyautogui.locateOnScreen(image_path228, confidence=0.9)
                    time.sleep(0.2)
                    if locationminarboton_img5:
                        encontradas+=1
                        center = pyautogui.center(locationminarboton_img5)
                        pyautogui.click(center)
                        time.sleep(6.2) # Tiempo que tarda en llegar y minar
            else:
                contador+=1
    contador=0
    encontradas=0
    buscando_apoyo=0
    while contador<=3:
        if buscando_apoyo>=5:
            break
        pyautogui.moveTo(0, 0)
        time.sleep(0.3)
        for _, image_path13 in apoyo_p3_1.items(): # Buscar punto apoyo 1
            if buscando_apoyo>=5:
                print("break 328")
                break
            mina2=None
            mina2 = pyautogui.locateOnScreen(image_path13, confidence=0.9, grayscale=True)
            time.sleep(0.2)
            if mina2:
                contador=4
                center1 = pyautogui.center(mina2)
                del mina2
                pyautogui.click(center1)
                time.sleep(3)
            else:
                contador+=1
                buscando_apoyo+=1
                if(buscando_apoyo==2):
                    pyautogui.click(x=900,y=487) # Moverse para intentar buscar punto apoyo 1 abajo izq
                    time.sleep(2)
                if(buscando_apoyo==3):
                    pyautogui.click(x=472,y=274) # Moverse para intentar buscar punto apoyo 1 arriba derecha
                    time.sleep(1.7)
                    pyautogui.click(x=472,y=274) # Moverse para intentar buscar punto apoyo 1 arriba derecha
                    time.sleep(2)
    encontradas=0
    buscando_apoyo=0
    contador=0
    while contador<=3:
        if buscando_apoyo>=5:
            break
        pyautogui.moveTo(0, 0)
        time.sleep(0.3)
        for _, image_path14 in apoyo_p3_2.items(): # Buscar punto apoyo 2
            if buscando_apoyo>=5:
                print("break 350")
                break
            mina25=None
            mina25 = pyautogui.locateOnScreen(image_path14, confidence=0.9, grayscale=True)
            time.sleep(0.2)
            if mina25:
                contador=4
                center1 = pyautogui.center(mina25)
                del mina25
                pyautogui.click(center1)
                time.sleep(3.7)
            else:
                contador+=1
                buscando_apoyo+=1
                if(buscando_apoyo==2):
                    pyautogui.click(x=900,y=487) # Moverse para intentar buscar punto apoyo 1 abajo izq
                    time.sleep(2)
                if(buscando_apoyo==3):
                    pyautogui.click(x=472,y=274) # Moverse para intentar buscar punto apoyo 1 arriba derecha
                    time.sleep(1.7)
                    pyautogui.click(x=472,y=274) # Moverse para intentar buscar punto apoyo 1 arriba derecha
                    time.sleep(2)
    contador=0
    encontradas=0
    while contador<=20 and encontradas<=5:
        if contador>=20 or encontradas>=5:
            print("break 373R")
            break
        for _, image_path15R in img_p3_temporal.items(): # Buscar filón
            if contador>=20 or encontradas>=5:
                print("break 373R")
                break
            mina4R=None
            mina4R = pyautogui.locateOnScreen(image_path15R, confidence=0.9, region=abajo_region, grayscale=True)
            time.sleep(0.2)
            if mina4R:
                contador+=1
                print("Antes de buscar apoyo 3 del break 397 ENTRA IF DE MINA4R")
                center1 = pyautogui.center(mina4R)
                del mina4R
                pyautogui.rightClick(center1)
                for _, image_path277 in minarboton_img.items(): # Buscar botón minar
                    locationminarboton_img5 = pyautogui.locateOnScreen(image_path277, confidence=0.9)
                    time.sleep(0.2)
                    if locationminarboton_img5:
                        encontradas+=1
                        center = pyautogui.center(locationminarboton_img5)
                        pyautogui.click(center)
                        time.sleep(6.2) # Tiempo que tarda en llegar y minar
            else:
                contador+=1
                print("Antes de buscar apoyo 3 del break 397 ELSEEEE R")
    contador=0
    encontradas=0
    while contador<=20 and encontradas<=5:
        if contador>=20 or encontradas>=5:
            print("break 373")
            break
        for _, image_path15 in img_p3_temporal.items(): # Buscar filón
            if contador>=20 or encontradas>=5:
                print("break 373")
                break
            mina4=None
            mina4 = pyautogui.locateOnScreen(image_path15, confidence=0.9, grayscale=True)
            time.sleep(0.2)
            if mina4:
                contador+=1
                print("Antes de buscar apoyo 3 del break 397 ENTRA IF DE MINA4")
                center1 = pyautogui.center(mina4)
                del mina4
                pyautogui.rightClick(center1)
                for _, image_path277 in minarboton_img.items(): # Buscar botón minar
                    locationminarboton_img5 = pyautogui.locateOnScreen(image_path277, confidence=0.9)
                    time.sleep(0.2)
                    if locationminarboton_img5:
                        encontradas+=1
                        center = pyautogui.center(locationminarboton_img5)
                        pyautogui.click(center)
                        time.sleep(6.2) # Tiempo que tarda en llegar y minar
            else:
                contador+=1
                print("Antes de buscar apoyo 3 del break 397 ELSEEEE")

    print("Antes de buscar apoyo 3 del break 397")
    encontradas=0
    buscando_apoyo=0
    encontrado=0
    contador=0
    while contador<=3:
        if buscando_apoyo>=5:
            break
        pyautogui.moveTo(0, 0)
        time.sleep(0.3)
        for _, image_path16 in apoyo_p3_3.items(): # Buscar punto apoyo 3
            if buscando_apoyo>=5:
                print("break 397")
                break
            mina111=None
            mina111 = pyautogui.locateOnScreen(image_path16, confidence=0.9, grayscale=True)
            time.sleep(0.2)
            if mina111:
                contador=4
                print("Encontró punto de apoyo 3")
                center1 = pyautogui.center(mina111)
                del mina111
                pyautogui.click(center1)
                time.sleep(3)
                encontrado=1
            else:
                contador+=1
                buscando_apoyo+=1
                if(buscando_apoyo==2):
                    pyautogui.click(x=900,y=487) # Moverse para intentar buscar punto apoyo 1 abajo izq
                    time.sleep(2)
                if(buscando_apoyo==3):
                    pyautogui.click(x=472,y=274) # Moverse para intentar buscar punto apoyo 1 arriba derecha
                    time.sleep(1.7)
                    pyautogui.click(x=472,y=274) # Moverse para intentar buscar punto apoyo 1 arriba derecha
                    time.sleep(2)

    encontradas = 0
    buscando_apoyo = 0

    if encontrado != 1:
        contador = 0
        while contador <= 3:
            if buscando_apoyo >= 5:
                break
            pyautogui.moveTo(0, 0)
            time.sleep(0.3)
            mina127X = None
            for _, image_path17 in apoyo_p3_2.items():  # Buscar punto apoyo 2
                if buscando_apoyo >= 5:
                    print("break 422")
                    break
                mina127X = pyautogui.locateOnScreen(image_path17, confidence=0.9, grayscale=True)
                time.sleep(0.2)
                if mina127X:
                    contador = 4
                    print("Encontró punto de apoyo 2")
                    center1 = pyautogui.center(mina127X)
                    pyautogui.click(center1)
                    time.sleep(3.2)
                else:
                    contador += 1
                    buscando_apoyo += 1
                    if buscando_apoyo == 2:
                        pyautogui.click(x=900, y=487)  # Moverse para intentar buscar punto apoyo 1 abajo izq
                        time.sleep(2)
                    if buscando_apoyo == 3:
                        pyautogui.click(x=472, y=274)  # Moverse para intentar buscar punto apoyo 1 arriba derecha
                        time.sleep(1.7)
                        pyautogui.click(x=472, y=274)  # Moverse para intentar buscar punto apoyo 1 arriba derecha
                        time.sleep(2)

        contador=0
        encontradas=0
        buscando_apoyo=0
        while contador<=3:
            if buscando_apoyo>=5:
                break
            pyautogui.moveTo(0, 0)
            time.sleep(0.3)
            for _, image_path18 in apoyo_p3_3.items(): # Buscar punto apoyo 3
                if buscando_apoyo>=5:
                    print("break 445")
                    break
                mina13=None
                mina13 = pyautogui.locateOnScreen(image_path18, confidence=0.9, grayscale=True)
                time.sleep(0.2)
                if mina13:
                    contador=4
                    encontrado=1
                    center1 = pyautogui.center(mina13)
                    del mina13
                    pyautogui.click(center1)
                    time.sleep(3.2)
                else:
                    contador+=1
                    buscando_apoyo+=1
                    if(buscando_apoyo==2):
                        pyautogui.click(x=900,y=487) # Moverse para intentar buscar punto apoyo 1 abajo izq
                        time.sleep(2)
                    if(buscando_apoyo==3):
                        pyautogui.click(x=472,y=274) # Moverse para intentar buscar punto apoyo 1 arriba derecha
                        time.sleep(1.7)
                        pyautogui.click(x=472,y=274) # Moverse para intentar buscar punto apoyo 1 arriba derecha
                        time.sleep(2)
    contador=0
    encontradas=0
    while contador<=20 and encontradas<=5:
        if contador>=20 or encontradas>=5:
            print("break 373")
            break
        for _, image_path15W in img_p3_temporal.items(): # Buscar filón
            if contador>=20 or encontradas>=5:
                print("break 373")
                break
            mina4W=None
            mina4W = pyautogui.locateOnScreen(image_path15W, confidence=0.9, grayscale=True)
            time.sleep(0.2)
            if mina4W:
                contador+=1
                print("Antes de buscar apoyo 3 del break 397 ENTRA IF DE MINA4")
                center1 = pyautogui.center(mina4W)
                del mina4W
                pyautogui.rightClick(center1)
                for _, image_path277 in minarboton_img.items(): # Buscar botón minar
                    locationminarboton_img5 = pyautogui.locateOnScreen(image_path277, confidence=0.9)
                    time.sleep(0.2)
                    if locationminarboton_img5:
                        encontradas+=1
                        center = pyautogui.center(locationminarboton_img5)
                        pyautogui.click(center)
                        time.sleep(6.2) # Tiempo que tarda en llegar y minar
            else:
                contador+=1
                print("Antes de buscar apoyo 3 del break 397 ELSEEEE")

    encontradas=0
    buscando_apoyo=0
    contador=0
    while contador<=3:
        if buscando_apoyo>=5:
            break
        pyautogui.moveTo(0, 0)
        time.sleep(0.3)
        for _, image_path17W in apoyo_p3_2.items(): # Buscar punto apoyo 2
            if buscando_apoyo>=5:
                print("break 422")
                break
            mina12W=None
            mina12W = pyautogui.locateOnScreen(image_path17W, confidence=0.9, grayscale=True)
            time.sleep(0.2)
            if mina12W:
                contador=4
                print("Encontró punto de apoyo 2")
                center1 = pyautogui.center(mina12W)
                del mina12W
                pyautogui.click(center1)
                time.sleep(3.2)
            else:
                contador+=1
                buscando_apoyo+=1
                if(buscando_apoyo==2):
                    pyautogui.click(x=900,y=487) # Moverse para intentar buscar punto apoyo 1 abajo izq
                    time.sleep(2)
                if(buscando_apoyo==3):
                    pyautogui.click(x=472,y=274) # Moverse para intentar buscar punto apoyo 1 arriba derecha
                    time.sleep(1.7)
                    pyautogui.click(x=472,y=274) # Moverse para intentar buscar punto apoyo 1 arriba derecha
                    time.sleep(2)

    encontrado=0
    contador=0
    encontradas=0
    buscando_apoyo=0
    while contador<=3:
        if buscando_apoyo>=5:
            break
        pyautogui.moveTo(0, 0)
        time.sleep(0.3)
        for _, image_path18 in apoyo_p3_3.items(): # Buscar punto apoyo 3
            if buscando_apoyo>=5:
                print("break 445")
                break
            mina13=None
            mina13 = pyautogui.locateOnScreen(image_path18, confidence=0.9, grayscale=True)
            time.sleep(0.2)
            if mina13:
                contador=4
                encontrado=1
                center1 = pyautogui.center(mina13)
                del mina13
                pyautogui.click(center1)
                time.sleep(3.2)
            else:
                contador+=1
                buscando_apoyo+=1
                if(buscando_apoyo==2):
                    pyautogui.click(x=900,y=487) # Moverse para intentar buscar punto apoyo 1 abajo izq
                    time.sleep(2)
                if(buscando_apoyo==3):
                    pyautogui.click(x=472,y=274) # Moverse para intentar buscar punto apoyo 1 arriba derecha
                    time.sleep(1.7)
                    pyautogui.click(x=472,y=274) # Moverse para intentar buscar punto apoyo 1 arriba derecha
                    time.sleep(2)
    if(encontrado==1):
        pyautogui.rightClick(386, 208)
        pyautogui.moveTo(0, 0)
        time.sleep(0.2)
        for _, image_path228QB in minarboton_img.items(): # Buscar botón minar
            locationminarboton_img5QB=None
            locationminarboton_img5QB = pyautogui.locateOnScreen(image_path228QB, confidence=0.9)
            if locationminarboton_img5QB:
                center = pyautogui.center(locationminarboton_img5QB)
                del locationminarboton_img5QB
                pyautogui.click(center)
                time.sleep(5.4) # Tiempo que tarda en llegar y minar
                pyautogui.click(942, 516)
                pyautogui.moveTo(0, 0)
                time.sleep(2.1)
    contador=0
    buscando_apoyo=0
    while contador<=3:
        if buscando_apoyo>=5:
            break
        pyautogui.moveTo(0, 0)
        time.sleep(0.3)
        for _, image_path123 in apoyo_p3_2.items(): # Buscar punto apoyo 2
            if buscando_apoyo>=5:
                print("break 778")
                break
            mina14=None
            mina14 = pyautogui.locateOnScreen(image_path123, confidence=0.9, grayscale=True)
            time.sleep(0.2)
            if mina14:
                contador=4
                center1 = pyautogui.center(mina14)
                del mina14
                pyautogui.click(center1)
                time.sleep(3.2)
            else:
                contador+=1
                buscando_apoyo+=1
                if(buscando_apoyo==2):
                    pyautogui.click(x=900,y=487) # Moverse para intentar buscar punto apoyo 1 abajo izq
                    time.sleep(2)
                if(buscando_apoyo==3):
                    pyautogui.click(x=472,y=274) # Moverse para intentar buscar punto apoyo 1 arriba derecha
                    time.sleep(1.7)
                    pyautogui.click(x=472,y=274) # Moverse para intentar buscar punto apoyo 1 arriba derecha
                    time.sleep(2)
                if(buscando_apoyo==4):
                    pyautogui.click(x=814,y=444)
                    time.sleep(1.4)
    contador=0
    buscando_apoyo=0
    encontrado=0
    while contador<=3:
        if buscando_apoyo>=5:
            break
        pyautogui.moveTo(0, 0)
        time.sleep(0.3)
        for _, image_path124 in apoyo_p3_1.items(): # Buscar punto apoyo 1
            
            if buscando_apoyo>=5:
                print("break 805")
                break
            mina23=None
            mina23 = pyautogui.locateOnScreen(image_path124, confidence=0.9, grayscale=True)
            if mina23:
                contador=4
                encontrado=1
                center1 = pyautogui.center(mina23)
                del mina23
                pyautogui.click(center1)
            else:
                contador+=1
                buscando_apoyo+=1
                if(buscando_apoyo==2):
                    pyautogui.click(x=900,y=487) # Moverse para intentar buscar punto apoyo 1 abajo izq
                    time.sleep(2)
                if(buscando_apoyo==3):
                    pyautogui.click(x=472,y=274) # Moverse para intentar buscar punto apoyo 1 arriba derecha
                    time.sleep(1.7)
                    pyautogui.click(x=472,y=274) # Moverse para intentar buscar punto apoyo 1 arriba derecha
                    time.sleep(2)
                if(buscando_apoyo==4):
                    pyautogui.click(x=814,y=444)
                    time.sleep(1.4)

    if(encontrado!=1):
        print("Algo salió mal. No volvió al punto de inicio PUNTO DE APOYO 1")
    deslogeo()
    pass
#P444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
def action_for_p4(position): # Ocra BRAKMAR
    logeo(position)
    pyautogui.rightClick(1201, 189)
    pyautogui.moveTo(0, 0)
    encontradas=0
    time.sleep(0.2)
    for _, image_path228QSS in minarboton_img.items(): # Buscar botón minar
        locationminarboton_img5QSS=None
        locationminarboton_img5QSS = pyautogui.locateOnScreen(image_path228QSS, confidence=0.9)
        if locationminarboton_img5QSS:
            encontradas+=1
            center = pyautogui.center(locationminarboton_img5QSS)
            del locationminarboton_img5QSS
            pyautogui.click(center)
            time.sleep(5.8) # Tiempo que tarda en llegar y minar
            pyautogui.click(209, 577)
            time.sleep(3.2)

    pyautogui.rightClick(552, 556)
    encontradas=0
    pyautogui.moveTo(0, 0)
    time.sleep(0.2)
    for _, image_path228Q in minarboton_img.items(): # Buscar botón minar
        locationminarboton_img5Q=None
        locationminarboton_img5Q = pyautogui.locateOnScreen(image_path228Q, confidence=0.9)
        if locationminarboton_img5Q:
            encontradas+=1
            center = pyautogui.center(locationminarboton_img5Q)
            del locationminarboton_img5Q
            pyautogui.click(center)
            time.sleep(5) # Tiempo que tarda en llegar y minar
            pyautogui.rightClick(1024, 238)
            pyautogui.moveTo(0, 0)
            time.sleep(0.2)
            for _, image_path228QR in minarboton_img.items(): # Buscar botón minar
                locationminarboton_img5QR=None
                locationminarboton_img5QR = pyautogui.locateOnScreen(image_path228QR, confidence=0.9)
                time.sleep(0.2)
                if locationminarboton_img5QR:
                    encontradas+=1
                    center = pyautogui.center(locationminarboton_img5QR)
                    del locationminarboton_img5QR
                    pyautogui.click(center)
                    time.sleep(6) # Tiempo que tarda en llegar y minar
                    pyautogui.click(205, 283)
                    time.sleep(2.5)

    pyautogui.rightClick(942, 407)
    pyautogui.moveTo(0, 0)
    encontradas=0
    time.sleep(0.2)
    for _, image_path228QQ in minarboton_img.items(): # Buscar botón minar
        locationminarboton_img5QQ=None
        locationminarboton_img5QQ = pyautogui.locateOnScreen(image_path228QQ, confidence=0.9)
        time.sleep(0.2)
        if locationminarboton_img5QQ:
            encontradas+=1
            center = pyautogui.center(locationminarboton_img5QQ)
            del locationminarboton_img5QQ
            pyautogui.click(center)
            time.sleep(4.3) # Tiempo que tarda en llegar y minar


    contador=0
    encontradas=0
    while contador<=16 and encontradas<=4:
        if contador>=16 or encontradas>=4:
            print("break 306")
            break
        pyautogui.moveTo(0, 0)
        time.sleep(0.3)
        for _, image_path12Q in img_p4_temporal.items(): # Buscar filón
            if contador>=16 or encontradas>=4:
                print("break 310")
                break
            minaQ=None
            minaQ = pyautogui.locateOnScreen(image_path12Q, confidence=0.9, region=abajo_region, grayscale=True)
            time.sleep(0.2)
            if minaQ:
                contador+=1
                center1 = pyautogui.center(minaQ)
                del minaQ
                pyautogui.rightClick(center1)
                pyautogui.moveTo(0, 0)
                time.sleep(0.3)
                for _, image_path228 in minarboton_img.items(): # Buscar botón minar
                    locationminarboton_img5 = pyautogui.locateOnScreen(image_path228, confidence=0.9)
                    time.sleep(0.2)
                    if locationminarboton_img5:
                        encontradas+=1
                        center = pyautogui.center(locationminarboton_img5)
                        pyautogui.click(center)
                        time.sleep(6.2) # Tiempo que tarda en llegar y minar
            else:
                contador+=1
    contador=0
    encontradas=0
    while contador<=16 and encontradas<=4:
        if contador>=16 or encontradas>=4:
            print("break 306")
            break
        pyautogui.moveTo(0, 0)
        time.sleep(0.3)
        for _, image_path12 in img_p4_temporal.items(): # Buscar filón
            if contador>=16 or encontradas>=4:
                print("break 310")
                break
            mina=None
            mina = pyautogui.locateOnScreen(image_path12, confidence=0.9, grayscale=True)
            time.sleep(0.2)
            if mina:
                contador+=1
                center1 = pyautogui.center(mina)
                del mina
                pyautogui.rightClick(center1)
                pyautogui.moveTo(0, 0)
                time.sleep(0.3)
                for _, image_path228 in minarboton_img.items(): # Buscar botón minar
                    locationminarboton_img5 = pyautogui.locateOnScreen(image_path228, confidence=0.9)
                    time.sleep(0.2)
                    if locationminarboton_img5:
                        encontradas+=1
                        center = pyautogui.center(locationminarboton_img5)
                        pyautogui.click(center)
                        time.sleep(6.2) # Tiempo que tarda en llegar y minar
            else:
                contador+=1
    contador=0
    encontradas=0
    buscando_apoyo=0
    while contador<=3:
        if buscando_apoyo>=5:
            break
        pyautogui.moveTo(0, 0)
        time.sleep(0.3)
        for _, image_path13 in apoyo_p4_1.items(): # Buscar punto apoyo 1
            if buscando_apoyo>=5:
                print("break 328")
                break
            mina2=None
            mina2 = pyautogui.locateOnScreen(image_path13, confidence=0.9, grayscale=True)
            time.sleep(0.2)
            if mina2:
                contador=4
                center1 = pyautogui.center(mina2)
                del mina2
                pyautogui.click(center1)
                time.sleep(3)
            else:
                contador+=1
                buscando_apoyo+=1
    encontradas=0
    buscando_apoyo=0
    contador=0
    while contador<=3:
        if buscando_apoyo>=5:
            break
        pyautogui.moveTo(0, 0)
        time.sleep(0.3)
        for _, image_path14 in apoyo_p4_2.items(): # Buscar punto apoyo 2
            if buscando_apoyo>=5:
                print("break 350")
                break
            mina25=None
            mina25 = pyautogui.locateOnScreen(image_path14, confidence=0.9, grayscale=True)
            time.sleep(0.2)
            if mina25:
                contador=4
                center1 = pyautogui.center(mina25)
                del mina25
                pyautogui.click(center1)
                time.sleep(3.7)
            else:
                contador+=1
                buscando_apoyo+=1
    contador=0
    encontradas=0
    while contador<=20 and encontradas<=5:
        if contador>=20 or encontradas>=5:
            print("break 373")
            break
        for _, image_path15 in img_p4_temporal.items(): # Buscar filón
            if contador>=20 or encontradas>=5:
                print("break 373")
                break
            mina4c1=None
            mina4c1 = pyautogui.locateOnScreen(image_path15, confidence=0.9, grayscale=True)
            if mina4c1:
                contador+=1
                print("Antes de buscar apoyo 3 del break 397 ENTRA IF DE MINA4")
                center1 = pyautogui.center(mina4c1)
                del mina4c1
                pyautogui.rightClick(center1)
                for _, image_path277 in minarboton_img.items(): # Buscar botón minar
                    locationminarboton_img5 = pyautogui.locateOnScreen(image_path277, confidence=0.9)
                    if locationminarboton_img5:
                        encontradas+=1
                        center = pyautogui.center(locationminarboton_img5)
                        pyautogui.click(center)
                        time.sleep(6.2) # Tiempo que tarda en llegar y minar
            else:
                contador+=1
                print("Antes de buscar apoyo 3 del break 397 ELSEEEE")

    print("Antes de buscar apoyo 3 del break 397")
    buscando_apoyo=0
    encontrado=0
    contador=0
    while contador<=3:
        if buscando_apoyo>=5:
            break
        if encontrado==1:
            break
        pyautogui.moveTo(0, 0)
        time.sleep(0.3)
        for _, image_path16 in apoyo_p4_3.items(): # Buscar punto apoyo 3
            if buscando_apoyo>=5 or encontrado==1:
                print("break 397")
                break
            mina111=None
            mina111 = pyautogui.locateOnScreen(image_path16, confidence=0.9, grayscale=True)
            time.sleep(0.2)
            if mina111:
                contador=4
                print("Encontró punto de apoyo 3")
                center1 = pyautogui.center(mina111)
                del mina111
                pyautogui.click(center1)
                time.sleep(3)
                encontrado=1
                pyautogui.rightClick(x=856,y=278)
                for _, image_path277c in minarboton_img.items(): # Buscar botón minar
                    locationminarboton_img5c = pyautogui.locateOnScreen(image_path277c, confidence=0.9)
                    time.sleep(0.2)
                    if locationminarboton_img5c:
                        encontradas+=1
                        center = pyautogui.center(locationminarboton_img5c)
                        pyautogui.click(center)
                        time.sleep(4.9) # Tiempo que tarda en llegar y minar
                        pyautogui.rightClick(x=557,y=454)

            else:
                contador+=1
                buscando_apoyo+=1

    contador=0
    encontradas=0
    while contador<=20 and encontradas<=5:
        if contador>=20 or encontradas>=5:
            print("break 373")
            break
        for _, image_path15D in img_p4_temporal.items(): # Buscar filón
            if contador>=20 or encontradas>=5:
                print("break 373")
                break
            mina4D=None
            mina4D = pyautogui.locateOnScreen(image_path15D, confidence=0.9, grayscale=True)
            time.sleep(0.2)
            if mina4D:
                contador+=1
                print("Antes de buscar apoyo 3 del break 397 ENTRA IF DE MINA4D")
                center1 = pyautogui.center(mina4D)
                del mina4D
                pyautogui.rightClick(center1)
                for _, image_path277 in minarboton_img.items(): # Buscar botón minar
                    locationminarboton_img5 = pyautogui.locateOnScreen(image_path277, confidence=0.9)
                    time.sleep(0.2)
                    if locationminarboton_img5:
                        encontradas+=1
                        center = pyautogui.center(locationminarboton_img5)
                        pyautogui.click(center)
                        time.sleep(6.2) # Tiempo que tarda en llegar y minar
            else:
                contador+=1
                print("Antes de buscar apoyo 3 del break 397 ELSEEEE")
    print("Antes de buscar apoyo 3 del break 397")
    encontradas=0
    buscando_apoyo=0
    encontrado=0
    contador=0
    while contador<=3:
        if buscando_apoyo>=5:
            break
        if encontrado==1:
            break
        pyautogui.moveTo(0, 0)
        time.sleep(0.3)
        for _, image_path16D in apoyo_p4_3.items(): # Buscar punto apoyo 3
            if buscando_apoyo>=5 or encontrado==1:
                print("break 397")
                break
            mina111D=None
            mina111D = pyautogui.locateOnScreen(image_path16D, confidence=0.9, grayscale=True)
            time.sleep(0.2)
            if mina111D:
                contador=4
                print("Encontró punto de apoyo 3")
                center1 = pyautogui.center(mina111D)
                del mina111D
                pyautogui.click(center1)
                time.sleep(3)
                encontrado=1
                pyautogui.rightClick(x=856,y=278)
                for _, image_path277c in minarboton_img.items(): # Buscar botón minar
                    locationminarboton_img5c = pyautogui.locateOnScreen(image_path277c, confidence=0.9)
                    time.sleep(0.2)
                    if locationminarboton_img5c:
                        encontradas+=1
                        center = pyautogui.center(locationminarboton_img5c)
                        pyautogui.click(center)
                        time.sleep(4.9) # Tiempo que tarda en llegar y minar
                        pyautogui.rightClick(x=557,y=454)
            else:
                contador+=1
                buscando_apoyo+=1

    encontradas=0
    buscando_apoyo=0
    if(encontrado!=1):
        contador=0
        while contador<=3:
            if buscando_apoyo>=5:
                break
            pyautogui.moveTo(0, 0)
            time.sleep(0.3)
            for _, image_path17 in apoyo_p4_2.items(): # Buscar punto apoyo 2
                if buscando_apoyo>=5:
                    print("break 422")
                    break
                mina12=None
                mina12 = pyautogui.locateOnScreen(image_path17, confidence=0.9, grayscale=True)
                time.sleep(0.2)
                if mina12:
                    contador=4
                    print("Encontró punto de apoyo 2")
                    center1 = pyautogui.center(mina12)
                    del mina12
                    pyautogui.click(center1)
                    time.sleep(3.2)
                else:
                    contador+=1
                    buscando_apoyo+=1
        contador=0
        encontradas=0
        buscando_apoyo=0
        encontrado==0
        while contador<=3:
            if buscando_apoyo>=5 or encontrado==1:
                break
            pyautogui.moveTo(0, 0)
            time.sleep(0.3)
            for _, image_path18 in apoyo_p4_3.items(): # Buscar punto apoyo 3
                if buscando_apoyo>=5 or encontrado==1:
                    print("break 445")
                    break
                mina13=None
                mina13 = pyautogui.locateOnScreen(image_path18, confidence=0.9, grayscale=True)
                time.sleep(0.2)
                if mina13:
                    contador=4
                    encontrado=1
                    center1 = pyautogui.center(mina13)
                    del mina13
                    pyautogui.click(center1)
                    time.sleep(3.2)
                    pyautogui.rightClick(x=856,y=278)
                    for _, image_path277c in minarboton_img.items(): # Buscar botón minar
                        locationminarboton_img5c = pyautogui.locateOnScreen(image_path277c, confidence=0.9)
                        time.sleep(0.2)
                        if locationminarboton_img5c:
                            encontradas+=1
                            center = pyautogui.center(locationminarboton_img5c)
                            pyautogui.click(center)
                            time.sleep(4.9) # Tiempo que tarda en llegar y minar
                            pyautogui.rightClick(x=557,y=454)
                else:
                    contador+=1
                    buscando_apoyo+=1
    contador=0
    encontradas=0
    buscando_apoyo=0
    encontrado=0
    while contador<=3:
        if buscando_apoyo>=5 or encontrado==1:
            break
        pyautogui.moveTo(0, 0)
        time.sleep(0.3)
        for _, image_path123 in apoyo_p4_2.items(): # Buscar punto apoyo 2
            if buscando_apoyo>=5 or encontrado==1:
                print("break 778")
                break
            mina14=None
            mina14 = pyautogui.locateOnScreen(image_path123, confidence=0.9, grayscale=True)
            time.sleep(0.2)
            if mina14:
                contador=4
                encontrado=1
                center1 = pyautogui.center(mina14)
                del mina14
                pyautogui.click(center1)
                time.sleep(2.8)
                
            else:
                contador+=1
                buscando_apoyo+=1
    contador=0
    encontradas=0
    buscando_apoyo=0
    encontrado=0
    while contador<=3:
        if buscando_apoyo>=5 or encontrado==1:
            break
        pyautogui.moveTo(0, 0)
        time.sleep(0.3)
        for _, image_path124 in apoyo_p4_1.items(): # Buscar punto apoyo 1
            
            if buscando_apoyo>=5 or encontrado==1:
                print("break 805")
                break
            mina23=None
            mina23 = pyautogui.locateOnScreen(image_path124, confidence=0.9, grayscale=True)
            time.sleep(0.2)
            if mina23:
                contador=4
                encontrado=1
                center1 = pyautogui.center(mina23)
                del mina23
                pyautogui.click(center1)
                time.sleep(0.3)
                
            else:
                contador+=1
                buscando_apoyo+=1

    if(encontrado!=1):
        print("Algo salió mal. No volvió al punto de inicio PUNTO DE APOYO 1")
    deslogeo()
    pass
#P55555555555555555555555555555555555555555555555555555555555555555555555555555555555555
def action_for_p5(position): # Osamoda
    logeo(position)
    pyautogui.rightClick(596, 588)
    encontradas=0
    pyautogui.moveTo(0, 0)
    time.sleep(0.2)
    image_path228Q=None
    for _, image_path228Q in minarboton_img.items(): # Buscar botón minar
        locationminarboton_img5Q=None
        locationminarboton_img5Q = pyautogui.locateOnScreen(image_path228Q, confidence=0.9)
        if locationminarboton_img5Q:
            encontradas+=1
            center = pyautogui.center(locationminarboton_img5Q)
            del locationminarboton_img5Q
            pyautogui.click(center)
            time.sleep(4.9) # Tiempo que tarda en llegar y minar
            pyautogui.rightClick(1024, 238)
            pyautogui.moveTo(0, 0)
            time.sleep(0.2)
            image_path228QR=None
            for _, image_path228QR in minarboton_img.items(): # Buscar botón minar
                locationminarboton_img5QR=None
                locationminarboton_img5QR = pyautogui.locateOnScreen(image_path228QR, confidence=0.9)
                time.sleep(0.2)
                if locationminarboton_img5QR:
                    encontradas+=1
                    center = pyautogui.center(locationminarboton_img5QR)
                    del locationminarboton_img5QR
                    pyautogui.click(center)
                    time.sleep(6.5) # Tiempo que tarda en llegar y minar
                    pyautogui.click(205, 283)

    pyautogui.rightClick(1069, 177)
    pyautogui.moveTo(0, 0)
    encontradas=0
    time.sleep(0.2)
    for _, image_path228QQ in minarboton_img.items(): # Buscar botón minar
        locationminarboton_img5QQ=None
        locationminarboton_img5QQ = pyautogui.locateOnScreen(image_path228QQ, confidence=0.9)
        time.sleep(0.2)
        if locationminarboton_img5QQ:
            encontradas+=1
            center = pyautogui.center(locationminarboton_img5QQ)
            del locationminarboton_img5QQ
            pyautogui.click(center)
            time.sleep(4.3) # Tiempo que tarda en llegar y minar

    contador=0
    encontradas=0
    while contador<=20 and encontradas<=5:
        if contador>=20 or encontradas>=5:
            print("break 306")
            break
        for _, image_path12Q in img_p5_temporal.items(): # Buscar filón
            if contador>=20 or encontradas>=5:
                print("break 310")
                break
            minaQ=None
            minaQ = pyautogui.locateOnScreen(image_path12Q, confidence=0.9, region=abajo_region, grayscale=True)
            time.sleep(0.2)
            if minaQ:
                contador+=1
                center1 = pyautogui.center(minaQ)
                del minaQ
                pyautogui.rightClick(center1)
                for _, image_path228Q in minarboton_img.items(): # Buscar botón minar
                    locationminarboton_img5 = pyautogui.locateOnScreen(image_path228Q, confidence=0.9)
                    time.sleep(0.2)
                    if locationminarboton_img5:
                        encontradas+=1
                        center = pyautogui.center(locationminarboton_img5)
                        pyautogui.click(center)
                        time.sleep(6.2) # Tiempo que tarda en llegar y minar
            else:
                contador+=1
    contador=0
    encontradas=0
    while contador<=20 and encontradas<=5:
        if contador>=20 or encontradas>=5:
            print("break 306")
            break
        for _, image_path12 in img_p5_temporal.items(): # Buscar filón
            if contador>=20 or encontradas>=5:
                print("break 310")
                break
            mina=None
            mina = pyautogui.locateOnScreen(image_path12, confidence=0.9, grayscale=True)
            time.sleep(0.2)
            if mina:
                contador+=1
                center1 = pyautogui.center(mina)
                del mina
                pyautogui.rightClick(center1)
                for _, image_path228 in minarboton_img.items(): # Buscar botón minar
                    locationminarboton_img5 = pyautogui.locateOnScreen(image_path228, confidence=0.9)
                    time.sleep(0.2)
                    if locationminarboton_img5:
                        encontradas+=1
                        center = pyautogui.center(locationminarboton_img5)
                        pyautogui.click(center)
                        time.sleep(6.2) # Tiempo que tarda en llegar y minar
            else:
                contador+=1
    contador=0
    encontradas=0
    buscando_apoyo=0
    while contador<=3:
        if buscando_apoyo>=5:
            break
        pyautogui.moveTo(0, 0)
        time.sleep(0.3)
        for _, image_path13 in apoyo_p5_1.items(): # Buscar punto apoyo 1
            if buscando_apoyo>=5:
                print("break 328")
                break
            mina2c=None
            mina2c = pyautogui.locateOnScreen(image_path13, confidence=0.9, grayscale=True)
            time.sleep(0.2)
            if mina2c:
                contador=4
                center1 = pyautogui.center(mina2c)
                del mina2c
                pyautogui.click(center1)
                time.sleep(3.2)
                pyautogui.rightClick(732, 254)
                pyautogui.moveTo(0, 0)
                time.sleep(0.2)
                for _, image_path228c in minarboton_img.items(): # Buscar botón minar
                    locationminarboton_img5c = pyautogui.locateOnScreen(image_path228c, confidence=0.9)
                    time.sleep(0.2)
                    if locationminarboton_img5c:
                        encontradas+=1
                        center = pyautogui.center(locationminarboton_img5c)
                        pyautogui.click(center)
                        time.sleep(4.5) # Tiempo que tarda en llegar y minar
                        pyautogui.rightClick(1025, 455)
                        pyautogui.moveTo(0, 0)
                        time.sleep(0.2)
                        for _, image_path228cc in minarboton_img.items(): # Buscar botón minar
                            locationminarboton_img5cc = pyautogui.locateOnScreen(image_path228cc, confidence=0.9)
                            time.sleep(0.2)
                            if locationminarboton_img5cc:
                                encontradas+=1
                                center = pyautogui.center(locationminarboton_img5cc)
                                pyautogui.click(center)
                                time.sleep(4.8) # Tiempo que tarda en llegar y minar
                                pyautogui.click(383, 411)
                                time.sleep(1)
                            else:
                                pyautogui.click(678, 476)
                                time.sleep(1)
            else:
                contador+=1
                buscando_apoyo+=1
    encontradas=0
    buscando_apoyo=0
    contador=0
    while contador<=3:
        if buscando_apoyo>=5:
            break
        pyautogui.moveTo(0, 0)
        time.sleep(0.3)
        for _, image_path14 in apoyo_p5_2.items(): # Buscar punto apoyo 2
            if buscando_apoyo>=5:
                print("break 350")
                break
            mina25=None
            mina25 = pyautogui.locateOnScreen(image_path14, confidence=0.9, grayscale=True)
            time.sleep(0.2)
            if mina25:
                contador=4
                center1 = pyautogui.center(mina25)
                del mina25
                pyautogui.click(center1)
                time.sleep(3.2)
            else:
                contador+=1
                buscando_apoyo+=1
    contador=0
    encontradas=0
    while contador<=20 and encontradas<=5:
        if contador>=20 or encontradas>=5:
            print("break 373")
            break
        for _, image_path15 in img_p5_temporal.items(): # Buscar filón
            if contador>=20 or encontradas>=5:
                print("break 373")
                break
            mina4=None
            mina4 = pyautogui.locateOnScreen(image_path15, confidence=0.9, grayscale=True)
            time.sleep(0.2)
            if mina4:
                contador+=1
                print("Antes de buscar apoyo 3 del break 397 ENTRA IF DE MINA4")
                center1 = pyautogui.center(mina4)
                del mina4
                pyautogui.rightClick(center1)
                for _, image_path277 in minarboton_img.items(): # Buscar botón minar
                    locationminarboton_img5 = pyautogui.locateOnScreen(image_path277, confidence=0.9)
                    time.sleep(0.2)
                    if locationminarboton_img5:
                        encontradas+=1
                        center = pyautogui.center(locationminarboton_img5)
                        pyautogui.click(center)
                        time.sleep(6.2) # Tiempo que tarda en llegar y minar
            else:
                contador+=1
                print("Antes de buscar apoyo 3 del break 397 ELSEEEE")

    print("Antes de buscar apoyo 3 del break 397")
    encontradas=0
    buscando_apoyo=0
    encontrado=0
    contador=0
    while contador<=3:
        if buscando_apoyo>=5:
            break
        pyautogui.moveTo(0, 0)
        time.sleep(0.2)
        for _, image_path16 in apoyo_p5_3.items(): # Buscar punto apoyo 3
            if buscando_apoyo>=5:
                print("break 397")
                break
            mina111=None
            mina111 = pyautogui.locateOnScreen(image_path16, confidence=0.9, grayscale=True)
            time.sleep(0.2)
            if mina111:
                contador=4
                print("Encontró punto de apoyo 3")
                center1 = pyautogui.center(mina111)
                del mina111
                pyautogui.click(center1)
                time.sleep(3)
                encontrado=1
                pyautogui.rightClick(511, 464)
                pyautogui.moveTo(0, 0)
                time.sleep(0.1)
                for _, image_path19c in img_p5_temporal.items(): # Buscar filón
                    mina5c=None
                    mina5c = pyautogui.locateOnScreen(image_path19c, confidence=0.9, grayscale=True)
                    time.sleep(0.2)
                    if mina5c:
                        center1 = pyautogui.center(mina5c)
                        del mina5c
                        pyautogui.rightClick(center1)
                        time.sleep(4.3)
                        pyautogui.rightClick(428, 406)
                        pyautogui.moveTo(0, 0)
                        time.sleep(0.1)
                        for _, image_path19cc in img_p5_temporal.items(): # Buscar filón
                            mina5cc=None
                            mina5cc = pyautogui.locateOnScreen(image_path19cc, confidence=0.9, grayscale=True)
                            time.sleep(0.2)
                            if mina5cc:
                                center1 = pyautogui.center(mina5cc)
                                del mina5cc
                                pyautogui.rightClick(center1)
                                time.sleep(4.4)
            else:
                contador+=1
                print("NO Encontró punto de apoyo 3")
                buscando_apoyo+=1

    encontradas=0
    buscando_apoyo=0
    if(encontrado!=1):
        contador=0
        while contador<=3:
            if buscando_apoyo>=5:
                break
            pyautogui.moveTo(0, 0)
            time.sleep(0.3)
            for _, image_path17 in apoyo_p5_2.items(): # Buscar punto apoyo 2
                if buscando_apoyo>=5:
                    print("break 422")
                    break
                mina12=None
                mina12 = pyautogui.locateOnScreen(image_path17, confidence=0.9, grayscale=True)
                time.sleep(0.2)
                if mina12:
                    contador=4
                    print("Encontró punto de apoyo 2")
                    center1 = pyautogui.center(mina12)
                    del mina12
                    pyautogui.click(center1)
                    time.sleep(3.2)
                else:
                    contador+=1
                    print("NO Encontró punto de apoyo 2")
                    buscando_apoyo+=1
        contador=0
        encontradas=0
        buscando_apoyo=0
        while contador<=3:
            if buscando_apoyo>=5:
                break
            pyautogui.moveTo(0, 0)
            time.sleep(0.3)
            for _, image_path18 in apoyo_p5_3.items(): # Buscar punto apoyo 3
                if buscando_apoyo>=5:
                    print("break 445")
                    break
                mina13=None
                mina13 = pyautogui.locateOnScreen(image_path18, confidence=0.9, grayscale=True)
                time.sleep(0.2)
                if mina13:
                    contador=4
                    encontrado=1
                    center1 = pyautogui.center(mina13)
                    del mina13
                    pyautogui.click(center1)
                    time.sleep(2.8)
                else:
                    contador+=1
                    buscando_apoyo+=1
    if(encontrado==1):
        contador=0
        encontradas=0
        while contador<=10 and encontradas<=2:
            if contador>=10 or encontradas>=2:
                print("break 470")
                break
            for _, image_path19 in img_p5_temporal.items(): # Buscar filón
                if contador>=10 or encontradas>=2:
                    print("break 470")
                    break
                mina5=None
                mina5 = pyautogui.locateOnScreen(image_path19, confidence=0.9, grayscale=True)
                time.sleep(0.2)
                if mina5:
                    contador+=1
                    center1 = pyautogui.center(mina5)
                    del mina5
                    pyautogui.rightClick(center1)
                    for _, image_path278 in minarboton_img.items(): # Buscar botón minar
                        locationminarboton_img5 = pyautogui.locateOnScreen(image_path278, confidence=0.9)
                        time.sleep(0.2)
                        if locationminarboton_img5:
                            encontradas+=1
                            center = pyautogui.center(locationminarboton_img5)
                            pyautogui.click(center)
                            time.sleep(6.2) # Tiempo que tarda en llegar y minar
                            
                else:
                    contador+=1
    contador=0
    encontradas=0
    buscando_apoyo=0
    encontrado=0
    while contador<=3:
        if buscando_apoyo>=5:
            break
        pyautogui.moveTo(0, 0)
        time.sleep(0.3)
        for _, image_path112 in apoyo_p5_4.items(): # Buscar punto apoyo 4
            
            if buscando_apoyo>=5:
                print("break 493")
                break
            mina8=None
            mina8 = pyautogui.locateOnScreen(image_path112, confidence=0.9, grayscale=True)
            time.sleep(0.2)
            if mina8:
                contador=4
                print("Encontró punto de apoyo 4")
                encontrado=1
                center1 = pyautogui.center(mina8)
                del mina8
                pyautogui.click(center1)
                time.sleep(3.2)
            else:
                contador+=1
                print("NO Encontró punto de apoyo 4")
                buscando_apoyo+=1
    if(encontrado!=1):
        contador=0
        encontradas=0
        buscando_apoyo=0
        encontrado=0
        while contador<=3:
            if buscando_apoyo>=5:
                break
            pyautogui.moveTo(0, 0)
            time.sleep(0.3)
            for _, image_path113 in apoyo_p5_3.items(): # Buscar punto apoyo 3
                
                if buscando_apoyo>=5:
                    print("break 520")
                    break
                mina6=None
                mina6 = pyautogui.locateOnScreen(image_path113, confidence=0.9, grayscale=True)
                time.sleep(0.2)
                if mina6:
                    contador=4
                    encontrado=1
                    center1 = pyautogui.center(mina6)
                    del mina6
                    pyautogui.click(center1)
                    time.sleep(3.2)
                else:
                    contador+=1
                    buscando_apoyo+=1
        contador=0
        encontradas=0
        buscando_apoyo=0
        encontrado=0
        while contador<=3:
            if buscando_apoyo>=5:
                break
            pyautogui.moveTo(0, 0)
            time.sleep(0.3)
            for _, image_path114 in apoyo_p5_4.items(): # Buscar punto apoyo 4
                
                if buscando_apoyo>=5:
                    print("break 546")
                    break
                mina15=None
                mina15 = pyautogui.locateOnScreen(image_path114, confidence=0.9, grayscale=True)
                time.sleep(0.2)
                if mina15:
                    contador=4
                    encontrado=1
                    center1 = pyautogui.center(mina15)
                    del mina15
                    pyautogui.click(center1)
                    time.sleep(3.2)
                else:
                    contador+=1
                    buscando_apoyo+=1
    if(encontrado==1):
        contador=0
        encontradas=0
        while contador<=20 and encontradas<=4:
            if contador>=20 or encontradas>=4:
                print("break 571")
                break
            for _, image_path115QQ in img_p5_temporal.items(): # Buscar filón
                if contador>=20 or encontradas>=4:
                    print("break 571")
                    break
                mina9QQ=None
                mina9QQ = pyautogui.locateOnScreen(image_path115QQ, confidence=0.9, region=abajo_region, grayscale=True)
                time.sleep(0.2)
                if mina9QQ:
                    contador+=1
                    center1 = pyautogui.center(mina9QQ)
                    del mina9QQ
                    pyautogui.rightClick(center1)
                    for _, image_path279 in minarboton_img.items(): # Buscar botón minar
                        locationminarboton_img5 = pyautogui.locateOnScreen(image_path279, confidence=0.9)
                        time.sleep(0.2)
                        if locationminarboton_img5:
                            encontradas+=1
                            center = pyautogui.center(locationminarboton_img5)
                            pyautogui.click(center)
                            time.sleep(6.2) # Tiempo que tarda en llegar y minar
                            
                else:
                    contador+=1
        contador=0
        encontradas=0
        while contador<=20 and encontradas<=4:
            if contador>=20 or encontradas>=4:
                print("break 571")
                break
            for _, image_path115 in img_p5_temporal.items(): # Buscar filón
                if contador>=20 or encontradas>=4:
                    print("break 571")
                    break
                mina9=None
                mina9 = pyautogui.locateOnScreen(image_path115, confidence=0.9, grayscale=True)
                time.sleep(0.2)
                if mina9:
                    contador+=1
                    center1 = pyautogui.center(mina9)
                    del mina9
                    pyautogui.rightClick(center1)
                    for _, image_path279 in minarboton_img.items(): # Buscar botón minar
                        locationminarboton_img5 = pyautogui.locateOnScreen(image_path279, confidence=0.9)
                        time.sleep(0.2)
                        if locationminarboton_img5:
                            encontradas+=1
                            center = pyautogui.center(locationminarboton_img5)
                            pyautogui.click(center)
                            time.sleep(6.3) # Tiempo que tarda en llegar y minar
                            
                else:
                    contador+=1
    contador=0
    encontradas=0
    buscando_apoyo=0
    encontrado=0
    while contador<=3:
        if buscando_apoyo>=5:
            break
        pyautogui.moveTo(0, 0)
        time.sleep(0.3)
        for _, image_path121 in apoyo_p5_4.items(): # Buscar punto apoyo 4
            if buscando_apoyo>=5:
                print("break 723")
                break
            mina21=None
            mina21 = pyautogui.locateOnScreen(image_path121, confidence=0.85, grayscale=True)
            time.sleep(0.2)
            if mina21:
                contador=4
                encontrado=1
                center1 = pyautogui.center(mina21)
                del mina21
                pyautogui.click(center1)
                time.sleep(3.2)
            else:
                contador+=1
                buscando_apoyo+=1
    pyautogui.rightClick(x=731,y=207)
    pyautogui.moveTo(0, 0)
    time.sleep(0.2)
    for _, image_path279FF in minarboton_img.items(): # Buscar botón minar
        locationminarboton_img5FF = pyautogui.locateOnScreen(image_path279FF, confidence=0.9)
        time.sleep(0.2)
        if locationminarboton_img5FF:
            encontradas+=1
            center = pyautogui.center(locationminarboton_img5FF)
            pyautogui.click(center)
            time.sleep(6.2) # Tiempo que tarda en llegar y minar
            pyautogui.click(x=682,y=519)
            time.sleep(2)
    pyautogui.rightClick(x=735,y=598)
    pyautogui.moveTo(0, 0)
    time.sleep(0.2)
    for _, image_path279FF1 in minarboton_img.items(): # Buscar botón minar
        locationminarboton_img5FF1 = pyautogui.locateOnScreen(image_path279FF1, confidence=0.9)
        time.sleep(0.2)
        if locationminarboton_img5FF1:
            encontradas+=1
            center = pyautogui.center(locationminarboton_img5FF1)
            pyautogui.click(center)
            time.sleep(6.2) # Tiempo que tarda en llegar y minar
            pyautogui.click(x=811,y=247)
            time.sleep(2)
    contador=0
    encontradas=0
    buscando_apoyo=0
    encontrado=0
    while contador<=3:
        if buscando_apoyo>=5:
            break
        pyautogui.moveTo(0, 0)
        time.sleep(0.3)
        for _, image_path122 in apoyo_p5_3.items(): # Buscar punto apoyo 3
            if buscando_apoyo>=5:
                print("break 751")
                break
            mina22=None
            mina22 = pyautogui.locateOnScreen(image_path122, confidence=0.85, grayscale=True)
            time.sleep(0.2)
            if mina22:
                contador=4
                encontrado=1
                center1 = pyautogui.center(mina22)
                del mina22
                pyautogui.click(center1)
                time.sleep(3.2)
                
            else:
                contador+=1
                buscando_apoyo+=1
    contador=0
    encontradas=0
    buscando_apoyo=0
    encontrado=0
    while contador<=3:
        if buscando_apoyo>=5:
            break
        pyautogui.moveTo(0, 0)
        time.sleep(0.3)
        for _, image_path123 in apoyo_p5_2.items(): # Buscar punto apoyo 2
            if buscando_apoyo>=5:
                print("break 778")
                break
            mina14=None
            mina14 = pyautogui.locateOnScreen(image_path123, confidence=0.85, grayscale=True)
            time.sleep(0.2)
            if mina14:
                contador=4
                encontrado=1
                center1 = pyautogui.center(mina14)
                del mina14
                pyautogui.click(center1)
                time.sleep(3.1)
                
            else:
                contador+=1
                buscando_apoyo+=1
    contador=0
    encontradas=0
    buscando_apoyo=0
    encontrado=0
    while contador<=3:
        if buscando_apoyo>=5:
            break
        pyautogui.moveTo(0, 0)
        time.sleep(0.3)
        for _, image_path124 in apoyo_p5_1.items(): # Buscar punto apoyo 1
            
            if buscando_apoyo>=5:
                print("break 805")
                break
            mina23=None
            mina23 = pyautogui.locateOnScreen(image_path124, confidence=0.85, grayscale=True)
            time.sleep(0.2)
            if mina23:
                contador=4
                encontrado=1
                center1 = pyautogui.center(mina23)
                del mina23
                pyautogui.click(center1)
                time.sleep(0.3)
            else:
                contador+=1
                buscando_apoyo+=1

    if(encontrado!=1):
        print("Algo salió mal. No volvió al punto de inicio PUNTO DE APOYO 1")
    deslogeo()
    pass
#P6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
def action_for_p6(position):
    logeo(position)
    contador=0
    encontradas=0
    while contador<=20 and encontradas<=6:
        if contador>=20 or encontradas>=6:
            print("break 306")
            break
        for _, image_path12Q in img_p5_temporal.items(): # Buscar filón
            if contador>=20 or encontradas>=5:
                print("break 310")
                break
            minaQ=None
            minaQ = pyautogui.locateOnScreen(image_path12Q, confidence=0.9, region=abajo_region, grayscale=True)
            time.sleep(0.2)
            if minaQ:
                contador+=1
                center1 = pyautogui.center(minaQ)
                del minaQ
                pyautogui.rightClick(center1)
                for _, image_path228Q in minarboton_img.items(): # Buscar botón minar
                    locationminarboton_img5 = pyautogui.locateOnScreen(image_path228Q, confidence=0.9)
                    time.sleep(0.2)
                    if locationminarboton_img5:
                        encontradas+=1
                        center = pyautogui.center(locationminarboton_img5)
                        pyautogui.click(center)
                        time.sleep(6.2) # Tiempo que tarda en llegar y minar
            else:
                contador+=1
    deslogeo()
    pass

def perform_action(image_key, position):
    # Elimina la extensión '.png' del image_key
    image_key = image_key.replace('.png', '')
    actions = {
        "p1": action_for_p1,
        "p2": action_for_p2,
        "p3": action_for_p3,
        "p4": action_for_p4,
        "p5": action_for_p5,
        "p6": action_for_p6,
        # Agrega más acciones para las demás imágenes
    }
    action = actions.get(image_key)
    if action:
        action(position)
    else:
        print("No se encontró una acción")

def parar_programa():
    global running
    running = False

def on_press(key):
    global timer
    if key == keyboard.Key.ctrl_l:
        print("Ctrl presionado")

def on_release(key):
    global timer
    key_to_hours = {keyboard.KeyCode.from_char(str(i)): i for i in range(1, 10)} # Hasta 9 horas

    if key == keyboard.Key.ctrl_l:
        print("Ctrl liberado")
    elif key in key_to_hours and timer is None:
        hours = key_to_hours[key]
        print(f"Detener el programa en {hours} horas")
        timer = threading.Timer(hours * 3600, parar_programa)
        timer.start()

running = True
timer = None

def buscar_personajes(positions):
    while running:
        # Acceder a las posiciones de imágenes de manera dinámica
        for i in range(1, np + 1):
            image_key = f"p{i}"
            position = positions.get(image_key, None)
            searching = False

            while not searching:
                if position:
                    searching = True
                    time.sleep(0.1)
                    # Dar doble click en la posición de la imagen del personaje a seleccionar
                    pyautogui.doubleClick(position)
                    time.sleep(0.1)
                    pyautogui.doubleClick(position)  # Para garantizar que entre
                    # Llamar a la función para realizar la acción deseada
                    perform_action(image_key, position)
                else:
                    print("x")

try:
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        buscar_personajes(positions)
        
except FileNotFoundError as e:
    print(f"Error de archivo no encontrado: {e}")
except ValueError as e:
    print(f"Error de valor: {e}")
except Exception as e:
    print(f"Se produjo un error: {e}")
finally:
    input("Presione cualquier tecla para cerrar...")