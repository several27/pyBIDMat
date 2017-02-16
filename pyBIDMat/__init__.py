import struct

def input_read_float(stream):
    return struct.unpack('<f', stream.read(4))[0]

def input_read_int(stream):
    return struct.unpack('<i', stream.read(4))[0]

def read_fmat(filename):
    columns = []
    rows = []
    values = []
    fmat = None
    with open(filename, 'rb') as fmat_input:
        mtype = str(input_read_int(fmat_input))

        nrows = input_read_int(fmat_input)
        ncols = input_read_int(fmat_input)
        nnz = input_read_int(fmat_input)

        # Dense matrix
        if mtype[0] == '1':
            fmat = numpy.zeros((nrows, ncols))

            for i in range(nrows * ncols):
                fmat[i - nrows * int(i / nrows), int(i / nrows)] = input_read_float(fmat_input)

        # Sparse matrix
        if mtype[0] == '2':
            for i in range(ncols + 1):
                columns.append(input_read_int(fmat_input))

            for i in range(nnz):
                rows.append(input_read_int(fmat_input))

            for i in range(nnz):
                values.append(input_read_float(fmat_input))

            # Reading sparse matrices
            tuples = []
            previous_column = 0
            for i in range(len(columns)):
                if i == 0:
                    continue

                column = columns[i]

                for j in range(previous_column, column):
                    tuples.append((rows[j], i - 1, values[j]))

                previous_column = column

    return fmat
