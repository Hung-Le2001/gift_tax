import math
LOWER_LIMITS = [5000, 25000, 55000, 200000, 1000000]
TAX_PERCENTS_RELATIVES = [0.08, 0.10, 0.12, 0.15, 0.17]
TAX_AT_LOWER_LIMIT_RELATIVES = [100, 1700, 4700, 22100, 142100]
TAX_PERCENTS_OTHERS = [0.19, 0.25, 0.29, 0.31, 0.33]
TAX_AT_LOWER_LIMIT_OTHERS = [100, 3900, 11400, 53450, 301450]

def calculate_gift_tax(gift_value, relative):
    if relative == 'yes':
        case = 4
        while gift_value - LOWER_LIMITS[case] < 0:
            case -= 1
        gift_tax = TAX_AT_LOWER_LIMIT_RELATIVES[case] + (gift_value - LOWER_LIMITS[case]) * TAX_PERCENTS_RELATIVES[case]
        return int(gift_tax)
    else:
        case = 4
        while gift_value - LOWER_LIMITS[case] < 0:
            case -= 1
        gift_tax = TAX_AT_LOWER_LIMIT_OTHERS[case] + (gift_value - LOWER_LIMITS[case]) * TAX_PERCENTS_OTHERS [case]
        return int(gift_tax)
    

def main():
    gift_value = int(input('Enter the value of the gift: \n'))
    relative = input ('Is the receiver a close relative (yes/no)?\n')
    if gift_value < 5000:
        print ('Gift tax is 0.00 euros')
    else:
        gift_tax = calculate_gift_tax(gift_value, relative)
        print ('Gift tax is {:.2f} euros.'.format(gift_tax))
    
    gift_tax_willing_pay = int(input('How much gift tax are you willing to pay at most?\n'))
    parts = math.ceil(gift_tax / gift_tax_willing_pay)
    years_to_give_whole_gift = (parts - 1) * 3
    gift_value_per_part = gift_value // parts
    tax_per_part = calculate_gift_tax(gift_value_per_part , relative)
    print ('You would have to part the gift in {} parts ({:.2f} euros per part).\n'.format(parts, gift_value_per_part))
    print ('Tax would be {:.2f} euros per part and {:.2f} euros in total.\n'.format(tax_per_part, tax_per_part*parts))
    print ('It would take you {} years to give away the whole gift.'.format(years_to_give_whole_gift))  

main()

















