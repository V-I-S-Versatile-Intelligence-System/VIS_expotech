# Controle de Iluminação — V.I.S. Smart Home 2050

## Objetivo

Foi desenvolvida uma interface de controle de iluminação na plataforma Bubble, com o objetivo de permitir que o usuário gerencie as luzes de diferentes ambientes da residência de maneira simples e intuitiva.

## 1. Painel de iluminação

O painel apresenta controles para os seguintes ambientes:

- Quarto 1
- Quarto 2
- Sala
- Cozinha
- Banheiro
- Garagem

Cada ambiente possui seu próprio controle, permitindo que o usuário selecione a iluminação desejada.

## 2. Controle manual

A interface utiliza botões interativos para representar o acionamento das luzes.

O usuário pode interagir com os controles para ligar ou desligar a iluminação de cada ambiente.

Também foi desenvolvida uma opção para acender todas as luzes simultaneamente.

## 3. Workflows do Bubble

Foram utilizados workflows para configurar as ações dos botões.

Esses workflows permitem:

- Identificar o botão selecionado.
- Executar ações ao clicar nos controles.
- Atualizar os estados representados na interface.
- Organizar o funcionamento individual dos ambientes.

## 4. Interface visual

O painel foi desenvolvido buscando oferecer uma experiência moderna e organizada.

Os controles foram distribuídos de maneira que o usuário consiga identificar facilmente os ambientes e suas respectivas funcionalidades.

## 5. Integração com a maquete

A interface de iluminação foi planejada para fazer parte da integração entre o Bubble e o ESP32.

A comunicação com a maquete poderá ser realizada por meio de requisições HTTP, permitindo que os comandos do site sejam enviados ao sistema físico.

Essa integração é uma etapa distinta do desenvolvimento visual e dos workflows internos do Bubble.

## Resultado

Foi desenvolvido um painel de iluminação com controles individuais e acionamento geral, demonstrando como uma interface digital pode facilitar o gerenciamento de uma residência inteligente.
