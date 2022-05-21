# gerenciador-tarefas

Desenvolvimento de uma aplicação usando Django para gerenciar tarefas.

Aplicação pronta está disponivel: https://minhasfinancas-edufgs-app.herokuapp.com/

# Ferramentas usadas:
* <b>Spring Boot V2.2.2:</b> O Spring Boot é um framework Open Source que nasceu a partir do Spring framework e veio para facilitar as configurações iniciais de um projeto.
  <br>Site da Documentação: https://docs.spring.io/spring-boot/docs/current/reference/html/features.html#data.sql
  
* <b>PostgreSQL:</b> O PostgreSQL é um poderoso sistema de banco de dados relacional de objeto de código.
  <br>Site Oficial: https://www.postgresql.org/

* <b>H2:</b> O H2 é um sistema de gerenciamento de banco de dados relacional escrito em Java. Ele pode ser incorporado em aplicativos Java ou executado no modo cliente-servidor. (Utilizado em testes).
  <br>Site Oficial: https://www.h2database.com/html/main.html

* <b>Lombok:</b> O Lombok é um framework para Java que permite escrever código eliminando a verbosidade, o que permite ganhar tempo de desenvolvimento para o que realmente é importante. Seu uso permite gerar em tempo de compilação os métodos getters e setters, métodos construtores, padrão builder e muito mais.
 <br>Site Oficial: https://projectlombok.org/

* <b>Jsonwebtoken:</b> é um pacote que implementa o protocolo JSON Web Token.
<br>Site: https://mvnrepository.com/artifact/io.jsonwebtoken/jjwt

# Editor de código-fonte:
* <b>Eclipse:</b> é uma IDE para desenvolvimento Java, porém suporta várias outras linguagens a partir de plugins como C/C++, PHP, ColdFusion, Python, Scala e Kotlin. Ele foi feito em Java e segue o modelo open source de desenvolvimento de software.

# Testes feitos com:
* <b>Junit5:</b> é um framework open-source, que se assemelha ao raio de testes software java.

* <b>Insomnia:</b> enviar solicitações REST, SOAP, GraphQL e GRPC. Assim com insomnia é possivel fazer testes de requisições HTTP.

* <b>H2:</b> O H2 é um sistema de gerenciamento de banco de dados relacional escrito em Java. Ele pode ser incorporado em aplicativos Java ou executado no modo cliente-servidor. Foi usado para testes do código.

# Instalações e Criação do Projeto: 

<b>Spring Boot:</b> No site https://start.spring.io/ crie o projeto preenchendo os dados e colocando todas as dependências como <b>PostgreSQL</b>, <b>H2</b>, <b>Lombok</b>, entre outros. Algumas dependências é preciso adicionar manualmente no arquivo pom.xml como o <b>Jsonwebtoken</b>:

```
  <dependency>
	<groupId>io.jsonwebtoken</groupId>
	<artifactId>jjwt</artifactId>
	<version>0.9.1</version>
  </dependency>
```

Ou indo no site https://mvnrepository.com/artifact/io.jsonwebtoken/jjwt onde tem várias versões para ser selecionadas.

Depois de preencher os dados é preciso baixar e importar para o <b>Eclipse</b> onde vai ser instalado todas as dependências adicionadas.

# Build projeto:

É usado o <b>maven</b> para criar o .jar do projeto mas é preciso instalar e colocar como variavel de ambiente. O site https://dicasdejava.com.br/como-instalar-o-maven-no-windows/ mostra como fazer.

Usando o comando "mvn clean package" no CMD dentro do diretorio do projeto, vai limpar, fazer os testes e montar o .jar. Caso não queira que os testes seja feito então use o comando "mvn clean -Dmaven.test.skip package". O build do projeto vai estar presente na pasta "target".

# Publicando aplicação na nuvem:
Foi utilizado o Heroku para publicação da aplicação onde ele é uma plataforma amplamente confiável como uma oferta de serviço que permite aos desenvolvedores realizar implantação, escalonamento e gerenciamento de aplicativos sem complicações. Esta plataforma oferece suporte para uma ampla gama de linguagens de programação, como Java, Ruby, PHP, Node.js, Python, Scala e Clojure. O Heroku executa aplicativos por meio de contêineres virtuais conhecidos como Dynos.

Aplicação pronta está disponivel: https://minhasfinancas-edufgs-app.herokuapp.com/

# Banco de dados
Foi usado o <b>PostgreSQL</b> como repositório dentro do Heroku. Nele estão presentes as credenciais e é possível acessar utilizando o PgAdmin (Site: https://www.pgadmin.org/download/) e assim configurar as tabelas de finanças para ser acessadas pela API.
