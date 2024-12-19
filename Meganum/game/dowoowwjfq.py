from setuptools import setup, find_packages

setup(
    name="MyGame",  # Название игры
    version="1.0",
    description="A cool Python game",
    author="Ваше Имя",
    author_email="your_email@example.com",
    packages=find_packages(),  # Автоматический поиск пакетов
    include_package_data=True,  # Включение файлов ресурсов
    install_requires=[
        "pygame",
        "PyMySQL",# Укажите ваши зависимости
    ],
    entry_points={
        "console_scripts": [
            "mygame=main:main",  # main.py должен содержать функцию main()
        ],
    },
)