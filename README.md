# devasc-study-team
Working together to pass the DEVASC exam

Lab 1 - Python Experiments 
• Task preparation and implementation: 
  Het iso bestandje gedownload van netacad om zo de vm aan te maken  
• Task troubleshooting:  
  Bij de eerste installatie lukte het niet om jupyter notebook te installeren ik heb toen een nieuwe vm aangemaakt en nu werkt het wel. Voor de idle moest ik eerst een sudo apt get-update doen
• Task verification:  
  voor python3 is dit python3 - -version, voor pip is dit pip - - version, voor visual studio code is dit code - - version, jupyter notebook - -  version, voor python idle is het type idle in de zoekbalk en dan zie je de     versie staan

Lab 2 - Explore rest apis with API-simulator and postman
• Task preparation and implementation:
  DEVASC Virtual Machine, Virtual Box or VMWare, 1 PC with operating system of your choice
• Task troubleshooting:
  import request moest apart gedownload worden 
• Task verification:
  POST, GET, DELETE, PUT, python3

Lab 3 - Python Review - Development tools and Classes
• Document your findings and important commands:
  Python3 -V = python versie
  Which python3 = locatie python
  Python3 -m venv devfun = aanmaken virtual environment en de -m laat de venv runnen 
  Source devfun/bin/activate = activeert de virtual environment 
  Pip3 freeze = laat zien welke packages er geinstalleerd zijn 
  Pip3 install requests = installeert python requests packages 
  Deactivate = zet de virtual environment uit
  Pip3 freeze > requirements.txt = zet de uitkomst van freeze in dit bestand 
  Pip3 install -r requitements.txt = install dit bestand op een nieuwe virtual envirment 

Lab 4 - Network Infrastructure and troubleshooting
• Install and configure your lab test environment according to the network drawing and instructions. This lab must be executed on hardware.
  Netwerk tekening is te vinden in de map van lab 4 samen met de configuratie van de router en switch

Lab 6 - Python Network automation with netmiko
• Document your findings and important commands.
    'device_type': ,
        'ip': ,
        'username': ,
        'password': ,
        'show version', 'show interfaces', 'show ip route'
        
Lab 7 - YANG, NETCONFIG and RESTCONFIG
• Document your findings and important commands.
Werkte niet in virtualbox en wel in vmware. Ik had de ova en de iso file nodig voordat het werkte. 
De vmnet moest aangepast worden naar bridged en na lang zoeken is de fout gevonden waarom ik niet kon pingen. De vm selecteerde de verkeerde netwerkkaart van mijn computer waardoor ik niet naar buiten kon pingen. 
