# Open Education Global Multilingual  
### Description  
This projet is a multilingual project deployed at the [Open Education Global 2022 Conference](https://www.oeglobal.org/) in Nantes. The goal is to break language barrier and allow a congres to be multilingual.   
The language taken into account this year is: *Arabic*, *English*, *French*, *Spanish*  
The [application](https://multiling-oeg.univ-nantes.fr/) transcribe a voice streaming input of the current talk, translate the transcription and generate a word cloud based first on the abstract of the current talk and then on the transcribed and the translated text for each language supported.  
WordCloud generated, transcription and translation is send to the website API developped through a dictionnary which is stored in a Database.  
### Repository organisation:
This repository is only for the website part
#### Technologies used:
The website have been developped using the micro Python frameword [Flask](https://flask.palletsprojects.com/en/2.1.x/)
(needs python >= 3.7)
#### Challenges: (:thinking:)

### Installation and Usage:  
This project can be used adaptively, you can use the word cloud generation part on its own, or you can use the transcription part on its ownn, or the translation part on its own or you can use them all together with another website by providing the website API routes where it's required.  
For sake of simplicity, you can use the website deployed with the application.  
For installation please use installer:   
Unix :
./setup.sh
Windows:
./setup.ps1

Prerequesites :
Python >= 3.7

For usage, run :
Unix :
./run.sh
Windows:
./run.ps1

### Licences:
This project is [CC BY](https://creativecommons.org/licenses/by/4.0/)  
