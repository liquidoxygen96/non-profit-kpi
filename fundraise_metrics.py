import math 

print('\n##################################################################\n')
print('Welcome to the basic KPI Metric Calculator for Non-profit Organizations')
print('\n#################################################################\n')

# I. FUNDRAISING KPI METRICS for a Non-Profit Organization 

	# 1. Gifts Secured: number of gifts per timeframe 
gifts_secured_quarterly = float(input('Enter the number of gifts received this quarter: '))

	# 2. Donor && Donation Growth
number_donor_previous = float(input('enter last years number of donors: '))
number_donor_current = float(input('enter this years number of donors: '))

	#calculation of donor growth rate: [(prev - current)/prev] *100
donor_growth_rate = ( (number_donor_current - number_donor_previous)/number_donor_previous) * 100 

total_donations_previous = float(input('Enter last years total donation in USD: $ '))
total_donations_current = float(input('enter the current years total donation size in USD: $ '))

donation_growth_rate = ((total_donations_current - total_donations_previous)/total_donations_previous) * 100

	# 3. Donor Retention Rate: percentage of donors who have given more than once 
	#retention rate is important: find rate and differentiate between new donors and retaining preceding donors 
		
donors_previous_year = float(input('Enter the number of donors for the previous year: '))
number_retained_donors = float(input('Enter the number of donors retained from last year (i.e donated again): '))
		
donor_retention_rate = (number_retained_donors / donors_previous_year)* 100


	# 4. Fundraising ROI - Return on Investment: Evaluating how effective the 	organization's fundraising effort and effective use of raised funds           compared to the cost incurred to generated the donated amount was

total_cost = float(input("Enter the total cost for fundrasing event(s): "))
total_funds_raised = float(input('Enter the total funds raised: ' ) ) 

fundrasing_roi = (total_cost / total_funds_raised)

#calculating the cost to gain a donor: exact amount needed to obtain a new donor 

#Example: 1000 $usd on ads that bring in 200 donors: 
cost_advertisements = float(input("Enter the total cost of advertisements: "))
number_donors_gained = int(input('How many new donors were gained through advert spending: '))
cost_per_donor_gained = cost_advertisements / number_donors_gained

	# 5. Donation Conversions by Channel: how many donors took action when prompted by the org, and where they decided to take the action ( organic, social, email, referral, airdrop + other types of new web3 incentives and CallsToAction

number_donors_callToAction = int(input('Enter the number of donors who donated based on a callToAction stimulus/infographic/incentive ' ))
donation_conversion = number_donor_current / number_donors_callToAction 


# II. MARKETING AND COMMUNICATIONS KPI METRICS (Bullshit and non-information sensitive) will do all I can to not use intrusive data collection! focus on mission, numbers will drive themselves (except maybe for website visitor number)

# 6. Website page views ++ time spent on website 

# 7. Email Open metric and Click-through rates (CTR)

# 8. Landing page conversion rates: number of people who complete donation process (analytics)
donation_conversion_rate_website= (number_website_visitors / total_number_donations) * 100

# 9. Amplification, Applause, and Conversation Rates


## III. Program Delivery Nonprifit KPIs

# 10. Number of beneficiaries served and Program attendance 

# 11. Beneficiary Satisfaction Rate 
	# Ask Benefactors how they feel, and if they have any insight on how to improve our program. Questionaires and on-chain satisfaction metrics must be documented and put to use. 
	
# IV. Human Resource Nonprofit Performance Metrics

# 12. Contributor/Employee Retention Rate!! 
number_contributors_quarterly = int(input('Enter the number of people who contributed to the project (quarterly or yearly): '))
number_contributors_retained_quarterly =  int(input('Enter the number of employed contributers '))


contributor_retention_rate = (number_contributors_quarterly / number_contributors_retained_quarterly) * 100 

# 13. Contributor/Employee Satisfaction Rate 
 # 13. a. Net Promoter Score
 # 13. b. Informal Inquiry on total employee Satisfaction 

#14 Percent of Performance Goals Met 
# Must have set goals in order to gauge completness 
# Can be implemented on an Agile System or Scrum performance metric ( percent of tasks completed, percent of goals that were deemed to be unnatainable) 

#15. Absenteeism Rate -- if people don't want to show up, then your project is not motivating enough. 

days_absent_per_employee = int(input('Enter the number of employee being absent: '))

total_work_days = int(input('how many days has the project been active: '))

absenteeism_rate = (days_absent_per_employee / total_work_days) * 100



## V. Financial KPIs for Nonprofits 

#16. Year Over Year Growth 
	#annual budges: total amount of funds your non-profit earns per year 
	# reccuring revenue
	
#17. Operating Surplus/Deficit:
# Resource Management [ net_assets vs. total_expenses ]


#18. Liquid Unrestricted Net Assets ( LUNA ) 
# Funds available to turn into working capital to pursue operations and growth opportunities 

#19. Program Efficiency 
# Program Expenses vs total Expenses 



## Print All important Metrics found 
print('################################### \n ')
print (' KPI metrics, calculated based on the organisations Input \n')
print('################################### \n \n \n ')


print('DONOR GROWTH RATE: %.4f % ' %donor_growth_rate)
print('DONATION GROWTH RATE: %.4f % ' %donation_growth_rate)
print('\nDONOR RETENTION RATE: %.4f %' %donor_retention_rate)

print('\nFUNDRAISING RETURN ON INVESTMENT: %.4f %' %fundraising_roi)
print('COST PER DONOR ACQUISITION: %.4f % '  %cost_per_donor_gained)

print(' DONATION CONVERSION RATE: %.4f %' %donation_conversion)

print('\nNumber of Donations Made through Website conversion: %.4f %' %donation_conversion_rate_website)

print('DONER RETENTION PERCENTAGE: %.4f %'%contributor_retention_rate)


print('EMPLOYEE/CONTRIBUTOR ABSENTEEISM RATE: %.4f %'  %absenteeism_rate)





		
		
