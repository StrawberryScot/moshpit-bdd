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
    "lt_LT",
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
Faker.seed(12345)
for num in range(200):
    fake = Faker(locales)
    name = fake.name()
    print(name)
