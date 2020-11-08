# Chatbot for Hotel 

Objective -
To build a simple chatbot for a hotel. The chatbot should be able to respond to and handle the following basic functionalities

1. Book room
2. Request Room Cleaning
3. Handle FAQs
4. Handle Greetings

Prerequisite: RASA (2.0.0), python(3.6.8)

<h1>Installation Step</h1>
Install Rasa Framework in a fresh virtual environment. 
<h3>Note:</h3> If you find error while installing Rasa 2.0.0 on your system, it is because pip has been updated after October, so might take some time to fix several issues. To work properly, if you see "sanic" version error, degrade it to 20.6.3 by using <h4>pip install sanic==20.6.3 </h4>.It will resolve the error.


<h2>To setup:</h2>  
1. Clone this repo 

2. cd into the directory

3. make a models directory

3. run command "rasa train"

4. to interact with the chatbot in the terminal run command "rasa shell"

<h2>Book Room</h2>
User: I want to book a room.

Bot: How many rooms would you like to book?

User: 2 rooms

Bot: What type of room would you want to book?

Button1 - Simple
Button 2 - Deluxe
User: (Clicks on Button 1)

Bot: You have chosen to book 2 simple rooms

(Clicking on button 2 should be handled similarly)

<h2>Clean room</h2>
Schedule cleaning right away -
User: I want to have my room cleaned

Bot: When should I arrange for a cleaning?

User: Could you send someone right now?

Bot: Sure, I will send someone to your room right away.

<h1>FAQs</h1>

<h2>Check-in timings -</h2>
User: What are your check-in timings?

Bot: Check-in time starts at 4 PM. Minimum check-in age is 21. Please contact the reception for early check-in requests.

<h2>Check-out timings -</h2>
User: What are your check-out timings?

Bot: Check-out time is 11 AM. Please contact the reception for late checkout requests.

<h2>Cancel Reservation -</h2>
User: How do I cancel a reservation?

Bot: To cancel a reservation, select the “Reservations” link from the homepage.

Bot: On the Reservations page, under the heading ‘View, Change or Cancel a Reservation,’ enter your confirmation number, and either the last name on the reservation or the last four digits of the credit card used to make the reservation.

<h2>Cancellation Policy - </h2>
User: What is your cancellation policy?

Bot: The booking deposit is refundable if the cancellation occurs at least 15 days before arrival. For cancellations made after this limit, a penalty will be imposed based on the cancellation policy.

<h2>Restaurant -</h2>
User: Does the hotel have a restaurant?

Bot: Yes, the hotel has a restaurant called the Zephyr Bar. With our menu we strive to reflect the historic art and the spirit of our neighborhood by offering a glimpse into what makes our area unique.

<h2>Breakfast Availability -</h2>
User: Does the hotel offer breakfast?

Bot: The hotel provides its guests with a free made-to-order breakfast each morning.

<h2>Breakfast timings -</h2>
User: What are the breakfast timings?

Bot: Monday through Friday breakfast is 6 am to 9 am. On Saturday and Sunday, we are open from 7 am to 10:30 am.

<h2>Restaurant timings -</h2>
User: What are the timings of your restaurant?

Bot: Our restaurant serves a dazzling 24-hour menu.
