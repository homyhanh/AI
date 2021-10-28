from ortools.algorithms import pywrapknapsack_solver
import os
import random
import time
import pandas as pd
import sys

def main(X, x):
    # Create the solver.
    solver = pywrapknapsack_solver.KnapsackSolver(
        pywrapknapsack_solver.KnapsackSolver.
        KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER, 'KnapsackExample')
    path_file = 'C:/Users/MyPC/Downloads/Knapsack_problem/kplib-master/'+ X
    print (X)
    # Với mỗi lần chạy test case, lưu trữ các thông tin cần thiết
    df = pd.DataFrame(columns = ['Testcase_Name', 'Number', 'Total_Value', 'Total_Weight', 'Is_Solution_Optimal'])
    for file_name in os.listdir(path_file): # xét mỗi trường có item khác nhau trong test case
        test_ = random.choice(os.listdir(os.path.join(path_file, file_name))) # chọn ngẫu nhiên testcase
        with open ('kplib-master/' + X +'/' + file_name + '/' + test_) as level_file:
            rows = level_file.read().split('\n')
        values = []
        weights = []
        for i in range (4, len(rows)-1):
            m, n = rows[i].split()  # tách hai giá trị: value & weight
            values.append(int (m))
            weights.append(int (n))
        weights = [weights]
        capacities = [int(rows[2])]

        solver.Init(values, weights, capacities)
        solver.set_time_limit(60)
        time_start=time.time()
        computed_value = solver.Solve()
        time_end=time.time()
        s = time_end - time_start

        packed_items = []
        packed_weights = []
        total_weight = 0
        if (s < 60): # Xét thời gian chạy của hàm Solve()
            is_solution_optimal = 'Optimal solution'
        else:
            is_solution_optimal = 'Inconclusive solution'
        print ('+ ' + file_name + '/' + test_)
        print('Total value =', computed_value)
        for i in range(len(values)):
            if solver.BestSolutionContains(i):
                packed_items.append(i)
                packed_weights.append(weights[0][i])
                total_weight += weights[0][i]
        print('Total weight:', total_weight)
        print('Packed items:', packed_items)
        print('Packed_weights:', packed_weights)
        print ("Runtime of " + file_name + ": ", s, "second.")
        print (is_solution_optimal)
        df = df.append({'Testcase_Name': X,'Number': rows[1], 'Total_Value': computed_value, 'Total_Weight': total_weight, 'Is_Solution_Optimal': is_solution_optimal}, ignore_index=True)    
    df.to_csv('result' + str(x) + '.csv') # Lưu bảng thống kê mỗi test case 
if __name__ == '__main__':
    for n in range (13):
        if (n==0): X = '00Uncorrelated'
        elif (n==1): X = '01WeaklyCorrelated'
        elif (n==2): X = '02StronglyCorrelated'
        elif (n==3): X = '03InverseStronglyCorrelated'
        elif (n==4): X = '04AlmostStronglyCorrelated'
        elif (n==5): X = '05SubsetSum'
        elif (n==6): X = '06UncorrelatedWithSimilarWeights'
        elif (n==7): X = '07SpannerUncorrelated'
        elif (n==8): X = '08SpannerWeaklyCorrelated'
        elif (n==9): X = '09SpannerStronglyCorrelated'
        elif (n==10): X = '10MultipleStronglyCorrelated'
        elif (n==11): X = '11ProfitCeiling'
        elif (n==12): X = '12Circle'
        # Với mỗi testcase ta lưu lại kết quả sau khi chạy
        sys.stdout = open("test"+str(n)+".txt", "w")
        main(X, n)
        sys.stdout.close()
    