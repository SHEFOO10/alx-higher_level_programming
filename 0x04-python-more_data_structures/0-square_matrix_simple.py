#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
  new_matrix = []
  for rows in matrix:
        row = []
        for columns in rows:
            row.append(columns ** 2)
        new_matrix.append(row)
  return new_matrix
