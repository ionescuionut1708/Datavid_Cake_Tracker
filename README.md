# Datavid Cake Tracker

Datavid Cake Tracker este un instrument de management destinat pentru a urmări zilele de naștere ale tuturor membrilor Datavid.

## Descriere

Acest proiect este o aplicație web simplă, construită folosind Flask și SQLAlchemy, care permite adăugarea și gestionarea membrilor unei companii și urmărește zilele lor de naștere. Aplicația asigură că toți membrii au cel puțin 18 ani și că nu există duplicări de nume și locație.

## Funcționalități

- Adăugarea unui membru cu atributele: Prenume, Nume, Data nașterii, Țara, Oraș.
- Validarea tuturor câmpurilor pentru a fi obligatorii.
- Asigurarea unicității combinației de prenume, nume și locație.
- Verificarea ca un membru să aibă cel puțin 18 ani.
- Vizualizarea listei tuturor membrilor.
- Vizualizarea listei membrilor sortați după zilele cele mai apropiate de ziua de naștere.

## Cerințe rulare proiect local

1. **Python 3.x**
2. **pip** - pentru instalarea pachetelor necesare.

## Configurare

1. Clonează acest repository:
    ```bash
    git clone https://github.com/ionescuionut1708/Datavid_Cake_Tracker
    ```
2. Navighează în directorul proiectului:
    ```bash
    cd <numele directorului>
    ```
3. Instalează dependențele necesare:
    ```bash
    pip install -r requirements.txt
    ```
4. Rulează aplicația:
    ```bash
    python app.py
    ```

## API Endpoints

- `GET /` - Ruta de întâmpinare
- `POST /add_member` - Adaugă un nou membru
- `GET /members` - Obține lista tuturor membrilor
- `GET /members/sorted_by_birthday` - Obține membrii sortați după zilele cele mai apropiate de ziua de naștere

## Bug-uri cunoscute

- În cazul în care baza de date nu este inițializată corect, aplicația poate returna erori de conexiune la baza de date.
- Gestionarea erorilor poate fi îmbunătățită pentru a oferi mesaje mai clare în cazul eșecurilor la adăugarea unui membru.

## Vulnerabilități

- Acest proiect este o implementare simplă și nu include măsuri avansate de securitate. Este recomandată integrarea unor mecanisme de autentificare și autorizare pentru utilizarea într-un mediu de producție.
- Validarea input-urilor poate fi extinsă pentru a proteja împotriva atacurilor de tip injection.

## Contribuții

Contribuțiile sunt binevenite! Dacă dorești să contribui la acest proiect, te rugăm să urmezi pașii de mai jos:

1. Fork acest repository.
2. Creează un branch nou pentru funcționalitatea sau bugfix-ul tău:
    ```bash
    git checkout -b nume-branch
    ```
3. Fă commit schimbărilor tale:
    ```bash
    git commit -m "Descrie schimbările tale aici"
    ```
4. Fă push branch-ului:
    ```bash
    git push origin nume-branch
    ```
5. Creează un Pull Request din branch-ul tău către branch-ul principal al repository-ului original.

Te rugăm să te asiguri că respecti ghidurile de stil și contribuție ale proiectului.

