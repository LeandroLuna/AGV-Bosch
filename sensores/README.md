Programação da parte operacional do AGV explicada:
- FC37
- HCSR04
- TCRT5000
- L298n (e motores)

FC37 – Hardware:
O sensor de chuva, FC37, é composto por 2 peças: uma peça é a placa eletrônica e a outra peça é a placa coletora, está última sendo onde a água cairá sobre. Na placa eletrônica encontramos um potenciômetro, utilizado para ajustar a sensibilidade da saída digital (D0); tal como um LED de saída digital, que liga quando há água sobre a placa coletora. 

Funcionamento: 
Basicamente, a resistência da placa coletora varia de acordo com a quantidade de água sobre a sua superfície. Quando a placa está molhada, a sua resistência aumenta, e sua voltagem de saída diminui (0). Já quando ela está seca, temos uma resistência menor, e uma voltagem de saída maior (1). Usando uma saída analógica (A0) podemos ter uma maior resolução e precisão na sua mensuração, porém não foi o modo utilizado por nossa equipe por não haver tal necessidade. Através disso conseguimos obter a informação binária (0 ou 1) para fazer o controle de velocidade dos motores.

HCSR04 – Hardware:
O sensor ultrassônico, HCSR04, consiste basicamente de 2 transdutores ultrassônicos: um conhecido como ‘Trigger’ (transmissor), e outro conhecido como ‘Echo’ (receptor). O transdutor transmissor, Trigger, converte um sinal elétrico em um pulso ultrassônico de 40KHz – para se ter noção, a audição humana consegue captar ondas sonoras de uma faixa 20Hz a até 20000Hz, ou seja, o som produzido pelo Trigger é quase inaudível – que será recebido pelo transdutor receptor, Echo, e que quando recebida pode-se determinar a largura da onda (que é proporcional ao tempo levado entre o momento de transmissão da onda até sua recepção), gerando-se assim um pulso de saída que será interpretado no programa.

Funcionamento:
Primeiramente deve-se ativar o transdutor responsável pela transmissão da onda, Trigger. A onda viajará através do espaço até ela encontrar em algo que possa refletir ela, mandando-a de volta para o transdutor responsável pelo recebimento, Echo. Agora que temos o tempo da diferença entre a emissão e a recepção, devemos converter ela para a velocidade do som em cm/s, e dividir tal valor por 2 – já que só queremos o ponto em que a onda sonora foi refletida pelo objeto. Tal equação pode ser escrita de tal maneira: (0.034 cm/µs x tempo em microssegundos) / 2. Após isso teremos o valor da distância do objeto, que em nosso caso, servirá para evitar acidentes e colisões.

TCRT5000 – Hardware:
O sensor de refletância, TCRT5000, funciona através da transmissão de uma luz, por um LED emissor, e registrando quaisquer luzes refletidas em um fototransistor - um pequeno receptor infravermelho. O fluxo de corrente é alterado de acordo com o nível de intensidade da luz que o fototransistor recebe. Quanto maior a intensidade dessa luz, maior é a corrente de saída; e quanto menor a intensidade dessa luz, menor é a sua corrente de saída. Através da saída analógica (A0) pode-se mensurar o quanto da corrente está sendo emitida, porém, no nosso caso, só usaremos a saída digital (binária, 0 ou 1) para fazer o controle do AGV segue-linha.  Para fazer a mensuração com a saída digital também encontramos no sensor um potenciômetro, que funcionará da seguinte maneira: quando o sensor estiver energizado e houver uma pouca intensidade na luz refletida no fototransistor, o pino digital estará recebendo a valor 0 (‘Low’, baixo) .Enquanto quando a intensidade dessa luz for alta – a ideia da intensidade da luz ‘baixa e alta’ é configurada através do potenciômetro -, o pino digital estará recebendo o valor 1 (‘High’, alto).

Funcionamento:
Através da saída digital (D0) será lida um valor (0 ou 1) para cada um dos 2 sensores encontrados no AGV. Caso ambos os sensores estejam recebendo no seu estado o valor 1, isso nos indica de que ambos os sensores estão recebendo uma certa intensidade de luz suficiente (conforme o parâmetro explicado na parte de hardware) para se manter sobre a linha. Nesse caso, devemos então somente ligar todos os motores para direção que queremos. Já caso somente o sensor de refletância da esquerda esteja recebendo uma intensidade de luz favorável para ter em seu estado o valor 1, os motores da direita serão desligados para refazer o reajuste da posição do AGV sobre a linha. Assim que o sensor da direita voltar a receber uma intensidade de luz suficiente para ser reativado, os motores da direita, consequentemente, também serão religados. Vice-versa. E é seguindo tal conceito que o algoritmo do segue-linha foi criado.

