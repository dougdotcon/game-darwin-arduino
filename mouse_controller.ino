#include <Mouse.h>

// Configurações do monitor (ajuste para sua resolução)
const int SCREEN_WIDTH = 1920;  // Largura da tela em pixels
const int SCREEN_HEIGHT = 1080; // Altura da tela em pixels

// Fatores de calibração
float scaleFactorX = 1.0;
float scaleFactorY = 1.0;

void setup() {
  Serial.begin(115200);
  Mouse.begin();
  calibrateMouse();
}

// Move o mouse para o canto superior esquerdo
void calibrateMouse() {
  // Move o mouse para o canto superior esquerdo com margem de segurança
  for (int i = 0; i < 50; i++) {
    Mouse.move(-127, -127, 0);
    delay(5);
  }
  delay(100); // Aguarda o movimento se estabilizar
}

// Move o mouse para uma posição absoluta na tela
void moveMouseTo(int targetX, int targetY) {
  // Limita as coordenadas aos limites da tela
  targetX = constrain(targetX, 0, SCREEN_WIDTH);
  targetY = constrain(targetY, 0, SCREEN_HEIGHT);
  
  // Reseta a posição para referência conhecida
  calibrateMouse();
  delay(50); // Aguarda estabilização
  
  // Calcula o movimento necessário considerando a escala
  int moveX = (int)(targetX * scaleFactorX);
  int moveY = (int)(targetY * scaleFactorY);
  
  // Move em incrementos menores para maior precisão
  const int STEP_SIZE = 10;
  int remainingX = moveX;
  int remainingY = moveY;
  
  while (remainingX != 0 || remainingY != 0) {
    int stepX = (abs(remainingX) > STEP_SIZE) ? (remainingX > 0 ? STEP_SIZE : -STEP_SIZE) : remainingX;
    int stepY = (abs(remainingY) > STEP_SIZE) ? (remainingY > 0 ? STEP_SIZE : -STEP_SIZE) : remainingY;
    
    Mouse.move(stepX, stepY, 0);
    
    remainingX -= stepX;
    remainingY -= stepY;
    delay(1); // Pequeno delay para controle mais preciso
  }
}

// Ajusta os fatores de calibração
void adjustScaleFactor(float newScaleX, float newScaleY) {
  scaleFactorX = constrain(newScaleX, 0.1, 2.0);
  scaleFactorY = constrain(newScaleY, 0.1, 2.0);
}

void loop() {
  if (Serial.available()) {
    String command = Serial.readStringUntil('\n');
    command.trim();
    
    if (command.startsWith("GOTO ")) {
      int spaceIndex = command.indexOf(' ', 5);
      if (spaceIndex != -1) {
        int targetX = command.substring(5, spaceIndex).toInt();
        int targetY = command.substring(spaceIndex + 1).toInt();
        moveMouseTo(targetX, targetY);
      }
    }
    else if (command.startsWith("SCALE ")) {
      int spaceIndex = command.indexOf(' ', 6);
      if (spaceIndex != -1) {
        float newScaleX = command.substring(6, spaceIndex).toFloat();
        float newScaleY = command.substring(spaceIndex + 1).toFloat();
        adjustScaleFactor(newScaleX, newScaleY);
      }
    }
  }
} 