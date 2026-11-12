# Testes e Soluções — Maquete V.I.S.

## Objetivo

Durante o desenvolvimento da maquete V.I.S. Smart Home 2050, foram realizados diversos testes para garantir o funcionamento dos componentes eletrônicos e das automações.

## 1. Sistema de iluminação

**Problema:** alguns LEDs utilizados inicialmente queimaram durante os testes de alimentação.

**Solução:** substituição dos LEDs e utilização de resistores para limitar a corrente elétrica.

**Resultado:** funcionamento da iluminação dos seis ambientes da residência.

## 2. Servo motor SG90

**Problema:** necessidade de ajustar o movimento do servo motor para abrir e fechar o portão corretamente.

**Solução:** realização de testes utilizando a biblioteca ESP32Servo e calibração do tempo de movimentação.

**Resultado:** abertura e fechamento do portão com tempo de acionamento aproximado de 2,56 segundos.

## 3. Sensor ultrassônico HC-SR04

**Problema:** necessidade de adaptar o sinal de saída do sensor para a tensão suportada pelo ESP32.

**Solução:** montagem de um divisor de tensão no pino ECHO.

**Resultado:** comunicação funcional entre o sensor e o microcontrolador.

## 4. Alimentação elétrica

**Problema:** necessidade de fornecer energia adequada aos componentes eletrônicos.

**Solução:** testes com fontes de alimentação e organização das conexões elétricas.

**Resultado:** alimentação funcional do sistema durante os testes.

## 5. Conexão Wi-Fi

**Problema:** dificuldades iniciais para conectar o ESP32 à rede Wi-Fi.

**Solução:** correção das credenciais e realização de novos testes de conexão.

**Resultado:** ESP32 conectado à rede e servidor HTTP local acessível pelo navegador.

## 6. Automação do portão

**Problema:** o sensor identificava continuamente a presença do veículo, dificultando a lógica de fechamento.

**Solução:** implementação provisória de fechamento temporizado após aproximadamente 7 segundos.

**Resultado:** funcionamento do ciclo de abertura e fechamento durante os testes.

## Conclusão

Os testes permitiram identificar problemas, realizar correções e melhorar o funcionamento da maquete.

Ao final dessa etapa, foi possível controlar as luzes e o portão por meio de um painel web conectado ao ESP32.
