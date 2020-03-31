# YuGiOh-Python-Proxies
A YuGiOh Proxies Generator based on @Linseneintopf 's [ygo-proxy-generator](https://github.com/Linseneintopf/ygo-proxy-generator)

## How to use
Place either `decklist.ydk` or `decklist.txt` in the directory, see the files for the exact formating
Run `proxies.py`
It will
- create the `decklist.txt` if needed
- download the missing images
- run `proxies.tex` to created `proxies.pdf`, which contains the proxies

## Requirement
To use you need
- python
- pdflatex

Was tested on MacOS, I don't know if it will work on Windows or Linux
