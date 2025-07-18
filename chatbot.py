from textblob import TextBlob

intents = {
   "hours":{
      "keywords":["hours", "open", "close"],
      "response": "We are open from 9 AM to 5 PM, Monday to Friday."
   },
   "return":{
      "keywords":["refund", "money back", "return"],
      "response":"I am happy."
   }
}
def get_response(message):
   message = message.lower()

   if any(word in message for word in intent_data["keywords"]):

      return intent_data["response"]
   
      sentiment = TextBlob(message).sentiment.polarity

   return ("That's so great to hear that" if sentiment > 0 else 
           "Iam so sorry to hear" if sentiment < 0 else "I see")
def chat():

   print ("chatbot: Hi, how can I help you today? ")

   while (user_mesage := input("You: ").strip().lower()) not in ['exit', 'quit', 'bye']:

      print(f"\nChatbot: {get_response(user_mesage)}")

   print("Chatbot: Thank you")

if __name__ == "__main__":
   chat()
   
