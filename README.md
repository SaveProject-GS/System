# System
Sistema de identificação e processamento de imagens para a Global Solution da FIAP Paulista.
Repositório dedicado para as Matérias de Edge Computing e Computational thinking with Python.

Integrantes:
- Leonardo de Farias Silva - RM: 555211.
- Giancarlo Cestarolli - RM: 555248.
- Gustavo Laur Pisanello - RM: 556603.

Projeto tinkercad: https://www.tinkercad.com/things/6CxT8PXSaCg-servo-motor-e-leds 
(Devido às limitações do tinkercad, um botão foi utilizado para representar o processamento de imagem)

Vídeo demonstração: https://youtu.be/-aAxORzMVLo

Requisitos de sistema:
- Python entre as versões 3.7 e 3.9 devido à compatibilidade com o Tensorflow.
- Baixar biblioteca Tensorflow.
- Baixar biblioteca pyserial.

Utilização:
- Faça o upload do arquivo "Controle_de_arduino.ino" Para a placa seguindo a numeração de cada uma das portas assim como no modelo do tinkercad, com excessão do botão que não precisa ser utilizado.
- Mantenha o cabo USB conectado ao dispositivo durante toda a execução.
- Abra a pasta "Processamento_de_imagem" no Visual Studio Code para que não precise ser feitas alterações no código, caso você queira abrir só o "project.py" deverá substituir o parâmetro de "load_model()" na linha 39 pelo caminho do arquivo no dispositivo.
- Execute o programa "project.py" via terminal, pois será necessário escolher a porta em que o Arduino está conectado.
- Escolha a porta em que o Arduino esá conectado
- Os modelos no repositório são os mesmos utilizados no video demonstração, caso queira testar em casa, utilize o Teacheble Machine(https://teachablemachine.withgoogle.com/train/image), faça o download do modelo e substitua os arquivos "labels.txt" e "kera_model.h5" da pasta "Processamento_de_imagem" pelos novos arquivos.
- Dica de utilização: caso queira classificar dois itens ou mais, adicione cada um dos itens ao Teacheble Machine e adicione também o fundo sem nenhum dos itens para evitar possíveis interferências.

Possíveis problemas:
- Caso algum erro envolvendo a câmera apareça, verifique se ela não está sendo utilizada por outro programa.
- Caso algum erro envolvendo timeout ou buffer apareça, desconecte e reconecte a placa Arduino.
- Em alguns casos, pode vir a acontecer de a câmera não estar aparecendo na tela do dispositivo, caso o programa continue rodando sem a câmera aparecer, o processamento vai continuar acontecendo em tempo real, não interferindo em nada na performance do programa. Caso você deseje visualizar a câmera mesmo assim, altere as dimensões da câmera como citado na linha 51.
