def read_string(file_name):
    f = open(file_name, "r")
    text = f.readlines()
    f.close()
    return "\n".join(text)


# remove from txt punctions and return the txt without them
def remove_punctuation(my_str, puncts):
    for i in my_str:
        for j in puncts:
            if i == j:
                my_str = my_str.replace(i, "")
    if my_str.endswith(" "):
        my_str = my_str.rstrip(" ")
    return my_str


# remove from the txt the stop words and return the txt without them
def remove_stopwords(my_str, stopwords):
    lst = my_str.split()
    Rstr = ""
    for i in range(len(lst)):
        if lst[i] in stopwords:
            continue
        Rstr += lst[i] + " "
    if Rstr.endswith(" "):
        Rstr = Rstr.rstrip(" ")
    return Rstr


# remove prefix like https from the txt and return without them
def remove_prefix(my_str, prefix_to_remove):
    lst = my_str.split(" ")
    Rstr = ""
    put_it = False
    for i in range(len(lst)):
        for j in range(len(prefix_to_remove)):
            if not lst[i].startswith(prefix_to_remove[j]):
                if not put_it:
                    put_it = True
            else:
                put_it = False
                break
        if put_it:
            Rstr += lst[i] + " "
        put_it = False
    if Rstr.endswith(" "):
        Rstr = Rstr.rstrip(" ")
    return Rstr


# the function get txt and the replacabke txt and the number if a word in the txt is there less than the mincount we replace the word with thx replacable txt we get
# TODO: set if include or not include min_count
def remove_oov(my_str, min_count, oov):
    lst = my_str.split(" ")
    count = 1
    Rstr = ""
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] == lst[j] and i != j and lst[i] != " ":
                count += 1
        if count < min_count:
            Rstr += oov + " "
            count = 1
        else:
            Rstr += lst[i] + " "
            count = 1
    if Rstr.endswith(" "):
        Rstr = Rstr.rstrip(" ")
    return Rstr


# remove spare spaces
def remove_spaces(my_str):
    Rstr = ""
    lst = my_str.split()
    for i in range(len(lst)):
        if i != len(lst) - 1:
            Rstr += lst[i] + " "
        else:
            Rstr += lst[i]
    return Rstr


# clean the txt from all punctions and stop words and spare spaces and the replacable txt
def clean_text(my_str, puncts_to_remove, stop_words, min_count, oov, prefix_to_remove):
    my_str.lower()
    my_str = remove_punctuation(my_str, puncts_to_remove)
    my_str = remove_stopwords(my_str, stop_words)
    my_str = remove_prefix(my_str, prefix_to_remove)
    my_str = remove_oov(my_str, min_count, oov)
    my_str = remove_spaces(my_str)
    return my_str


# gets a claer txt and put dictionary the the key is the word and the value is the number of time it is reapiting
def get_word2count(my_str):
    dict_of_words = {}
    count = 1
    lst = my_str.split()
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] == lst[j] and i != j:
                count += 1
        if lst[i] in dict_of_words:
            count = 1
        else:
            dict_of_words[lst[i]] = count
            count = 1
    return dict_of_words


# gets txt and return a dictionery thet the key is the number and the valsu is the lists of word that repoets the same time
def get_count2words(my_str):
    dict_of_words = {}
    count = 1
    lst = my_str.split()
    list_of_words = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] == lst[j] and i != j:
                count += 1
        if count in dict_of_words:
            list_of_words = dict_of_words.get(count)
            if lst[i] in list_of_words:
                list_of_words = []
                count = 1
            else:
                list_of_words.append(lst[i])
                dict_of_words[count] = list_of_words
                list_of_words = []
                count = 1
        else:
            list_of_words.append(lst[i])
            dict_of_words[count] = list_of_words
            list_of_words = []
            count = 1
    return dict_of_words

# the function gets a dictionary and a number at print the top reporting words in the eange of n if n is bigger than ll of the words in the dictionary than it print all of the words
def top_n_words(n, count2words_dict):
    list_of_keys = list(count2words_dict.keys())
    list_of_keys.sort(reverse=True)
    lst = []
    count = 0
    for i in range(n):
        if count >= n:
            break
        if i == len(list_of_keys):
            break
        if len(count2words_dict.get(list_of_keys[i])) < (n - count):
            for j in range(len(count2words_dict.get(list_of_keys[i]))):
                lst.append((count2words_dict.get(list_of_keys[i]))[j])
            count += len(count2words_dict.get(list_of_keys[i]))
        elif len(count2words_dict.get(list_of_keys[i])) >= (n - count):
            for j in range(n-count):
                lst.append((count2words_dict.get(list_of_keys[i]))[j])
            break
    return lst


# check the lvl of similarity between 2 txts
def compare_texts(n, text_path1, text_path2):
    str1 = read_string(text_path1)
    str2 = read_string(text_path2)
    str1 = clean_text(str1, ["!","'","\n",",","!","?"], ['i','am','he','she','it','on'], 2, "", ['http://','https://'])
    str2 = clean_text(str2, ["!","'","\n",",","!","?"], ['i','am','he','she','it','on'], 2, "", ['http://','https://'])
    dict_of_words1 = get_count2words(str1)
    dict_of_words2 = get_count2words(str2)
    Top_n_word1 = top_n_words(n, dict_of_words1)
    Top_n_word2 = top_n_words(n, dict_of_words2)
    similarity = 0
    for i in range(len(Top_n_word1)):
        if Top_n_word1[i] in Top_n_word2:
            similarity += 1
    return similarity