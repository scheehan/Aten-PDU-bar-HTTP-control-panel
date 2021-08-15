import re
import telnetlib
from time import sleep
import cgi, cgitb

def main():
    # credential and telnet server info
    HOST = "192.168.148.180"
    user = 'teladmin'
    password = 'telpwd'

    # init connection to PDU 
    tn = telnetlib.Telnet(HOST)
    # tn.set_debuglevel(100) //enable debug output; may cause apache2 to return unexpected error

    # capture "Login" and provides username
    tn.read_until(b"Login: ", 3)
    tn.write("teladmin".encode('ascii') + "\r\n".encode('ascii'))

    # capture "Password" and provides password
    tn.read_until(b"Password: ", 3)
    tn.write("telpwd".encode('ascii') + "\r\n".encode('ascii'))

    # send command to read status on socket 24
    tn.write("read status o24".encode('ascii'))
    tn.write("\r".encode('ascii'))

    # pause for 1 second
    sleep(1)

    # send command to close telnet session
    tn.write("quit".encode('ascii'))
    tn.write("\r".encode('ascii'))

    # save and decode output
    b_data = tn.read_all().decode('ascii')

    # split string into list, then remove special character
    l_list = list(b_data)
    l_list_2 = [x.replace('\r', '') for x in l_list]
    l_list_3 = [x.replace('\n', '') for x in l_list_2]

    # join list back into string
    s_string = ''
    s_string_1 = s_string.join(l_list_3).strip()

    # perform regex find to output desirable output 
    p_match = re.findall(r'\>(.*) O', s_string_1)
    p_match_1 = re.findall(r'4(.*)>', s_string_1)

    print ("Content-type: text/html\n")                      
    print ("<html>\n")
    print("<body>\n")

    print('<p> Command Ran:' + str(p_match[0]) + ' </p>')
    print('<p> Result Recv:' + str(p_match_1[0]) + ' </p>')

    print("</body>\n")
    print("</html>\n")

if __name__ == '__main__':
    main()