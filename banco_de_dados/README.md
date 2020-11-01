Explicação da arquitetura do banco de dados:

É no banco de dados que as informações lidas das tags RFID serão armazenadas e processadas. Planejado com uma interface SQL com o uso do servidor MariaDB, e com o PHPMYADMIN para gerir e administrar a estrutura SQL através da internet.
Dentro do banco de dados (estoques) encontramos uma tabela (baterias, filtros, freios) para cada tipo de produto – essa informação será associada e lida em conjunto com as tags RFID: 

|     **estoques**     |
|:------------------:|
| baterias           |
| filtros            |
| freios             |

Na estrutura no interior de cada tabela encontramos as informações a serem armazenadas, tais como:  
* ID, auto incrementado sempre que um novo dado for inserido na tabela; 
* Nome, para além da identificação do produto pelo ID, ter-se uma segunda via para acessar cada produto; 
* Posição, usado para informar ao AGV os ‘campos’ livres para armazenagem do produto – para isso o armazém da Bosch precisará ser mapeado e enumerado -; 
* Data, irá armazenar tanto a data, quanto o horário, que a TAG do produto for escrita.  

| *Field*   | *Type*             | *Null* | *Key* | *Default* | *Extra*          |
|:-------:|:----------------:|:----:|:---:|:-------:|:--------------:|
| **id**      | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
| **nome**    | text             | YES  |     | NULL    |                |
| **posicao** | tinyint(4)       | YES  |     | NULL    |                |
| **data**    | text             | YES  |     | NULL    |                |

Esses dados poderão ser acessados através do servidor local (localhost/phpmyadmin) quanto pelo IP da raspberry (no nosso caso, 127.0.0.1). Há também a possibilidade de acesso remoto a esse banco de dados. Assim sendo, poderá ser criado ‘n’ usuários com diferentes privilégios no acesso a essas informações. 
