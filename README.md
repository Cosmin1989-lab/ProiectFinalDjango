Aceasta este o aplicație de administrare bloc (asociație de proprietari) dezvoltată în Django, care permite gestionarea eficientă a facturilor, avizierului, și a datelor fiecărui locatar. Fiecare client (locatar) are acces securizat la contul său, unde poate vizualiza informațiile personale legate de cheltuielile de întreținere și notificările din avizier.

Funcționalități principale:
Dashboard personalizat pentru locatari: Fiecare utilizator are un cont propriu, unde poate accesa facturile curente și istoricul plăților.
Gestionarea facturilor: Administrarea facturilor comune pentru întreținere, apă, gaze, și alte cheltuieli de bloc. Posibilitatea de a marca facturile ca plătite.
Avizier online: Posibilitatea de a publica anunțuri pentru locatari direct în platformă (ex: notificări despre reparații, anunțuri de interes general).
Autentificare securizată: Fiecare locatar are acces doar la informațiile sale, folosind un sistem de autentificare sigur (Django Auth).
Roluri de utilizatori: Administratorul are acces complet pentru gestionarea locatarilor, facturilor și anunțurilor, în timp ce utilizatorii obișnuiți (locatarii) au acces limitat la propriile date.
Raportare și istorice: Posibilitatea de a genera rapoarte cu cheltuielile lunare sau anuale pentru fiecare locatar.
Tehnologii utilizate:
Backend: Django (Python)
Frontend: HTML, CSS, JavaScript (Django Templates)
Bază de date: PostgreSQL / SQLite (configurabil)
Autentificare și Autorizare: Django Auth
API REST: Django Rest Framework (opțional, pentru extinderea funcționalităților)
