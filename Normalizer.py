# Python program to remove duplicates, the order of
# characters is not maintained in this program
 
# Utility function to convert string to list
def toMutable(string):
    temp = []
    for x in string:
        temp.append(x)
    return temp
 
# Utility function to convert string to list
def toString(List):
    return ''.join(List)
 
# Function to remove duplicates in a sorted array
def removeDupsSorted(List):
    res_ind = 1
    ip_ind = 1
 
    # In place removal of duplicate characters
    while ip_ind != len(List):
        if List[ip_ind] != List[ip_ind-1]:
            List[res_ind] = List[ip_ind]
            res_ind += 1
        ip_ind+=1
 
    # After above step string is stringiittg.
    # Removing extra iittg after string
    string = toString(List[0:res_ind])
 
    return string
 
# Function removes duplicate characters from the string
# This function work in-place and fills null characters
# in the extra space left
def removeDups(string):
    # Convert string to list
    List = toMutable(string)
 
    # Sort the character list
    # List.sort()
 
    # Remove duplicates from sorted
    return removeDupsSorted(List)
 
# Driver program to test the above functions
# string = "waaaaaaaaaaaaaaaaaaw"
# print (removeDups(string))
 
# This code is contributed by Bhavya Jain