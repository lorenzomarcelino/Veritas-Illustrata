import pytest
from scripts.bible import BibleLoader

EXPECTED_COUNTS = {
    # Antigo Testamento
    "Gênesis": 50,
    "Êxodo": 40,
    "Levítico": 27,
    "Números": 36,
    "Deuteronômio": 34,
    "Josué": 24,
    "Juízes": 21,
    "Rute": 4,
    "I Samuel": 31,
    "II Samuel": 24,
    "I Reis": 22,
    "II Reis": 25,
    "I Crônicas": 29,
    "II Crônicas": 36,
    "Esdras": 10,
    "Neemias": 13,
    "Tobias": 14,
    "Judite": 16,
    "Ester": 16,
    "I Macabeus": 16,
    "II Macabeus": 15,
    "Jó": 42,
    "Salmos": 150,
    "Provérbios": 31,
    "Eclesiastes": 12,
    "Cântico dos Cânticos": 8,
    "Sabedoria": 19,
    "Eclesiástico": 51,
    "Isaías": 66,
    "Jeremias": 52,
    "Lamentações": 5,
    "Baruc": 6,
    "Ezequiel": 48,
    "Daniel": 14,
    "Oséias": 14,
    "Joel": 4,
    "Amós": 9,
    "Abdias": 1,
    "Jonas": 4,
    "Miquéias": 7,
    "Naum": 3,
    "Habacuc": 3,
    "Sofonias": 3,
    "Ageu": 2,
    "Zacarias": 14,
    "Malaquias": 3,
    # Novo Testamento
    "São Mateus": 28,
    "São Marcos": 16,
    "São Lucas": 24,
    "São João": 21,
    "Atos dos Apóstolos": 28,
    "Romanos": 16,
    "I Coríntios": 16,
    "II Coríntios": 13,
    "Gálatas": 6,
    "Efésios": 6,
    "Filipenses": 4,
    "Colossenses": 4,
    "I Tessalonicenses": 5,
    "II Tessalonicenses": 3,
    "I Timóteo": 6,
    "II Timóteo": 4,
    "Tito": 3,
    "Filêmon": 1,
    "Hebreus": 13,
    "São Tiago": 5,
    "I São Pedro": 5,
    "II São Pedro": 3,
    "I São João": 5,
    "II São João": 1,
    "III São João": 1,
    "São Judas": 1,
    "Apocalipse": 22,
}

@pytest.fixture(scope="module")
def bible():
    loader = BibleLoader("data/bible/bibliaAveMaria.json")
    loader.load()
    return loader

def test_all_books_present(bible):
    at_books = bible.get_books("antigoTestamento")
    nt_books = bible.get_books("novoTestamento")

    for name in EXPECTED_COUNTS:
        assert name in at_books + nt_books, f"Falta o livro {name}"

def test_structure_counts(bible):
    bible.validate_structure(EXPECTED_COUNTS)
