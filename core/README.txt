# Créer des instances d'employés
employe1 = Employe.objects.create(
    nom="Farid",
    prenom="ELGOUMARI",
    email="mohammed.ali@example.com",
    jours_de_travail="LMTWTF",
    demi_jour_mercredi=True,
    nombre_jours_de_travail=6,
)
employe2 = Employe.objects.create(
    nom="Abdelhamid",
    prenom="BOULILA",
    email="fatima.zakaria@example.com",
    jours_de_travail="LMTWTF",
    demi_jour_mercredi=True,
    nombre_jours_de_travail=6,
)
employe3 = Employe.objects.create(
    nom="Elyazid",
    prenom="MAAROUFI",
    email="ahmed.bensouda@example.com",
    jours_de_travail="LMTWTF",
    demi_jour_mercredi=False,
    nombre_jours_de_travail=6,
)
employe4 = Employe.objects.create(
    nom="Abdelmalek",
    prenom="ELFAIR",
    email="amina.lahlou@example.com",
    jours_de_travail="LMTWTF",
    demi_jour_mercredi=False,
    nombre_jours_de_travail=6,
)
employe5 = Employe.objects.create(
    nom="Abdelwahed",
    prenom="AITKHIRA",
    email="omar.driss@example.com",
    jours_de_travail="LMTWTH",
    demi_jour_mercredi=False,
    nombre_jours_de_travail=5,
)


# Créer des utilisateurs pour chaque employé
for employe in Employe.objects.all():
    user = User.objects.create_user(employe.nom, employe.email)
    user.save()

