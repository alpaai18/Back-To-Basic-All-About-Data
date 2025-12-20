import numpy as np

def calculate(input_function):
    change_to_list = list(map(int, input_function))

    if len(change_to_list) == 9:
        # reshape process
        transform_to_3x3_matrix = np.array(change_to_list).reshape(3,3)
        
        # calculation the target
            # mean
        mean_axis_0 = np.mean(transform_to_3x3_matrix, axis=0).tolist()
        mean_axis_1 = np.mean(transform_to_3x3_matrix, axis=1).tolist()
        mean_all = np.mean(transform_to_3x3_matrix).tolist()
        
            # variance
        variance_axis_0 = np.var(transform_to_3x3_matrix, axis=0).tolist()
        variance_axis_1 = np.var(transform_to_3x3_matrix, axis=1).tolist()
        variance_all = np.var(transform_to_3x3_matrix).tolist()
        
            # std
        standard_deviation_axis_0 = np.std(transform_to_3x3_matrix, axis=0).tolist()
        standard_deviation_axis_1 = np.std(transform_to_3x3_matrix, axis=1).tolist()
        standard_deviation_all = np.std(transform_to_3x3_matrix).tolist()
        
            # max
        max_axis_0 = np.max(transform_to_3x3_matrix, axis=0).tolist()
        max_axis_1 = np.max(transform_to_3x3_matrix, axis=1).tolist()
        max_all = np.max(transform_to_3x3_matrix).tolist()
        
            # min
        min_axis_0 = np.min(transform_to_3x3_matrix, axis=0).tolist()
        min_axis_1 = np.min(transform_to_3x3_matrix, axis=1).tolist()
        min_all = np.min(transform_to_3x3_matrix).tolist()
        
            # sum
        sum_axis_0 = np.sum(transform_to_3x3_matrix, axis=0).tolist()
        sum_axis_1 = np.sum(transform_to_3x3_matrix, axis=1).tolist()
        sum_all = np.sum(transform_to_3x3_matrix).tolist()
        
        
        
        target_dictionary = {
        'mean'                  : [mean_axis_0, mean_axis_1, mean_all],
        'variance'              : [variance_axis_0, variance_axis_1, variance_all],
        'standard deviation'    : [standard_deviation_axis_0, standard_deviation_axis_1, standard_deviation_all],
        'max'                   : [max_axis_0, max_axis_1, max_all],
        'min'                   : [min_axis_0, min_axis_1, min_all],
        'sum'                   : [sum_axis_0, sum_axis_1, sum_all],
    }
    else:
        print("List must contain nine numbers.")
        
    return list(target_dictionary.items())

# calculate(input(list(str('Submit 9 numbers: '))))
calculate(list(str('123456789')))