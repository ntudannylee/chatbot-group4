import numpy as np
import pandas as pd

# data reference : https://hwms.epa.gov.tw/dispPageBox/shop/shopCP.aspx?ddsPageID=TABLEWAREE&

def get_data():
    data = pd.read_csv('臺北市自備餐具優惠業者清單.csv', encoding='big5')
    data = data.iloc[:,0].values.tolist()
    return data
