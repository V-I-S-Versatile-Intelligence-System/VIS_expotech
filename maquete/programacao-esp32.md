# Programação e Automação — V.I.S.

## Desenvolvimento do sistema

A programação da maquete V.I.S. Smart Home 2050 foi realizada utilizando a Arduino IDE e a linguagem C++, com o microcontrolador ESP32.

O objetivo foi integrar os componentes eletrônicos para permitir o controle automatizado da residência.

## Controle da iluminação

Foi desenvolvido um sistema para controlar individualmente as luzes de seis ambientes:

- Quarto 1
- Quarto 2
- Sala
- Cozinha
- Banheiro
- Garagem

Também foi implementada a função de acender e apagar todas as luzes simultaneamente.

## Automação do portão

O portão utiliza um servo motor SG90, responsável pelo movimento do mecanismo de pinhão e cremalheira.

Durante o desenvolvimento, foram realizados testes para ajustar a velocidade e o tempo de movimentação.

O tempo de acionamento foi calibrado para aproximadamente 2,56 segundos.

O sistema também utiliza um sensor ultrassônico HC-SR04 para identificar a aproximação de veículos.

O fechamento temporizado foi configurado para ocorrer após aproximadamente 7 segundos.

## Comunicação Wi-Fi

O ESP32 foi configurado para se conectar a uma rede Wi-Fi.

Foi implementado um servidor HTTP local, permitindo acessar um painel de controle pelo navegador.

Por meio desse painel, é possível:

- Acender e apagar as luzes.
- Controlar o portão.
- Acionar a iluminação da garagem durante a abertura do portão.

## Testes realizados

Durante o desenvolvimento, foram realizados testes de:

- Comunicação entre o ESP32 e os componentes.
- Funcionamento do sensor ultrassônico.
- Movimentação do servo motor.
- Controle individual dos LEDs.
- Conexão Wi-Fi.
- Funcionamento do painel web.

## Resultado

O sistema foi testado com sucesso, permitindo controlar a iluminação e o portão por meio do ESP32 e de uma interface web local.

A integração com o Bubble e o n8n faz parte da etapa de conexão entre a interface principal e a automação física.
