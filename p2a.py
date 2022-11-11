#creating a class 
class P2a(object):
    '''P2A with one method'''
    def __init__(self,annual_salary,portion_saved,total_cost)->None:
        self.__a = annual_salary
        self.__p = portion_saved/100
        self.__t = total_cost*0.25
    def clculate(self,year=False)->str:
        '''return number of months to buy the dream house'''
        Count = 0
        invest = 0
        R = 0.04
        monthly_salary = self.__a/12
        percent_for_save = monthly_salary*self.__p
        while True :
            if invest >= self.__t :
                if year == True :
                    return f'number of years :{Count/12}'
                return f'number of months :{Count}'
            Count += 1
            monthly_R = invest*R/12
            save = percent_for_save + monthly_R
            invest+=save
#getting inputs from user
a_s = input('Enter your annual salary:')
try :
    if type(eval(a_s)) is str :
        raise
    elif type(eval(a_s)) is int :
        a_s = int(a_s)
    else :
        a_s = float(a_s)
except :
    print('please enter a valid number')
    raise
p_s = input('Enter the percent of your salary to save, as a decimal:')
try :
    if type(eval(p_s)) is str :
        raise
    elif type(eval(p_s)) is int :
        p_s = int(p_s)
    else :
        p_s = float(p_s)
except :
    print('please enter a valid number')
    raise
t_c = input('Enter the cost of your dream home:')
try :
    if type(eval(t_c)) is str :
        raise
    elif type(eval(t_c)) is int:
        t_c = int(t_c)
    else :
        t_c = float(t_c)
except :
    print('please enter a valid number')
    raise
sample = P2a(a_s,p_s,t_c)
print(sample.clculate())
exit = input('please enter any key to exit :')
