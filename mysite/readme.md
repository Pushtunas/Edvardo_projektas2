# Aplikacija "Užrašinė" (Django)

Paprasta užrašinės tipo aplikacija su vartotojo prisijungimu.

### Nustatymai aplikacijos paleidimui su nauja DB:

1. `virtualenv venv`
1. `source venv/Scripts/activate` arba `source venv/bin/activate`
1. `pip install -r requirements.txt`
1. `python manage.py migrate`
1. `python manage.py createsuperuser` (sekite pranešimus)
1. `python manage.py runserver `

### Nustatymai aplikacijos paleidimui naudojant esamą DB:

1. `virtualenv venv`
1. `source venv/Scripts/activate` arba `source venv/bin/activate`
1. `pip install -r requirements.txt`
1. `python manage.py runserver `

#### Demo vartotojas:
Vardas: `vartotojas` Slaptažodis: `slaptazodis`

#### Administratoriaus prisijungimas:

http://127.0.0.1:8000/admin

Vardas: `admin` Slaptažodis: `admin`

### Nuotraukos
![](https://img001.prntscr.com/file/img001/qNgpG4YmToakoqDsPndGJA.png "Registracijoas langas")
![](https://img001.prntscr.com/file/img001/n0XOnajPSVOnjIJG1pIOEA.png "Pagrindinis langas")
![](https://img001.prntscr.com/file/img001/6tpLzV6iR-q_vlZfym-adA.png "Pridėti įrašą")

