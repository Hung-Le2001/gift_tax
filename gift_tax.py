import math
LOWER_LIMITS = [5000, 25000, 55000, 200000, 1000000]
TAX_PERCENTS_RELATIVES = [0.08, 0.10, 0.12, 0.15, 0.17]
TAX_PERCENTS_OTHERS = [0.19, 0.25, 0.29, 0.31, 0.33]

def calculate_gift_tax(gift_value, relative):
    if relative == 'yes':
        case = 0
        START_TAX = 100
        while gift_value - LOWER_LIMITS[case +1] > 0:
            case +=1
            START_TAX = START_TAX + (LOWER_LIMITS[case] - LOWER_LIMITS[case -1]) * TAX_PERCENTS_RELATIVES[case -1]
            if case == 4:
                break            
        gift_tax = START_TAX + (gift_value - LOWER_LIMITS[case]) * TAX_PERCENTS_RELATIVES[case]
        return int(gift_tax)
    
    else:
        case = 0
        START_TAX = 100
        while gift_value - LOWER_LIMITS[case +1] > 0:
            case += 1
            START_TAX = START_TAX + (LOWER_LIMITS[case] - LOWER_LIMITS[case -1]) * TAX_PERCENTS_OTHERS[case -1]
            if case == 4:
                break
        gift_tax = START_TAX + (gift_value - LOWER_LIMITS[case]) * TAX_PERCENTS_OTHERS [case]
        return int(gift_tax)
    
def calculate_gift_tax_willing_pay (gift_tax, gift_value, relative):
    gift_tax_willing_pay = int(input('How much gift tax are you willing to pay at most?\n'))
    parts = math.ceil(gift_tax / gift_tax_willing_pay)
    years_to_give_whole_gift = (parts - 1) * 3
    gift_value_per_part = gift_value // parts
    tax_per_part = calculate_gift_tax(gift_value_per_part , relative)
    print ('You would have to part the gift in {} parts ({:.2f} euros per part).\n'.format(parts, gift_value_per_part))
    print ('Tax would be {:.2f} euros per part and {:.2f} euros in total.\n'.format(tax_per_part, tax_per_part*parts))
    print ('It would take you {} years to give away the whole gift.'.format(years_to_give_whole_gift))
    
def main():
    gift_value = int(input('Enter the value of the gift: \n'))
    gift_value= int(gift_value /100) *100
    relative = input ('Is the receiver a close relative (yes/no)?\n')
    if gift_value < 5000:
        print ('Gift tax is 0.00 euros')
    else:
        gift_tax = calculate_gift_tax(gift_value, relative)
        print ('Gift tax is {:.2f} euros.'.format(gift_tax))
    calculate_gift_tax_willing_pay (gift_tax, gift_value, relative)
      

main()


















