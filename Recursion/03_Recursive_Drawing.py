# *****
# ****
# ***
# **
# *
# #
# ##
# ###
# ####
# #####

def draw(n):
    if n == 1:
        return '*'

    if n > 1:
        return '*' + draw(n - 1)


number = int(input())
print(draw(number))
