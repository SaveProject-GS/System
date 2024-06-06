import serial # Bibliotera para comunicação com o Arduino, necessário pip install serial
import serial.tools.list_ports # Lista das portas do dispositivo
import cv2 # Biblioteca para visualização da câmera
from keras.models import load_model # Necessário para interpretação dos modelos de Machine Learning, requer pip install tensorflow
import numpy as np
import time # Necessário para regulagem da taxa de fotos para o processamento

# Inicialização do seriado e câmera
ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()
portList = []

# Lista as portas USB com dispositivos conectados
for one in ports:
    portList.append(str(one))
    print(str(one))

com = input('Selecione a porta para o Arduino pelo número: ')
found_port = False

# Verifica se a porta escolhida pelo usuário possui algum dispositivo conectado
for i in range(len(portList)):
    if portList[i].startswith('COM' + str(com)):
        use = 'COM' + str(com)
        print('Porta selecionada: ' + use)
        found_port = True
        break

if not found_port:
    print("Porta não encontrada!")
    exit()

serialInst.baudrate = 9600 # Deve ser o mesmo valor iniciado no arduino
serialInst.port = use
serialInst.timeout = 5  # Evita erros de timeout por 5 segundos
serialInst.open()

# Carregar o modelo de Machine Learning
model = load_model('keras_model.h5') # Caminho relativo até o arquivo .h5
classes = ['caminho', 'vermelho', 'verde'] # Deve seguir a mesma ordem do arquivo labels.txt

cap = cv2.VideoCapture(0) # Inicia a visualização pela câmera/webcam, número padrão 0

while True:
    # Leitura da imagem da câmera
    success, img = cap.read()
    if not success:
        print("Erro ao ler a imagem da câmera!")
        break

    # Define as dimensões da câmera
    imgS = cv2.resize(img, (224, 224))
    image_array = np.asarray(imgS)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    data[0] = normalized_image_array

    # Previsão do modelo
    prediction = model.predict(data)
    indexVal = np.argmax(prediction)
    # print(prediction) Descomente essa linha para ve,r as porcentagens de cada um dos labels
    print(classes[indexVal])

    # Enviar comando ao Arduino
    try:
        if classes[indexVal] == 'vermelho':
            serialInst.reset_output_buffer()  # Reset output buffer evita erros de envio via serial
            serialInst.write('ON'.encode('utf-8'))
            serialInst.flush()  # Flush pending data evita acúmulo de dados desnecessários via serial
            print("Comando enviado: ON")
        else:
            serialInst.reset_output_buffer()  
            serialInst.write('OFF'.encode('utf-8'))
            serialInst.flush()  
            print("Comando enviado: OFF")
    except serial.SerialTimeoutException:
        print("Erro de timeout ao enviar comando ao Arduino!")
        serialInst.close()
        break

    # Exibe imagem com texto
    cv2.putText(img, str(classes[indexVal]),(50,50), cv2.FONT_HERSHEY_COMPLEX, 2, (0,255,0), 2)
    cv2.imshow('img',img)

    time.sleep(1) # Tempo mínimo suportado pelo Arduino Uno R3 em segundos, pode ser menor dependendo do processamento do microcontrolador

# Fecha a câmera e o seriado
cap.release()
cv2.destroyAllWindows()
serialInst.close()