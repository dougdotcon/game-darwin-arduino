# ArduinoMouseController

Este projeto permite controlar o mouse do computador através de um Arduino, com uma interface gráfica amigável para configuração e teste.

## 📋 Pré-requisitos

1. **Hardware:**
   - Arduino (qualquer modelo compatível com a biblioteca Mouse)
   - Cabo USB para conectar o Arduino ao computador

2. **Software:**
   - Python 3.6 ou superior
   - Arduino IDE
   - Drivers do Arduino instalados

## 🔧 Instalação

### 1. Preparar o Arduino
- Abra o arquivo `mouse_controller.ino` na Arduino IDE
- Faça o upload do código para o seu Arduino
- Mantenha o Arduino conectado via USB

### 2. Instalar Dependências Python
bash
pip install -r requirements.txt


## 🚀 Como Usar

### 1. Iniciar a Interface
bash
python interface.py


### 2. Configuração Inicial
- **Seção Conexão Arduino:**
  1. Clique em "Atualizar Portas" para localizar seu Arduino
  2. Selecione a porta correta na lista
  3. Clique em "Conectar"

- **Seção Configurações:**
  1. Ajuste a resolução da sua tela (ex: 1920x1080)
  2. Ajuste as escalas X e Y se necessário
  3. Clique em "Salvar Configurações"

### 3. Testar o Movimento
Use a área de teste para verificar o funcionamento:
1. Clique em "Calibrar Mouse" para resetar a posição
2. Clique em qualquer ponto da área branca para mover o mouse
3. Use "Testar Movimento Aleatório" para movimento automático

## ⚙️ Ajustes Finos

Se o mouse não estiver se movendo corretamente:

1. **Calibração de Posição:**
   - Use o botão "Calibrar Mouse" para resetar a posição
   - Verifique se a resolução configurada corresponde à sua tela

2. **Ajuste de Escala:**
   - Se o mouse move muito: reduza os valores de escala (ex: 0.8)
   - Se o mouse move pouco: aumente os valores de escala (ex: 1.2)
   - Clique em "Salvar Configurações" após ajustes

## 🔍 Solução de Problemas

1. **Arduino não aparece na lista de portas:**
   - Verifique se o Arduino está conectado
   - Clique em "Atualizar Portas"
   - Reinstale os drivers se necessário

2. **Mouse move para posição errada:**
   - Verifique se a resolução está correta
   - Calibre o mouse usando o botão "Calibrar Mouse"
   - Ajuste as escalas X e Y

3. **Erro de conexão:**
   - Desconecte e reconecte o Arduino
   - Feche e abra novamente o programa
   - Verifique se outro programa não está usando a porta

## 📝 Notas Importantes

- Mantenha o Arduino conectado durante todo o uso
- Não mova o mouse manualmente durante a calibração
- Salve as configurações após qualquer ajuste
- Em caso de comportamento estranho, recalibre o mouse

## 🛠️ Desenvolvimento

O projeto consiste em dois componentes principais:

1. **Código Arduino (`mouse_controller.ino`):**
   - Controla o movimento físico do mouse
   - Recebe comandos via porta serial

2. **Interface Python (`interface.py`):**
   - Fornece interface gráfica para configuração
   - Gerencia a comunicação com o Arduino
   - Salva e carrega configurações