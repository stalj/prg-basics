facebook = True
twitter = True
instagram = False

if facebook and twitter:
    print('You are a good influencer')
elif twitter and instagram:
    print('You are a good influencer')
elif facebook and instagram:
    print('You are a good influencer')
else:
    print('You are a bad influencer')