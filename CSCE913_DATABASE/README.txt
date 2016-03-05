There are 4 files
1. phylogenetic.py which is code written in python
2. 'table.txt' which is used to create search table
3.  'DNA-database.txt' which contains sample data
4. 'README.txt' which contains description of the files

In the code phylogenetic.py, there are two parts.
The first part of the code is used to create table by using file table.txt.

The second part of the code is used to read sample data information and search each sample
through each node in the tree (which information is stored in table), and each node has some
values. The code search values in each node, if any value is contained in the sample data, it would
increment com_value (compare value, which is used to store how many values in each node the sample has).
The code could output the Classification in the end. You also could uncomment lines 64, 69, 70
  # print 'value = ',value
  # print 'max_value = ', max_value
  # print 'label = ', label, '\n\n'

to print intermediate information like how many values in some node contain sample data information,
which node has the maximum values, and the related maximum value.
                 
