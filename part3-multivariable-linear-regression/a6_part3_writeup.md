# Part 3 - Multivariable Linear Regression Writeup

After completing `a6_part3.py` answer the following questions

## Questions to answer

1. What is the R Squared coefficient for your model? What does that mean about the model in relation to your data?

.86. It means is stronlgy positivly correlated

2. Is your model accurate? Why or why not?

Its decenly accruate due to the high r2 val. But it ussaly underestimetes as 8/10 times the predictded val is lower than the actul val

3. What does the model predict a 10-year-old car with 89000 miles is worth? What about a car that is 20 years old with 150000 miles?

8752.17596198 and  1827.89235411 

4. You may notice that some of your predicted results are negative. This is occurring when the value of age and the mileage of the car are very high. Why do you think this is happening?

This is because the slope of the line of best fit will eveantully cross the x axis and go negative so if the age and milage is high enough it will predict a negative number. The computer does not know a car cant cost negative dollars 