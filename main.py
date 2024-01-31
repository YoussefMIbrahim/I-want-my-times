# THis is a program that will hopefully get the times from our google sheets and add them to my google calander, because I was lazy and bored
import gspread 




def main():
    #placeholder
    # gc = gspread.oauth(
    # credentials_filename='/home/busterscruggs/.config/gspread/credentials.json',
    # authorized_user_filename='/home/busterscruggs/.config/gspread/authorized_user.json'
    # )

    gc = gspread.service_account(filename='/home/busterscruggs/.config/gspread/k ')
    sh = gc.open('Test-sheet"')
    worksheet1 = sh.get_worksheet(0)

    test1 = worksheet1.cell(1,2).value

    print(test1)
    print('Hello')





main()