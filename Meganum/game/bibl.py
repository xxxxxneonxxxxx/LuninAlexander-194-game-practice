import subprocess
import sys

def install_requirements():
    try:
        # Установить зависимости из requirements.txt
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("Все зависимости успешно установлены.")
    except Exception as e:
        print(f"Ошибка при установке зависимостей: {e}")
        sys.exit(1)
