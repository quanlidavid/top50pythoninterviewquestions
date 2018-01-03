# 49. What is the output of following code in Python?
# >>>name = 'John Smith'
# print name[:5]+name[5:]

"""
John Smith

This is an example of Slicing. Since we are slicing at the same index,
the first name[:5] gives the substring name upto 5th location excluding 5th location.
The name[:5] gives the rest of the substring of name from the 5th location.
So we get the full name as output.
"""
