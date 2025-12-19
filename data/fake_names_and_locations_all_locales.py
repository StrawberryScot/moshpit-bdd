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

# Map locales to their countries in native language
locale_to_native_country = {
    "bg_BG": "България",           # Bulgaria
    "cs_CZ": "Česká republika",    # Czech Republic
    "de_AT": "Österreich",         # Austria
    "de_DE": "Deutschland",        # Germany
    "dk_DK": "Danmark",            # Denmark
    "el_GR": "Ελλάδα",            # Greece
    "en_US": "United States",      # United States
    "es_ES": "España",             # Spain
    "es_MX": "México",             # Mexico
    "fa_IR": "ایران",             # Iran 
    "fi_FI": "Suomi",              # Finland
    "fr_FR": "France",             # France
    "hi_IN": "भारत",              # India 
    "it_IT": "Italia",             # Italy
    "ja_JP": "日本",               # Japan
    "ko_KR": "대한민국",            # South Korea
    "ne_NP": "नेपाल",              # Nepal
    "nl_NL": "Nederland",          # Netherlands
    "no_NO": "Norge",              # Norway
    "pl_PL": "Polska",             # Poland
    "pt_BR": "Brasil",             # Brazil
    "pt_PT": "Portugal",           # Portugal
    "ru_RU": "Россия",             # Russia
    "sl_SI": "Slovenija",          # Slovenia
    "sv_SE": "Sverige",            # Sweden
    "tr_TR": "Türkiye",            # Turkey
    "uk_UA": "Україна",            # Ukraine
    "zh_CN": "中国",               # China 
    "zh_TW": "台灣",               # Taiwan 
}

users = []

Faker.seed(12345)
for locale in locales:
    fake = Faker(locale)
    country = locale_to_native_country.get(locale, "-")

    for _ in range(10):
        name = fake.name()
        city = fake.city()

        users.append({"name": name, "city": city, "country": country})
        print(name)
        print(city)
        print(country)
        print("")

with open("./names_cities_countries.csv", "a", encoding='utf-8') as f:
    for user in users:
        print(user)
        line = f"{user['name']}, {user['city']}, {user['country']}\n"
        f.write(line)
