# spaCy-Features
Main features of the NLP library spaCy

Для работы с библиотекой, её нужно загрузить. Для этого можно воспользоваться одним из трёх способов:
1.	Установка с помощью pip. 
```console
> pip install -U pip setuptools wheel 
> pip install -U spacy
```

2.	Установка с помощью Conda. 
```console
> conda install -c conda-forge spacy
```

3.	Скомпилировать из исходников.
```console
> python -m pip install -U pip setuptools wheel 	  # install/update build tools
> git clone https://github.com/explosion/spaCy  	  # clone spaCy
> cd spaCy                                      	  # navigate into dir
> python -m venv .env                          		  # create environment in .env
> source .env/bin/activate                      		# activate virtual env
> pip install -r requirements.txt               		# install requirements
> pip install --no-build-isolation --editable . 		# compile and install spaCy
```

Пакет, на котором специализируется данный скрипт - __ru_core_news_md__.
Для того, чтобы загрузить пакет достаточно выполнить следующую команду: 
```console
> python -m spacy download ru_core_news_md
```
При запуске скрипта необходимо указать единственный аргумент, отвечающий за функцию, которую по итогу выполнит скрипт.
Пример запуска: 
```console
D:\Projects\PycharmProjects\spaCyFeatures>main.py 1
```
Аргумент может принимать одно из следующих значений:
```console
0 - Displaying information about tokens, 
1 - Vector representation of text tokens, 
2 - Search for text by pattern, 
3 - Identifying the token and assigning the provided attributes to it, 
4 - Named Entity Recognition.
```
