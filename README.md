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


## Programátorská dokumentace hry Wordle
### RANDOM
Nejprve importujeme modul **_random_**, který je nutný k náhodnému výběru slov pro hádání.
### SLOVNÍK
Dále potřebujeme mít nějaký seznam slov, ze kterého bude hra slova vybírat. 
-	Proto jsem si stáhl z internetu seznam nejpoužívanějších anglických slov a pak z nich vybral pouze ta pětimístná.
-	Vytvoříme tak soubor **possible_words.txt** 
### WORDLE
#### 1.	**Načtení slovníku**

Vytvoříme funkci **_load_words(file_path)_**, pomocí které program otevře soubor **possible_words.txt** a z jednotlivých slov ve slovníku vytvoří seznam – **words**.


#### 2.	**Zkoumání jednotlivých písmen a poskytnutí nápovědy**
   
Funkce **_check_place(guess, wordle)_** nám bude sloužit při zkoumání slova daného hráčem.

-	Jejím výstupem bude seznam **feedback**, který bude obsahovat nápovědy
-	Parametr **guess** reprezentuje dané slovo hráčem a parametr **wordle** zas hledané slovo náhodně vybrané hrou 
-	Funkce postupně porovnává písmena na stejných pozicích těchto dvou parametrů
  
    -	Pokud jsou na stejných pozicích stejná písmena, do výsledného seznamu **feedback** se uloží pozice, písmeno a zpráva, že je písmeno na SPRÁVNÉM, tedy stejném, místě
      
    -	Pokud jsou na stejné pozici jiná písmena, ale písmeno se v hledaném slově nachází (in **wordle**), do výsledného seznamu **feedback** se uloží pozice, písmeno a zpráva, že je písmeno na ŠPATNÉM místě
      
    -	Pokud se písmeno v hledaném slově nenachází vůbec, do seznamu **feedback** se neuloží nic
-	Např:
    -	guess = PLANE, wordle = APPLE => check_place(guess, wordle) 

=>	 feedback = [“1. Letter – P: WRONG place”, „2. Letter – L: WRONG place”, “3. Letter – A: WRONG place”, “5. Letter – E: RIGHT place”]

-	Funkce vrací seznam **feedback**
  

#### 3.	**Kontrola správného formátu zadaných slov**
   
Funkce **_get_valid_guess()_** kontroluje, zda je slovo zadané hráčem (**guess**) validní, tedy jestli je pětimístné.

-	Kontrola je umožněna while cyklem, který končí v momentě, kdy je zadáno validní slovo.
-	Nejprve vyzveme hráče, aby zadal slovo. Toto slovo uložíme do proměnné **guess**. Pak následuje kontrola:
  
    -	Pokud slovo není pětimístné, vrací program zprávu: _"That was not a five letter word!"_ a cyklus pokračuje
      
    -	Pokud slovo je pětimístné, je validní a tedy jej můžeme použít. Cyklus je zastaven.
      
-	Funkce vrací proměnnou **guess**, tedy validní slovo
  

#### 4.	**Samotná hra**
   
Nejprve využijeme funkci **_load_words(„possible_words.txt“)_** a vytvoříme tak seznam slov -  **words**.

Poté s pomocí příkazu **_random.choice(words)_** z tohoto seznamu do proměnné **wordle** uložíme náhodně vybrané slovo. Toto slovo chce hráč uhodnout.

Uživatel má šest pokusů na to, aby slovo uhádl, proto vytvoříme while cyklus, který se zastaví po šestém pokusu, a nebo v případě, že hráč slovo uhodne.

Následuje výzva hráče k hádání. Využijeme funkci **_get_valid_guess()_** a obdržíme tak od uživatele validní slovo, které uložíme do proměnné **guess**.

Pokud je **guess** stejné jako **wordle**, hráč vyhrál. Program mu tuto skutečnost sdělí pomocí zprávy _„You won!“_ a poté ukončí cyklus – break.

Jinak použijeme funkci **_check_place(guess, wordle)_**, která postupně srovná písmena obou parametrů **guess** a **wordle** na první až na páté (poslední) pozici. Hráč tak dostane nápovědy a hádá znovu.

V momentě, kdy dojdou všechny pokusy a slovo není stále uhodnuto -  cyklus skončil přirozeně, uživatel prohrává. Program vytiskne zprávu _„You lost!“_  a sdělí správnou odpověď: _„The right answer was: {wordle} “_

Konec programu

