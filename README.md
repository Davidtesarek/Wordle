# Wordle
Zápočtový program, hra Wordle 

## Uživatelská dokumentace hry Wordle
### Cíl hry Wordle
Cílem hry je uhodnout pětimístné anglické slovo během šesti pokusů.
### Co potřebujeme ke spuštění? 
Ke spuštění hry jsou potřeba dva soubory: samotná hra Wordle a slovník pětimístných anglických slov, z něhož si hra náhodně vybírá slovo, které bude hráč hádat.

Po spuštění kódu v pythonu hra ihned začíná.
### Jak hrát?   
Na obrazovce se zobrazí nápis _Guess the word!:_ a hráč začíná hádat – napíše pětimístné anglické slovo.

Jestliže slovo uhodl, hráč vyhrál a hra končí. 

Pokud neuhodl, hra mu napoví a hráč může hádat znovu.
### Jak funguje nápověda?
-	Kód prošetří jednotlivě všechna písmena hráčem zadaného slova a vrátí o nich pomocné informace. Pokud se písmeno v hledaném slově:
    -	nachází a je na správné pozici, sdělí hra tuto skutečnost hráči textem RIGHT place
    -	nachází, ale je na špatné pozici, objeví se text WRONG place
    -	nenachází, nesdělí o něm hra nic

V případě, že hráčem zadané slovo není pětimístné nebo toto slovo neexistuje, hra hráče na chybu upozorní a pokus je opakován. 

Pokud se hráči do šesti pokusů nepodaří slovo uhodnout, prohrál a hra končí.
### Příklad hry
Guess the word!: 	APPLE

- 4.letter - L: WRONG place

Guess the word!:	LIGHT

- 1.letter - L: WRONG place

- 2.letter - I: WRONG place

Guess the word!:	IDEAL

- 1.letter - I: WRONG place

- 2.letter - D: WRONG place

- 5.letter - L: WRONG place

Guess the word!:	BUILD

- 2.letter - U: WRONG place.

- 3.letter – I: WRONG place.

- 4.letter - L: WRONG place.

- 5.letter - D: RIGHT place

Guess the word!: FLUID

You won!

