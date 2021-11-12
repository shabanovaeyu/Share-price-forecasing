# Функция find_coefs(params)
# 
# принимает: словарь параметров
#            params.T - период, за который определяется дельта котировок
#            params.day - день публикации новостной статьи
#            params.month - месяц публикации новостной статьи
#            params.year - год публикации новостной статьи
#            params.ticker - тикер акции, которой посвящена статья
#            params.quotes - датафрейм с котировками акций
#            params.dataset - датафрейм, в который будут записаны T, a1, a2
# 
# возращает: кортеж (T, a1, a2)
#            a1 - к-т линейной регрессии на интервале (дата публикации - T дней, дата публиаккции)
#            a2 - к-т линейной регрессии на интервале (дата публикации, дата публиаккции + T дней)

# params = {'T': 30,
#           'day': 15,
#           'month': 9,
#           'year': 2020,
#           'ticker': 'SBER',
#           'quotes': quotes,
#           'dataset': dataset}

def find_coefs(params):
    
    quotes = params['quotes']
    dataset = params['dataset']
    T = params['T']
    
    q = quotes[quotes['ticker']==params['ticker']]
     
    q.loc[len(q)] = [params['year'], params['month'], params['day'],
                          None, None, None, None, None, None, None]
 
    # Сортировка dataset в естественном порядке течения времени и сброс индексов
    q = q.sort_values(['year', 'month', 'day', 'ticker']).reset_index()
    
    j = q.index[q['ticker'].isnull()][0] # индекс записи с датой публикации статьи
    
    q = q.drop(index = j)
    
    j = j - 1 # индекс записи с котировкой на дуту публикации статьи или
              # на ближайшую слева к дате публикации дату (если на дату публикации нет котировки)
    
    if j >= T and j <= len(q) - T: # проверка - прошел ли период длиной T с даты публикации
    
        v1 = q[j - T: j]['Close'].values
        v2 = q[j : j + T]['Close'].values
        t = np.array(range(1,len(v1)+1))

        a1 = ((t * v1).mean() - t.mean() * v1.mean()) / ((t**2).mean() - (t.mean())**2)
        a2 = ((t * v2).mean() - t.mean() * v2.mean()) / ((t**2).mean() - (t.mean())**2)

    else: return T, None, None

    return T, a1, a2


# Функция tokenizer(df, col)

def tokenizer(df, col):
   
    morph = MorphAnalyzer()
    stemmer = PorterStemmer()
    words = stopwords.words('russian')
    patterns = "[A-Za-z0-9!#№$%&'()*+«»,./:;<=>?@[\]^_`{|}~—\"\-]+"
    col_cln = col + '_cln'
    
    df[col_cln] = df[col].apply(lambda x: ' '.join([morph.normal_forms(stemmer.stem(i.strip()))[0] \
                                                    for i in re.sub(patterns, ' ', x).replace('ё', 'е').split() \
                                                    if i.strip() not in words]).lower())
    return df
