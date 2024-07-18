days_since_release = 139
original_price = 60
greatest_hits = False

#Write a conditional that determines the price of a
#newly-released game, movie, or album based on the time since
#it was released.
#
#Assume that a new release loses $2 off its price for every
#full week since it was released. So, two full weeks (14 days)
#after a $60 game is released, it will cost $56.
#
#However, if the release is considered a "greatest hit", it
#loses value half as fast: after two weeks, it will be $58
#instead of $56.
#
#No release will ever fall to below $20, however, no matter
#how fast it loses value or whether it's a greatest hit.
#
#Add some code below to print the current price of the release.
#For example, with the values above, it would pring $58.


#Add your code here! Make sure to print the dollar sign, too.

def game_price(input_days_since_release, input_original_price, input_greatest_hits):
    price_decay = (input_days_since_release // 7) * 2
    if input_greatest_hits:
        price_decay /= 2      
    current_price = (int(input_original_price - price_decay))
    if current_price < 20:
        current_price = 20
    return "$"+ str(current_price)

print(game_price(days_since_release, original_price, greatest_hits))





