# MCU ALLIO STM32F072CB
 
## Goal
STM32F072CB MCU 의 모든 IO 를 쉽게 사용할 수 있는 보드 제작 

## TODO
- [ ] Library : 2.54mm pin header for PCB 
- [ ] Library : holes for PCB supporter
- [ ] Library : TP
- [ ] Library : 



## Board 사양
- USB connector for power and DP DN signals
- 2.54mm Pin headers for all MCU pins (including power and ground pins)


## MCU 선정
USB 2.0 FS (12Mbps), crystal-less 선호   
납땜 고려하여 LQFP48 or LQFP64 패키지   
스터디용 보드이므로, 가격은 크게 고려하지 않음.   
SRAM, Flash 용량은 가능하면 큰 것   
STM32 : https://www.st.com/en/microcontrollers-microprocessors/stm32-mainstream-mcus.html   
STM32F0 : https://www.st.com/en/microcontrollers-microprocessors/stm32f0-series.html   
STM32F0x2 : https://www.st.com/en/microcontrollers-microprocessors/stm32f0x2.html   

## Fabrication steps ( JLCPCB )
Menu -> Order -> Order PCB 를 이용하면, 아주 간단하게 PCB 및 SMT 까지 주문 가능

## EasyPCB
prohibited rectangle (with copper) 을 이용하여 Copper 안 깔리는 영역 지정 가능   
Switch to top / bottom 는 Tool -> Settings -> hotkeys 에서 T / B 사용하게 설정

