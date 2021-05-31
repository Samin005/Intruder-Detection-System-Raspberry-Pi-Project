###############################################################################
# Makefile for project 
###############################################################################

## General options
PROJECT = 
MCU = MSP430F2132
COMPILER = "GCC for MSP430"
TARGET = Debug
SHELL = C:\Windows\system32\cmd.exe

## Tools general options
CCFLAGS=-gdwarf-2 -fomit-frame-pointer -Wall -fverbose-asm -MD -MP -fsigned-char -O0 -mmcu=msp430f2132
LDFLAGS=-mmcu=msp430f2132

## Processing Tools
CC=msp430-gcc.exe
LD=msp430-gcc.exe
ASM=msp430-gcc.exe
BIN2HEX=msp430-objcopy.exe
#  C:/Users/14101005/Documents/MSP430F2132/Debug/Debug.elf: TOOL=LD
#     C:/Users/14101005/Documents/MSP430F2132/Debug/main.o: TOOL=CC
#        C:/Users/14101005/Documents/MSP430F2132/main.c

# Build tree:
all:	Debug

Debug:	Debug.elf

Debug.elf:	main.o 
	$(LD) $(LDFLAGS)  -o "Debug.elf" "main.o"

main.o:	../main.c 
	$(CC) -c $(CCFLAGS)   "../main.c" -o "main.o" 

# tidy - delete all temporary files which are not involved in the target generation
tidy:
	rm -rf ./main.d

# cleanup - delete all generated files
clean:	tidy
	rm -rf Debug.elf
	rm -rf main.o

