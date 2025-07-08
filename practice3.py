# The volume of a sphere with a radius r is 4/3(pie)r^3. What is the volume of sphere with the radius 5?
import math

def volume(r):
   return 4/3*math.pi*r**3


print(volume(5))

# the cover price of a book is $24.95, bookstores get a 40% discount, shipping is $3 first book $0.75 after, find cost for 60 books
 
quantity = 60
price = 24.95 ; 
discount = price * 0.40 ; 
bookstore_price =  price - discount; 
shipping = 3 + (0.75*(quantity-1)) ; 
total_cost = bookstore_price * quantity + shipping ; 
print(f"The total cost for {quantity} books is: ${total_cost:2f}")

#Left house at 6:52am, ran 1 mile at an easy pace 8:15 per mile, then 3 miles at tempo 7:12 per mile and 1 mile at easy
#What time do I reach home?

easy_pace = 8 + (15/60)
tempo = 7 + (12/60)
distance_ran = easy_pace + (tempo*3) + easy_pace
print(distance_ran)
print(f"You will reach home about {distance_ran} minutes after start time of 06:52am: around 7:31am")


#Create a function that prints something twice, four times
def print_twice(test):
   print(test)
   print(test)

print_twice ( ("Jahlique" + " ") * 4)

#Write a function called right_justify that takes a string named s and prints the string with enough leading 
#spaces so that the last letter of the string is in column 70 of the display

def right_justify(s):
   spaces = 70 - len(s)
   print(" " * spaces + s)

right_justify('smoke')

#Write a function that draws a grid that looks like the following + - - - - + - - - - +
#                                                                 |         |         |
#                                                                 |         |         |
#                                                                 |         |         |
#                                                                 |         |         |
#                                                                 + - - - - + - - - - +
#                                                                 |         |         |
#                                                                 |         |         |
#                                                                 |         |         |
#                                                                 |         |         |
#                                                                 + - - - - + - - - - +

def draw_grid():
   top = ("+" + (" " + " - ") * 4) + " " + ("+" + (" " + " - ") * 4) + " " + "+"
   side = "|" + " " * 17 + "|" + " " * 17 + "|"
   print(top)
   print(side)
   print(side)
   print(side)
   print(side)
   print(top)
   print(side)
   print(side)
   print(side)
   print(side)
   print(top)

draw_grid()

# Write a function that drawsa similar grid with four rows and four columns
