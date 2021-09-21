import spacy
from spacy.matcher import Matcher
from cl_interface import cl_args


def pos_dep_lem():
    """Вывод информации о токенах: POS-тег, роль токена в предложении, базовая форма токена."""
    doc = nlp("В глубине поляны стоял небольшой деревянный дом, отличавшийся изысканной простотой.")
    for token in doc:
        print(token.text, token.pos_, token.dep_, token.lemma_)


def vectorization():
    """Представление токенов текста в векторном виде."""
    doc = nlp("Новые правила для сделок.")
    for token in doc:
        print(token.text, '\n', token.vector, '\n')

    print("Среднее значение векторов всего текста целиком:")
    print(doc.vector)


def text_finder():
    """Поиск текста по шаблону."""
    matcher = Matcher(nlp.vocab)
    # Добавление шаблона с идентификатором "ПриветДружище"
    pattern = [{"LOWER": "привет"}, {"IS_PUNCT": True}, {"LOWER": "дружище"}]
    matcher.add("ПриветДружище", [pattern])
    doc = nlp("Привет, дружище! Привет дружище!")
    matches = matcher(doc)
    for match_id, start, end in matches:
        string_id = nlp.vocab.strings[match_id]  # Строковое представление
        span = doc[start:end]  # Соответствующий промежуток совпадения
        print(match_id, string_id, start, end, span.text)


def attribute_ruler_possibilities():
    """Идентификация токена и присвоение ему предоставленных атрибутов."""
    text = "Магазин 'Магнит' стоит рядом с моим домом. Магнит, купленный там, сломался."
    doc1 = nlp(text)

    print("Теги токенов, полученные с помощью обработки текста устройством:")
    print(doc1[2].text, doc1[2].tag_, doc1[2].pos_)  # NOUN NOUN
    print(doc1[10].text, doc1[10].tag_, doc1[10].pos_)  # NOUN NOUN

    # Инициализация инструмента attribute ruler
    ruler = nlp.get_pipe("attribute_ruler")
    # Шаблон для соответствия "Магнит"
    patterns = [[{"LOWER": "магнит", "IS_SENT_START": False}]]
    # Атрибуты, присваиваемые сопоставленному токену
    attrs = {"TAG": "NNP", "POS": "PROPN"}
    # Добавление правил для attribute ruler
    ruler.add(patterns=patterns, attrs=attrs, index=0)

    doc2 = nlp(text)
    print("Теги токенов, с учетом правила attribute ruler:")
    print(doc2[2].text, doc2[2].tag_, doc2[2].pos_)  # NNP PROPN
    print(doc2[10].text, doc2[10].tag_, doc2[10].pos_)  # NOUN NOUN, т.е. остался без изменений


def ner():
    """Распознавание именованных сущностей."""
    doc = nlp("Первым делом в Англии нужно посетить Лондон, так говорила моя бабушка Лида.")
    for ent in doc.ents:
        print(ent.text, ent.start_char, ent.end_char, ent.label_)


if __name__ == '__main__':
    nlp = spacy.load("ru_core_news_md")

    if cl_args.feature == 0:
        pos_dep_lem()
    elif cl_args.feature == 1:
        vectorization()
    elif cl_args.feature == 2:
        text_finder()
    elif cl_args.feature == 3:
        attribute_ruler_possibilities()
    elif cl_args.feature == 4:
        ner()
