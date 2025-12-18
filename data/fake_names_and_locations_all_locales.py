from faker import Faker
locales = [
    "bg_BG",
    "cs_CZ",
    "de_AT",
    "de_DE",
    "dk_DK",
    "el_GR",
    "en_US",
    "es_ES",
    "es_MX",
    "fa_IR",
    "fi_FI",
    "fr_FR",
    "hi_IN",
    "it_IT",
    "ja_JP",
    "ko_KR",
    "lv_LV",
    "ne_NP",
    "nl_NL",
    "no_NO",
    "pl_PL",
    "pt_BR",
    "pt_PT",
    "ru_RU",
    "sl_SI",
    "sv_SE",
    "tr_TR",
    "uk_UA",
    "zh_CN",
    "zh_TW",
]

users = []

with open("./names_and_cities.csv", "w") as f:
    f.write("")

Faker.seed(12345)
for locale in locales:
    for _ in range(10):
        fake = Faker(locale)
        name = fake.name()
        city = fake.city()
        users.append({"name": name, "city": city})
        print(name)
        print(city)
        print("")
with open("./names_and_cities.csv", "a") as f:
    for user in users:
        print(user)
        line = f"{user['name']}, {user['city']}\n"
        f.write(line)

