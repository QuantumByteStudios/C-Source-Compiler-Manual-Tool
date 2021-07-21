#!/bin/bash

#Author & Developer
#	FrosT2k5
#		Visit: https://frost2k5.games/


# Colors
RED="\033[1;31m" # For errors / warnings
GREEN="\033[1;32m" # For info
YELLOW="\033[1;33m" # For info
BLUE="\033[1;36m" # For info again XD
NC="\033[0m" # reset color

clear
echo -e "${YELLOW}Welcome to C Source Compiler Manual Tool"
echo -e "Developed by: FrosT2k5 & Quatum Byte Studios
=================================================
	${BLUE}+ https://frost2k5.games/
	${BLUE}+ http://quantumbyteofficial.tech/
${YELLOW}================================================="

echo -en "${GREEN}Enter the C source file path(direct paths are prefferable) : ${NC}"
read filesource

echo -en "${GREEN}Enter the name of your program, it will be used as binary name : ${NC}"
read filepath

gcc ${filesource} -o ${filepath}

echo -e "${GREEN}Gcc compiler ran successfully, Press enter to exit ${NC}"
read wait
