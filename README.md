# web-app
# Description: 
A partner of your company has requested to build a software application that will predict the rate of the fuel based on the following criteria:
- Client Location (in-state or out-of-state)
- Client history (existing customer with previous purchase or new)
- Gallons requested
- Company profit margin (%)

# Software must include following components:
- Login (Allow Client to register if not a client yet)
- Client Registration (Initially only username and Password)
- Client Profile Management (after client registers they should login first to complete profile)
- Fuel Quote Form with Pricing module (Once user enters all required information pricing module calculates the rate provides total cost)
- Fuel Quote History

A fuel company (FuelX) needs a system to track rate of fuel for clients. It wants to keep track of *CLient location, Client history, Gallons requested, and Company profit margin%.* The software will allow *login and Registration, Registration only needs username and password, After registration the client logs in to complete profile (location, etc), After all fields in the Fuel Quote Form are entered the Pricing Module will calculate total cost, Then the information will be saved in Client Fuel Quote History. 

# Classes:
Login
- username: string
- password: string
- isValid(): boolean
- register()

Client
-firstName
-lastName

Company
- fuelRate: int
+ profitMargin(): int

History
- client
- orderDate: date

FuelQuote
- date
- location: boolean (in-state or out-of-state)
- gallonRequest: int
+ priceCalc(): int
