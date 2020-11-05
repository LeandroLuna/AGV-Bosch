# AGV-Bosch
Toda programação do projeto Jabuti-AGV para o desafio Bosch.

Overview do projeto:
O AGV será modulado com base em uma raspberry pi zero W com função de controle e gerenciamento de estoque, visando redução de recursos humanos expendidos e uma maior autonomia para os estoques da Bosch. 

Insight:
O AGV será um segue-linha (sensor de refletância QRE1113), que com auxilio dos sensor de chuva (FC-37: controlará velocidade do AGV com intuito de preservar a carga) e sensor ultrassônico (HC-SR04: fará o amparo da locomoção da carga; evitando acidentes), exercerá locomoção da carga desde sua entrada no armazém Bosch até seu devido sítio nos estoques. Arquitetado também com um leitor RFID (MFRC522: as tags serão escritas e posicionadas em pontos especificos para locomoção do AGV no armazém; e também servirá para fazer o controle das informações de cada carga, enviando essas informações para um banco de dados.).

Modelo de utilização:
Com o AGV posicionado sobre uma linha projetada, o AGV primeiramente buscará a leitura do RFID inicial, ou 'entrada', onde ele irá buscar a carga para começar a fazer o seu devido transporte. Assim que a carga for reconhecida na entrada do armazém, o leitor de RFID associará as informações escritas nas TAGS, recebendos dados tais como ID do produto, Nome de identificação, Posição (servirá sobretudo para o transporte da carga, e o controle dos 'campos' vazios dos estoques) e data de inserção do produto. Reconhecido a devida categoria do tipo do produto, e sua posição a onde ele deverá ser colocado, o AGV começara o processo de locomoção. Vale salientar que o produto deverá ser posto sobre o AGV por algum responsável técnico, ou robo. No nosso prototipo, ele não terá nenhum meio de fazer o recolhimento do produto intuitivamente. As TAGS RFID serão posicionadas nas 'esquinas'(travessas) de cada estoque, e em frente de cada 'prateleira'. O AGV então fará um desvio na rota do segue-linha original, e dentro desse estoque se posicionará para que algo, ou alguém, remova a carga sobre ele. O AGV só poderá, assim, voltar ao percurso de entrada/saida de cargas quando a carga for retirada - e é também nesse momento, após a carga ser recolhida, que os dados serão inseridos no banco de dados. Após isso o AGV fará o percurso de retorno, seguindo instruções contrárias do que ele usou para chegar a aquele devido 'campo', retornando assim ao percurso segue-linha padrão. Concluindo-o, ele voltará a posição inicial de recolhimento de cargas, ou entrada, e fará a leitura de um novo produto.

As informações do estoque serão apresentadas via celular (podendo ser até aplicativos, já que com uso do protocolo MQTT, a informação poderá ser apresentada em diversos lugares), e todo o produto que for removido do estoque deverá obrigatóriamente ser informado no aplicativo para que o robo não perca o controle dos 'campos' vazios e ocupados do estoque.


***AVISO: Houve um problema com a arquitetura do projeto e o modulo da mini-camera OV7670. O projeto inicialmente seria construido com base em uma placa arduino, mas todavia vimos que o microprocessador raspberry entregaria uma maior potencia para a montagem eletronica, quanto para uma maior facilidade na conexão MQTT. Dessa mudança pensavamos que a microcamera (modulo OV7670) teria suporte na raspberry, porém o barramento GPIO (I/O) não suporta uma alta velocidade de interface suficiente para o tal módulo. Seria necessário um output de 25mb/s para que esse módulo funcione. As alternativas para contornar esse infortúnio seriam comprar outro modelo de camera que a PI0 suporte, e o único modelo que conhecemos é o Raspicam (OV5647), ou uma camera com suporte USB. Por hora, como não se há tempo hábil para realizarmos a troca desse modulo, removeremos essa tecnologia/funcionalidade do projeto, mas o escopo da ideia original será mantida. Obs: Além desse problema de integração, ela não foi entregue a tempo hábil.

Video de seu funcionamento: 
https://www.youtube.com/watch?v=U6FojX3zOjM&list=LL&index=3
