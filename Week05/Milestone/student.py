import csv

key_column_index = 0
key_name_index = 1

def main():
  i_number = input("Type student's I-Number:")
  i_number = i_number.replace('-','')
  students = read_dictionary('Week05/Milestone/students.csv', key_column_index)
  if i_number in students:
    print(students[i_number])
  else:
    print('No such student')

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.
    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    students = {}
    with open(filename, "rt") as student_file:
        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(student_file)
        # The first row of the CSV file contains column
        # headings and not data about a dental office,
        # so this statement skips the first row of the
        # CSV file.
        next(reader)
        for row_list in reader:
            # If the current row is not blank, add the
            # data from the current to the dictionary.
            if len(row_list) != 0:
                # From the current row, retrieve the data
                # from the column that contains the key.
                key = row_list[key_column_index]
                # Store the data from the current
                # row into the dictionary.
                students[key] = row_list[key_name_index]
        return students


# Call main to start this program.
if __name__ == "__main__":
    main()