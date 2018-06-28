import os
from docx import Document

from .decision_create import (
    add_line,
    application_reason,
    application_subject,
    find_staff,
    line_with_bold,
    normal_center,
    normal_left,
    referent_speech,
    staff_decree
    )
from .styles import my_styles


class Protokol():
    def __init__(self, values):
        self.values = values
        self.document = my_styles(Document())
    
    def create(self):
        normal_center(
            self.document,
            "Protokół Nr    ",
            size=14,
            bold=True
            )
        normal_center(
            self.document,
            "z posiedzenia Zespołu Orzekającego\n"
            " Poradni Psychologiczno – Pedagogicznej\n"
            "w Grodzisku Wlkp. z dnia {}\n".format(self.values['staff_meeting_date']),
            size=12
            )

        line_with_bold(
            self.document,
            "Na wniosek: ",
            self.values['applicant_g']
            )
        add_line(self.document, 10)
        line_with_bold(
            self.document,
            "W sprawie: ",
            "wniosku o wydanie {}".format(
                application_subject(self.values)
                )
            )
        add_line(self.document, 10)
        line_with_bold(
            self.document,
            "Imię i nazwisko: ",
            self.values['name_n']
            )
        add_line(self.document, 10)
        line_with_bold(
            self.document,
            "Data i miejsce urodzenia: ",
            "{}r., {}".format(
                self.values['birth_date'],
                self.values['birth_place']
                )
            )
        add_line(self.document, 10)
        line_with_bold(
            self.document,
            "PESEL: ",
            self.values['pesel']
            )
        add_line(self.document, 10)
        line_with_bold(
            self.document,
            "Adres zamieszkania dziecka: ",
            "{}, {} {}".format(
                self.values['address'],
                self.values['zip_code'],
                self.values['city']
                )
            )
        add_line(self.document, 10)
        line_with_bold(
            self.document,
            "Nazwa i adres przedszkola lub nazwa i adres szkoły oraz" 
            "klasa: ",
            "{}, {}, {}, {}, kl. {}".format(
                self.values['school_name'],
                self.values['school_sort'],
                self.values['school_city'],
                self.values['school_address'],
                self.values['class']
                )
            )
        add_line(self.document, 10)
        staff_decree(
            self.document,
            self.values
            )
        add_line(self.document, 10)
        normal_left(
            self.document,
            "Inne osoby uczestniczące w zespole orzekającym : -"
            )
        add_line(self.document, 10)
        normal_left(
            self.document,
            "Na posiedzeniu Zespół Orzekający przeprowadził postępowanie"
            " orzekające (zapis dyskusji): ",
            size=12
            )
        add_line(self.document, 10)
        normal_left(
            self.document,
            referent_speech(find_staff(self.values, 'psycholog'))
            )
        normal_left(
            self.document,
            referent_speech(find_staff(self.values, 'pedagog'))
            )
        add_line(self.document, 10)
        normal_left(
            self.document,
            "Przeprowadzono głosowanie.\n",
            size=12
            )
        normal_left(
            self.document,
            "Wyniki głosowania:\n"
            "liczba głosów za: \n"
            "liczba głosów przeciw: \n"
            "liczba wstrzymujących się: \n"
            )
        normal_left(
            self.document,
            "W związku z powyższym",
            size=12
            )
        normal_left(
            self.document,
            "Zespół Orzekający orzeka o {}".format(
                ' '.join(application_subject(self.values).split(' ')[2:])
                )
            )
        normal_left(
            self.document,
            "z uwagi na {}".format(application_reason(self.values['reason']))
            )
        normal_left(
            self.document,
            "na czas (w okresie) {}".format(
                self.values['timespan'] + self.values['timespan_ind']
                )
            )
        add_line(self.document, 10)
        normal_left(
            self.document,
            "Przewodniczący Zespołu Orzekającego wyznaczyła osoby, które"
            " sporządzą diagnozę, zalecenia: {}".format(
                find_staff(self.values, "pedagog")[0][0]
                )
            )

    def save(self):
        self.document.save(
            os.path.join(
                './orzeczenia',
                "{} - {} prot.docx".format(
                    self.values['name_n'],
                    self.values['staff_meeting_date']
                    )
                )
            ) 