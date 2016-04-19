# fredknows.it Code Challenge

The scope of this challenge is to create an API application responding to an endpoint called ``probabilities``. For the purpose of this challenge we expect you to use Python.  We are mainly interested in code style and structure.

## Specifications

* You can find our dataset here: https://docs.google.com/spreadsheets/d/1GH_-stmmKIK7NvrQLPTVtfgpIYXTX3SNlqh-U78ZmDM/edit

* Transform this dataset into a database. You can use a storage engine of your choice

* Create an API endpoint that gets the probability of persons that match given attributes. We assume that there is a chance of 20% that an attribute is accidentally wrong. The URL could like that: ``/probabilities/{attribute-1}/{attribute-2}/{attribute-3}/.../{atrribute-n}``

* **Example**: 
	
	``GET /probabilities/blond/politician`` returns 
	
	```	
	{
		'Person 1': 0.512, 
		'Person 2': 0.128,
		'Person 3': 0.128,
		'Person 4': 0.032,
		...
	}
		
	```
	
## Bonus

* Create an automatic test for this endpoint. It could be a functional or unit test. Decide for one.


## Procedure

1. Please do the following at least **48 hours in advance**:
    - Push your final code to public git repository (GitHub or bitbucket)
    - Send an email to fredknows.it to notify them about your work
    
2. On the **day of the challenge**:
    - Be prepared to provide a quick overview over your code (shouldn't take longer than 10 - 15 minutes)
    - Be able to explain how you resolved the challenge to a couple of people from our team
    - Be able to answer questions about your implementation

All in all the whole event will probably not take longer than 60 minutes.