**Functional Programming**
# **BEFORE CLASS**
1. Watch the video ‘3 Simple Ideas From Functional Programming To Improve Your Code’:

   <https://youtu.be/4B24vYj_vaI?feature=shared>

1. Familiarise yourself with the basic concepts of functional programming:

   <https://www.geeksforgeeks.org/functional-programming-in-python/>

1. Read the text related to functional programming in Python:

   <https://www.codecademy.com/article/functional-programming-in-python>

1. Watch the video to learn about higher order functions:

   <https://youtu.be/xZtTIm3fpfA?feature=shared>

1. Explain the concepts related to functional programming:
   1. Pure function
   1. Side effect
   1. Higher order function
   1. First class function
   1. Anonymous function
   1. Recursion
1. Python offers functions that support the functional programming paradigm. Watch the video to learn how to use these functions.

   <https://youtu.be/hUes6y2b--0?feature=shared>
# **DURING CLASS**
## **Anonymous (lambda) function**
1. Write a program that calculates the arithmetic mean of two numbers. Use an anonymous function. Sample result:

   n1 = 5
   n2 = 10
   mean = lambda x,y: (x+y)/2
   result = mean(n1,n2)
   print(f"Arithmetic mean of {n1} and {n2} is {result}")

1. Write a program that converts speed in meters per second to speed in kilometers per hour. Define a function ms\_to\_kmh(ms) that returns the calculated speed in km/h. Sample result:

   10 m/s = 36 km/h
   35 m/s = 126 km/h

1. Write a program that converts speed in meters per second to speed in kilometers per hour. Use an anonymous function. Sample result:

   10 m/s = 36 km/h
   35 m/s = 126 km/h

1. Write a program that calculates the average speed of a vehicle. Enter from the keyboard: a distance in km, a number of travel hours and a number of travel minutes. Define a function avg\_speed(distance,hours,minutes) that returns the calculated average speed. Sample result:

   Enter distance in km: 70
   Enter number of travel hours: 1
   Enter number of travel minutes: 23
   Average speed: 50.6 km/h 

1. Write a program that calculates the average speed of a vehicle. Enter from the keyboard: a distance in km, a number of travel hours and a number of travel minutes. Use an anonymous function. Sample result:

   Enter distance in km: 70
   Enter number of travel hours: 1
   Enter number of travel minutes: 23
   Average speed: 50.6 km/h 
## **Higher-order function**
1. The educational course ends with a test checking the participants' knowledge. To pass the course, the participant must obtain a minimum number of points. Write a program that checks whether a participant has passed the course. Define a higher order function. Sample result:

   def min\_pts(limit):
   `    `def check(pts):
   `        `if pts >= limit:
   `            `return True
   `        `return False
   `    `return check

   print("=== MIN 50 PTS TO PASS ===")
   assess\_test = min\_pts(50)
   print(f"52 pts -> {assess\_test(52)}")
   print(f"39 pts -> {assess\_test(39)}")

   print("=== MIN 60 PTS TO PASS ===")
   assess\_test = min\_pts(60)
   print(f"52 pts -> {assess\_test(52)}")
   print(f"39 pts -> {assess\_test(39)}")

1. In a beverage factory, a machine fills bottles of various capacities. A computer checks whether a bottle has been filled correctly. The allowable tolerance is 2% for a 500ml bottle, 3% for a 1000ml bottle and 5% for a 1500ml bottle. Write a program that checks whether the bottle has been filled correctly or not. Define a higher order function. Sample result:

   507: True
   489: False
   984: True
   1032: False
   1578: False
   1430: True 
## **Data mapping**
1. The report below shows the last five credit card payments in Euro:

   15\.90
   38\.47
   4\.07
   132\.70
   9\.15

   Write a program that calculates and displays transaction amounts in Polish zlotys (1 EUR = 4.5 PLN). Use anonymous and map() functions. Sample result:

   eur = [15.90,38.47,4.07,132.70,9.15]
   pln = list(map(lambda x:x\*4.5, eur))
   # print pln list ...

   71\.55
   173\.11
   18\.31
   597\.15
   41\.17

1. For the following text:

   I completely agree with you

   write a program that calculates and displays the number of letters in each word. Use the map() and an anonymous functions to calculate the number of letters. Tip: to split text into words, use the split() function. Sample result:

   Text: I completely agree with you
   No. of letters in words: [1,10,5,4,3]

1. The data below contains a list of products available in stock and their unit price.

   stock = [(20,5.50),(15,8.30),(37,3.85),(4,11.60)]

   Write a program that calculates the total value of products in stock. Use the map(), sum() and an anonymous function. Sample result:

   Products in stock: [(20,5.50),(15,8.30),(37,3.85),(4,11.60)]
   Total value: 423.35
## **Data filtering**
1. The following people are employed in one of the company's departments:

   SMITH Lucy
   JONES Janet
   LEE Jerry
   JACKSON Peter
   JOHNSON Rick
   LEWIS Terry
   CLARKE Robin

   Save the list of employees in a string array. Then, write a program that displays people whose surnames start with the letter 'J'. Use anonymous and filter() functions. Sample result:

   employees = ["SMITH Lucy","JONES Janet","LEE Jerry",
   `             `"JACKSON Peter","JOHNSON Rick",
   `             `"LEWIS Terry","CLARKE Robin"]
   emp\_J = list(filter(lambda e:e[0]=="J", employees))
   # print a list … 
   ...

   JONES Janet
   JACKSON Peter
   JOHNSON Rick

1. A speed camera located in a city measures the speed of passing vehicles. The maximum permitted speed of vehicles is 50 km/h. In the last minute, the speed camera recorded the following values:

   48,47,54,50,42,68,39,46

   Write a program that displays speed values higher than the allowed speed. Use anonymous and filter() functions. Sample result:

   Recorded values: 48,47,54,50,42,68,39,46
   Speed too high: 54,68

1. The final grades obtained by students in the "Economic Geography" course are included in the array:

   [3.0,5.0,2.0,3.5,4.0,4.0,3.5,2.0,4.0,2,0]

   Write a program that calculates the arithmetic mean of the grades, excluding negative grades (2.0). Use the filter() along with an anonymous function. Sample result:

   Arithmetic mean for grades <> 2.0 is 3.85
# **AFTER CLASS**
1. An array contains numbers from 1 to 20. Write a program that calculates and displays their third power. Use the map() and an anonymous function.
1. An array contains numbers from 1 to 20. Write a program that displays only numbers divisible by 2 and 3 without remainder. Use the filter() and an anonymous function.
1. The array below contains employee data: 

   [("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),
   ` `("Jackson","Peter"),("Johnson","Rick"),
   ` `("Lewis","Terry"),("Clarke","Robin")]

   Write a program that determines and displays a list of employees whose last names are given in capital letters followed by first names, separated by commas. Sample result:

   SMITH, Lucy
   JONES, Janet
   …
   …

1. In ski jumping competitions, each competitor is assessed by five judges. Each judge can award a score from 0 to 20 points. The highest and lowest scores are discarded. The remaining three scores are added up to form the final score obtained by the competitor. The ratings of four players are presented below.

   [(17,15,16,17,15),
   ` `(16,18,19,17,19),
   ` `(19,15,15,19,18),
   ` `(18,17,19,15,16)]

   Calculate and display the total points obtained by competitors. Tip: use the Python built-in functions: map(), sum(), min(), max(). Sample result:

   [48, 54, 52, 51]

1. The educational course finished with a test checking the participants' knowledge. Here are the results obtained by the students:

   [37,51,44,23,78,92,39,84,83,51]

   Write a program that calculates and displays student scores that are equal to or greater than the following minimum number of points to pass the course:

   1. 70
   1. 40
   1. 30

Use the filter() function and the following higher order function:

def min\_pts(limit):
`    `return lambda pts: pts>=limit

Sample result:

Min 70 pts: [78, 92, 84, 83]
Min 40 pts: [51, 44, 78, 92, 84, 83, 51]
Min 30 pts: [37, 51, 44, 78, 92, 39, 84, 83, 51]

1. Measuring stations recorded the following temperatures in degrees Celsius:

   {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}

   Write a program that displays the names of towns where positive temperatures were recorded. Use anonymous and filter() functions. Sample result:

   `	`Cities with positive temperatures: Krakow Sopot Opole

1. Measuring stations recorded the following temperatures in degrees Celsius:

   {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}

   Write a program that creates a bar chart showing temperatures recorded in cities. Add a title for the chart and descriptions for the x and y axes. Tip: use the map() function to create two arrays of data for the chart.

1. Students obtained the following test results (in points, from 0 to 100):

   test\_results = [
   `    `{"name":"Peter","result":27},
   `    `{"name":"Anna","result":63},
   `    `{"name":"Robert","result":92},
   `    `{"name":"Paul","result":46},
   `    `{"name":"Barbara","result":52}]

   Write a program that displays students whose scores are between 50 and 70 points. Use an anonymous function and filter() function.

1. At one of the Olympic Games, the medal classification is as follows:

   {"country":"Denmark","gold":2,"silver":4,"bronze":6}
   {"country":"Finland","gold":5,"silver":0,"bronze":4}
   {"country":"USA","gold":12,"silver":5,"bronze":11}
   {"country":"Peru","gold":0,"silver":1,"bronze":7}

   Write a program that displays the data of countries that have won at least 10 medals. Use anonymous and filter() functions. Sample result:

   COUNTRIES WITH AT LEAST 10 MEDALS
   Denmark: 2,4,6
   USA: 12,5,11

1. At one of the Olympic Games, the medal classification is as follows:

   {"country":"Denmark","gold":2,"silver":4,"bronze":6}
   {"country":"Finland","gold":5,"silver":0,"bronze":4}
   {"country":"USA","gold":12,"silver":5,"bronze":11}
   {"country":"Peru","gold":0,"silver":1,"bronze":7}

   Write a program that creates a bar chart showing the total number of medals won by each country. Add a title for the chart and descriptions for the x and y axes. Tip: Use the map() function to create arrays of data for your chart.

1. In a beverage factory, a machine fills 500ml bottles. The computer checks whether the bottle has been filled correctly. For a 500ml bottle, the allowable tolerance is 2%. In the last ten bottles checked, the filling was:

   508,500,512,499,492,511,503,476,501,509

   Write a program that calculates the percentage of incorrectly filled bottles. Use the filter() along with a higher order function. Sample result:

   Bottle capacity:    500ml
   Filling tolerance:  2%
   Filled bottles:     508,500,512,499,492,511,503,476,501,509
   Incorrectly filled: 30%


1

