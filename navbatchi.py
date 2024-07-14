from datetime import datetime, timedelta
navbatchilar = ["Navbatchi 1", "Navbatchi 2", "Navbatchi 3", "Navbatchi 4", "Navbatchi 5"]
oy_boshlanish = datetime(2024, 7, 11)
oy_tugash = datetime(2024, 7, 31)
jadval = {}
kun_soni = (oy_tugash - oy_boshlanish).days + 1
hafta_kunlari = ["Dushanba", "Seshanba", "Chorshanba", "Payshanba", "Juma", "Shanba", "Yakshanba"]
for kun in range(kun_soni):
    sana = oy_boshlanish + timedelta(days=kun)
    hafta_kuni = hafta_kunlari[sana.weekday()]
    navbatchi = navbatchilar[kun % len(navbatchilar)]
    jadval[sana.strftime("%Y-%m-%d")] = (hafta_kuni, navbatchi)
for sana, (hafta_kuni, navbatchi) in jadval.items():
    print(f"{sana} ({hafta_kuni}): {navbatchi}")