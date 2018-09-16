#build a calculator to estimate the revenue

>>> visitor = input('Please input the number of monthly visitors: ')
Please input the number of monthly visitors: 
>>> subscriber = int(visitor)/10
>>> subscription_fee = subscriber*15
>>> ad_revenue = 0.8*int(visitor)
>>> revenue = subscription_fee + ad_revenue 
>>> print(revenue)

#when visitor = 40000

>>> content_cost = 70000
>>> labor_cost = 30000
>>> server_cost = 50000
>>> visitor = input('Please input the number of monthly visitors: ')
Please input the number of monthly visitors: 40000
>>> subscriber = int(visitor)/10
>>> subscription_fee = subscriber*15
>>> ad_revenue = 0.8*int(visitor)
>>> net_income = subscription_fee + ad_revenue - content_cost - labor_cost - server_cost
>>> print(net_income)
-58000.0

#when visitor = 60000

>>> content_cost = 70000
>>> labor_cost = 30000
>>> server_cost = 50000
>>> visitor = input('Please input the number of monthly visitors: ')
Please input the number of monthly visitors: 60000
>>> subscriber = int(visitor)/10
>>> subscription_fee = subscriber*15
>>> ad_revenue = 0.8*int(visitor)
>>> net_income = subscription_fee + ad_revenue - content_cost - labor_cost - server_cost
>>> print(net_income)
-12000.0

#when visitor = 60000

>>> content_cost = 70000
>>> labor_cost = 30000
>>> server_cost = 50000
>>> visitor = input('Please input the number of monthly visitors: ')
Please input the number of monthly visitors: 80000
>>> subscriber = int(visitor)/10
>>> subscription_fee = subscriber*15
>>> ad_revenue = 0.8*int(visitor)
>>> net_income = subscription_fee + ad_revenue - content_cost - labor_cost - server_cost
>>> print(net_income)
34000.0