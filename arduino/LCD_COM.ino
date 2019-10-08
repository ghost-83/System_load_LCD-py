#include <Wire.h> 
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27,20,4);
int data[2];
int lin1,lin2;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  lcd.init();
  lcd.backlight();
  lcd.setCursor(0,0);
  lcd.print("CPU");
  lcd.setCursor(0,1);
  lcd.print("RAM");

}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0){
    data[0] = Serial.read();
    data[1] = Serial.read();
    lcd.setCursor(15,0);
    lcd.print("%");
    lcd.setCursor(15,1);
    lcd.print("%");
    lin1 = data[0]/10;
    for(int i=3; i<13; i++){
      if(lin1 > (i-3)){
        lcd.setCursor(i,0);
        lcd.print("\xFF");
      }
      else{
        lcd.setCursor(i,0);
        lcd.print("\x20");
      }
    }
    lin2 = data[1]/10;
    for(int i=3; i<13; i++){
      if(lin2 > (i-3)){
        lcd.setCursor(i,1);
        lcd.print("\xFF");
      }
      else{
        lcd.setCursor(i,1);
        lcd.print("\x20");
      }
    }
    if(data[0] <10){
      lcd.setCursor(13,0);
      lcd.print("0");
      lcd.setCursor(14,0);
      lcd.print(data[0]);
    }
    else{
      lcd.setCursor(13,0);
      lcd.print(data[0]);
    }
        if(data[1] <10){
      lcd.setCursor(13,1);
      lcd.print("0");
      lcd.setCursor(14,1);
      lcd.print(data[1]);
    }
    else{
      lcd.setCursor(13,1);
      lcd.print(data[1]);
    }
  }
  delay(200);
}
