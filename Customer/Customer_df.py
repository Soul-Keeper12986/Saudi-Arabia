import numpy as np
import pandas as pd
import datetime
import time
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import re
import csv
import matplotlib.pyplot as plt
from datetime import timedelta

class Customer:
	
	def __init__(self, customer_ID, first_name, last_name, 
		date_of_birth, gender, agree_for_promo, autoplay_card,
		email, msisdn, customer_status, customer_category,
		customer_since, region, language, termination_date):
		self.customer_ID = customer_ID
		self.first_name = first_name
		self.last_name = last_name
		self.date_of_birth = date_of_birth
		self.gender = gender
		self.agree_for_promo = agree_for_promo
		self.autoplay_card = autoplay_card
		self.email = email
		self.msisdn = msisdn
		self.customer_status = customer_status
		self.customer_category = customer_category
		self.customer_since = customer_since
		self.region = region
		self.language = language
		self.termination_date = termination_date

'''
def generate_First_name(population, gender):
	if gender == 'Male':
		with open('Male_Arabic_name_list.csv', newline='') as f:
			reader = csv.reader(f)
			data = list(reader)[0]
	else:
		with open('Female_Arabic_name_list.csv', newline='') as f:
			reader = csv.reader(f)
			data = list(reader)[0]
	Customer_Names = []
	for i in range(0, population):
		Customer_Names.append(np.random.choice(data))
		#print(Names)
	return(Customer_Names)
'''

def generate_Date_of_Birth(population):
	'''
	max_age = 85
	min_age = 18
	now = datetime.datetime.now()
	start_delta_days = max_age*365  
	end_delta_days =  min_age*365

	start_date = now - timedelta(days = start_delta_days)
	end_date = now - timedelta(days = end_delta_days)

	print(start_date, end_date)
	
	first_part = np.random.normal(loc=11, scale=7.5, size=1500)
	second_part = np.random.normal(loc=41, scale=5.5, size=1500)
	#third_part = np.random.uniform(high=25, size=500)
	#all_together = np.concatenate([first_part, second_part, third_part])
	all_together = np.concatenate([first_part, second_part])

	all_together = all_together[(all_together >=0)]
	np.random.shuffle(all_together)

	plt.hist(all_together, bins=(max_age-min_age));
	plt.show()

	np.random.randint()
	'''
	Customer_dates_of_birth = []
	for i in range(0, population):
		a = np.random.choice(['0-4','5-9','10-14','15-19','20-24','25-29','30-34','35-39',
			'40-44','45-49','50-54','55-59','60-64','65-69','70-74','75-79','80-84','85-89'], 
			p = [0.0816, 0.0853, 0.0817, 0.0728, 0.0693, 0.0746, 0.0959, 0.0941, 0.0888,
			 0.0853, 0.0639, 0.0444, 0.0302, 0.0178, 0.0071, 0.0036, 0.0018, 0.0018]).split(sep ='-')
		#print(a)
		max_age = int(a[1])
		min_age = int(a[0])
		age_range = (max_age - min_age)* 365
		days_of_life = np.random.randint(age_range) + min_age*365
		date_of_birth = datetime.datetime.now() - timedelta(days = days_of_life)
		date_of_birth =  date_of_birth.strftime("%Y-%m-%d")
		#print(date_of_birth)
		Customer_dates_of_birth.append(date_of_birth)
	return(Customer_dates_of_birth)

    
def generate_First_name(population):
	with open('Male_Arabic_name_list.csv', newline='') as f:
		reader = csv.reader(f)
		data = list(reader)[0]
	Customer_Names = []
	for i in range(0, population):
		Customer_Names.append(np.random.choice(data))
		#print(Names)
	return(Customer_Names)

def generate_Last_name(population):
	with open('Arabic_Surnames_list.csv', newline='') as f:
		reader = csv.reader(f)
		data = list(reader)[0]
		Customer_Surnames = []
		for i in range(0, population):
			Customer_Surnames.append(np.random.choice(data))
	return(Customer_Surnames)

def generate_Region(population):
	Regions = ['Mecca Region','Riyadh Region','Eastern Region','Asir Region',
	'Jizan Region','Medina Region','Al-Qassim Region','Hail Region',
	'Najran Region','Al-Jawf Region','Al-Bahah Region','Northern Borders Region']
	Customer_regions = []
	for i in range(0, population):
		Customer_regions.append(np.random.choice(Regions))
	return(Customer_regions)

def generate_ID(population):
	customer_ID_list = np.arange(population)
	x = np.random.shuffle(customer_ID_list)	
	#print(customer_ID_list)
	return(customer_ID_list)

def generate_Gender(population):
	Genders = []
	for i in range(population):
		Genders.append(np.random.choice(['Male', 'Female'], p = [0.539, 0.461]))
	return(Genders)

def generate_Gender(population):
	Genders = []
	for i in range(population):
		Genders.append(np.random.choice(['Male', 'Female'], p = [0.539, 0.461]))
	return(Genders)

def generate_Language(population):
	Languages = []
	for i in range(population):
		Languages.append(np.random.choice(['Arabic','English','Other'], p = [0.979, 0.012 ,0.009]))
	return(Languages)

def generate_MSISDN(population):
	Customer_Numbers = []
	for i in range(population):
		country_code = "+996"
		NDC = ['50', '53', '54', '55', '56', '58', '59']
		num =np.random.randint(9999999)
		number = country_code +'-'+ np.random.choice(NDC)+'-'+(f'{num:07}')
		Customer_Numbers.append(number)
	return(Customer_Numbers)

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
#customer_dataframe = pd.DataFrame(columns = customer_columns)
customer_dataframe = pd.DataFrame()

customer_dataframe['Customer_ID'] = generate_ID(population) 
customer_dataframe['Gender'] = generate_Gender(population) 
customer_dataframe['First name'] = generate_First_name(population)
customer_dataframe['Last name'] = generate_Last_name(population) 
customer_dataframe['Region'] = generate_Region(population) 
customer_dataframe['Language'] = generate_Language(population) 
customer_dataframe['Date_of_birth'] = generate_Date_of_Birth(population) 
customer_dataframe['MSISDN'] = generate_MSISDN(population)

pd.set_option('display.max_columns', None)
#pd.set_option('display.max_rows', None)

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
print(customer_dataframe)

#customer_dataframe.to_csv('Customers.csv', sep=',')
