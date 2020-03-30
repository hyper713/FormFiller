from selenium import webdriver
from random import randint
import sys
import time
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException,UnexpectedAlertPresentException  

#Static VARs
first = ["Lahcen","Zineb","Mohammed","Yassine","Amine","Fatima-Ezzrhra","Said","Jaafar","Adam","Malak","Asmae","Adil","Anass","Hamid","Touria","Nihal","Hajar","Montassir","Leila","Soukaina","Fahd","Sakina","Ismail","Anouar","Omar","Aya","Amina","Sahar"]

second = ["RizKi","Aloui","Bdiri","Nonji","Bakha","Daroui","Nagoli","Naimi","Lmri","Twil","Nafri","Namosi","Bnrin","Twil","Jafrani","Lawfi","Aoudi","Montassir","Mjrani","Hafi","Nasir","Faris","Donia","Amrosi","Lmwafi","Jabrani","Rizki","Bgari"]

domain = ["protonmail.com","gmail.com","outlook.com","taalim.ma","outlook.fr","yahoo.com","hotmail.com","yahoo.fr","gmail.com","hotmail.fr","zoho.com","gmail.com","hotmail.com","gmail.com","hotmail.com","gmail.com","outlook.fr","hotmail.com","outlook.fr","gmail.com","outlook.fr"]

addition = ["1243","boo","hype","34","24r","45","67","87","yuo","xs","poi","33z","ox","qwe","546","198","33","6","234","65","7","wer","yb87","1qw","tue","as34"]

separator = [".","-",".",".","_","."]

games = ["/html/body/div/div[2]/form/div/div/div[2]/div[4]/div/div[2]/div/span/div/div[1]/label/div[2]/div[1]/div/div[3]/div"
        ,"/html/body/div/div[2]/form/div/div/div[2]/div[4]/div/div[2]/div/span/div/div[2]/label/div[2]/div[1]/div/div[3]/div"]

levels = ["/html/body/div/div[2]/form/div/div/div[2]/div[6]/div/div[2]/div/span/div/div[1]/label/div/div[1]/div/div[3]/div", #API S2
            "/html/body/div/div[2]/form/div/div/div[2]/div[6]/div/div[2]/div/span/div/div[2]/label/div/div[1]/div/div[3]/div", #TM S2
            "/html/body/div/div[2]/form/div/div/div[2]/div[6]/div/div[2]/div/span/div/div[3]/label/div/div[1]/div/div[3]/div", #TM S4
            "/html/body/div/div[2]/form/div/div/div[2]/div[6]/div/div[2]/div/span/div/div[4]/label/div/div[1]/div/div[3]/div", #GE S2
            "/html/body/div/div[2]/form/div/div/div[2]/div[6]/div/div[2]/div/span/div/div[5]/label/div/div[1]/div/div[3]/div", #GE S4
            "/html/body/div/div[2]/form/div/div/div[2]/div[6]/div/div[2]/div/span/div/div[6]/label/div/div[1]/div/div[3]/div", #GLT S4
            "/html/body/div/div[2]/form/div/div/div[2]/div[6]/div/div[2]/div/span/div/div[7]/label/div/div[1]/div/div[3]/div", #BIG DATA S6
            "/html/body/div/div[2]/form/div/div/div[2]/div[6]/div/div[2]/div/span/div/div[8]/label/div/div[1]/div/div[3]/div", #BIG DATA S8
            "/html/body/div/div[2]/form/div/div/div[2]/div[6]/div/div[2]/div/span/div/div[9]/label/div/div[1]/div/div[3]/div", #FIA S6
            "/html/body/div/div[2]/form/div/div/div[2]/div[6]/div/div[2]/div/span/div/div[10]/label/div/div[1]/div/div[3]/div"] #FIA S8

email="/html/body/div/div[2]/form/div/div/div[2]/div[1]/div[2]/div/div[1]/div/div[1]/input"
name="/html/body/div/div[2]/form/div/div/div[2]/div[5]/div/div[2]/div/div[1]/div/div[1]/input"
phone="/html/body/div/div[2]/form/div/div/div[2]/div[7]/div/div[2]/div/div[1]/div/div[1]/input"
submit="/html/body/div/div[2]/form/div/div/div[3]/div[1]/div/div/span"

#launch url
url = "https://forms.gle/wsqnCVWQ5v1Nd4Np6"

#Functions
def generate():
        firstname = first[randint(0, len(first)-1)]
        secondname = second[randint(0, len(second)-1)]
        return [firstname.lower()+separator[randint(0, len(separator)-1)]+secondname.lower()+separator[randint(0, len(separator)-1)]+addition[randint(0, len(addition)-1)]+"@"+domain[randint(0, len(domain)-1)],firstname+" "+secondname]

def generate_phone():
        return "0"+str(randint(6,7))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))

def generate_game():
        return games[randint(0, len(games)-1)]

def generate_level():
        return levels[randint(0, len(levels)-1)]

def check_exists(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True



if int(sys.argv[1])>0:
        counter =0
        start = time.time()
        # create a new session
        driver = webdriver.Chrome(executable_path=r'chromedriver.exe')
        for x in range(int(sys.argv[1])):
                driver.get(url)
                try:
                        var=generate()
                        driver.find_element_by_xpath(email).send_keys(var[0]) #fill the email
                        driver.find_element_by_xpath(generate_game()).click() #fill the game
                        driver.find_element_by_xpath(name).send_keys(var[1]) #fill tha name
                        driver.find_element_by_xpath(generate_level()).click() #fill the level
                        driver.find_element_by_xpath(phone).send_keys(generate_phone()) #fill tha phone
                        driver.find_element_by_xpath(submit).click() #submit the form
                except UnexpectedAlertPresentException:
                        continue
                else:
                        time.sleep(1)
                        if check_exists("/html/body/div[1]/div[2]/div[1]/div/div[3]"):
                                counter = counter+1
        end = time.time()
        f = open("log.txt", "a")
        line = "["+datetime.now().strftime("%d-%b-%Y (%H:%M:%S)")+"] [Total requested forms: "+str(sys.argv[1])+"] [Total submitted forms: "+str(counter)+"] [Total time: "+str(int(end-start))+"sec]\n"
        f.write(line)
        f.close()

        driver.quit()
        print("\n")
        print("Submited forms ",counter)
        print("")
        print("Used time",int(end-start),"sec")
else:
        print("Bad Argument")


