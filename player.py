
# CREATE TABLE client (
#   id INT NOT NULL AUTO_INCREMENT,
#   user_id VARCHAR(255),
#   Panier_global VARCHAR(255),
#   Total VARCHAR(255),
#   livraison VARCHAR(255),
#   Adresse_client VARCHAR(255),
#   Code_postale VARCHAR(255),
#   photos_received TEXT,
#   photos_received1 TEXT,
#   PRIMARY KEY (id)
#  );


import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import os
from urllib.request import urlretrieve
from telebot import types
from telegram import ReplyKeyboardRemove
import requests
from telegram.ext import Updater
import mysql.connector

# Connexion à la base de données
mydb = mysql.connector.connect(
  host="yanisgale2.mysql.pythonanywhere-services.com",
  user="yanisgale2",
  password="911-Da10-287",
  database="yanisgale2$default"
)

user= []

# Remplacez le jeton par votre propre jeton de bot
bot = telebot.TeleBot("6202574546:AAF9x0K8i3jdHmdsW7DCL9XdJ0ydpTUVNVg")

#Créer le clavier d'accueil avec les trois options
menu_demarrage = ReplyKeyboardMarkup(resize_keyboard=True)
menu_demarrage.add(KeyboardButton('Livraison'))

# Créer le clavier d'accueil avec les quatres menus
menu_principal = ReplyKeyboardMarkup(resize_keyboard=True)
menu_principal.row(KeyboardButton('MENU HASH'), KeyboardButton('MENU WEED '))

menu_principal1 = ReplyKeyboardMarkup(resize_keyboard=True)
menu_principal1.row(KeyboardButton('MENU HASH'), KeyboardButton('MENU WEED '))


# Créer le clavier de sous-menu de MENU HASK
sous_menus_hash= ReplyKeyboardMarkup(resize_keyboard=True)
sous_menus_hash.add(KeyboardButton('Filtré'))
sous_menus_hash.add(KeyboardButton('Olives X3'))
sous_menus_hash.add(KeyboardButton('Static'))
sous_menus_hash.add(KeyboardButton('Mousseux'))
sous_menus_hash.add(KeyboardButton('Retour'))

# Créer le clavier de sous-menu de MENU WEED
sous_menus_weed= ReplyKeyboardMarkup(resize_keyboard=True)
sous_menus_weed.add(KeyboardButton('Hollandaise'))
sous_menus_weed.add(KeyboardButton('Californienne'))
sous_menus_weed.add(KeyboardButton('Espagnole'))
sous_menus_weed.add(KeyboardButton('Retour'))


# Créer le clavier de sous-menu de MENU PUFF THC
sous_menus_puff= ReplyKeyboardMarkup(resize_keyboard=True)
sous_menus_puff.add(KeyboardButton('Green Magic'))
sous_menus_puff.add(KeyboardButton('Retour '))

#clavier pour les sous variete de chaque produit
#menu hash
#Filtré
sous_var_filtre= ReplyKeyboardMarkup(resize_keyboard=True)
sous_var_filtre.add(KeyboardButton('120u'))
sous_var_filtre.add(KeyboardButton('Retour vers menu Hash'))

#Olives X3
sous_var_olives= ReplyKeyboardMarkup(resize_keyboard=True)
sous_var_olives.add(KeyboardButton('90u'))
sous_var_olives.add(KeyboardButton('Retour vers menu Hash'))

#Static
sous_var_static= ReplyKeyboardMarkup(resize_keyboard=True)
sous_var_static.add(KeyboardButton('120u'))
sous_var_static.add(KeyboardButton('Retour vers menu Hash'))

#Mousseux
sous_var_mouss= ReplyKeyboardMarkup(resize_keyboard=True)
sous_var_mouss.add(KeyboardButton('San Ku Kai'))
sous_var_mouss.add(KeyboardButton('Retour vers menu Hash'))

#Hollandaise
sous_var_holl= ReplyKeyboardMarkup(resize_keyboard=True)
sous_var_holl.add(KeyboardButton('Amnésia Haze 666'))
sous_var_holl.add(KeyboardButton('Retour vers menu Weed'))

#Californienne
sous_var_cali= ReplyKeyboardMarkup(resize_keyboard=True)
sous_var_cali.add(KeyboardButton('Sunset Sherbert'))
sous_var_cali.add(KeyboardButton('Gorilla x Zkittlez'))
sous_var_cali.add(KeyboardButton('Retour vers menu Weed'))

#espagnole
sous_var_esp= ReplyKeyboardMarkup(resize_keyboard=True)
sous_var_esp.add(KeyboardButton('Runtz'))
sous_var_esp.add(KeyboardButton('Retour vers menu Weed'))

#green magic
sous_var_mag= ReplyKeyboardMarkup(resize_keyboard=True)
sous_var_mag.add(KeyboardButton('300'))
sous_var_mag.add(KeyboardButton('Retour vers menu Puff Thc'))


# Créer le clavier de chaque prix et grammage
#type filtré
grammage_type0 = ReplyKeyboardMarkup(resize_keyboard=True)
grammage_type0.add(KeyboardButton('60€/5g'))
grammage_type0.add(KeyboardButton('120€/10g'))
grammage_type0.add(KeyboardButton('230€/25g'))
grammage_type0.add(KeyboardButton('Retour vers menu Hash'))

#type24k gold
grammage_type1 = ReplyKeyboardMarkup(resize_keyboard=True)
grammage_type1.add(KeyboardButton('90€/5g'))
grammage_type1.add(KeyboardButton('170€/10g'))
grammage_type1.add(KeyboardButton('Retour vers menu Hash'))

#type olives
grammage_type2 = ReplyKeyboardMarkup(resize_keyboard=True)
grammage_type2.add(KeyboardButton('90€/pièce'))
grammage_type2.add(KeyboardButton('160€/par 2'))
grammage_type2.add(KeyboardButton('350€/par 5'))
grammage_type2.add(KeyboardButton('Retour vers menu Hash'))

#type satic
grammage_type3 = ReplyKeyboardMarkup(resize_keyboard=True)
grammage_type3.add(KeyboardButton('70€/5g'))
grammage_type3.add(KeyboardButton('130€/10g'))
grammage_type3.add(KeyboardButton('250€/25g'))
grammage_type3.add(KeyboardButton('450€/50g'))
grammage_type3.add(KeyboardButton('800€/100g'))
grammage_type3.add(KeyboardButton('Retour vers menu Hash'))

#type mousseaux
grammage_type4 = ReplyKeyboardMarkup(resize_keyboard=True)
grammage_type4.add(KeyboardButton('120€/25g'))
grammage_type4.add(KeyboardButton('170€/50g'))
grammage_type4.add(KeyboardButton('300€/100g'))
grammage_type4.add(KeyboardButton('Retour vers menu Hash'))

#type carlifornienne
grammage_type5 = ReplyKeyboardMarkup(resize_keyboard=True)
grammage_type5.add(KeyboardButton('70€/3,5g(1bag)'))
grammage_type5.add(KeyboardButton('190€/10,5g(3bag)'))
grammage_type5.add(KeyboardButton('Retour vers menu Weed'))

grammage_type51 = ReplyKeyboardMarkup(resize_keyboard=True)
grammage_type51.add(KeyboardButton('80€/3,5g(1bag)'))
grammage_type51.add(KeyboardButton('200€/10,5g(3bag)'))
grammage_type51.add(KeyboardButton('Retour vers menu Weed'))

#type Hollandaise
grammage_type6 = ReplyKeyboardMarkup(resize_keyboard=True)
grammage_type6.add(KeyboardButton('50€/5g'))
grammage_type6.add(KeyboardButton('100€/10g'))
grammage_type6.add(KeyboardButton('180€/25g'))
grammage_type6.add(KeyboardButton('350€/50g'))
grammage_type6.add(KeyboardButton('650€/100g'))
grammage_type6.add(KeyboardButton('Retour vers menu Weed'))

#type Colombienne
grammage_type7 = ReplyKeyboardMarkup(resize_keyboard=True)
grammage_type7.add(KeyboardButton('70€/5g'))
grammage_type7.add(KeyboardButton('130€/10g'))
grammage_type7.add(KeyboardButton('280€/25g'))
grammage_type7.add(KeyboardButton('Retour vers menu Weed'))

#type Green Magic
grammage_type8 = ReplyKeyboardMarkup(resize_keyboard=True)
grammage_type8.add(KeyboardButton('60€/pièce'))
grammage_type8.add(KeyboardButton('110€/les 2'))
grammage_type8.add(KeyboardButton('250€/les 5'))
grammage_type8.add(KeyboardButton('Retour vers menu Weed'))



#type autre article
autre_article= ReplyKeyboardMarkup(resize_keyboard=True)
autre_article.row(KeyboardButton('Ajouter un autre article'),KeyboardButton('Payer'),KeyboardButton('Voir le panier'))
autre_article.add(KeyboardButton('Supprimer le panier'))

#type
confirmation_achat= ReplyKeyboardMarkup(resize_keyboard=True)
confirmation_achat.row(KeyboardButton('Ok'),KeyboardButton('Retour'))


#type
final_livraison= ReplyKeyboardMarkup(resize_keyboard=True)
final_livraison.row(KeyboardButton('Retour'))


# Créer le clavier confirmation commande4
confirmation4= ReplyKeyboardMarkup(resize_keyboard=True)
confirmation4.add(KeyboardButton("Envoyer"))
confirmation4.add(KeyboardButton('Retour'))

#************************Message de bienvenu *****************************************
@bot.message_handler(func=lambda message: message.text in ["/start"])
def handle_choice_one(message):
        mycursor = mydb.cursor()
        chat_id = message.chat.id
        query = "DELETE FROM client WHERE user_id = %s"
        values = (chat_id,)
        mycursor.execute(query, values)

        mydb.commit()
        user.clear()
        bot.reply_to(message, "Bonjour " + message.chat.first_name + ". Bienvenue chez Sarkoffee91, clique sur livraison pour commander 🚛📦  ", reply_markup=menu_demarrage)

    #***********************************************************************************************************************************
@bot.message_handler(func=lambda message: message.text  == "Livraison")
def handle_message(message):
    try:
        chat_id = message.chat.id
        # Exemple d'insertion de données dans une table
        mycursor = mydb.cursor()
        sql = "INSERT INTO client ( user_id, livraison) VALUES (%s, %s)"
        # sql = "UPDATE client SET user_id = %s, choix_menu_hash = %s"
        values = (chat_id, "livraison")
        mycursor.execute(sql, values)
        mydb.commit()
        bot.reply_to(message, f"Nos menus", reply_markup=menu_principal)
    except Exception as e:
         bot.reply_to(message, f" Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

@bot.message_handler(func=lambda message: message.text == "Retour")
def handle_message(message):
    try:
            mycursor = mydb.cursor()
            chat_id = message.chat.id
            query = "UPDATE client SET Panier_global = NULL, Total = NULL,Adresse_client = NULL, Code_postale = NULL, photos_received = NULL, photos_received1 = NULL WHERE user_id = %s"
            values = (chat_id,)
            mycursor.execute(query, values)
            mydb.commit()
            user.clear()
            bot.reply_to(message, "Retour vers le menu principal", reply_markup=menu_principal)

    except Exception as e:
         bot.reply_to(message, f" Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

@bot.message_handler(func=lambda message: message.text == "Retour vers menu Hash")
def handle_message(message):
    try:
            user.clear()
            bot.reply_to(message, "Retour vers le menu Hash", reply_markup=sous_menus_hash)
    except Exception as e:
         bot.reply_to(message, f" Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

@bot.message_handler(func=lambda message: message.text == "Retour vers menu Weed")
def handle_message(message):
    try:
                bot.reply_to(message, "Retour vers le menu Weed", reply_markup=sous_menus_weed)
    except Exception as e:
         bot.reply_to(message, f" Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)


#**********************************Les  menus******************************************************************************
@bot.message_handler(func=lambda message: message.text == "MENU HASH")
def handle_choice_one(message):
    try:
        bot.reply_to(message, f"Veuillez choisir une variété  :", reply_markup=sous_menus_hash)
    except Exception as e:
         bot.reply_to(message, f" Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

@bot.message_handler(func=lambda message: message.text == "MENU WEED")
def handle_choice_one(message):
    try:
        bot.reply_to(message, f"Veuillez choisir une variété :", reply_markup=sous_menus_weed)
    except Exception as e:
         bot.reply_to(message, f" Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

 #********************************Les varietes*********************************************************
  #********************************Menu Hash*********************************************************
@bot.message_handler(func=lambda message: message.text == "Filtré")
def handle_choice_one(message):
    try:
                 user.insert(0, "Filtré")
                 bot.reply_to(message, f"Veuillez choisir une varieté :", reply_markup=sous_var_filtre)
    except Exception as e:
         bot.reply_to(message, f" Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)
@bot.message_handler(func=lambda message: message.text == "Olives X3")
def handle_choice_one(message):
    try:
        bot.reply_to(message, f"Veuillez choisir une varieté :", reply_markup=sous_var_olives)
    except Exception as e:
         bot.reply_to(message, f" Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)
@bot.message_handler(func=lambda message: message.text == "Static")
def handle_choice_one(message):
    try:
        bot.reply_to(message, f"Veuillez choisir une varieté :", reply_markup=sous_var_static)
    except Exception as e:
         bot.reply_to(message, f" Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

@bot.message_handler(func=lambda message: message.text == "Mousseux")
def handle_choice_one(message):
    try:
        bot.reply_to(message, f"Veuillez choisir une varieté :", reply_markup=sous_var_mouss)
    except Exception as e:
         bot.reply_to(message, f" Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

#*****************************************************Menu weeed***************************************************************************************************
@bot.message_handler(func=lambda message: message.text == "Hollandaise")
def handle_choice_one(message):
    try:
        bot.reply_to(message, f"Veuillez choisir une varieté :", reply_markup=sous_var_holl)
    except Exception as e:
         bot.reply_to(message, f" Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

@bot.message_handler(func=lambda message: message.text == "Espagnole")
def handle_choice_one(message):
    try:
        bot.reply_to(message, f"Veuillez choisir une varieté :", reply_markup=sous_var_esp)
    except Exception as e:
         bot.reply_to(message, f" Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

@bot.message_handler(func=lambda message: message.text == "Californienne")
def handle_choice_one(message):
    try:
        bot.reply_to(message, f"Veuillez choisir une variete :", reply_markup=sous_var_cali)
    except Exception as e:
         bot.reply_to(message, f" Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

#******************************************************Menu puff**********************************************************
@bot.message_handler(func=lambda message: message.text == "Green Magic")
def handle_choice_one(message):
    try:
        bot.reply_to(message, f"Veuillez choisir une varieté :", reply_markup=sous_var_mag)
    except Exception as e:
         bot.reply_to(message, f" Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)


#********************************Les grammage et prix*********************************************************
#********************************Menu Hash*********************************************************
try:
    @bot.message_handler(func=lambda message: message.text == "120u" and user[0] == "Filtré")
    def handle_choice_one(message):

            bot.reply_to(message, f"Veuillez choisir un grammage :", reply_markup=grammage_type0)
except Exception as e:
         bot.reply_to(message, f" Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)
@bot.message_handler(func=lambda message: message.text == "90u" )
def handle_choice_one(message):
    try:
        bot.reply_to(message, f"Veuillez choisir un grammage :", reply_markup=grammage_type2)
    except Exception as e:
         bot.reply_to(message, f" Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)
@bot.message_handler(func=lambda message: message.text == "120u")
def handle_choice_one(message):
    try:
        bot.reply_to(message, f"Veuillez choisir un grammage :", reply_markup=grammage_type3)
    except Exception as e:
         bot.reply_to(message, f" Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

@bot.message_handler(func=lambda message: message.text == "San Ku Kai")
def handle_choice_one(message):
    try:
        bot.reply_to(message, f"Veuillez choisir un grammage :", reply_markup=grammage_type4)
    except Exception as e:
         bot.reply_to(message, f" Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

#*****************************************************Menu weeed***************************************************************************************************
@bot.message_handler(func=lambda message: message.text == "Amnésia Haze 666")
def handle_choice_one(message):
    try:
        bot.reply_to(message, f"Veuillez choisir un grammage :", reply_markup=grammage_type6)
    except Exception as e:
         bot.reply_to(message, f" Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

@bot.message_handler(func=lambda message: message.text == "Runtz")
def handle_choice_one(message):
    try:
        bot.reply_to(message, f"Veuillez choisir un grammage :", reply_markup=grammage_type7)
    except Exception as e:
         bot.reply_to(message, f" Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

@bot.message_handler(func=lambda message: message.text == "Sunset Sherbert")
def handle_choice_one(message):
    try:
        bot.reply_to(message, f"Veuillez choisir un grammage :", reply_markup=grammage_type5)
    except Exception as e:
         bot.reply_to(message, f" Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

@bot.message_handler(func=lambda message: message.text == "Gorilla x Zkittlez")
def handle_choice_one(message):
    try:
        bot.reply_to(message, f"Veuillez choisir un grammage :", reply_markup=grammage_type51)
    except Exception as e:
         bot.reply_to(message, f" Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

#******************************************************Menu puff**********************************************************
@bot.message_handler(func=lambda message: message.text == "300")
def handle_choice_one(message):
    try:
        bot.reply_to(message, f"Veuillez choisir un un grammage :", reply_markup=grammage_type8)
    except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

#*****************************Factures ************************************************
#*****************************Menu hash(filtré) ************************************************
@bot.message_handler(func=lambda message: message.text == "60€/5g")
def handle_choice_one(message):
 try:
    chat_id = message.chat.id
    mycursor = mydb.cursor()
    mycursor.execute("SELECT Panier_global FROM client WHERE user_id = %s", (chat_id,))
    rows = mycursor.fetchall()
    Panier_global0 = rows[0][0]
    if Panier_global0:

        try:
                 chat_id = message.chat.id
                 mycursor = mydb.cursor()
                  # Exécuter une requête pour récupérer les valeurs
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                    # #  sql = "INSERT INTO client (Panier_global,Total) VALUES (%s,%s) WHERE user_id = chat_id"
                 sql = "UPDATE client SET Panier_global = %s, Total = %s WHERE user_id = %s"
                 Values = (f"5g de 120u Filtré (Menu hash) à 60€\n\n {rows[0][0]}",sum([60,int(rows[0][1])]),chat_id )
                 mycursor.execute(sql, Values)
                 mydb.commit()
                  # Exécuter une requête pour récupérer les valeurs
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                 bot.reply_to(message,f" 🏆 Article(s) dans le Panier 🏆 : \n\n{rows[0][0]}\n \n Total : {rows[0][1]}€",reply_markup= autre_article)
        except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

    else :
        try:
                 chat_id = message.chat.id
                 mycursor = mydb.cursor()
                  #  sql = "INSERT INTO client (Panier_global,Total) VALUES (%s,%s) WHERE user_id = chat_id"
                 sql = "UPDATE client SET Panier_global = %s, Total = %s WHERE user_id = %s"
                 Values = (f"5g de 120u Filtré (Menu hash) à 60€",60,chat_id )
                 mycursor.execute(sql, Values)
                 mydb.commit()
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                 bot.reply_to(message,f" 🏆 Article(s) dans le Panier 🏆 : \n\n{rows[0][0]} \n\n Total : {rows[0][1]}€",reply_markup= autre_article)
        except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)
 except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

@bot.message_handler(func=lambda message: message.text == "120€/10g")
def handle_choice_one(message):
 try:
    chat_id = message.chat.id
    mycursor = mydb.cursor()
    mycursor.execute("SELECT Panier_global FROM client WHERE user_id = %s", (chat_id,))
    rows = mycursor.fetchall()
    Panier_global0 = rows[0][0]
    if Panier_global0:

        try:
                 chat_id = message.chat.id
                 mycursor = mydb.cursor()
                  # Exécuter une requête pour récupérer les valeurs
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                    # #  sql = "INSERT INTO client (Panier_global,Total) VALUES (%s,%s) WHERE user_id = chat_id"
                 sql = "UPDATE client SET Panier_global = %s, Total = %s WHERE user_id = %s"
                 Values = (f"10g de 120u Filtré (Menu hash) à 120€\n\n {rows[0][0]}",sum([120,int(rows[0][1])]),chat_id )
                 mycursor.execute(sql, Values)
                 mydb.commit()
                  # Exécuter une requête pour récupérer les valeurs
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                 bot.reply_to(message,f" 🏆 Article(s) dans le Panier 🏆 : \n\n{rows[0][0]}\n \n Total : {rows[0][1]}€",reply_markup= autre_article)
        except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

    else :
        try:
                 chat_id = message.chat.id
                 mycursor = mydb.cursor()
                  #  sql = "INSERT INTO client (Panier_global,Total) VALUES (%s,%s) WHERE user_id = chat_id"
                 sql = "UPDATE client SET Panier_global = %s, Total = %s WHERE user_id = %s"
                 Values = (f"10g de 120u Filtré (Menu hash) à 120€",120,chat_id )
                 mycursor.execute(sql, Values)
                 mydb.commit()
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                 bot.reply_to(message,f" 🏆 Article(s) dans le Panier 🏆 : \n\n{rows[0][0]} \n\n Total : {rows[0][1]}€",reply_markup= autre_article)
        except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)
 except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)



@bot.message_handler(func=lambda message: message.text == "230€/25g")
def handle_choice_one(message):
 try:
    chat_id = message.chat.id
    mycursor = mydb.cursor()
    mycursor.execute("SELECT Panier_global FROM client WHERE user_id = %s", (chat_id,))
    rows = mycursor.fetchall()
    Panier_global0 = rows[0][0]
    if Panier_global0:

        try:
                 chat_id = message.chat.id
                 mycursor = mydb.cursor()
                  # Exécuter une requête pour récupérer les valeurs
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                    # #  sql = "INSERT INTO client (Panier_global,Total) VALUES (%s,%s) WHERE user_id = chat_id"
                 sql = "UPDATE client SET Panier_global = %s, Total = %s WHERE user_id = %s"
                 Values = (f"25g de 120u Filtré (Menu hash) à 230€\n\n {rows[0][0]}",sum([230,int(rows[0][1])]),chat_id )
                 mycursor.execute(sql, Values)
                 mydb.commit()
                  # Exécuter une requête pour récupérer les valeurs
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                 bot.reply_to(message,f" 🏆 Article(s) dans le Panier 🏆 : \n\n{rows[0][0]}\n \n Total : {rows[0][1]}€",reply_markup= autre_article)
        except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

    else :
        try:
                 chat_id = message.chat.id
                 mycursor = mydb.cursor()
                  #  sql = "INSERT INTO client (Panier_global,Total) VALUES (%s,%s) WHERE user_id = chat_id"
                 sql = "UPDATE client SET Panier_global = %s, Total = %s WHERE user_id = %s"
                 Values = (f"25g de 120u Filtré (Menu hash) à 230€",230,chat_id )
                 mycursor.execute(sql, Values)
                 mydb.commit()
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                 bot.reply_to(message,f" 🏆 Article(s) dans le Panier 🏆 : \n\n{rows[0][0]} \n\n Total : {rows[0][1]}€",reply_markup= autre_article)
        except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)
 except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)


 #***************************************************OLIVES****************************************************************************

@bot.message_handler(func=lambda message: message.text == "90€/pièce")
def handle_choice_one(message):
 try:
    chat_id = message.chat.id
    mycursor = mydb.cursor()
    mycursor.execute("SELECT Panier_global FROM client WHERE user_id = %s", (chat_id,))
    rows = mycursor.fetchall()
    Panier_global0 = rows[0][0]
    if Panier_global0:

        try:
                 chat_id = message.chat.id
                 mycursor = mydb.cursor()
                  # Exécuter une requête pour récupérer les valeurs
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                    # #  sql = "INSERT INTO client (Panier_global,Total) VALUES (%s,%s) WHERE user_id = chat_id"
                 sql = "UPDATE client SET Panier_global = %s, Total = %s WHERE user_id = %s"
                 Values = (f"pièce de 90u olives X3 (Menu hash) à 90€\n\n {rows[0][0]}",sum([90,int(rows[0][1])]),chat_id )
                 mycursor.execute(sql, Values)
                 mydb.commit()
                  # Exécuter une requête pour récupérer les valeurs
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                 bot.reply_to(message,f" 🏆 Article(s) dans le Panier 🏆 : \n\n{rows[0][0]}\n \n Total : {rows[0][1]}€",reply_markup= autre_article)
        except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

    else :
        try:
                 chat_id = message.chat.id
                 mycursor = mydb.cursor()
                  #  sql = "INSERT INTO client (Panier_global,Total) VALUES (%s,%s) WHERE user_id = chat_id"
                 sql = "UPDATE client SET Panier_global = %s, Total = %s WHERE user_id = %s"
                 Values = (f"pièce de 90u olives X3 (Menu hash) à 90€",90,chat_id )
                 mycursor.execute(sql, Values)
                 mydb.commit()
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                 bot.reply_to(message,f" 🏆 Article(s) dans le Panier 🏆 : \n\n{rows[0][0]} \n\n Total : {rows[0][1]}€",reply_markup= autre_article)
        except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)
 except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

@bot.message_handler(func=lambda message: message.text == "160€/par 2")
def handle_choice_one(message):
 try:
    chat_id = message.chat.id
    mycursor = mydb.cursor()
    mycursor.execute("SELECT Panier_global FROM client WHERE user_id = %s", (chat_id,))
    rows = mycursor.fetchall()
    Panier_global0 = rows[0][0]
    if Panier_global0:

        try:
                 chat_id = message.chat.id
                 mycursor = mydb.cursor()
                  # Exécuter une requête pour récupérer les valeurs
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                    # #  sql = "INSERT INTO client (Panier_global,Total) VALUES (%s,%s) WHERE user_id = chat_id"
                 sql = "UPDATE client SET Panier_global = %s, Total = %s WHERE user_id = %s"
                 Values = (f"par 2 de 90u olives X3 (Menu hash) à 160€\n\n {rows[0][0]}",sum([160,int(rows[0][1])]),chat_id )
                 mycursor.execute(sql, Values)
                 mydb.commit()
                  # Exécuter une requête pour récupérer les valeurs
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                 bot.reply_to(message,f" 🏆 Article(s) dans le Panier 🏆 : \n\n{rows[0][0]}\n \n Total : {rows[0][1]}€",reply_markup= autre_article)
        except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

    else :
        try:
                 chat_id = message.chat.id
                 mycursor = mydb.cursor()
                  #  sql = "INSERT INTO client (Panier_global,Total) VALUES (%s,%s) WHERE user_id = chat_id"
                 sql = "UPDATE client SET Panier_global = %s, Total = %s WHERE user_id = %s"
                 Values = (f"par 2 de 90u olives X3 (Menu hash) à 60€",160,chat_id )
                 mycursor.execute(sql, Values)
                 mydb.commit()
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                 bot.reply_to(message,f" 🏆 Article(s) dans le Panier 🏆 : \n\n{rows[0][0]} \n\n Total : {rows[0][1]}€",reply_markup= autre_article)
        except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)
 except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

@bot.message_handler(func=lambda message: message.text == "350€/par 5")
def handle_choice_one(message):
 try:
    chat_id = message.chat.id
    mycursor = mydb.cursor()
    mycursor.execute("SELECT Panier_global FROM client WHERE user_id = %s", (chat_id,))
    rows = mycursor.fetchall()
    Panier_global0 = rows[0][0]
    if Panier_global0:

        try:
                 chat_id = message.chat.id
                 mycursor = mydb.cursor()
                  # Exécuter une requête pour récupérer les valeurs
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                    # #  sql = "INSERT INTO client (Panier_global,Total) VALUES (%s,%s) WHERE user_id = chat_id"
                 sql = "UPDATE client SET Panier_global = %s, Total = %s WHERE user_id = %s"
                 Values = (f"par 5 de 90u olives X3 (Menu hash) à 350€\n\n {rows[0][0]}",sum([350,int(rows[0][1])]),chat_id )
                 mycursor.execute(sql, Values)
                 mydb.commit()
                  # Exécuter une requête pour récupérer les valeurs
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                 bot.reply_to(message,f" 🏆 Article(s) dans le Panier 🏆 : \n\n{rows[0][0]}\n \n Total : {rows[0][1]}€",reply_markup= autre_article)
        except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

    else :
        try:
                 chat_id = message.chat.id
                 mycursor = mydb.cursor()
                  #  sql = "INSERT INTO client (Panier_global,Total) VALUES (%s,%s) WHERE user_id = chat_id"
                 sql = "UPDATE client SET Panier_global = %s, Total = %s WHERE user_id = %s"
                 Values = (f"par 5 de 90u olives X3 (Menu hash) à 350€",350,chat_id )
                 mycursor.execute(sql, Values)
                 mydb.commit()
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                 bot.reply_to(message,f" 🏆 Article(s) dans le Panier 🏆 : \n\n{rows[0][0]} \n\n Total : {rows[0][1]}€",reply_markup= autre_article)
        except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)
 except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

 #****************************************************Static************************************************************************

@bot.message_handler(func=lambda message: message.text == "70€/5g")
def handle_choice_one(message):
 try:
    chat_id = message.chat.id
    mycursor = mydb.cursor()
    mycursor.execute("SELECT Panier_global FROM client WHERE user_id = %s", (chat_id,))
    rows = mycursor.fetchall()
    Panier_global0 = rows[0][0]
    if Panier_global0:

        try:
                 chat_id = message.chat.id
                 mycursor = mydb.cursor()
                  # Exécuter une requête pour récupérer les valeurs
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                    # #  sql = "INSERT INTO client (Panier_global,Total) VALUES (%s,%s) WHERE user_id = chat_id"
                 sql = "UPDATE client SET Panier_global = %s, Total = %s WHERE user_id = %s"
                 Values = (f"5g de 120u static (Menu hash) à 70€\n\n {rows[0][0]}",sum([70,int(rows[0][1])]),chat_id )
                 mycursor.execute(sql, Values)
                 mydb.commit()
                  # Exécuter une requête pour récupérer les valeurs
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                 bot.reply_to(message,f" 🏆 Article(s) dans le Panier 🏆 : \n\n{rows[0][0]}\n \n Total : {rows[0][1]}€",reply_markup= autre_article)
        except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

    else :
        try:
                 chat_id = message.chat.id
                 mycursor = mydb.cursor()
                  #  sql = "INSERT INTO client (Panier_global,Total) VALUES (%s,%s) WHERE user_id = chat_id"
                 sql = "UPDATE client SET Panier_global = %s, Total = %s WHERE user_id = %s"
                 Values = (f"5g de 120u  static (Menu hash) à 70€",70,chat_id )
                 mycursor.execute(sql, Values)
                 mydb.commit()
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                 bot.reply_to(message,f" 🏆 Article(s) dans le Panier 🏆 : \n\n{rows[0][0]} \n\n Total : {rows[0][1]}€",reply_markup= autre_article)
        except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)
 except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)


@bot.message_handler(func=lambda message: message.text == "130€/10g")
def handle_choice_one(message):
 try:
    chat_id = message.chat.id
    mycursor = mydb.cursor()
    mycursor.execute("SELECT Panier_global FROM client WHERE user_id = %s", (chat_id,))
    rows = mycursor.fetchall()
    Panier_global0 = rows[0][0]
    if Panier_global0:

        try:
                 chat_id = message.chat.id
                 mycursor = mydb.cursor()
                  # Exécuter une requête pour récupérer les valeurs
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                    # #  sql = "INSERT INTO client (Panier_global,Total) VALUES (%s,%s) WHERE user_id = chat_id"
                 sql = "UPDATE client SET Panier_global = %s, Total = %s WHERE user_id = %s"
                 Values = (f"10g de 120u static (Menu hash) à 130€\n\n {rows[0][0]}",sum([130,int(rows[0][1])]),chat_id )
                 mycursor.execute(sql, Values)
                 mydb.commit()
                  # Exécuter une requête pour récupérer les valeurs
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                 bot.reply_to(message,f" 🏆 Article(s) dans le Panier 🏆 : \n\n{rows[0][0]}\n \n Total : {rows[0][1]}€",reply_markup= autre_article)
        except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

    else :
        try:
                 chat_id = message.chat.id
                 mycursor = mydb.cursor()
                  #  sql = "INSERT INTO client (Panier_global,Total) VALUES (%s,%s) WHERE user_id = chat_id"
                 sql = "UPDATE client SET Panier_global = %s, Total = %s WHERE user_id = %s"
                 Values = (f"10g de 120u  static (Menu hash) à 130€",130,chat_id )
                 mycursor.execute(sql, Values)
                 mydb.commit()
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                 bot.reply_to(message,f" 🏆 Article(s) dans le Panier 🏆 : \n\n{rows[0][0]} \n\n Total : {rows[0][1]}€",reply_markup= autre_article)

        except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)
 except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

@bot.message_handler(func=lambda message: message.text == "250€/25g")
def handle_choice_one(message):
 try:
    chat_id = message.chat.id
    mycursor = mydb.cursor()
    mycursor.execute("SELECT Panier_global FROM client WHERE user_id = %s", (chat_id,))
    rows = mycursor.fetchall()
    Panier_global0 = rows[0][0]
    if Panier_global0:

        try:
                 chat_id = message.chat.id
                 mycursor = mydb.cursor()
                  # Exécuter une requête pour récupérer les valeurs
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                    # #  sql = "INSERT INTO client (Panier_global,Total) VALUES (%s,%s) WHERE user_id = chat_id"
                 sql = "UPDATE client SET Panier_global = %s, Total = %s WHERE user_id = %s"
                 Values = (f"25g de 120u static (Menu hash) à 250€\n\n {rows[0][0]}",sum([250,int(rows[0][1])]),chat_id )
                 mycursor.execute(sql, Values)
                 mydb.commit()
                  # Exécuter une requête pour récupérer les valeurs
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                 bot.reply_to(message,f" 🏆 Article(s) dans le Panier 🏆 : \n\n{rows[0][0]}\n \n Total : {rows[0][1]}€",reply_markup= autre_article)
        except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

    else :
        try:
                 chat_id = message.chat.id
                 mycursor = mydb.cursor()
                  #  sql = "INSERT INTO client (Panier_global,Total) VALUES (%s,%s) WHERE user_id = chat_id"
                 sql = "UPDATE client SET Panier_global = %s, Total = %s WHERE user_id = %s"
                 Values = (f"25g de 120u  static (Menu hash) à 250€",250,chat_id )
                 mycursor.execute(sql, Values)
                 mydb.commit()
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                 bot.reply_to(message,f" 🏆 Article(s) dans le Panier 🏆 : \n\n{rows[0][0]} \n\n Total : {rows[0][1]}€",reply_markup= autre_article)

        except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)
 except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)


@bot.message_handler(func=lambda message: message.text == "450€/50g")
def handle_choice_one(message):
 try:
    chat_id = message.chat.id
    mycursor = mydb.cursor()
    mycursor.execute("SELECT Panier_global FROM client WHERE user_id = %s", (chat_id,))
    rows = mycursor.fetchall()
    Panier_global0 = rows[0][0]
    if Panier_global0:

        try:
                 chat_id = message.chat.id
                 mycursor = mydb.cursor()
                  # Exécuter une requête pour récupérer les valeurs
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                    # #  sql = "INSERT INTO client (Panier_global,Total) VALUES (%s,%s) WHERE user_id = chat_id"
                 sql = "UPDATE client SET Panier_global = %s, Total = %s WHERE user_id = %s"
                 Values = (f"50g de 120u static (Menu hash) à 450€\n\n {rows[0][0]}",sum([450,int(rows[0][1])]),chat_id )
                 mycursor.execute(sql, Values)
                 mydb.commit()
                  # Exécuter une requête pour récupérer les valeurs
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                 bot.reply_to(message,f" 🏆 Article(s) dans le Panier 🏆 : \n\n{rows[0][0]}\n \n Total : {rows[0][1]}€",reply_markup= autre_article)
        except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

    else :
        try:
                 chat_id = message.chat.id
                 mycursor = mydb.cursor()
                  #  sql = "INSERT INTO client (Panier_global,Total) VALUES (%s,%s) WHERE user_id = chat_id"
                 sql = "UPDATE client SET Panier_global = %s, Total = %s WHERE user_id = %s"
                 Values = (f"50g de 120u  static (Menu hash) à 450€",450,chat_id )
                 mycursor.execute(sql, Values)
                 mydb.commit()
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                 bot.reply_to(message,f" 🏆 Article(s) dans le Panier 🏆 : \n\n{rows[0][0]} \n\n Total : {rows[0][1]}€",reply_markup= autre_article)
        except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)
 except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

@bot.message_handler(func=lambda message: message.text == "800€/100g")
def handle_choice_one(message):
 try:
    chat_id = message.chat.id
    mycursor = mydb.cursor()
    mycursor.execute("SELECT Panier_global FROM client WHERE user_id = %s", (chat_id,))
    rows = mycursor.fetchall()
    Panier_global0 = rows[0][0]
    if Panier_global0:

        try:
                 chat_id = message.chat.id
                 mycursor = mydb.cursor()
                  # Exécuter une requête pour récupérer les valeurs
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                    # #  sql = "INSERT INTO client (Panier_global,Total) VALUES (%s,%s) WHERE user_id = chat_id"
                 sql = "UPDATE client SET Panier_global = %s, Total = %s WHERE user_id = %s"
                 Values = (f"100g de 120u static (Menu hash) à 800€\n\n {rows[0][0]}",sum([800,int(rows[0][1])]),chat_id )
                 mycursor.execute(sql, Values)
                 mydb.commit()
                  # Exécuter une requête pour récupérer les valeurs
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                 bot.reply_to(message,f" 🏆 Article(s) dans le Panier 🏆 : \n\n{rows[0][0]}\n \n Total : {rows[0][1]}€",reply_markup= autre_article)
        except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

    else :
        try:
                 chat_id = message.chat.id
                 mycursor = mydb.cursor()
                  #  sql = "INSERT INTO client (Panier_global,Total) VALUES (%s,%s) WHERE user_id = chat_id"
                 sql = "UPDATE client SET Panier_global = %s, Total = %s WHERE user_id = %s"
                 Values = (f"100g de 120u  static (Menu hash) à 800€",800,chat_id )
                 mycursor.execute(sql, Values)
                 mydb.commit()
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                 bot.reply_to(message,f" 🏆 Article(s) dans le Panier 🏆 : \n\n{rows[0][0]} \n\n Total : {rows[0][1]}€",reply_markup= autre_article)
        except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)
 except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)


    #************************************************Mousseaux*******************************************************************************

@bot.message_handler(func=lambda message: message.text == "120€/25g")
def handle_choice_one(message):
 try:
    chat_id = message.chat.id
    mycursor = mydb.cursor()
    mycursor.execute("SELECT Panier_global FROM client WHERE user_id = %s", (chat_id,))
    rows = mycursor.fetchall()
    Panier_global0 = rows[0][0]
    if Panier_global0:

        try:
                 chat_id = message.chat.id
                 mycursor = mydb.cursor()
                  # Exécuter une requête pour récupérer les valeurs
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                    # #  sql = "INSERT INTO client (Panier_global,Total) VALUES (%s,%s) WHERE user_id = chat_id"
                 sql = "UPDATE client SET Panier_global = %s, Total = %s WHERE user_id = %s"
                 Values = (f"25g de San Ku Kai Mousseux (Menu hash) à 120€\n\n {rows[0][0]}",sum([120,int(rows[0][1])]),chat_id )
                 mycursor.execute(sql, Values)
                 mydb.commit()
                  # Exécuter une requête pour récupérer les valeurs
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                 bot.reply_to(message,f" 🏆 Article(s) dans le Panier 🏆 : \n\n{rows[0][0]}\n \n Total : {rows[0][1]}€",reply_markup= autre_article)
        except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

    else :
        try:
                 chat_id = message.chat.id
                 mycursor = mydb.cursor()
                  #  sql = "INSERT INTO client (Panier_global,Total) VALUES (%s,%s) WHERE user_id = chat_id"
                 sql = "UPDATE client SET Panier_global = %s, Total = %s WHERE user_id = %s"
                 Values = (f"25g de San Ku Kai Mousseux (Menu hash) à 120€",120,chat_id )
                 mycursor.execute(sql, Values)
                 mydb.commit()
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                 bot.reply_to(message,f" 🏆 Article(s) dans le Panier 🏆 : \n\n{rows[0][0]} \n\n Total : {rows[0][1]}€",reply_markup= autre_article)
        except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)
 except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

@bot.message_handler(func=lambda message: message.text == "170€/50g")
def handle_choice_one(message):
 try:
    chat_id = message.chat.id
    mycursor = mydb.cursor()
    mycursor.execute("SELECT Panier_global FROM client WHERE user_id = %s", (chat_id,))
    rows = mycursor.fetchall()
    Panier_global0 = rows[0][0]
    if Panier_global0:

        try:
                 chat_id = message.chat.id
                 mycursor = mydb.cursor()
                  # Exécuter une requête pour récupérer les valeurs
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                    # #  sql = "INSERT INTO client (Panier_global,Total) VALUES (%s,%s) WHERE user_id = chat_id"
                 sql = "UPDATE client SET Panier_global = %s, Total = %s WHERE user_id = %s"
                 Values = (f"50g de San Ku Kai Mousseux (Menu hash) à 170€\n\n {rows[0][0]}",sum([170,int(rows[0][1])]),chat_id )
                 mycursor.execute(sql, Values)
                 mydb.commit()
                  # Exécuter une requête pour récupérer les valeurs
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                 bot.reply_to(message,f" 🏆 Article(s) dans le Panier 🏆 : \n\n{rows[0][0]}\n \n Total : {rows[0][1]}€",reply_markup= autre_article)
        except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

    else :
        try:
                 chat_id = message.chat.id
                 mycursor = mydb.cursor()
                  #  sql = "INSERT INTO client (Panier_global,Total) VALUES (%s,%s) WHERE user_id = chat_id"
                 sql = "UPDATE client SET Panier_global = %s, Total = %s WHERE user_id = %s"
                 Values = (f"50g de San Ku Kai Mousseux (Menu hash) à 170€",170,chat_id )
                 mycursor.execute(sql, Values)
                 mydb.commit()
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                 bot.reply_to(message,f" 🏆 Article(s) dans le Panier 🏆 : \n\n{rows[0][0]} \n\n Total : {rows[0][1]}€",reply_markup= autre_article)
        except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)
 except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

@bot.message_handler(func=lambda message: message.text == "300€/100g")
def handle_choice_one(message):
 try:
    chat_id = message.chat.id
    mycursor = mydb.cursor()
    mycursor.execute("SELECT Panier_global FROM client WHERE user_id = %s", (chat_id,))
    rows = mycursor.fetchall()
    Panier_global0 = rows[0][0]
    if Panier_global0:

        try:
                 chat_id = message.chat.id
                 mycursor = mydb.cursor()
                  # Exécuter une requête pour récupérer les valeurs
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                    # #  sql = "INSERT INTO client (Panier_global,Total) VALUES (%s,%s) WHERE user_id = chat_id"
                 sql = "UPDATE client SET Panier_global = %s, Total = %s WHERE user_id = %s"
                 Values = (f"100g de San Ku Kai Mousseux (Menu hash) à 300€\n\n {rows[0][0]}",sum([300,int(rows[0][1])]),chat_id )
                 mycursor.execute(sql, Values)
                 mydb.commit()
                  # Exécuter une requête pour récupérer les valeurs
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                 bot.reply_to(message,f" 🏆 Article(s) dans le Panier 🏆 : \n\n{rows[0][0]}\n \n Total : {rows[0][1]}€",reply_markup= autre_article)
        except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

    else :
        try:
                 chat_id = message.chat.id
                 mycursor = mydb.cursor()
                  #  sql = "INSERT INTO client (Panier_global,Total) VALUES (%s,%s) WHERE user_id = chat_id"
                 sql = "UPDATE client SET Panier_global = %s, Total = %s WHERE user_id = %s"
                 Values = (f"100g de San Ku Kai Mousseux (Menu hash) à 300€",300,chat_id )
                 mycursor.execute(sql, Values)
                 mydb.commit()
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                 bot.reply_to(message,f" 🏆 Article(s) dans le Panier 🏆 : \n\n{rows[0][0]} \n\n Total : {rows[0][1]}€",reply_markup= autre_article)
        except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)
 except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

 #****************************************************Menus weed***************************************************************************
  #****************************************************Hollandaise***************************************************************************
@bot.message_handler(func=lambda message: message.text == "50€/5g")
def handle_choice_one(message):
 try:
    chat_id = message.chat.id
    mycursor = mydb.cursor()
    mycursor.execute("SELECT Panier_global FROM client WHERE user_id = %s", (chat_id,))
    rows = mycursor.fetchall()
    Panier_global0 = rows[0][0]
    if Panier_global0:

        try:
                 chat_id = message.chat.id
                 mycursor = mydb.cursor()
                  # Exécuter une requête pour récupérer les valeurs
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                    # #  sql = "INSERT INTO client (Panier_global,Total) VALUES (%s,%s) WHERE user_id = chat_id"
                 sql = "UPDATE client SET Panier_global = %s, Total = %s WHERE user_id = %s"
                 Values = (f"5g de Amnésia Haze 666 Hollandaise  (Menu weed) à 50€\n\n {rows[0][0]}",sum([50,int(rows[0][1])]),chat_id )
                 mycursor.execute(sql, Values)
                 mydb.commit()
                  # Exécuter une requête pour récupérer les valeurs
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                 bot.reply_to(message,f" 🏆 Article(s) dans le Panier 🏆 : \n\n{rows[0][0]}\n \n Total : {rows[0][1]}€",reply_markup= autre_article)
        except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

    else :
        try:
                 chat_id = message.chat.id
                 mycursor = mydb.cursor()
                  #  sql = "INSERT INTO client (Panier_global,Total) VALUES (%s,%s) WHERE user_id = chat_id"
                 sql = "UPDATE client SET Panier_global = %s, Total = %s WHERE user_id = %s"
                 Values = (f"5g de Amnésia Haze 666 Hollandaise  (Menu weed) à 50€",50,chat_id )
                 mycursor.execute(sql, Values)
                 mydb.commit()
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                 bot.reply_to(message,f" 🏆 Article(s) dans le Panier 🏆 : \n\n{rows[0][0]} \n\n Total : {rows[0][1]}€",reply_markup= autre_article)
        except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)
 except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)


@bot.message_handler(func=lambda message: message.text == "100€/10g")
def handle_choice_one(message):
 try:
    chat_id = message.chat.id
    mycursor = mydb.cursor()
    mycursor.execute("SELECT Panier_global FROM client WHERE user_id = %s", (chat_id,))
    rows = mycursor.fetchall()
    Panier_global0 = rows[0][0]
    if Panier_global0:

        try:
                 chat_id = message.chat.id
                 mycursor = mydb.cursor()
                  # Exécuter une requête pour récupérer les valeurs
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                    # #  sql = "INSERT INTO client (Panier_global,Total) VALUES (%s,%s) WHERE user_id = chat_id"
                 sql = "UPDATE client SET Panier_global = %s, Total = %s WHERE user_id = %s"
                 Values = (f"10g de Amnésia Haze 666 Hollandaise  (Menu weed) à 100€\n\n {rows[0][0]}",sum([100,int(rows[0][1])]),chat_id )
                 mycursor.execute(sql, Values)
                 mydb.commit()
                  # Exécuter une requête pour récupérer les valeurs
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                 bot.reply_to(message,f" 🏆 Article(s) dans le Panier 🏆 : \n\n{rows[0][0]}\n \n Total : {rows[0][1]}€",reply_markup= autre_article)
        except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

    else :
        try:
                 chat_id = message.chat.id
                 mycursor = mydb.cursor()
                  #  sql = "INSERT INTO client (Panier_global,Total) VALUES (%s,%s) WHERE user_id = chat_id"
                 sql = "UPDATE client SET Panier_global = %s, Total = %s WHERE user_id = %s"
                 Values = (f"10g de Amnésia Haze 666 Hollandaise  (Menu weed) à 100€",100,chat_id )
                 mycursor.execute(sql, Values)
                 mydb.commit()
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                 bot.reply_to(message,f" 🏆 Article(s) dans le Panier 🏆 : \n\n{rows[0][0]} \n\n Total : {rows[0][1]}€",reply_markup= autre_article)

        except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)
 except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)


@bot.message_handler(func=lambda message: message.text == "180€/25g")
def handle_choice_one(message):
 try:
    chat_id = message.chat.id
    mycursor = mydb.cursor()
    mycursor.execute("SELECT Panier_global FROM client WHERE user_id = %s", (chat_id,))
    rows = mycursor.fetchall()
    Panier_global0 = rows[0][0]
    if Panier_global0:

        try:
                 chat_id = message.chat.id
                 mycursor = mydb.cursor()
                  # Exécuter une requête pour récupérer les valeurs
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                    # #  sql = "INSERT INTO client (Panier_global,Total) VALUES (%s,%s) WHERE user_id = chat_id"
                 sql = "UPDATE client SET Panier_global = %s, Total = %s WHERE user_id = %s"
                 Values = (f"25g de Amnésia Haze 666 Hollandaise  (Menu weed) à 180€\n\n {rows[0][0]}",sum([180,int(rows[0][1])]),chat_id )
                 mycursor.execute(sql, Values)
                 mydb.commit()
                  # Exécuter une requête pour récupérer les valeurs
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                 bot.reply_to(message,f" 🏆 Article(s) dans le Panier 🏆 : \n\n{rows[0][0]}\n \n Total : {rows[0][1]}€",reply_markup= autre_article)
        except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

    else :
        try:
                 chat_id = message.chat.id
                 mycursor = mydb.cursor()
                  #  sql = "INSERT INTO client (Panier_global,Total) VALUES (%s,%s) WHERE user_id = chat_id"
                 sql = "UPDATE client SET Panier_global = %s, Total = %s WHERE user_id = %s"
                 Values = (f"25g de Amnésia Haze 666 Hollandaise  (Menu weed) à 180€",180,chat_id )
                 mycursor.execute(sql, Values)
                 mydb.commit()
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                 bot.reply_to(message,f" 🏆 Article(s) dans le Panier 🏆 : \n\n{rows[0][0]} \n\n Total : {rows[0][1]}€",reply_markup= autre_article)
        except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)
 except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

@bot.message_handler(func=lambda message: message.text == "350€/50g")
def handle_choice_one(message):
 try:
    chat_id = message.chat.id
    mycursor = mydb.cursor()
    mycursor.execute("SELECT Panier_global FROM client WHERE user_id = %s", (chat_id,))
    rows = mycursor.fetchall()
    Panier_global0 = rows[0][0]
    if Panier_global0:

        try:
                 chat_id = message.chat.id
                 mycursor = mydb.cursor()
                  # Exécuter une requête pour récupérer les valeurs
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                    # #  sql = "INSERT INTO client (Panier_global,Total) VALUES (%s,%s) WHERE user_id = chat_id"
                 sql = "UPDATE client SET Panier_global = %s, Total = %s WHERE user_id = %s"
                 Values = (f"50g de Amnésia Haze 666 Hollandaise  (Menu weed) à 350€\n\n {rows[0][0]}",sum([350,int(rows[0][1])]),chat_id )
                 mycursor.execute(sql, Values)
                 mydb.commit()
                  # Exécuter une requête pour récupérer les valeurs
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                 bot.reply_to(message,f" 🏆 Article(s) dans le Panier 🏆 : \n\n{rows[0][0]}\n \n Total : {rows[0][1]}€",reply_markup= autre_article)
        except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

    else :
        try:
                 chat_id = message.chat.id
                 mycursor = mydb.cursor()
                  #  sql = "INSERT INTO client (Panier_global,Total) VALUES (%s,%s) WHERE user_id = chat_id"
                 sql = "UPDATE client SET Panier_global = %s, Total = %s WHERE user_id = %s"
                 Values = (f"50g de Amnésia Haze 666 Hollandaise  (Menu weed) à 350€",350,chat_id )
                 mycursor.execute(sql, Values)
                 mydb.commit()
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                 bot.reply_to(message,f" 🏆 Article(s) dans le Panier 🏆 : \n\n{rows[0][0]} \n\n Total : {rows[0][1]}€",reply_markup= autre_article)

        except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

 except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

@bot.message_handler(func=lambda message: message.text == "650€/100g")
def handle_choice_one(message):
 try:
    chat_id = message.chat.id
    mycursor = mydb.cursor()
    mycursor.execute("SELECT Panier_global FROM client WHERE user_id = %s", (chat_id,))
    rows = mycursor.fetchall()
    Panier_global0 = rows[0][0]
    if Panier_global0:

        try:
                 chat_id = message.chat.id
                 mycursor = mydb.cursor()
                  # Exécuter une requête pour récupérer les valeurs
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                    # #  sql = "INSERT INTO client (Panier_global,Total) VALUES (%s,%s) WHERE user_id = chat_id"
                 sql = "UPDATE client SET Panier_global = %s, Total = %s WHERE user_id = %s"
                 Values = (f"100g de Amnésia Haze 666 Hollandaise  (Menu weed) à 650€\n\n {rows[0][0]}",sum([650,int(rows[0][1])]),chat_id )
                 mycursor.execute(sql, Values)
                 mydb.commit()
                  # Exécuter une requête pour récupérer les valeurs
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                 bot.reply_to(message,f" 🏆 Article(s) dans le Panier 🏆 : \n\n{rows[0][0]}\n \n Total : {rows[1][1]}€",reply_markup= autre_article)
        except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

    else :
        try:
                 chat_id = message.chat.id
                 mycursor = mydb.cursor()
                  #  sql = "INSERT INTO client (Panier_global,Total) VALUES (%s,%s) WHERE user_id = chat_id"
                 sql = "UPDATE client SET Panier_global = %s, Total = %s WHERE user_id = %s"
                 Values = (f"100g de Amnésia Haze 666 Hollandaise (Menu weed) à 650€",650,chat_id )
                 mycursor.execute(sql, Values)
                 mydb.commit()
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                 bot.reply_to(message,f" 🏆 Article(s) dans le Panier 🏆 : \n\n{rows[0][0]} \n\n Total : {rows[0][1]}€",reply_markup= autre_article)
        except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)
 except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)


    #**************************************************Carlifornienne*****************************************************************************

@bot.message_handler(func=lambda message: message.text == "70€/3,5g(1bag)")
def handle_choice_one(message):
 try:
    chat_id = message.chat.id
    mycursor = mydb.cursor()
    mycursor.execute("SELECT Panier_global FROM client WHERE user_id = %s", (chat_id,))
    rows = mycursor.fetchall()
    Panier_global0 = rows[0][0]
    if Panier_global0:

        try:
                 chat_id = message.chat.id
                 mycursor = mydb.cursor()
                  # Exécuter une requête pour récupérer les valeurs
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                    # #  sql = "INSERT INTO client (Panier_global,Total) VALUES (%s,%s) WHERE user_id = chat_id"
                 sql = "UPDATE client SET Panier_global = %s, Total = %s WHERE user_id = %s"
                 Values = (f"3,5g(1bag) de Sunset Sherbert Californienne (Menu weed) à 70€\n\n {rows[0][0]}",sum([70,int(rows[0][1])]),chat_id )
                 mycursor.execute(sql, Values)
                 mydb.commit()
                  # Exécuter une requête pour récupérer les valeurs
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                 bot.reply_to(message,f" 🏆 Article(s) dans le Panier 🏆 : \n\n{rows[0][0]}\n \n Total : {rows[0][1]}€",reply_markup= autre_article)
        except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

    else :
        try:
                 chat_id = message.chat.id
                 mycursor = mydb.cursor()
                  #  sql = "INSERT INTO client (Panier_global,Total) VALUES (%s,%s) WHERE user_id = chat_id"
                 sql = "UPDATE client SET Panier_global = %s, Total = %s WHERE user_id = %s"
                 Values = (f"3,5g(1bag) de Sunset Sherbert Californienne (Menu weed) à 70€",70,chat_id )
                 mycursor.execute(sql, Values)
                 mydb.commit()
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                 bot.reply_to(message,f" 🏆 Article(s) dans le Panier 🏆 : \n\n{rows[0][0]} \n\n Total : {rows[0][1]}€",reply_markup= autre_article)

        except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)
 except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

@bot.message_handler(func=lambda message: message.text == "190€/10,5g(3bag)")
def handle_choice_one(message):
 try:
    chat_id = message.chat.id
    mycursor = mydb.cursor()
    mycursor.execute("SELECT Panier_global FROM client WHERE user_id = %s", (chat_id,))
    rows = mycursor.fetchall()
    Panier_global0 = rows[0][0]
    if Panier_global0:

        try:
                 chat_id = message.chat.id
                 mycursor = mydb.cursor()
                  # Exécuter une requête pour récupérer les valeurs
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                    # #  sql = "INSERT INTO client (Panier_global,Total) VALUES (%s,%s) WHERE user_id = chat_id"
                 sql = "UPDATE client SET Panier_global = %s, Total = %s WHERE user_id = %s"
                 Values = (f"10,5g(3bag) de Sunset Sherbert Californienne (Menu weed) à 190€\n\n {rows[0][0]}",sum([190,int(rows[0][1])]),chat_id )
                 mycursor.execute(sql, Values)
                 mydb.commit()
                  # Exécuter une requête pour récupérer les valeurs
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                 bot.reply_to(message,f" 🏆 Article(s) dans le Panier 🏆 : \n\n{rows[0][0]}\n \n Total : {rows[0][1]}€",reply_markup= autre_article)
        except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

    else :
        try:
                 chat_id = message.chat.id
                 mycursor = mydb.cursor()
                  #  sql = "INSERT INTO client (Panier_global,Total) VALUES (%s,%s) WHERE user_id = chat_id"
                 sql = "UPDATE client SET Panier_global = %s, Total = %s WHERE user_id = %s"
                 Values = (f"10,5g(3bag) de Sunset Sherbert Californienne (Menu weed) à 190€",190,chat_id )
                 mycursor.execute(sql, Values)
                 mydb.commit()
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                 bot.reply_to(message,f" 🏆 Article(s) dans le Panier 🏆 : \n\n{rows[0][0]} \n\n Total : {rows[0][1]}€",reply_markup= autre_article)
        except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)
 except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

@bot.message_handler(func=lambda message: message.text == "80€/3,5g(1bag)")
def handle_choice_one(message):
 try:
    chat_id = message.chat.id
    mycursor = mydb.cursor()
    mycursor.execute("SELECT Panier_global FROM client WHERE user_id = %s", (chat_id,))
    rows = mycursor.fetchall()
    Panier_global0 = rows[0][0]
    if Panier_global0:

        try:
                 chat_id = message.chat.id
                 mycursor = mydb.cursor()
                  # Exécuter une requête pour récupérer les valeurs
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                    # #  sql = "INSERT INTO client (Panier_global,Total) VALUES (%s,%s) WHERE user_id = chat_id"
                 sql = "UPDATE client SET Panier_global = %s, Total = %s WHERE user_id = %s"
                 Values = (f"3,5g(1bag) de Gorilla x Zkittlez Californienne (Menu weed) à 80€\n\n {rows[0][0]}",sum([80,int(rows[0][1])]),chat_id )
                 mycursor.execute(sql, Values)
                 mydb.commit()
                  # Exécuter une requête pour récupérer les valeurs
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                 bot.reply_to(message,f" 🏆 Article(s) dans le Panier 🏆 : \n\n{rows[0][0]}\n \n Total : {rows[0][1]}€",reply_markup= autre_article)
        except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

    else :
        try:
                 chat_id = message.chat.id
                 mycursor = mydb.cursor()
                  #  sql = "INSERT INTO client (Panier_global,Total) VALUES (%s,%s) WHERE user_id = chat_id"
                 sql = "UPDATE client SET Panier_global = %s, Total = %s WHERE user_id = %s"
                 Values = (f"3,5g(1bag) de Gorilla x Zkittlez Californienne (Menu weed) à 80€",80,chat_id )
                 mycursor.execute(sql, Values)
                 mydb.commit()
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                 bot.reply_to(message,f" 🏆 Article(s) dans le Panier 🏆 : \n\n{rows[0][0]} \n\n Total : {rows[0][1]}€",reply_markup= autre_article)
        except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)
 except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

@bot.message_handler(func=lambda message: message.text == "200€/10,5g(3bag)")
def handle_choice_one(message):
 try:
    chat_id = message.chat.id
    mycursor = mydb.cursor()
    mycursor.execute("SELECT Panier_global FROM client WHERE user_id = %s", (chat_id,))
    rows = mycursor.fetchall()
    Panier_global0 = rows[0][0]
    if Panier_global0:

        try:
                 chat_id = message.chat.id
                 mycursor = mydb.cursor()
                  # Exécuter une requête pour récupérer les valeurs
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                    # #  sql = "INSERT INTO client (Panier_global,Total) VALUES (%s,%s) WHERE user_id = chat_id"
                 sql = "UPDATE client SET Panier_global = %s, Total = %s WHERE user_id = %s"
                 Values = (f"10,5g(1bag) de Gorilla x Zkittlez Californienne (Menu weed) à 300€\n\n {rows[0][0]}",sum([300,int(rows[0][1])]),chat_id )
                 mycursor.execute(sql, Values)
                 mydb.commit()
                  # Exécuter une requête pour récupérer les valeurs
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                 bot.reply_to(message,f" 🏆 Article(s) dans le Panier 🏆 : \n\n{rows[0][0]}\n \n Total : {rows[0][1]}€",reply_markup= autre_article)
        except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

    else :
        try:
                 chat_id = message.chat.id
                 mycursor = mydb.cursor()
                  #  sql = "INSERT INTO client (Panier_global,Total) VALUES (%s,%s) WHERE user_id = chat_id"
                 sql = "UPDATE client SET Panier_global = %s, Total = %s WHERE user_id = %s"
                 Values = (f"10,5g(3bag) de Gorilla x Zkittlez Californienne (Menu weed) à 300€",300,chat_id )
                 mycursor.execute(sql, Values)
                 mydb.commit()
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                 bot.reply_to(message,f" 🏆 Article(s) dans le Panier 🏆 : \n\n{rows[0][0]} \n\n Total : {rows[0][1]}€",reply_markup= autre_article)
        except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)
 except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

#************************************************espagnole**************************************

@bot.message_handler(func=lambda message: message.text == "70€/5g")
def handle_choice_one(message):
 try:
    chat_id = message.chat.id
    mycursor = mydb.cursor()
    mycursor.execute("SELECT Panier_global FROM client WHERE user_id = %s", (chat_id,))
    rows = mycursor.fetchall()
    Panier_global0 = rows[0][0]
    if Panier_global0:

        try:
                 chat_id = message.chat.id
                 mycursor = mydb.cursor()
                  # Exécuter une requête pour récupérer les valeurs
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                    # #  sql = "INSERT INTO client (Panier_global,Total) VALUES (%s,%s) WHERE user_id = chat_id"
                 sql = "UPDATE client SET Panier_global = %s, Total = %s WHERE user_id = %s"
                 Values = (f"5g de Runtz Espagnole (Menu weed) à 70€\n\n {rows[0][0]}",sum([70,int(rows[0][1])]),chat_id )
                 mycursor.execute(sql, Values)
                 mydb.commit()
                  # Exécuter une requête pour récupérer les valeurs
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                 bot.reply_to(message,f" 🏆 Article(s) dans le Panier 🏆 : \n\n{rows[0][0]}\n \n Total : {rows[0][1]}€",reply_markup= autre_article)
        except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

    else :
        try:
                 chat_id = message.chat.id
                 mycursor = mydb.cursor()
                  #  sql = "INSERT INTO client (Panier_global,Total) VALUES (%s,%s) WHERE user_id = chat_id"
                 sql = "UPDATE client SET Panier_global = %s, Total = %s WHERE user_id = %s"
                 Values = (f"5g de Runtz Espagnole (Menu weed) à 70€",70,chat_id )
                 mycursor.execute(sql, Values)
                 mydb.commit()
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                 bot.reply_to(message,f" 🏆 Article(s) dans le Panier 🏆 : \n\n{rows[0][0]} \n\n Total : {rows[0][1]}€",reply_markup= autre_article)
        except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)
 except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

@bot.message_handler(func=lambda message: message.text == "130€/10g")
def handle_choice_one(message):
 try:
    chat_id = message.chat.id
    mycursor = mydb.cursor()
    mycursor.execute("SELECT Panier_global FROM client WHERE user_id = %s", (chat_id,))
    rows = mycursor.fetchall()
    Panier_global0 = rows[0][0]
    if Panier_global0:

        try:
                 chat_id = message.chat.id
                 mycursor = mydb.cursor()
                  # Exécuter une requête pour récupérer les valeurs
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                    # #  sql = "INSERT INTO client (Panier_global,Total) VALUES (%s,%s) WHERE user_id = chat_id"
                 sql = "UPDATE client SET Panier_global = %s, Total = %s WHERE user_id = %s"
                 Values = (f"10g de Runtz Espagnole (Menu weed) à 130€\n\n {rows[0][0]}",sum([130,int(rows[0][1])]),chat_id )
                 mycursor.execute(sql, Values)
                 mydb.commit()
                  # Exécuter une requête pour récupérer les valeurs
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                 bot.reply_to(message,f" 🏆 Article(s) dans le Panier 🏆 : \n\n{rows[0][0]}\n \n Total : {rows[0][1]}€",reply_markup= autre_article)
        except Exception as e:
         bot.reply_to(message, f"❌ Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

    else :
        try:
                 chat_id = message.chat.id
                 mycursor = mydb.cursor()
                  #  sql = "INSERT INTO client (Panier_global,Total) VALUES (%s,%s) WHERE user_id = chat_id"
                 sql = "UPDATE client SET Panier_global = %s, Total = %s WHERE user_id = %s"
                 Values = (f"10g de Runtz Espagnole (Menu weed) à 130€",130,chat_id )
                 mycursor.execute(sql, Values)
                 mydb.commit()
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                 bot.reply_to(message,f" 🏆 Article(s) dans le Panier 🏆 : \n\n{rows[0][0]} \n\n Total : {rows[0][1]}€",reply_markup= autre_article)
        except Exception as e:
         bot.reply_to(message, f"❌ Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)
 except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)


@bot.message_handler(func=lambda message: message.text == "280€/25g")
def handle_choice_one(message):
 try:
    chat_id = message.chat.id
    mycursor = mydb.cursor()
    mycursor.execute("SELECT Panier_global FROM client WHERE user_id = %s", (chat_id,))
    rows = mycursor.fetchall()
    Panier_global0 = rows[0][0]
    if Panier_global0:

        try:
                 chat_id = message.chat.id
                 mycursor = mydb.cursor()
                  # Exécuter une requête pour récupérer les valeurs
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                    # #  sql = "INSERT INTO client (Panier_global,Total) VALUES (%s,%s) WHERE user_id = chat_id"
                 sql = "UPDATE client SET Panier_global = %s, Total = %s WHERE user_id = %s"
                 Values = (f"25g de Runtz Espagnole (Menu weed) à 230€\n\n {rows[0][0]}",sum([280,int(rows[0][1])]),chat_id )
                 mycursor.execute(sql, Values)
                 mydb.commit()
                  # Exécuter une requête pour récupérer les valeurs
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                 bot.reply_to(message,f" 🏆 Article(s) dans le Panier 🏆 : \n\n{rows[0][0]}\n \n Total : {rows[0][1]}€",reply_markup= autre_article)
        except Exception as e:
         bot.reply_to(message, f"❌ Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

    else :
        try:
                 chat_id = message.chat.id
                 mycursor = mydb.cursor()
                  #  sql = "INSERT INTO client (Panier_global,Total) VALUES (%s,%s) WHERE user_id = chat_id"
                 sql = "UPDATE client SET Panier_global = %s, Total = %s WHERE user_id = %s"
                 Values = (f"25g de Runtz Espagnole (Menu weed) à 230€",280,chat_id )
                 mycursor.execute(sql, Values)
                 mydb.commit()
                 mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
                 rows = mycursor.fetchall()
                 bot.reply_to(message,f" 🏆 Article(s) dans le Panier 🏆 : \n\n{rows[0][0]} \n\n Total : {rows[0][1]}€",reply_markup= autre_article)
        except Exception as e:
         bot.reply_to(message, f"❌ Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)
 except Exception as e:
         bot.reply_to(message, f" ❌Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

#****************************************************Les fonction au niveau du pannier*************************
@bot.message_handler(func=lambda message: message.text == "Ajouter un autre article")
def handle_choice_one(message):
     try:
         bot.reply_to(message, f"Choissisez un produit :",reply_markup=menu_principal1)
     except Exception as e:
         bot.reply_to(message, f"❌ Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

@bot.message_handler(func=lambda message: message.text == "Voir le panier")
def handle_choice_one(message):
    try:
          chat_id = message.chat.id
          mycursor = mydb.cursor()
          mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
          rows = mycursor.fetchall()
          bot.reply_to(message,f" 🏆 Article(s) dans le Panier 🏆 : \n\n{rows[0][0]} \n\n Total : {rows[0][1]}€",reply_markup= autre_article)

        #   Total = sum(Prix_article)
        #   Panier_global1= "\n \n".join(Panier_global)
        #   bot.reply_to(message,f"🏆 Article(s) dans le Panier 🏆 : \n\n{Panier_global1} \n \n Total : {Total}€",reply_markup= autre_article)
    except Exception as e:
         bot.reply_to(message, f" ❌ Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)
@bot.message_handler(func=lambda message: message.text == "Supprimer le panier")
def handle_choice_one(message):
    try:
            mycursor = mydb.cursor()
            chat_id = message.chat.id
            # Exécuter la requête pour supprimer le contenu des colonnes pour l'utilisateur spécifié
            query = "UPDATE client SET Panier_global = NULL, Total = NULL WHERE user_id = %s"
            values = (chat_id,)
            mycursor.execute(query, values)
            mydb.commit()  # Correction : appeler commit() sur mydb
            bot.reply_to(message, f"Panier supprimé", reply_markup=final_livraison)

    except Exception as e:
      bot.reply_to(message, f"❌ Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)
@bot.message_handler(func=lambda message: message.text == "Payer")
def handle_choice_one(message):
    try:
          chat_id = message.chat.id
          mycursor = mydb.cursor()
          mycursor.execute("SELECT Panier_global, Total FROM client WHERE user_id = %s", (chat_id,))
          rows = mycursor.fetchall()
          bot.reply_to(message,f" 🏆 Article(s) dans le Panier 🏆 : \n\n{rows[0][0]} \n\n Total : {rows[0][1]}€",reply_markup= confirmation_achat)
    except Exception as e:
      bot.reply_to(message, f"❌ Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)


#*************************************************************************************************************************************
@bot.message_handler(func=lambda message: message.text == "Ok")
def handle_choice_one(message):
     try:
          bot.reply_to(message, f"Confirmer votre commande en suivant ces étapes : \n\n👉🏼 Adresse\n\n👉🏼 Code postale\n\n👉🏼 Selfie avec ce signe   « 🫡 »\n\n👉🏼 Carte d'identité\n\nEntrer en premier lieu votre Adresse ( Ex : Adresse : ........)",reply_markup=final_livraison)
     except Exception as e:
      bot.reply_to(message, f"❌ Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

@bot.message_handler(func=lambda message: message.text == "Envoyer"  )
def handle_choice_one(message):
     try:
         chat_id = message.chat.id
         mycursor = mydb.cursor()
         mycursor.execute("SELECT Panier_global, Total,Adresse_client,Code_postale,photos_received,photos_received1 FROM client WHERE user_id = %s", (chat_id,))
         rows = mycursor.fetchall()
         bot.reply_to(message, f"Votre commande a été envoyée avec succès! ✅")
         bot.reply_to(message, f"Récapitulatif de la commande :\n\n 🏆 Article(s) dans le Panier 🏆 : \n\n {rows[0][0]} \n \n Total : {rows[0][1]}€ \n\n👉🏼  Mode de livraison : Livraison\n\n👉🏼  Adresse {rows[0][2]}\n\n👉🏼  Code_postale {rows[0][3]}\n\n👉🏼  Mode de paiement : Espèce \n\n🇺🇸🇲🇦Sarkoffee bot🇪🇸🇳🇱",reply_markup=final_livraison)
         bot.send_message(chat_id=5333192125, text=f"Vous avez une nouvelle commande de {message.chat.first_name }\n\n Récapitulatif de la commande :\n\n🏆 Article(s) dans le Panier 🏆 : \n\n{rows[0][0]} \n \n Total : {rows[0][1]}€ \n\n👉🏼  Adresse {rows[0][2]} \n\n👉🏼  Code_postale {rows[0][3]}\n\n👉🏼  Mode de paiement : Espèce \n\n👉🏼  Nom du bot : Sarkoffee_bot ")
        #  for photo in rows[0][4]:
         bot.send_photo(chat_id=5333192125, photo=rows[0][4])
        #  for photo in rows[0][5]:
         bot.send_photo(chat_id=5333192125, photo=rows[0][5])

     except Exception as e:
      bot.reply_to(message, f"❌ Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)



#********************************************************Confirmation commande**********************************************************
@bot.message_handler(func=lambda message: message.text.lower().startswith("adresse"))
def handle_address(message):
    try:
            address = message.text[len("Adresse "):].strip()
            mycursor = mydb.cursor()
            chat_id = message.chat.id
            query = "UPDATE client SET Adresse_client = %s WHERE user_id = %s"
            values = (address,chat_id)
            mycursor.execute(query, values)
            mydb.commit()
            bot.reply_to(message, f"Entrer votre Code postale : (Ex : Code postale : .......)",reply_markup=final_livraison)
    except Exception as e:
      bot.reply_to(message, f"❌ Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)

@bot.message_handler(func=lambda message: message.text.lower().startswith("code postale"))
def handle_address(message):
    try:
            Code  = message.text[len("Code postale"):].strip()
            mycursor = mydb.cursor()
            chat_id = message.chat.id
            query = "UPDATE client SET Code_postale= %s WHERE user_id = %s"
            values = (Code,chat_id)
            mycursor.execute(query, values)
            mydb.commit()
            bot.reply_to(message, f"Envoyer votre selfie")
    except Exception as e:
      bot.reply_to(message, f"❌ Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)
#*********************les images ******************************************************

@bot.message_handler(content_types=['photo'])
def handle_photos(message):
  try:
      chat_id = message.chat.id
      mycursor = mydb.cursor()
      mycursor.execute("SELECT photos_received FROM client WHERE user_id = %s", (chat_id,))
      rows = mycursor.fetchall()
      if rows[0][0]:
          # Récupérer l'ID de la dernière photo envoyée
            photo_id = message.photo[-1].file_id

        # Ajouter l'ID de la photo à la liste
            mycursor = mydb.cursor()
            chat_id = message.chat.id
            query = "UPDATE client SET photos_received1 = %s WHERE user_id = %s"
            values = (photo_id,chat_id)
            mycursor.execute(query, values)
            mydb.commit()
            bot.reply_to(message, "Cliquer sur Envoyer",reply_markup=confirmation4)

      else:

        # Récupérer l'ID de la dernière photo envoyée
            photo_id = message.photo[-1].file_id

        # Ajouter l'ID de la photo à la liste
            mycursor = mydb.cursor()
            chat_id = message.chat.id
            query = "UPDATE client SET photos_received = %s WHERE user_id = %s"
            values = (photo_id,chat_id)
            mycursor.execute(query, values)
            mydb.commit()
            bot.reply_to(message, " Envoyer la photo de votre carte d'identité",reply_markup=final_livraison)
  except Exception as e:
      bot.reply_to(message, f"❌ Erreur en choisissant cette commande : veuillez réessayer. ",reply_markup=final_livraison)



# Démarrer le bot
bot.polling()





























from os import sys
import time
from PIL import *
from tkinter import *
from tkinter import filedialog
from pygame import mixer
import os

root = Tk()
root.title("Simpli Music Player")
root.geometry("485x700+290+10")
root.configure(background='#333333')
root.resizable(False, False)
mixer.init()

# Create a function to open a file
def AddMusic():
    path = filedialog.askdirectory()
    if path:
       os.chdir(path)
       songs = os.listdir(path)

       for song in songs:
              if song.endswith(".mp3"):
                     Playlist.insert(END, song)


def PlayMusic():
    Music_Name = Playlist.get(ACTIVE)
    print(Music_Name[0:-4])
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()
    
    
# icon
lower_frame = Frame(root , bg = "#FFFFFF", width = 485 , height = 180 )
lower_frame.place ( x = 0 , y = 400)



image_icon = PhotoImage(file="C:/Users/alim/Desktop/Projet python/mp3 code source/logo.png")
root.iconphoto(False, image_icon)


frameCnt = 30
frames = [PhotoImage(file='C:/Users/alim/Desktop/Projet python/mp3 code source/aa1.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

def update(ind):

    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    root.after(40, update, ind)
label = Label(root)
label.place(x=0, y=0)
root.after(0, update, 0)




# Button
ButtonPlay = PhotoImage(file="C:/Users/alim/Desktop/Projet python/mp3 code source/play1.png")
Button(root, image=ButtonPlay, bg="#FFFFFF", bd=0, height = 60, width =60,
       command=PlayMusic).place(x=215, y=487)

ButtonStop = PhotoImage(file="C:/Users/alim/Desktop/Projet python/mp3 code source/stop1.png")
Button(root, image=ButtonStop, bg="#FFFFFF", bd=0, height = 60, width =60,
       command=mixer.music.stop).place(x=130, y=487)

Buttonvolume = PhotoImage(file="C:/Users/alim/Desktop/Projet python/mp3 code source/volume.png")
Button(root, image=Buttonvolume, bg="#FFFFFF", bd=0, height = 60, width =60,
       command=mixer.music.unpause).place(x=20, y=487)

ButtonPause = PhotoImage(file="C:/Users/alim/Desktop/Projet python/mp3 code source/pause1.png")
Button(root, image=ButtonPause, bg="#FFFFFF", bd=0, height = 60, width =60,
       command=mixer.music.pause).place(x=300, y=487)

# Label       
Menu = PhotoImage(file="C:/Users/alim/Desktop/Projet python/mp3 code source/menu.png")
Label(root, image=Menu).place(x=0, y=580, width=485, height=120)

Frame_Music = Frame(root, bd=2, relief=RIDGE)
Frame_Music.place(x=0, y=585, width=485, height=100)



Button(root, text="Browse Music", width=59, height=1, font=("calibri",
      12, "bold"), fg="Black", bg="#FFFFFF", command=AddMusic).place(x=0, y=550)

Scroll = Scrollbar(Frame_Music)
Playlist = Listbox(Frame_Music, width=100, font=("Times new roman", 10), bg="#333333", fg="grey", selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=Scroll.set)
Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT, fill=Y)
Playlist.pack(side=RIGHT, fill=BOTH)

# Execute Tkinter

root.mainloop()
