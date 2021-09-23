"""
Sort Big File: Imagine you have a 20 GB file with one string per line. Explain how you would sort
the file.

A good algorighm to sort big files on disk is merge sort.
I would implement a merge sort where the split part creates new files and delete old ones, same for the merge part
One needs external sort: Breaks the big file into small chunks and sort them separately inserting into the file system. Then do the sorted merge of the files into a big one.


log(knlogn) time complexity where n is the number of strings and K is the size of the biggest string

"""



