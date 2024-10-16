facebook = input('Do you have facebook (Yes/No): ')
twitter = input('Do you have twitter (Yes/No): ')
instagram = input('Do you have instagram (Yes/No): ')
influencer = 0
if facebook == 'Yes':
    influencer+=1
if twitter == 'Yes':
    influencer+=1
if instagram == 'Yes':
    influencer+=1
if influencer>=2:
    print('You are a good influencer')
else:
    print("You are a bad influencer")