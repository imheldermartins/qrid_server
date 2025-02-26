@echo off
:: Apagar arquivos .pyc, .pyo e diretórios __pycache__
for /r %%i in (__pycache__ *.pyc *.pyo) do (
    del /q "%%i"
)

:: Excluir as pastas __pycache__
for /d /r %%d in (__pycache__) do (
    rd /s /q "%%d"
)

echo Cache cleaned!
