import numpy as np
import pandas as pd
import time
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import re
import csv
import matplotlib.pyplot as plt
from datetime import timedelta, datetime, date

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


def generate_First_name(population, gender):
	with open('Male_Arabic_name_list.csv', newline='') as file_male:
		reader = csv.reader(file_male)
		male_names = list(reader)[0]
	with open('Female_Arabic_name_list.csv', newline='') as  file_female:
		reader = csv.reader(file_female)
		female_names = list(reader)[0]
	Customer_Names = []
	for i in range(0, population):
		if gender[i] == 'Male':
			Customer_Names.append(np.random.choice(male_names))
		else:
			Customer_Names.append(np.random.choice(female_names))
		#print(Names)
	return(Customer_Names)


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
	strats = [
			'0-4',
			'5-9',
			'10-14',
			'15-19',
			'20-24',
			'25-29',
			'30-34',
			'35-39',
			'40-44',
			'45-49',
			'50-54',
			'55-59',
			'60-64',
			'65-69',
			'70-74',
			'75-79',
			'80-84',
			'85-89'
			]
	while len(Customer_dates_of_birth) < population:
		a = np.random.choice(strats, 
			p = [0.0816, 0.0853, 0.0817, 0.0728, 0.0693, 0.0746, 0.0959, 0.0941, 0.0888,
			 0.0853, 0.0639, 0.0444, 0.0302, 0.0178, 0.0071, 0.0036, 0.0018, 0.0018]).split(sep ='-')
		#print(a)
		max_age = int(a[1])
		min_age = int(a[0])
		age_range = (max_age - min_age) * 365
		days_of_life = np.random.randint(age_range) + min_age * 365
		if days_of_life > 18 *365:
			date_of_birth = datetime.now() - timedelta(days = days_of_life)
			date_of_birth =  date_of_birth.strftime("%Y-%m-%d")
			Customer_dates_of_birth.append(date_of_birth)
	return(Customer_dates_of_birth)


def generate_Customer_Since(population, dates_of_birth):
	adult_age = 18
	Customers_Since = []
	for i in range(population):
		b = dates_of_birth[i].split('-')
		bb = date(int(b[0]),int(b[1]),int(b[2]))
		min_date = bb + timedelta(days = 365 * adult_age)
		max_date = datetime.now().date()
		max_days = (max_date  - min_date).days
		real_days = np.random.randint(max_days)
		random_date = min_date + timedelta(days = real_days)
		Customers_Since.append(random_date)
	return(Customers_Since)


def generate_Last_name(population):
	with open('Arabic_Surnames_list.csv', newline='') as f:
		reader = csv.reader(f)
		data = list(reader)[0]
		Customer_Surnames = []
		for i in range(0, population):
			Customer_Surnames.append(np.random.choice(data))
	return(Customer_Surnames)


def generate_Region(population):
	Regions = {
				'Mecca':8_099_473,
				'Riyadh':7_910_864,
				'Eastern':4_762_871,
				'Asir':2_194_463,
				'Medina':2_061_383,
				'Jizan':1_568_727,
				'Al-Qassim':1_402_974,
				'Tabuk':907_494,
				'Hail':685_820,
				'Najran':581_789,
				'Al-Jawf':506_372,
				'Al-Bahah':471_755,
				'Northern Borders':367_433
				}
	Customer_regions = []
	probabilities = []
	sum_population = sum(Regions.values())

	for value in Regions.values():
		probabilities.append(value/sum_population)

	for i in range(0, population):
		Customer_regions.append(np.random.choice((list(Regions.keys())), p = probabilities))
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


def generate_Language(population):
	Languages = []
	for i in range(population):
		Languages.append(np.random.choice(['Arabic','English','Other'], p = [0.979, 0.012 ,0.009]))
	return(Languages)


def generate_MSISDN(population):
	Customer_Numbers = []
	country_code = "+996"
	NDC = ['50', '53', '54', '55', '56', '58', '59']
	for i in range(population):
		num =np.random.randint(9999999)
		number = country_code +'-'+ np.random.choice(NDC)+'-'+(f'{num:07}')
		Customer_Numbers.append(number)
	return(Customer_Numbers)


def generate_agree_for_promo(population):
	Customers_agree = []
	for i in range(population):
		Customers_agree.append(np.random.choice(['Yes', 'No'], p = [0.4, 0.6]))
	return(Customers_agree)


def generate_Agree_for_promo(population):
	Customers_agree = []
	for i in range(population):
		Customers_agree.append(np.random.choice(['Yes', 'No'], p = [0.5, 0.5]))
	return(Customers_agree)


def generate_Autopay_card(population):
	Customers_Autopay = []
	for i in range(population):
		k = np.random.randint(10,20)/100
		Customers_Autopay.append(np.random.choice(['Yes', 'No'], p = [0.2+k, 0.8-k]))
	return(Customers_Autopay)


def generate_Email(population, names, surnames):
	domains = [
				'awalnet.sa', 
				'aramco.com.sa', 
				'saudia-omline.com',
				'gmail.com', 
				'naseej.com.sa',
				'123arab.com',
				'sol.net.sa',
				'zajil.net.sa',
				'sahara.com.sa',
				'compuserve.com',
				'sps.net.sa',
				'arasco.net.sa'
				]
	Customers_Emails = []
	for i in range(population):
		address =str(names[i]+surnames[i]+str(np.random.randint(100))+'@'+np.random.choice(domains))
		Customers_Emails.append(address) 
	return(Customers_Emails)


def generate_Statuses(population):
	Statuses = []
	for i in range(population):
		k = np.random.randint(10,20)/100
		Statuses.append(np.random.choice(['Active', 'Inactive'], p = [0.35+k, 0.65-k]))
	return(Statuses)

def generate_Categories(population):
	Customer_Categories = []
	for i in range(population):
		k = np.random.randint(1,4)/100
		Customer_Categories.append(np.random.choice(['Business', 'Physical'], p = [0.87+k, 0.13-k]))
	return(Customer_Categories)


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

population = 10000
#customer_dataframe = pd.DataFrame(columns = customer_columns)
customer_df = pd.DataFrame()

customer_df['Customer_ID'] = generate_ID(population)
customer_df['Gender'] = generate_Gender(population) 
customer_df['First name'] = generate_First_name(population,customer_df['Gender'])
customer_df['Last name'] = generate_Last_name(population) 
customer_df['Date_of_birth'] = generate_Date_of_Birth(population) 
customer_df['Agree_for_promo'] = generate_Agree_for_promo(population)
customer_df['autoplay_card'] = generate_Autopay_card(population)
customer_df['Customer_Email'] = generate_Email(population, customer_df['First name'], customer_df['Last name'])
customer_df['MSISDN'] = generate_MSISDN(population)
customer_df['Status'] = generate_Statuses(population)
customer_df['Category'] = generate_Categories(population)
customer_df['Customer_Since'] = generate_Customer_Since(population,customer_df['Date_of_birth'])
customer_df['Region'] = generate_Region(population) 
customer_df['Language'] = generate_Language(population) 
customer_df['termination_date'] = np.NaN


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
#print(customer_df)
customer_df.to_csv('Customers.csv', sep=',')
