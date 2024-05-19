# You are given an array of unique integers salary where salary[i] is the salary of the ith employee.

# Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual answer will be accepted.


def average(salary):

        # calculating minimum and maximum from list
        min_sal=min(salary)
        max_sal=max(salary)

        # filter the list in which not min not max
        salary_filter=[i for i in salary if i !=min_sal and i !=max_sal]

        # calculating average

        average=sum(salary_filter)/len(salary_filter)
        return average
                

print(average([1000,20000,3000]))