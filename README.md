# meteo_Bot_pi
Raspberry: sensore DHT 11 con invio dati su Telegram

Come ben sappiamo il mondo Raspberry permette di creare una moltitudine di progetti interessati. Rispetto ad Arduino con Raspberry è possibile realizzare interfacce di invio dati tramite App su smartphone e PC in quanto l’instaurarsi di una connessione a internet è più semplice rispetto alla board Arduino dal momento che non vi è la necessità di utilizzare shield o componenti particolari per connettersi al proprio router-modem poiché il modulo per la connessione wifi è integrato negli ultimi modelli di Raspberry.

Fase preliminare: idea

In questo articolo sarà illustrato un progetto tramite il quale sarà possibile misurare i valori di temperatura e umidità tramite un sensore di temperatura DHT 11 in un determinato luogo a nostra scelta. La visualizzazione dei dati avverrà tramite l’ausilio di un messaggio di testo inviato da un bot Telgram. Inoltre saranno illustrati in questa guida la metodologia per la creazione del bot su Telegram e di varie estensioni al progetto.

Componenti

Le componenti basilari di questo progetto sono i seguenti:

Board Raspberry PI 3 o 4, connessa a internet
sensore di temperatura DHT 11 (o altri sensori come DHT 22)
Breadboard
3x jumper

![alt text] (https://i0.wp.com/www.moreware.org/wp/wp-content/uploads/2020/12/componenti.png?resize=1024%2C552&ssl=1)

Vi sono altri componenti da poter utilizzare ma sarà visto in seguito nel momento in cui si parlerà delle possibili estensioni.

Sensore DHT 11: datasheet

Il sensore DHT è un  sensore in grado di rilevare umidità e temperatura grazie alle semplici librerie forniteci da Adafruit.

Le specifiche tecniche sono le seguenti:

Range di misurazione: Umidità: 20-90%RH , Temperatura: 0-50°
Accuratezza umiditià: Umiditià ±5％RH
Accuratezza Temperatura: ±2℃
Risoluzione: 1
Alimentazione: 3-5.5v
Attenzione, in alcuni modelli di sensore DHT 11 i pin Vcc e Signal possono essere invertiti. Un eventuale problema per il quale il programma compilato non funzioni potrebbe consistere in questo motivo.

![alt text](https://i0.wp.com/www.moreware.org/wp/wp-content/uploads/2020/12/DHT11-Pinout-for-three-pin-and-four-pin-types-2.jpg?w=1024&ssl=1)

Il sensore DHT11 espone 3 pin denominati:

GND: piedino di massa
VCC: piedino di alimentazione
sitgnal: piedino di comunicazione dati 1-wire
Il DHT11 va alimentato con una tensione compresa tra i 3 e 5V. In che modo rileva l’umidità relativa e la temperatura?  Il DHT11 è in grado di rilevare il valore percentuale dell’umidità relativa misurando la resistenza elettrica tra i due elettrodi. La conduttività tra gli elettrodi aumenta all’aumentare dell’umidità relativa. Mentre per quanto concerne la temperatura il DHT11 utilizza un sensore NTC.

Collegamenti con la board Raspberry

Il piedino signal sarà collegato al pin 7 (GPIO). Il piedino Vcc sarà collegato al pin 2, mentre il pedino GND sarà collegato al pin 6.

ecco qui una schema dei pin GPIO

![alt text](https://i0.wp.com/www.moreware.org/wp/wp-content/uploads/2020/12/Raspberry-Pi-GPIO-Layout-Model-B-Plus-rotated-2700x900-1.png?resize=1024%2C341&ssl=1)

È importante notare che la numerazione in figura è valida solo per i seguenti modelli:

Raspberry Pi Model B+
Raspberry Pi 2B
Raspberry Pi Zero
Raspberry Pi Zero W
Raspberry Pi 3B
Raspberry PI 4
ecco qui il diagramma di collegamento

![alt text](https://i0.wp.com/www.moreware.org/wp/wp-content/uploads/2020/12/How-to-Setup-the-DHT11-on-the-Raspberry-Pi-Three-pin-DHT11-Wiring-Diagram-768x359-1.png?w=768&ssl=1)

Creazione bot

Il primo passo consiste nell’aprire l’applicazione telegram. Una volta aperta cerchiamo “BotFather” tramite la funzione cerca cliccando sull’apposita lente di ingrandimento.

“BotFather” è un bot che permette di creare altri bot.

Avviamo il bot scrivendo “/start“, poi premiamo invio.

![alt text](https://i0.wp.com/www.moreware.org/wp/wp-content/uploads/2020/12/bothfather1.png?w=623&ssl=1)

Per creare un nuovo bot digitiamo “/newbot”.

BotFather ci chiederà di assegnare un nome al nostro nuovo Bot, basta digitare un qualsiasi nome e poi premere Invio.

Dobbiamo anche inserire un username che lo renderà riconoscibile pubblicamente. Username deve terminare in “Bot” o ” _bot”.

In seguito alla assegnazione del nome e dell’username BotFather ci comunicherà informazioni importanti in seguito per compilare il codice per il funzionamento del sensore e dell’invio dati. ATTENZIONE: QUESTE INFOMAZIONI LE DOVREMMO TENERE SOLO PER NOI. La prima parte riguarda il percorso per trovare il nostro bot. La seconda è la API che sarà utilizzato nel nostro codice.

![alt text](https://i0.wp.com/www.moreware.org/wp/wp-content/uploads/2020/12/botfather2.png?w=618&ssl=1)

Operazioni preliminari per la programmazione del codice su Raspberry

Per utilizzare il sensore dobbiamo scaricare la libreria Adafruit. Digitiamo sul terminale la seguente stringa:

`sudo apt-get install git-core`

Se da errore provare ad utilizzare la stringa `sudo apt-get update` e riprovare.

Installiamo la libreria utilizzando la seguente stringa:

`git clone https://github.com/adafruit/Adafruit_Python_DHT.git`

Cambiamo directory con la seguente stringa:

`cd Adafruit_Python_DHT`

Ora digitiamo;

`sudo apt-get install build-essential python-dev`

e installiamo la libreria con:

`sudo python setup.py install`

Tutto questo per il funzionamento del sensore DHT 11. Per l’implementazione del bot occorre una specifica libreria. Per installare questa libreria basta eseguire il comando (prima usciamo dalle eventuali directory digitando cd).

`pip install telepot`

Codice completo

Ecco il codice in python che permette di leggere i dati dal sensore e inviarli tramite messaggio di testo tramite il bot creato da noi.

Per far si che i miei passaggi corrispondano con quelli degli esempi seguenti è consigliabile creare un nuovo file dal nome “simple_bot_DHT.py” nella cartella “examples” contenuta a sua volta nella cartella “Adafruit_Python_DHT”.

Ecco qui il codice: https://github.com/SimoneMoreWare/meteo_Bot_pi/blob/main/dht_bot.py
Maggiori dettagli https://www.moreware.org/wp/blog/2020/12/13/raspberry-sensore-dht-11-con-invio-dati-su-telegram/

per testare il programma dobbiamo utilizzare il terminale usando diversi comandi:


`cd Adafruit_Python_DHT
cd examples
python simple_bot_DHT.py`

Una volta comparsa nel terminale la scritta “listeling…” apriamo la chat telegram ed iniziamo a messaggiare con il nostro bot.

![alt text](https://i0.wp.com/www.moreware.org/wp/wp-content/uploads/2020/12/fd13d4a7-589f-4704-a59b-d2bff4a4f40e.jpg?resize=461%2C1024&ssl=1)

Per chiudere il programma basta premere i pulsanti ctrl-C dal terminale.

Possibili estensioni

Vi sono tantissime estensioni per quanto riguarda questo progetto. Una tra le tante è l’uso di una cassetta di  derivazione in plastica al cui interno è inserita la board Raspberry alimentato da un power bank. In questo sarà possibile inserire questa cassetta nel balcone della propria abitazione (la board deve essere connessa a internet) e osservare in che modo i dati cambino durante il corso della giornata.

![alt text](https://i0.wp.com/www.moreware.org/wp/wp-content/uploads/2020/12/61tdjhkS06L._AC_SL1103_.jpg?w=1024&ssl=1)

Inoltre è possibile anche realizzare una “piccola stazione meteo” dotata di più componenti come un barometro BME280 che ci permette di misurare la pressione.

![alt text](https://i0.wp.com/www.moreware.org/wp/wp-content/uploads/2020/12/bme280-barometersensor-temperatur-luftdruck-luftfeuchtigkeit-rapsberry-pi-arduino-arduino-7483-700x700-1.jpg?w=700&ssl=1)

Vi è data anche la possibilità di salvare i dati in locale sulla propria board Raspberry tramite l’utilizzo dei File. Vi è un tutorial del nostro caro Luigi Morelli a riguardo: [Pillole di Python #020 – Files e persistenza](https://www.youtube.com/watch?v=944w5KtysjY&list=PLn67k_7YnLzLPSYykxZwyjFi3SSZ4EQwf&index=22)

Componenti utilizzati

Board Raspberry PI 3 o 4,Modello B+
Sensore di temperatura e umidità DHT 11
Breadboard
Jumper
Cassetta di Derivazione da Parete esterna
Barometro BME280

https://www.youtube.com/watch?v=Mgut50-7D10
