# age = 20
# if age >= 18:
#     print( 'You age is:', age )
#     print('你已经成年')
# elif age <= 10:
#     print('attion')

birth = input('Birth:')
birth = int( birth )
if birth > 2000:
    print( '00后' )
else:
    print( '00前' )