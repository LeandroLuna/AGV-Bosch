# AGV-Bosch
Toda programação do projeto AGV para o desafio Bosch.

Overview do case:
O AGV será modulado com base em uma raspberry pi zero W com função de controle e gerenciamento de estoque, visando redução de recursos humanos e uma maior autonomia para o stock da Bosch. 

Insight:
O AGV será um segue-linha (sensor de refletância QRE1113), que com auxilio dos sensor de chuva (FC-37, controlará velocidade do AGV com intuito de preservar a carga) e sensor ultrassônico (HC-SR04, fará o amparo da locomoção da carga, evitando acidentes), exercerá locomoção da carga desde sua entrada no armazém Bosch até seu devido sítio no stock. Arquitetado também com uma micro-câmera (OV7670, que lerá QR Code para armazenar as informações dos itens, e suas posições no stock) e leitor RFID (MFRC522, as tags serão escritas e posicionadas em pontos especificos para locomoção do AGV no armazém; e também controle das informações das cargas, garantindo uma garantia de controle das informações de cada carga).

Modelo de utilização:
Com o AGV posicionado sobre a linha, ele buscará a leitura do RFID inicial, ou 'entrada', onde ele terá que buscar a carga. Assim que a carga for reconhecida na entrada do armazém, o leitor de QR Code associara a informação com RFID de localização para mover a carga a seu respectivo stock. Reconhecido o devido stock (RFID poderá ser posicionado nas esquinas de cada stock, e em frente de cada 'prateleira'), o AGV fará um desvio na rota do segue-linha original, e dentro desse stock se posicionará para que algo, ou alguém, remova a carga sobre ele. O AGV só poderá, assim, voltar ao percurso de entrada/saida de cargas, quando a carga for retirada. Após isso o AGV fará o percurso de volta de dentro do stock, retornando ao percurso segue-linha padrão. Concluindo-o, ele voltará a posição inicial de recolhimento de cargas, ou entrada.

As informações do estoque serão apresentadas em um aplicativo(podendo ser até websites; com uso do protocolo MQTT, a informaçao podera ser apresentada em diversos lugares), e todo o produto que for removido do estoque deverá obrigatóriamente ser informado no aplicativo para que o robo não perca o controle dos 'slots' vazios, e ocupados, do stock.
