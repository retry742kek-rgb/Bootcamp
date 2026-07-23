import csv
import hashlib
import shutil
from pathlib import Path

FOLDER = Path("downloads")

CATEGORIES = {
    "Изображения": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".heic", ".bmp"],
    "Музыка": [".mp3", ".wav", ".flac", ".m4a", ".ogg"],
    "Видео": [".mp4", ".mov", ".avi", ".mkv", ".webm"],
    "Документы": [".pdf", ".docx", ".doc", ".txt", ".rtf", ".xlsx", ".pptx", ".csv"],
    "Программы": [".exe", ".msi", ".dmg", ".apk"],
    "Архивы": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Код": [".py", ".js", ".html", ".css", ".json"],
}


def get_files():
    """Все файлы в папке. Папки пропускаем."""
    return [f for f in FOLDER.iterdir() if f.is_file()]


def get_category(file):
    """Определяет категорию по расширению."""
    for category, extensions in CATEGORIES.items():
        if file.suffix.lower() in extensions:
            return category
    return "Прочее"


def count_duplicates():
    """Считает, сколько файлов являются копиями."""
    pass


def analyze():
    pass


def sort_files():
    for file in get_files():
        folder = FOLDER / get_category(file)
        folder.mkdir(exist_ok=True)
        target = folder / file.name
        if not target.exists():
            shutil.move(file, target)

    print("\nГотово! Теперь в папке:\n")
    for folder in sorted(FOLDER.iterdir()):
        if folder.is_dir():
            print(f"  {folder.name}/  ({len(list(folder.iterdir()))} шт)")



def save_report():
    pass


def delete_duplicates():
    pass


def main():
    while True:
        print("\n" + "=" * 35)
        print("  1 - Проанализировать папку")
        print("  2 - Разложить по папкам")
        print("  3 - Сохранить отчёт")
        print("  0 - Выход")
        print("=" * 35)

        choice = input("Твой выбор: ").strip()

        if choice == "1":
            analyze()
        elif choice == "2":
            sort_files()
        elif choice == "3":
            save_report()
        elif choice == "0":
            break
        else:
            print("Нет такого пункта")


main()
