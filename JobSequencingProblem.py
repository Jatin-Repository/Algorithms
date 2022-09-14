class JobSequencingProblem:
    def __init__(self, description):
        self.description = description

    def Jobsequence(self):
        deadline = list()
        for y in self.description.values():
            deadline.append((y[0]))
        max_deadline = max(deadline)
        sort_orders = dict(sorted(self.description.items(), key=lambda x: x[1][1], reverse=True))
        list1 = list()
        max_profit = 0
        while max_deadline > 0:
            for x, y in sort_orders.items():
                if int(y[0]) >= max_deadline:
                    list1.append(x)
                    max_profit += y[1]
                    del sort_orders[x]
                    max_deadline -= 1
                    break
            else:
                list1.append("-")
                max_deadline -= 1
        print("Job_Schedule_List:", list1[::-1])
        return max_profit


job = dict()
print("Enter the number of Job to be Schedule")
n = int(input())
for i in range(1, n+1):
    list1 = list()
    print("Enter the Deadline for Job", i)
    x = int(input())
    list1.append(x)
    print("Enter the Profit for Job", i)
    y = int(input())
    list1.append(y)
    job[i] = list1
t = JobSequencingProblem(job)
print("Max_Profit:",  t.Jobsequence())



