#creating a class 
class P2b(object):
    '''P2B with one method'''
    def __init__(self,annual_salary,portion_saved,total_cost,semi_annual_raise)->None:
        self.__a = annual_salary
        self.__p = portion_saved/100
        self.__t = total_cost*0.25
        self.__s = semi_annual_raise/100
    def clculate(self,year=False)->str:
        '''return number of months to buy the dream house by increasing salary per six months'''
        Count = 0
        six_month = 0
        invest = 0
        R = 0.04
        monthly_salary = self.__a/12
        while True :
            if invest >= self.__t :
                if year == True :
                    return f'number of years :{Count/12}'
                return f'number of months :{Count}'
            Count += 1
            percent_for_save = monthly_salary*self.__p
            monthly_R = invest*R/12
            save = percent_for_save + monthly_R
            invest+=save
            if Count%6==0 :
                monthly_salary += (monthly_salary*self.__s)
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
s_a_r = input('Enter the semiannual raise, as a decimal:')
try :
    if type(eval(s_a_r)) is str :
        raise
    elif type(eval(s_a_r)) is int:
        s_a_r = int(s_a_r)
    else :
        s_a_r = float(s_a_r)
except :
    print('please enter a valid number')
    raise
sample = P2b(a_s,p_s,t_c,s_a_r)
print(sample.clculate())
exit = input('please enter any key to exit :')
