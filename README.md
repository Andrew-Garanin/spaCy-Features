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

Пакет, на котором специализируется данный скрипт - __<span style="color:blue">ru_core_news_md</span>__.
Для того, чтобы загрузить пакет достаточно выполнить следующую команду: 
```console
> python -m spacy download ru_core_news_md
```
При запуске скрипта необходимо указать единственный аргумент, отвечающий за функцию, которую по итогу выполнит скрипт.
Пример запуска: 
```console
D:\Projects\PycharmProjects\spaCyFeatures>main.py 1
```
Более подробная информация об аргументе: 
```console
D:\Projects\PycharmProjects\spaCyFeatures>main.py -h
```
