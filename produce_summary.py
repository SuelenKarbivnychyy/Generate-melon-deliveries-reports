""" Generate melon deliveries reports """

def prepare_report(file_name): # function definition
    daily_report = open(file_name) #open each file per time assigned to daily_report variable

    final_report = "" # created an empty variable, will use it later to avoid overwrite each report.
    
    for line in daily_report: #Iterating thought each line of the file
        line = line.rstrip() #removing all whitespace on the right from each line
        words = line.split('|') #turning string into list at the given separator.

        melon = words[0] #assign the product from list position [0] to the melon variable
        count = words[1] #assign the product amount from list position [1] to the count variable
        amount = words[2] #assign the pricefrom list position [2] to the amount variable

        final_report = final_report + ( f"Delivered {count} {melon}s for total of ${amount} \n") # putting the report together with product / amount / price and add line in beetween the results. 
    return final_report    #returning the correct final report

print("Day 1 report")  # Especify which day is being returning
print(prepare_report("um-deliveries-day-1.txt")) #Calling the function and passing the first list "day1" as argument
print("Day 2 report") # Describing which day is being returning
print(prepare_report("um-deliveries-day-2.txt")) #Calling the function and passing the first list "day2" as argument
print("Day 3 report") #Describing which day is being returning
print(prepare_report("um-deliveries-day-3.txt")) #Calling the function and passing the first list "day3" as argument