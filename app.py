
#imports
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
app = Flask(__name__)
#create chatbot
Bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")


trainer = ListTrainer(Bot)
trainer.train([
    "hello there!",
    "hi there!",
    "how are you doing now?",
    "i am fine,you?",
    "i am also fine, thanks for asking",
    "Great,how can i help you?",
    "Suggest me 3 romantic songs",
    "well,here is your 3 romantic song, 1.https://www.youtube.com/watch?v=SAcpESN_Fk4 \n 2.https://www.youtube.com/watch?v=DAYszemgPxc \n 3.https://www.youtube.com/watch?v=2drIKUOCZxU",
    "Who built you?",
    "My creator name is  Ridoy. want to know about him?",
    "sure",
    "His full name is Faysal Ahmed Ridoy .He is a Final year computer engineering student at East West University \n Email : ridoy2468@gmail.com, \n Mobile number : 01961186010 \n Location : Badda,Dhaka \n BSC : Computer Science & Engineering-(2017-2021) -- CGPA :3.19 '\n' SSC: Motijheel Model High School and College - (2008 - 2015) --  GPA: 5.00 '\n' HSC: Dhaka CIty College - (2015-2016) -- GPA: 4.86 ",
    "Very nice",
    "Yes,How is your day?",
    "not very good",
    "why?",
    "so much rain outside",
    "ohh!, sad",
    "How old are you?",
    "I was built 3days ago",
    "which language you are built in?",
    "I was built by Python and Flask ",
    "Wow, That's great",
    "Yes, Thanks",
    "Can i talk to you about myself?",
    "Why not, Go ahead",
    "Thank You bot",
    "You welcome",
    "Ask me anything",
    "Okay, are a normal person or physically challaged person? feel free to share.",
    "physically challenged",
    "Do you have proper accessibility? (Yes or No)",
    "Yes",
    "Great to hear that",
    "No",
    "Really sad to hear it, what can i do for you?",
    "Suggest me anything",
    "You can read book to spend your time like \n 1.Pother Pachali, \n 2.Misir Ali, \n 3.Himur Hate Nil Poddo.",
    "Thanks"
    "Do you feeling better now?",
    "Yes"
    "Great to hear that",
    "Not at all",
    "So,are you felling being ignored? (Yes i am /No i am not)",
    "Yes i am",
    "Okay, no worries you can spend your time by watching movies or hangout with your family and relatives. They can help you to overcome your boredom",
    "then suggest me a movie",
    "Movie Name : The Miracle(2015)",
    "okay,Thank You",
    "Are you feeling of being incompetent? (yes i do/no i don't)",
    "yes i do",
    "then you can distract  yourself to do anything else or find things to do in order to keep yourself from obsessing over the person who is ignoring you",
    "nice, thanks",
    "Welcome, can i help you more with anything else?",
    "Yes please",
    "Tell me, are you often teased and abused by someone or somethings? (Yes i was/ No i wasn't)",
    "Yes i was",
    "Often people find satisfaction in putting others down. They find superiority in bullying the weak and underprivileged. Challanged people often find themselves at the receiving end of such violent and disgusting actions,\n No worries, you can reach out to family and friends or Seek the guidance of a consultant else you can Stand up for yourself to fight back the abuse",
    "Okay, i wll. Thank You So Much",
    "Most Welcome, Have a good day",
    "No i wasn't",
    "Sounds Great",
    "Thank You So Much Bot",
    "Most Welcome, Have a good day",

]) #train the chatter bot 

corpus_trainer = ChatterBotCorpusTrainer(Bot)
corpus_trainer.train('chatterbot.corpus.english')

#define app routes
@app.route("/")
def home():
    return render_template("home.html")
@app.route("/get")
#function for the bot response
def get_bot_response():
    userText = request.args.get('msg')
    return str(Bot.get_response(userText))
if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0')
