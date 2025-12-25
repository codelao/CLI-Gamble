#!/bin/bash

export LC_CTYPE=en_US.UTF-8
clear

banner() {
printf " .=============-\  .=============-\ \n" 
printf " |             ||  |             || \n"
printf " |  ●          ||  |   ●     ●   || \n"
printf " |             ||  |             || \n"
printf " |      ●      ||  |   ●     ●   || \n"
printf " |             ||  |             || \n"
printf " |          ●  ||  |   ●     ●   || \n"
printf " |_____________#/  |_____________#/ \n"
printf "       CLI              GAMBLE      \n"
printf "~[\$\$\$__________by Lao__________\$\$\$]~\n"
}


installation() {
	if python3 --version && pip3 --version && git --version; then
		if ! (git clone https://github.com/codelao/CLI-Gamble.git && 
			pip3 install CLI-Gamble/.); then
			return 1
		else
			rm -rf CLI-Gamble
			return 0
		fi
	else
		return 1
}


if [ "$1" = "--quiet" ]; then
    exec 3>&1 4>&2
    exec >/dev/null 2>&1
elif [ "$1" = "" ]; then
	banner
else
	printf "\033[31m[!]\033[0m Unknown argument(s).\n"
	exit 1
fi

if installation; then
	if [ "$1" = "--quiet" ]; then
		exec 1>&3 2>&4
		exec 3>&- 4>&-
	fi
	printf "\033[32m[!]\033[0m Installed successfully.\n"
	exit 0
else
	if [ "$1" = "--quiet" ]; then
		exec 1>&3 2>&4
		exec 3>&- 4>&-
	fi
	printf "\033[31m[!]\033[0m The installation wasn't successful.\n"
	exit 1
fi
