# AGV-Bosch
Toda programação do projeto AGV para o desafio Bosch.

Overview do case:
O AGV será modulado com base em uma raspberry pi zero W com função de controle e gerenciamento de estoque, visando redução de recursos humanos e uma maior autonomia para o stock da Bosch. 

Insight:
O AGV será um segue-linha (sensor de refletância QRE1113), que com auxilio dos sensor de chuva (FC-37, controlará velocidade do AGV com intuito de preservar a carga) e sensor ultrassônico (HC-SR04, fará o amparo da locomoção da carga, evitando acidentes), exercerá locomoção da carga desde sua entrada no armazém Bosch até seu devido sítio no stock. Arquitetado também com uma micro-câmera (OV7670, onde ajudará o AGV se situar no armazém: entrada/saida de produtos, e respectivos stocks; assim como ajudará o operador responsável pelo AGV a situar-se de sua situação) e leitor RFID (MFRC522, as tags serão escritas e posicionadas nas cargas, para o controle do que entra e sai do armazém).

Modelo de utilização:
Com o AGV posicionado sobre a linha, ele buscará a leitura do QR Code inicial, ou 'entrada', onde ele terá que buscar a carga. Assim que a carga for reconhecida na entrada do armazém, o leitor RFID associara a informação com QR Code de localização para mover a carga a seu respectivo stock. Reconhecido o devido stock (QR Code poderá ser posicionado tanto no chão da fábrica, quanto na entrada de cada stock), o AGV fará um desvio na rota do segue-linha original, e dentro desse stock se posicionará para que algo, ou alguém, remova a carga sobre ele. O AGV só poderá, assim, voltar ao percurso de entrada/saida de cargas, quando a carga for retirada. Após isso o AGV fará o percurso até o fim do stock, e detectada alguma parede/objeto/sinal, ele fará o caminho contrário de dentro do stock, retornando ao percurso segue-linha padrão. Concluindo-o, ele voltará a posição inicial de recolhimento de cargas, ou entrada.
