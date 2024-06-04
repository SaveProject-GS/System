import serial
import serial.tools.list_ports
import cv2
from keras.models import load_model
import numpy as np
import time

# Inicialização do seriado e câmera
ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()
portList = []

for one in ports:
    portList.append(str(one))
    print(str(one))

com = input('Selecione a porta para o Arduino pelo número: ')
found_port = False

for i in range(len(portList)):
    if portList[i].startswith('COM' + str(com)):
        use = 'COM' + str(com)
        print('Porta selecionada: ' + use)
        found_port = True
        break

if not found_port:
    print("Porta não encontrada!")
    exit()

serialInst.baudrate = 9600
serialInst.port = use
serialInst.open()

# Carregar o modelo de aprendizado de máquina
model = load_model('keras_model.h5')
classes = ['fundo', 'controle', 'ao']

cap = cv2.VideoCapture(0)

while True:
    # Leitura da imagem da câmera
    success, img = cap.read()
    if not success:
        print("Erro ao ler a imagem da câmera!")
        break

    imgS = cv2.resize(img, (224, 224))
    image_array = np.asarray(imgS)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    data[0] = normalized_image_array

    # Previsão do modelo
    prediction = model.predict(data)
    indexVal = np.argmax(prediction)
    print(classes[indexVal])

    # Enviar comando ao Arduino
    if classes[indexVal] == 'controle':
        serialInst.write('ON'.encode('utf-8'))
        print("Comando enviado: ON")
    else:
        serialInst.write('OFF'.encode('utf-8'))
        print("Comando enviado: OFF")

    # Exibir imagem com texto
    cv2.putText(img, str(classes[indexVal]),(50,50), cv2.FONT_HERSHEY_COMPLEX, 2, (0,255,0), 2)
    cv2.imshow('img',img)

    time.sleep(1)

# Fechar a câmera e o seriado
cap.release()
cv2.destroyAllWindows()
serialInst.close()