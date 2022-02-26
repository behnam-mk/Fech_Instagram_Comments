from contextlib import nullcontext
from curses.ascii import NUL
from time import sleep
import selenium.webdriver as wd
import csv
import simpleaudio 


#replace your link here
link = "https://www.instagram.com/reel/CabOSMuDNdA/?utm_source=ig_web_copy_link"

#you must download driver and addres here
driver = wd.Chrome(r" ") # you can change it 

username = ' ' #Enter username here
password = ' ' #Enter password here

def login(username, password) :
    driver.find_element_by_xpath('//input[@name="username"]').send_keys(username)
    driver.find_element_by_xpath('//input[@name="password"]').send_keys(password)
    driver.find_element_by_xpath('//button[@type="submit"]').click()

def playRing():
    wave_obj = simpleaudio.WaveObject.from_wave_file("bell.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()

def formatMyString(comment, counter):
    if comment == NUL:
        return ""
    comment = comment.strip()

    
    
    return comment

#def fetch_comments(link):
def fetch_comments():

    driver.get(link)
    i = 1
    sleepTime1 = 1
    sleepTime2 = 1

    while True:
        try:
            if i < 60 and i > 20:
                sleepTime1 = 2
            elif i < 90 and i > 60:
                sleepTime2 = 2
            elif i > 90 and i < 120:
                sleepTime1 = 3
            elif i > 120 and i < 140:
                sleepTime2 = 3
            elif i > 140 and i < 165:
                sleepTime1 = 4
            elif i > 165 and i < 190:
                sleepTime2 = 5
            elif i > 190:
                sleepTime1=6
                sleepTime2=8
                
            sleep(sleepTime1)
              
            driver.find_element_by_xpath('//div[@class="             qF0y9          Igw0E     IwRSH        YBx95       _4EzTm                                                                                                            NUiEW  "]/button[@class="wpO6b  "]').click()
            print('clicked  '+ str(i))
            i += 1
            sleep(sleepTime2)
            
        except Exception as e:
            print(e)
            i = 0
            newLine = ''
            playRing()

            comments = driver.find_elements_by_xpath(f"//span[@class='_7UhW9   xLCgt      MMzan   KV-D4           se6yk       T0kll ']")
            print(len(comments)-1)

            userNames = driver.find_elements_by_xpath(f"//span[@class='Jv7Aj mArmR MqpiF  ']/a[@class='sqdOP yWX7d     _8A5w5   ZIAjV ']")
            userPictures = driver.find_elements_by_xpath(f"//a[@class='_2dbep qNELH kIKUG']/img[@class='_6q-tv']")
            commentsTime = driver.find_elements_by_xpath(f"//time[@class='FH9sR RhOlS']")

            numberOfNames = len(userNames)
            numberOfPictures = len(userPictures)
            numberOfCommentTime = len(commentsTime)

            with open('comments.csv', 'a', encoding='UTF-8', newline='') as f:
                for comment in comments:
                    if i==0:
                        i +=1
                    else :
                        writer = csv.writer(f)

                        comment = formatMyString(comment.text, i)

                        if i+1 < numberOfNames: 
                            writer.writerow([userNames[i+1].text])
                        else:
                            print("\nError in Index of user Name")
                        
                        if i-1 < numberOfPictures:
                            writer.writerow([userPictures[i-1].get_attribute("src")])
                        else:
                            print("\nError in Index of user picture")
                        
                        writer.writerow([comment])
                        
                        if i-1 < numberOfCommentTime:
                            writer.writerow([commentsTime[i].get_attribute("datetime")])
                        else:
                            print("\nError in Index of user Comment time")

                        writer.writerow(newLine)

                        print('Done comment: '+ str(i))
                        i+=1                   
                f.close()

            print("\nnumber of comments: ",len(comments))
            print("number of user names: ",len(userNames))
            print("number of user pictures is: ",len(userPictures))
            print("number of comments time is: ",len(commentsTime))

            print('\nAll Done!')
            driver.close()
            break

def main() :
    driver.get('https://www.instagram.com/')
    try :
        driver.find_element_by_xpath('//button[text()="Accept"]').click()
    except :
        pass
    sleep(2)
    login(username, password)
    sleep(8)
    try :
        login(username, password)
    except :
        pass
    sleep(5)
    while True:
        #fetch_comments(input('post link >>'))
        fetch_comments()
        break

if __name__ == '__main__':
    main()
