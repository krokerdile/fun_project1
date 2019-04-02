#!/bin/bash
LIST=()

while [[ 1 ]] 
        do
                echo -e "Enter a new word: "
                read word

                if [[ $word == "list" ]]
                        then
                                echo ${LIST[*]}
                elif [[ $word == "quit" ]]
                        then
                                exit 0
                else
                        LIST+=($word)
                        echo "Length: " ${#LIST[*]}
                fi
        done
