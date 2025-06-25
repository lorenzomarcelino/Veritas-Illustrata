# scripts/bible.py

import json
from pathlib import Path

class BibleLoader:
    def __init__(self, path: str):
        self.path = Path(path)
        self.data = {}

    def load(self):
        with self.path.open(encoding="utf-8") as f:
            self.data = json.load(f)

    def get_books(self, testament: str) -> list[str]:
        return [b["nome"] for b in self.data[testament]]

    def validate_structure(self, expected: dict[str, int]) -> None:
        for testament, books in self.data.items():
            for book in books:
                name = book["nome"]
                assert name in expected, f"Livro inesperado: {name}"
                cap_count = len(book["capitulos"])
                assert cap_count == expected[name], (
                    f"{name} deveria ter {expected[name]} capítulos, mas tem {cap_count}"
                )
                for cap in book["capitulos"]:
                    assert cap["versiculos"], (
                        f"{name} capítulo {cap['capitulo']} sem versículos"
                    )

if __name__ == "__main__":
    loader = BibleLoader("data/bible/bibliaAveMaria.json")
    loader.load()
    at = len(loader.get_books("antigoTestamento"))
    nt = len(loader.get_books("novoTestamento"))
    print(f"Antigo: {at} livros, Novo: {nt} livros")