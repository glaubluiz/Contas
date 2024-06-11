# Historia do projeto

## Descrição/Objetivo
O objetivo deste projeto é periodicamente lembrar você das contas a serem pagas
e servir para monitorar os gastos fixos de todos da casa e gerar tabelas sobre
esses gastos. Para isso as contas terão classificações a respeito da sua 
prioridade e importancia. Também cada conta será atribuida a alguem ou ser 
atribuida a varias pessoas (neste caso deve aparecer a porcentagem ou valor que
cada um deve pagar).

Para fazer isso o projeto deve ter um servidor para rodar em segundo plano e um
menu de interação por linha de comando.

## Especificação dos requisitos

### Requisitos funcionais
- RF1: Servidor
    - RF1.1: Deve ser em sqlite para minimizar instalações acrecentais.
    - RF1.2: Deve se iniciar quando o computador ligar.
    - RF1.3: Deve avisar com antecedencia as contas a serem pagas (5 dias).
    - RF1.4: Deve mandar pop-ups das contas a pagar.
- RF2: Menu
    - RF2.1: Deve, de forma facil, alterar configurações de uso do servidor (ex:
    quantos dias de antecedencia deve avisar sobre as contas).
    - RF2.2: Deve ser possivel ver o historico das contas passadas.
- RF3: As contas 
    - RF3.1: Devem ter um sistema de classificação de prioridade.
    - RF3.2: 5 dias antes de vencer 1 aviso, cada dia vencida 2 avisos.
- RF4: Monitoramento das contas
    - RF4.1: Deve gerar tabelas com os maiores/menores gastos
        RF4.1.1: Valor total das parcelas de uma compra
        RF4.1.2: Valores do mês
        RF4.1.3: Tipos de gastos
    - RF4.2: Deve ser possivel ver os todos gastos de cada um dos usuarios 
    cadatrados.

### Requisitos não funcionais
- RNF1: O programa deve ser executado enquanto o computador estiver ligado
- RNF2: Deve ser de facil instalação

