import numpy


def calculate(list):
    if len(list) != 9:
        return ('List must contain nine numbers.')
    else:
        # transform input (type = list) to np.array 3x3
        data = numpy.array(list).reshape((3, 3))
        print('data: ', data)
        print('data ndim: ', data.ndim)
        print('data shape: ', data.shape)
        print('data size: ', data.size)

        # np.array -> reshape(9) == .flatten())
        flt_matrix = numpy.array(data).reshape(1,9)
        print('flt_matrix: ', flt_matrix)
        print('type flt_matrix: ', type(flt_matrix))
        print('flt_matrix ndim: ', flt_matrix.ndim)
        print('flt_matrix shape: ', flt_matrix.shape)
        print('flt_matrix size: ', flt_matrix.size)

        #flattened calcs
        flt_mean = numpy.mean(flt_matrix)
        flt_var = numpy.var(flt_matrix)
        flt_std = numpy.std(flt_matrix)
        print('mean: ', flt_mean)
        print('var: ', flt_var)
        print('std: ', flt_std)

        # Axis 1 & 2 == Axis 0 & 1 (assuming axis 0 == axis 1 (as called on the assignment))
        # if you change 0 to 1 and 1 to 2 -> IndexError: tuple index out of range
        mean_axis1 = numpy.mean(data, axis=0).tolist()
        mean_axis2 = numpy.mean(data, axis=1).tolist()
        var_axis1 = numpy.var(data, axis=0).tolist()
        var_axis2 = numpy.var(data, axis=1).tolist()
        std_axis1 = numpy.std(data, axis=0).tolist()
        std_axis2 = numpy.std(data, axis=1).tolist()
        # assemble_dict()
        calc_dict = {
            'mean': [mean_axis1, mean_axis2, flt_mean],
            'variance': [var_axis1, var_axis2, flt_var],
            'standard deviation': [std_axis1, std_axis2, flt_std]
        }
        print('Calculations Dictionary: ', calc_dict)
        return calc_dict