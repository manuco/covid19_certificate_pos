import datetime
import escpos.printer as ep

def get_printer():
    p = ep.Usb(0x04b8, 0x0e03)

    return p

def print_title(p):
    p.set(font="a")
    p.set(align="center", bold=True, custom_size=True, width=2, height=2, smooth=True)
    p.textln("ATTESTATION DE\nDÉPLACEMENT DÉROGATOIRE")
    p.ln()
    p.set(font="b", align="center")
    p.text("En application de")
    p.text(" l’article ")
    p.text("1er du décret du 16 mars 2020\nportant réglementation des déplacements dans le cadre de\nla lutte contre la propagation du virus Covid-19 :")
    p.ln(2)
    p.set(align="left", font="a")



def print_personnal_informations(p, params):
    if params["gender"] == "male":
        p.text("Je, soussigné\t")
    else:
        p.text("Je, soussignée\t")

    p.set(bold=True)
    p.text(params["name"])
    p.ln()
    p.set()
    if params["gender"] == "male":
        p.text("Né le\t\t")
    else:
        p.text("Née le\t\t")

    p.set(bold=True)
    p.text(params["birthdate"].strftime("%d/%m/%Y"))
    p.ln()
    p.set()
    p.textln("Demeurant")

    p.set(bold=True)
    for line in params["address"]:
        p.text("\t\t")
        p.textln(line)
    p.ln()

def format_testimony(text, prefix_len=0, max_len=48):

    words = text.split()
    lines = []
    line = []
    length = prefix_len
    for word in words:
        length += len(word) + 1
        if length > max_len:
            lines.append(" ".join(line))
            length = prefix_len + len(word) + 1
            line = [word]
        else:
            line.append(word)

    lines.append(" ".join(line))
    return lines

def print_with_prefix(p, text, fl_prefix=""):
    p.text(fl_prefix)
    for line in format_testimony(text, prefix_len=len(fl_prefix)):
        p.textln(line)
        p.text(" " * len(fl_prefix))

kinds = {
    "work": "déplacements entre le domicile et le lieu d’exercice de l’activité professionnelle, lorsqu’ils sont indispensables à l’exercice d’activités ne pouvant être organisées sous forme de télétravail (sur justificatif permanent) ou déplacements professionnels ne pouvant être différés.",
    "shopping": "déplacements pour effectuer des achats de première nécessité dans des établissements autorisés (liste sur gouvernement.fr).",
    "health": "déplacement pour motif de santé.",
    "family": "déplacements pour motif familial impérieux, pour l’assistance aux personnes vulnérables ou la garde d’enfants.",
    "walk": "déplacements brefs, à proximité du domicile, liés à l’activité physique individuelle des personnes, à l’exclusion de toute pratique sportive collective, et aux besoins des animaux de compagnie.",
}


def print_testimony(p, kind):
    p.set()
    print_with_prefix(p, "certifie que mon déplacement est lié au motif suivant autorisé par l’article 1er du décret du 16 mars 2020 portant réglementation des déplacements dans le cadre de la lutte contre la propagation du virus Covid-19 :")
    p.ln()

    p.set(bold=True)
    print_with_prefix(p, kinds[kind], "- ")
    p.ln()

def print_signature(p, params):
    p.set()
    p.text("Fait à :\t")
    p.set(bold=True)
    p.textln(params["location"])
    p.set(bold=False)

    p.set()
    p.text("Le :\t\t")
    p.set(bold=True)
    p.textln(datetime.date.today().strftime("%d/%m/%Y"))
    p.set(bold=False)

    p.ln()

    p.text("Signature :")
    p.ln(7)
    p.set(bold=True, align="right")
    p.text(params["name"])




def print_attestation(params):
    p = get_printer()
    print_title(p)

    print_personnal_informations(p, params)

    print_testimony(p, params["kind"])

    print_signature(p, params)


    p.cut()

if __name__ == "__main__":

    #print_attestation(params={
        #"name": "Emmanuel Coirier",
        #"gender": "male",
        #"birthdate": datetime.date(1982, 8, 19),
        #"address": [
            #"60 avenue Beauséjour",
            #"94230 Cachan",
        #],
        #"kind": "shopping",
        #"location": "Cachan",
    #})

    print_attestation(params={
        "name": "Hélène Séguarra",
        "gender": "female",
        "birthdate": datetime.date(1978, 5, 9),
        "address": [
            "Quelque part dans Paris",
            "75001 Paris",
        ],
        "kind": "walk",
        "location": "Paris",
    })

