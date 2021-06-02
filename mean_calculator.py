import numpy as np 

def calculate(lst):
    try:

        if len(lst)<9:
            raise ValueError #if list contains less than nine elements so Value Error will be raised
        else:
            a=np.array(lst).reshape(3,3) 
            flatten=a.flatten() #flatten_matrix

            #mean:

            mean1=list(a.mean(axis=0))
            mean2=list(a.mean(axis=1))
            flatten_mean=flatten.mean()
            mean=[mean1,mean2,flatten_mean] 

            #variance:

            var1=list(a.var(axis=0))
            var2=list(a.var(axis=1))
            flatten_var=var1=flatten.var()
            var=[var1,var2,flatten_var]

            #standard deviation:

            std1=list(a.std(axis=0))
            std2=list(a.std(axis=1))
            flatten_std=a.std()
            std=[std1,std2,flatten_std]

            #max

            max1=list(a.max(axis=0))
            max2=list(a.max(axis=1))
            flatten_max=a.max()
            max_total=[max1,max2,flatten_max]

            # min

            min1=list(a.min(axis=0))
            min2=list(a.min(axis=1))
            flatten_min=a.min()
            min_total=[min1,min2,flatten_min]

            #sum

            sum1=list(a.sum(axis=0))
            sum2=list(a.sum(axis=1))
            flatten_sum=a.sum()
            sum_total=[sum1,sum2,flatten_sum]

            values=[mean,var,std,max_total,min_total,sum_total]
            keys=['mean','variance','standard deviation','max','min','sum']
            calculations={}
            for k,v in zip(keys,values): #iterating
                calculations[k]=v
            return(calculations)  #returned dictionary

    except ValueError: #if value Error will be raised then this block of code executes
        return("Exception : List must contain nine numbers.")

print(calculate([1,2,3,4,5,6,7,8,9]))

