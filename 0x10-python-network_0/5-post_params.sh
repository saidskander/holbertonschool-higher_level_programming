#!/bin/bash
# Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response
curl "$1" -sd "email=hr@holbertonschool.com&subject=I%20will%20always%20be%20here%20for%20PLD"
