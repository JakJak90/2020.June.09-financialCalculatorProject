Task requirement:

A program that allows a user to access two different financial calculators: 
an investment calculator and a home loan repayment calculator

Planning:

User first needs to select type of calculator. 
	
	Selection can be performed using input command.
		Advantages:
			Simple, straight forward code
			Familiarity with method means less chance of introducing errors
			If assignment is tested via pre-set unit test, most likely to be successful
		
		Disadvantages:
			Checking for spelling and capitalisation required
			Worse user experience than simply selecting an option
			
		Conclusion:
			Most suitable method for assignment however a better option such as a drop down list or button
			should be added before implementing into portfolio
		
		Note:
			Once loops have been covered, implement a loop to not allow program to proceed until valid
			option has been selected - preferable to currently implementation of sys.exit() function
	
	
	Inquirer (PyInquirer for windows) library may work for keyboard selection.
		Advantages: 
			Eliminates need to check for spelling, capitalisation
			Lower effort required by user, no typing
			
		Disadvantages:
			Unsure how to go about implementing the library
			If assignment testing is performed via pre-set unit tests, it may cause issues with grading
			Unsure if the library would be required to be installed on tester's system to run
			Overcomplicating assignment
			
		Conclusion:
			Interesting idea to perhaps be looked at with refactoring prior to adding task to portfolio
			Unsuitable for task hand-in at the moment
			
			
User selection will determine type of calculation required
	
	an if/else statement would be suitable, with their own input prompts required as follows:
	
Calculation requirements for "investment" option
	
	Required information:
		Amount of money deposited
			data type float - low-medium possibility that cents would be included in deposit, however it 
			is possible especially if user is calculating based on existing compounded funds.
		
		Interest rate
			data type float - interest rates are often reported to 2 decimal places
		
		Number of years over which investment is planned
			data type float - very unlikely chance that investment period is set for fractions of a year,
			however user may have short time goal of 3 or 6 months investment
		
		Type of interest
			simple or compound. Aanswer, of data type string, will determine calculation formula
			
			note: as with the type of calculator decision above, refactoring to include a for loop to account 
			for spelling errors etc should be added in future. Additionally, if the Inquirer library proves 
			beneficial it should be considered as well, for the same reasons as stated above
			
			
Calculation requirements for "bond" option

	Required information:
		Present house value
			Data type float - Very likely that repayment will be made based on a percentage value which has
			a likely chance of calculating to a fractional value
		
		Interest rate
			data type float - interest rates are often reported to 2 decimal places
			
		Intended repayment term in months
			data type integer - extremely unlikely chance of a partial month being required


Running the calculations

	Formuals required for all 3 calculations (investment under simple interest, investment under compound interest
	and bond repayment) require simple arithmetic not requiring the extra functionality provided by the import math command.
	

Output
	
	For both investment calculations, a message indicating the expected value of the investment after the time period must
	be displayed
	
	For the home repayment calculation, a message stating the amount for the monthly instalment must be displayed