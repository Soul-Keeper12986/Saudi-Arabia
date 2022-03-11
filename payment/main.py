from datetime import datetime

import numpy as np
from datetime import datetime,timedelta
import warnings
import pandas as pd



warnings.simplefilter(action='ignore', category=FutureWarning)



class Customer:

    def __init__(self,payment_ID, customer_ID, payment_method,
                 date):
        self.payment_ID = payment_ID
        self.customer_ID = customer_ID
        self.payment_method = payment_method
        self.date = date





def generate_Date(population):
    starttime = '2012-01-01'
    Date = []
    if type(starttime) == type('rrr'):
        a = datetime.strptime(starttime,'%Y-%m-%d').date()
    else:
            a = starttime

    for i in range(population):
        day_ = a + timedelta(days=np.random.randint(1,3650))
        Date.append(day_.strftime("%Y-%m-%d"))
    return Date




def generate_Payment_ID(population):
    payment_ID_list = np.arange(population)
    x = np.random.shuffle(payment_ID_list)
    # print(customer_ID_list)
    return (payment_ID_list)

def generate_Payment_Method(population):
    Method = []
    for i in range(population):
        Method.append(np.random.choice(['Card','Cash'], p =[0.7, 0.3]))
    return (Method)



'''
customer_columns  = ['Customer_ID',
					'First name', 
					'Last name',
					'Date of birth',
					'Gender',
					'Agree_for_promo',
					'Autopay_card',
					'Email',
					'MSISDN',
					'Status',
					'Customer category',
					'Customer_since',
					'Region',
					'Language',
					'Termination_date']
'''
population = 50
# customer_dataframe = pd.DataFrame(columns = customer_columns)
payment_dataframe = pd.DataFrame()

payment_dataframe['Payment_ID'] = generate_Payment_ID(population)
payment_dataframe['Payment_method'] = generate_Payment_Method(population)
payment_dataframe['Date'] = generate_Date(population)


pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)

'''
for i in range(0, population):
	customer_dataframe = customer_dataframe.append(
		pd.Series(['N/A',
				'N/A',
				'N/A',
				'N/A',
				'N/A',
				'N/A',
				'N/A',
				'N/A',
				'N/A',
				'N/A',
				'N/A',
				'N/A',
				'N/A',
				'N/A',
				'N/A',],
				index = customer_columns),
		ignore_index = True)
'''
print(payment_dataframe)

payment_dataframe.to_csv('Payment.csv', sep=',')