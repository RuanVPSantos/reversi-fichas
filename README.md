# Maia-Controle-De-Efetivo
 Sistema de controle de efetivo referente ao projeto Maia
## A proposta
 O objetivo deste programa é gerar um sistema que permita gerenciamento, visualização e controle de um banco de dados onde constarão o controle de diárias do pessoal de obra.
## As tecnologias
 Utilizaremos do banco de dados sqlite para manter as informações, da linguagem de programação python utilizando a biblioteca flask para geração do sistema, como front end html, css e js e o framework bootstrap. Os contatos do sistema com o banco de dados serão gerenciados a partir da biblioteca cs50. O programa está sendo gerado em um ambiente virtual pipenv a fim de facilitar o deploy dado pelo sistema Heroku. O controle de versão será por git e o código ficará como privado no meu Github.
## A arquitetura
 Na raiz do programa, ficarão: os arquivos python centrais, os arquivos Pipfile e Pipfile.lock. Na pasta data ficarão o banco de dados e um arquivo capaz de zerá-lo e recriá-lo. Na pasta templates ficarão dispostas as estruturas referentes aos arquivos html. Na pasta static, serão contidas imagens e outros artifícios que competirão às páginas de exibição do sistema.
## Do banco de dados
 O banco de dados, como já referido, foi criado e está sendo mantido pela tecnologia SQLite3, e para sua padronização, utilizando a ferramenta CASE encontrada no site [sqlite-workbench](https://www.sqlite-workbench.com). Suas tabelas estão na 5FN.
## Da metodologia
 O modo de produção e integra é dado a partir do modelo incremental, donde cada versão carrega, consigo, um incremento de um mvp referente à uma ou mais funcionalidades. 