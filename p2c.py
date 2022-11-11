#creating a class 
class P2c(object):
    '''P2C with one method'''
    def __init__(self,annual_salary,total_cost)->None:
        self.__a = annual_salary
        self.__t = total_cost*0.25
    def clculate(self,year=False)->str:
        '''return all needed foactors to buy dream house in three years'''
        monthly_salary = self.__a/12
        Count = 0
        invest = 0
        R = [i/100 for i in range(1,101)]
        percent_salary = [i/100 for i in range(1,101)]
        increase_salary = [i/100 for i in range(1,101)]
        for i in R :
            for k in increase_salary:
                for j in percent_salary :
                    while True :
                        if invest >= self.__t :
                            if Count==36 :
                                return f'R : {i*100}\npercent of salary for saving : {j*100}\npercent of per year increasing : {k*100}\nin {Count} months'
                            else :
                                Count = 0
                                invest = 0
                                break
                        Count +=1
                        monthly_R = invest*i/12
                        percent_of_salary = monthly_salary*j
                        save = monthly_R + percent_of_salary
                        invest += save 
                        if Count%6==0 :
                            monthly_salary += (monthly_salary*k)
        return 'It is not possible to pay the down payment in three years.'
                            
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
sample = P2c(a_s,t_c)
print(sample.clculate())
exit = input('please enter any key to exit :')
