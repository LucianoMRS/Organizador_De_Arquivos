## Organização de arquivos em Python

O código utiliza as bibliotecas **`pathlib`**, **`datetime`** e **`shutil`** para organizar arquivos de acordo com suas extensões. O método `iterdir()` percorre os arquivos da pasta, enquanto `exists()` verifica se a subpasta de destino já existe e `mkdir()` cria essa subpasta quando necessário.

A função `shutil.copy2()` copia os arquivos para suas respectivas subpastas. Já `datetime.now()` obtém a data e o horário atuais, `strftime()` formata essas informações e `write()` registra a operação no arquivo de log.

Também são utilizados os seguintes atributos:

- `suffix`: obtém a extensão do arquivo;
- `name`: obtém o nome completo do arquivo.
