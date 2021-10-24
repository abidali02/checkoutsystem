from collections import Counter
from price_reader import *

# defining all the rule for price calculation for each item in separate function


def atv_rule(count):    # atv_rule function is to calculate the total cost of the Apple TV
    if count % 3 == 0:
        price = ((count/3)*2)*atv_price
    else:
        price = (count // 3) * 2 * atv_price + ((count % 3) * atv_price)
    return price


def ipd_rule(count):    # ipd_rule function is to calculate the total cost of the Super iPad
    if count > 4:
        price = count*499.99
    else:
        price = count*ipd_price
    return price


def mbp_rule(count):    # mbp_rule function is to calculate the total cost of the MacBook Pro
    price = count*mbp_price
    return price


def vga_rule(count, mbp_count):     # mbp_rule function is to calculate the total cost of the VGA adapter
    if count <= mbp_count:
        price = 0
    else:
        price = (count-mbp_count) * vga_price
    return price


def price_calculator(input_str):   # logic function is to call the calculation function for each item
    string_list = input_str.split(",")  # string_list is to store the split input on the basis of comma
    obj_counter = Counter(string_list)
    bar_code_list = obj_counter.most_common()   # changing input into list with number of occurrence of each item

    total_cost = 0  # initiating total_cost as zero
    mbp_count = 0   # initiating macbook pro count as zero
    # this will be used during vga cost calculation

    for element in bar_code_list:   # looping all the element from input list
        if element[0] == "atv":     # if barcode is atv its calling apple tv rule function for calculation
            atv_cost = atv_rule(element[1])
            total_cost = total_cost+atv_cost    # adding apple tv cost in total cost

        elif element[0] == "ipd":   # if barcode is ipd its calling ipd rule function for calculation
            ipd_cost = ipd_rule(element[1])
            total_cost = total_cost+ipd_cost    # adding ipd cost in total cost

        elif element[0] == "mbp":   # if barcode is mbp, calling macbook pro rule function for calculation
            mbp_cost = mbp_rule(element[1])
            total_cost = total_cost+mbp_cost    # adding macbookPro cost in total cost
            mbp_count = element[1]      # updating mbp_count which will be used for vga cost calculation

        elif element[0] == "vga":   # if barcode is vga, calling vga rule function for calculation
            vga_cost = vga_rule(element[1], mbp_count)
            total_cost = total_cost+vga_cost    # adding VGA Adapter cost in total cost

        else:   # if input is new item, calling default function which will just multiply each item price x count
            print(element[0] + " is not a valid SKU, please check the spelling or extra whitespace")
    return total_cost   # returning total_cost after adding all items cost


