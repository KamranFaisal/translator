# language_translator.py

import streamlit as st
from googletrans import Translator

def translate_text(text, target_language):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

def main():
    st.title("Language Translator")

    # Input text to translate
    input_text = st.text_area("Enter text to translate:", height=150)

    # Select target language
    target_language = st.selectbox("Select target language:", ["English", "Spanish", "French", "German", "Chinese (Mandarin)", "Japanese", "Korean", "Hindi", "Arabic", "Russian",
"Portuguese", "Italian", "Dutch", "Swedish", "Turkish", "Bengali", "Punjabi", "Urdu", "Gujarati", "Telugu",
"Marathi", "Tamil", "Vietnamese", "Tagalog", "Thai", "Malay", "Burmese", "Indonesian", "Farsi", "Hausa",
"Yoruba", "Igbo", "Zulu", "Swahili", "Somali", "Amharic", "Oromo", "Tigrinya", "Haitian Creole", "Sundanese",
"Filipino", "Javanese", "Maithili", "Uzbek", "Sindhi", "Malagasy", "Nepali", "Sinhala", "Khmer", "Lao",
"Hmong", "Maori", "Tongan", "Samoan", "Fijian", "Marshallese", "Chamorro", "Palauan", "Chukese", "Yapese",
"Nauruan", "Kosraean", "Kiribati", "Tahitian", "Hawaiian", "Rapa Nui", "Niuean", "Tok Pisin", "Hiri Motu",
"Solomon Islands Pijin", "Bislama", "Rotuman", "Nakanai", "Tolai", "Kuanua", "Kiriwina", "Tokelauan",
"Tuvaluan", "Nukuoro", "Kapingamarangi", "Nauruan", "Pingelapese", "Mokilese", "Ngatikese", "Belarusian",
"Bislama", "Bosnian", "Breton", "Bulgarian", "Catalan", "Chechen", "Chichewa", "Chinese", "Chuvash",
"Cornish", "Corsican", "Cree", "Croatian", "Czech", "Danish", "Divehi", "Dzongkha", "Esperanto", "Estonian",
"Ewe", "Faroese", "Finnish", "Fula", "Galician", "Georgian", "Greek", "Greenlandic", "Guarani", "Haitian Creole",
"Hebrew", "Herero", "Hungarian", "Icelandic", "Ido", "Indonesian", "Interlingua", "Interlingue", "Inuktitut",
"Inupiaq", "Irish", "Italian", "Kalaallisut", "Kannada", "Kanuri", "Kashmiri", "Kazakh", "Kikuyu", "Kinyarwanda",
"Kirghiz", "Komi", "Kongo", "Kurdish", "Kwanyama", "Lao", "Latin", "Latvian", "Limburgish", "Lingala",
"Lithuanian", "Luba-Katanga", "Luxembourgish", "Macedonian", "Malagasy", "Malay", "Malayalam", "Maltese",
"Manx", "Maori", "Marathi", "Marshallese", "Moldavian", "Mongolian", "Nauruan", "Navajo", "Ndonga", "North Ndebele",
"Northern Sami", "Norwegian", "Nuosu", "Occitan", "Ojibwe", "Old Church Slavonic", "Oriya", "Oromo", "Ossetian",
"Pāli", "Pashto", "Persian", "Polish", "Portuguese", "Quechua", "Romanian", "Romansh", "Samoan", "Sango",
"Sanskrit", "Serbian", "Serbo-Croatian", "Sesotho", "Setswana", "Shona", "Sichuan Yi", "Sindhi", "Slovak",
"Slovenian", "Somali", "South Ndebele", "Southern Sotho", "Spanish", "Sundanese", "Swahili", "Swati", "Swedish",
"Tagalog", "Tahitian", "Tajik", "Tamil", "Tatar", "Telugu", "Thai", "Tibetan", "Tigrinya", "Tonga", "Tsonga",
"Tswana", "Turkish", "Turkmen", "Twi", "Uighur", "Ukrainian", "Urdu", "Uzbek", "Venda", "Vietnamese", "Volapük",
"Walloon", "Welsh", "Western Frisian", "Wolof", "Xhosa", "Yiddish", "Yoruba", "Zhuang", "Zulu"
])

    # Translate button
    if st.button("Translate"):
        if input_text:
            translated_text = translate_text(input_text, target_language)
            st.success(f"Translated Text ({target_language}): {translated_text}")
        else:
            st.warning("Please enter text to translate.")

if __name__ == "__main__":
    main()
