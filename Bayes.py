# Content of the text file is as follows:
data ="""
Weekday	Yes	Yes	Yes
Weekday	Yes	Yes	Yes
Weekday	No	No	No
Holiday	Yes	Yes	Yes
Weekend	Yes	Yes	Yes
Holiday	No	No	No
Weekend	Yes	No	Yes
Weekday	Yes	Yes	Yes
Weekend	Yes	Yes	Yes
Holiday	Yes	Yes	Yes
Holiday	No	Yes	Yes
Holiday	No	No	No
Weekend	Yes	Yes	Yes
Holiday	Yes	Yes	Yes
Holiday	Yes	Yes	Yes
Weekday	Yes	Yes	Yes
Holiday	No	Yes	Yes
Weekday	Yes	No	Yes
Weekend	No	No	Yes
Weekend	No	Yes	Yes
Weekday	Yes	Yes	Yes
Weekend	Yes	Yes	No
Holiday	No	Yes	Yes
Weekday	Yes	Yes	Yes
Holiday	No	No	No
Weekday	No	Yes	No
Weekday	Yes	Yes	Yes
Weekday	Yes	Yes	Yes
Holiday	Yes	Yes	Yes
Weekend	Yes	Yes	Yes
"""

data = data.strip().split('\n')

sum_samples = len(data)
sum_weekday, sum_weekend, sum_holidays,sum_disc, sum_nodisc, sum_deliv, sum_nodeliv, sum_purchase, sum_not_purchase = 0, 0, 0, 0, 0, 0, 0, 0, 0

px2_weekday, px2_weekend, px2_holidays, px2_disc, px2_nodisc, px2_deliv, px2_nodeliv = 0,0,0,0,0,0,0

npx2_weekday, npx2_weekend, npx2_holidays,npx2_disc, npx2_nodisc, npx2_deliv, npx2_nodeliv = 0,0,0,0,0,0,0

for line in data:
    day, disc, delivery, purchase = line.split()
    if day =="Weekday":
        sum_weekday +=1
        if purchase == "Yes":
            px2_weekday +=1
        elif (purchase == "No"):
            npx2_weekday +=1
    elif day == "Weekend":
        sum_weekend +=1
        if purchase == "Yes":
            px2_weekend +=1
        elif (purchase == "No"):
            npx2_weekend +=1
    elif day == "Holiday":
        sum_holidays +=1
        if purchase == "Yes":
            px2_holidays +=1
        elif (purchase == "No"):
            npx2_holidays +=1

    if disc == "Yes":
        sum_disc +=1
        if purchase == "Yes":
            px2_disc +=1
        elif (purchase == "No"):
            npx2_disc +=1
    elif disc == "No":
        sum_nodisc +=1
        if purchase == "Yes":
            px2_nodisc +=1
        elif (purchase == "No"):
            npx2_nodisc +=1

    if delivery == "Yes":
        sum_deliv +=1
        if purchase == "Yes":
            px2_deliv +=1
        elif (purchase == "No"):
            npx2_deliv +=1
    elif delivery == "No":
        sum_nodeliv +=1
        if purchase == "Yes":
            px2_nodeliv +=1
        elif (purchase == "No"):
            npx2_nodeliv +=1

    if purchase == 'Yes':
        sum_purchase += 1
    elif purchase == "No":
        sum_not_purchase += 1


p_purchase = sum_purchase/sum_samples
p_nopurchase = sum_not_purchase/sum_samples

p_weekday = sum_weekday/sum_samples
p_weekend = sum_weekend/sum_samples
p_holidays =sum_holidays/sum_samples

p_disc = sum_disc/sum_samples
p_nodisc = sum_nodisc/sum_samples

p_deliv =sum_deliv/sum_samples
p_nodeliv=sum_nodeliv/sum_samples

def calculate_conditional(x, y):
    return x / y if y != 0 else 0

# days
weekday_p = calculate_conditional(sum_weekday,sum_purchase)
weekday_np = calculate_conditional(sum_weekday,sum_not_purchase)
weekend_p = calculate_conditional(sum_weekend,sum_purchase)
weekend_np = calculate_conditional(sum_weekend,sum_not_purchase)
holiday_p = calculate_conditional(sum_holidays,sum_purchase)
holiday_np = calculate_conditional(sum_holidays,sum_not_purchase)

# discount
discount_p = calculate_conditional(sum_disc,sum_purchase)
discount_np = calculate_conditional(sum_disc,sum_not_purchase)
nodiscount_p = calculate_conditional(sum_nodisc,sum_purchase)
nodiscount_np = calculate_conditional(sum_nodisc,sum_not_purchase)

# delivery
delivery_p = calculate_conditional(sum_deliv,sum_purchase)
delivery_np = calculate_conditional(sum_deliv,sum_not_purchase)
nodelivery_p = calculate_conditional(sum_nodeliv,sum_purchase)
nodelivery_np =calculate_conditional(sum_nodeliv,sum_not_purchase)


# weekday no yes (purchase & not purchase)
def calculation(Day, Discount, Delivery):
    Day_1, Day_2, Day_3 = 0, 0, 0
    #This to check the day
    if Day == "Weekday":
        Day_1 = p_weekday
        Day_2 = px2_weekday
        Day_3 = npx2_weekday
    elif Day == "Weekend":
        Day_1 = p_weekend
        Day_2 = px2_weekend
        Day_3 = npx2_weekend
    elif Day == "Holiday":
        Day_1 = p_holidays
        Day_2 = px2_holidays
        Day_3 = npx2_holidays

    Discount_1, Discount_2, Discount_3 = 0, 0, 0
    #This is to check have discount or not
    if Discount == "Yes":
        Discount_1 = p_disc
        Discount_2 = px2_disc
        Discount_3 = npx2_disc
    elif Discount == "No":
        Discount_1 = p_nodisc
        Discount_2 = px2_nodisc
        Discount_3 = npx2_nodisc

    Delivery_1, Delivery_2, Delivery_3 = 0, 0, 0
    #This is to check have free delivery or not
    if Delivery == "Yes":
        Delivery_1 = p_deliv
        Delivery_2 = px2_deliv
        Delivery_3 = npx2_deliv
    elif Delivery == "No":
        Delivery_1 = p_nodeliv
        Delivery_2 = px2_nodeliv
        Delivery_3 = npx2_nodeliv

    d_purchase  = p_purchase
    d_nopurchase = p_nopurchase

    px = Day_1 * Discount_1 *Delivery_1

    px2_purchase = Day_2/sum_purchase*Discount_2/sum_purchase*Delivery_2/sum_purchase

    px2_nopurchase =  Day_3/sum_not_purchase*Discount_3/sum_not_purchase*Delivery_3/sum_not_purchase

    bayes_purchase = px2_purchase * d_purchase / px
    bayes_nopurchase = px2_nopurchase * d_nopurchase / px
    
    print("It is",Day,", and there is",Discount,"discount",", and has",Delivery, "free delivery")
    print("===================================================================")
    print("Probability of people purchasing: ", bayes_purchase)
    print("Phe probability of people not purchasing: ", bayes_nopurchase)
    print("===================================================================")

day = "Weekday"

have_discount = "No"

have_freeDelivery = "Yes"

calculation(day,have_discount,have_freeDelivery)


 