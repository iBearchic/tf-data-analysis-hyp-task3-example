import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

# # Загрузка и предварительный просмотр исторических данных из файла hyp3_historical_data.csv
# historical_data = pd.read_csv('hyp3_historical_data.csv')

# # Подготовка данных: первая половина колонок для контрольной группы, вторая половина - для тестовой
# control_sample = historical_data.iloc[0, 1:2501].values  
# test_sample = historical_data.iloc[0, 2501:].values 

# control_sample = control_sample.astype(float)
# test_sample = test_sample.astype(float)


chat_id = 539822853 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Выполнение t-теста для двух независимых выборок
    t_stat, p_value = ttest_ind(x, y, equal_var=False)
    
    # Уровень значимости (alpha) задан 9%
    alpha = 0.09
    
    # Возвращаем True, если p-значение меньше alpha (различия статистически значимы)
    return p_value < alpha

# solution_result = solution(control_sample, test_sample)
# print(solution_result) # Дает ответ False
