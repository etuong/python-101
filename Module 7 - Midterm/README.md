# Ethan Thomas Uong, euong1

## _Module 7 - Midterm_

### OCT 17, 2021

#### Python Version: 3.8.0

#### PyCharm IDE, Community Edition Version 2021.2.1

---

## Run Programs

```
python freq_analysis.py
```

## Approach

I knew I had to manage two dictionaries - one to store the frequencies of the encrypted message characters and their
count and another dictionary to manage the frequency count for each character as it appears in the decrypted message

I opened and parsed the two files into their respective dictionaries. After that, my approach was to loop through each
character at a time but rely on the frequency dictionary to extract the corresponding shifted decrypted character.

The tricky part here is that there could be more than one character associated to the frequency count, so to remediate
this I wanted to break out of the dictionary loop as soon as the first character is found. The rest is manually decipher
by hand. This approach is practically reasonable because in real life, and given a random arbitrary string, it's most
likely uncommon for characters to have the same frequency count.

## Known Bugs

- N/A

## Hand Calculation

The encrypted message is "sajvs aovyu hyl aol vzz hnluaz tllapun pu aol ylhy vm zhpua thyfz zvbao jobyjo hmaly ylhy
hktpyhs ztpao ylabyuz myvt opz ayhcls hiyvhk av thbypahuph mvy vwlyhapvu psspjpazjlua"

The semi-complete decrypted message from my program is "mtcom thorn are the oss agents meeting in the rear of saint
marys softh chfrch after rear agmiram smith retfrns from his trayem ayroag to mafritania for oyeration immicitscent
"

The following common characters and their count are used to hand fix the message.

* 6: m,l
* 4: f,u
* 2: g,d
* 1: y,v,b,p

The complete decypted message is **"LtCol thorn are the OSS agents meeting in the rear of Saint Marys south church after
Rear Admiral Smith returns from his travel abroad to Mauritania for operation Illicitscent"**