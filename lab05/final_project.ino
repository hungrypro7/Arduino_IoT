#include <Servo.h>

Servo servo;

int value = 0;          // 서보 모터 값
int rain_sensor = 12;   // 우적 센서
int speakerPin = 8;     // 부저
int tones1[] = {1046, 783, 1046, 1174, 1318, 1174, 1046, 783, 880, 698, 880, 1046, 1396, 659, 587, 523};    // 알림음 
int tones2[] = {987, 783, 987, 1174, 1567, 1396, 1318, 1174, 1318, 1567, 1174, 1567, 1046};

#define RED 2             // R 
#define GREEN 3           // G
#define BLUE 4            // B
#define ECHO_BUS 9      // 초음파 센서 2 echo
#define TRIG_BUS 10     // 초음파 센서 2 trig
#define ECHO_PEO 5      // 초음파 센서 1 echo
#define TRIG_PEO 6      // 초음파 센서 1 trig

void setup() {
  pinMode(RED, OUTPUT);         
  pinMode(GREEN, OUTPUT);
  pinMode(BLUE, OUTPUT);
  
  pinMode(rain_sensor, INPUT);
  Serial.begin(9600);                   // 시리얼 통신, 9600 bit/s
  pinMode(TRIG_BUS, OUTPUT);
  pinMode(ECHO_BUS, INPUT);
  pinMode(TRIG_PEO, OUTPUT);
  pinMode(ECHO_PEO, INPUT);
  servo.attach(11);               // 서보 모터를 몇 번 핀으로 컨트롤 할지 정함
}

void loop() {
  
  long distance_bus, distance_peo;      // 거리 변수 할당

  distance_bus = count_distance(ECHO_BUS, TRIG_BUS);      // 거리 2
  distance_peo = count_distance(ECHO_PEO, TRIG_PEO);      // 거리 1
  Serial.print("distance : ");
  Serial.print(distance_peo);       // 거리 1 출력
  Serial.print("cm \n");

  // put your main code here, to run repeatedly:
  if(digitalRead(rain_sensor) == LOW && distance_bus < 3 && distance_peo < 5) {       // 우적 센서 감지 & 거리 2 < 3cm & 거리 1 < 5cm
    value += 90;        // 모터값 90도 설정
    servo.write(value);       // 서보 90도 회전 

    analogWrite(RED, 255);        // 빨간불로 알림
    analogWrite(GREEN, 0);
    analogWrite(BLUE, 0);
    
    for(int i=0; i<16; i++) {       // 알림음
      tone(speakerPin, tones1[i]);
      delay(200);
    }
    
    for(int i=0; i<13; i++) {     // 알림음
      tone(speakerPin, tones2[i]);
      delay(200);
    }
    noTone(speakerPin); 

    delay(3000);    // 3초 delay

    distance_bus = count_distance(ECHO_BUS, TRIG_BUS);      // 거리 2 측정
    distance_peo = count_distance(ECHO_PEO, TRIG_PEO);      // 거리 1 측정
    Serial.print("distance_peo : ");
    Serial.print(distance_peo);   // 거리 1 출력
    Serial.print("cm \n");

    while(distance_peo < 5) {       // 거리 1 < 5cm 이면,
      Serial.print("------\n");     
      tone(speakerPin, tones1[0]);      // 알림음이 일정 주기로 울림 
      delay(100);
      noTone(speakerPin);               
      delay(1000);
      distance_bus = count_distance(ECHO_BUS, TRIG_BUS);    // 거리 2 측정
      distance_peo = count_distance(ECHO_PEO, TRIG_PEO);    // 거리 1 측정
    }

    value -= 90;    // 서보 모터 값 0으로 초기화
    servo.write(value);     // 서보 모터 회전 (원래 상태로 복귀)
    delay(200);
  }

  analogWrite(RED, 0);
  analogWrite(GREEN, 255);      // 평소에는 초록불로 점등
  analogWrite(BLUE, 0);
  noTone(speakerPin);
  servo.write(0);
  delay(100);
}

int count_distance(int length, int trig) {    // 거리를 cm로 변환하는 함수

  long duration, distance;

  digitalWrite(trig, LOW);                  // 초음파 센서에 신호를 보내고 받을 준비를 함
  delayMicroseconds(2);
  digitalWrite(trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig, LOW);

  duration = pulseIn(length, HIGH);           // HIGH 상태의 펄스의 지속 시간을 마이크로초 단위로 반환
  distance = duration * 17 / 1000;            // 초음파의 속도와 시간 간의 관계를 이용하여 펄스의 지속 시간을 센티미터 단위의 거리로 변환하는 공식
  return distance;
}
