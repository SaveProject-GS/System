# pip install pyserial
import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()
portList = []

for one in ports:
    portList.append(str(one))
    print(str(one))

com = input('Selecione a porta para o Arduino pelo número: ')

for i in range(len(portList)):
    if portList[i].startswith('COM' + str(com)):
        use = 'COM' + str(com)
        print('Porta selecionada: ' + use)

serialInst.baudrate = 9600
serialInst.port = use
serialInst.open()

while True:
    command = input('(ON/OFF): ')
    serialInst.write(command.encode('utf-8'))
    
    if command == 'sair':
        exit()