# -*- coding: utf-8 -*-


def convert_to_words(num):
    """
    https://www.geeksforgeeks.org/convert-number-to-words/


    Parameters
    ----------
    num : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
 
    # Get number of digits
    # in given number
    l = len(num)
 
    # Base cases
    if (l == 0):
        print("empty string")
        return
 
    if (l > 4):
        print("Length more than 4 is not supported")
        return
 
    # The first string is not used,
    # it is to make array indexing simple
    single_digits = ["zero", "one", "two", "three",
                     "four", "five", "six", "seven",
                     "eight", "nine"]
 
    # The first string is not used,
    # it is to make array indexing simple
    two_digits = ["", "ten", "eleven", "twelve",
                  "thirteen", "fourteen", "fifteen",
                  "sixteen", "seventeen", "eighteen",
                  "nineteen"]
 
    # The first two string are not used,
    # they are to make array indexing simple
    tens_multiple = ["", "", "twenty", "thirty", "forty",
                     "fifty", "sixty", "seventy", "eighty",
                     "ninety"]
 
    tens_power = ["hundred", "thousand"]
 
    # Used for debugging purpose only
    #print(num, ":", end=" ")
    
    result=""
 
    # For single digit number
    if (l == 1):
        #print(single_digits[ord(num[0]) - 48])
        result+="{}".format(single_digits[ord(num[0]) - 48])
        return result
    # Iterate while num is not '\0'
    x = 0
    while (x < len(num)):
 
        # Code path for first 2 digits
        if (l >= 3):
            if (ord(num[x]) - 48 != 0):
                #print(single_digits[ord(num[x]) - 48],
                #      end=" ")
                result+="{} ".format(single_digits[ord(num[x]) - 48])
                #print(tens_power[l - 3], end=" ")
                result+="{} ".format(tens_power[l - 3])

                # here len can be 3 or 4
 
            l -= 1
 
        # Code path for last 2 digits
        else:
 
            # Need to explicitly handle
            # 10-19. Sum of the two digits
            # is used as index of "two_digits"
            # array of strings
            if (ord(num[x]) - 48 == 1):
                sum = (ord(num[x]) - 48 +
                       ord(num[x+1]) - 48)
                #print(two_digits[sum])
                result+="{} ".format(two_digits[sum])

                return result
 
            # Need to explicitly handle 20
            elif (ord(num[x]) - 48 == 2 and
                  ord(num[x + 1]) - 48 == 0):
                #print("twenty")
                result+="{}".format("twenty")

                return result
 
            # Rest of the two digit
            # numbers i.e., 21 to 99
            else:
                i = ord(num[x]) - 48
                if(i > 0):
                    #print(tens_multiple[i], end=" ")
                    result+="{} ".format(tens_multiple[i])

                else:
                   # print("", end="")
                    result+=""

                x += 1
                if(ord(num[x]) - 48 != 0):
                    #print(single_digits[ord(num[x]) - 48])
                    result+="{}".format(single_digits[ord(num[x]) - 48])

        x += 1
    return result


# convert_to_words("9923") # Four Digits
# convert_to_words("523") # Three Digits
# convert_to_words("89") # Two Digits
# convert_to_words("8") # One Digits

# print("---------")
# print("res",convert_to_words("36"))
# print("res",convert_to_words("101"))
# print("res",convert_to_words("5789"))