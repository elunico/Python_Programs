try:
    from Tkinter import *
except ImportError:
    from tkinter import *
import smtplib
import getpass

# ERROR CODES

# A36
# Any code that is commented out
# or is written in with the line comment
# '#A36' is code that is related to this error
# I could not get the servers for clients
# besides Gmail to respond to TLS requests
# or stop refusing login
# Therefore this code was modified to prevent the user
# from changing the client from Gmail to anything else
# To do that certain things were removed
# to re-instate the option of choosing servers
# uncomment whatever is commented with #A36
# and comment out whatever is uncommented with the tag #A36

class Application(object):
    SMTP_SERVERS = {"Gmail":'smtp.gmail.com'}#, "Hotmail":'smtp.live.com', "Yahoo":'smtp.mail.yahoo.com', "Aol":'smtp.aol.com'}
    PORTS = {'Gmail':587}#, 'Hotmail':25, 'Hotmail2':465, 'Yahoo':465, 'Yahoo2':587, 'Aol':587}
    def doSend(self, c, t, u, p, s, m):
        alert = Tk()
        alert.title("Progress")
        alertText = Text(alert, font=("Courier", "13", "normal"))
        alertText.pack()
        try:
            alertText.insert(END, "\nOpening server")
            alert.update()
            if c == "Hotmail" or c == "Yahoo":
                pass
                # try: CODE #A36
                #     server = smtplib.SMTP(Application.SMTP_SERVERS[c], Application.PORTS[c])
                #     port = Application.PORTS[c]
                # except:
                #     server = smtplib.SMTP(Application.SMTP_SERVERS[c], Application.PORTS[str(c + "2")])
                #     port = Application.PORTS[str(c + '2')]
            else:
                port = Application.PORTS[c]
                server = smtplib.SMTP(Application.SMTP_SERVERS[c], Application.PORTS[c])
            alertText.insert(END, "\n\nOpened '%s' at %d" % (Application.SMTP_SERVERS[c], port))
            alert.update()
            alertText.insert(END, "\n\nContacting...")
            alert.update()
            server.ehlo()
            alertText.insert(END, "\nSuccessfully sent EHLO")
            alert.update()
            alertText.insert(END, "\n\nEstablishing TLS...")
            alert.update()
            server.starttls()
            server.ehlo()
            alertText.insert(END, "\nTLS established.")
            alert.update()
            alertText.insert(END, "\n\nAttempting Login...")
            alert.update()
            server.login(u, p)
            alertText.insert(END, "\nLogin succeeded.\n")
            alert.update()
            header = 'To:' + t + "\n" + 'From: ' + u + "\n" + "Subject:" + s
            message = header + m
            alertText.insert(END, "\n\nPreparing to send...")
            alert.update()
            server.sendmail(u, t, m)
            alertText.insert(END, "\nMessage sent!")
            alert.update()
        except Exception as E:
            alertText.insert(END, "\n\nERROR\n")
            alert.update()
            alertText.insert(END, E)
        finally:
            try:
                server.quit()
            except UnboundLocalError:
                pass
            except:
                alertText.insert(END, "\n\nERROR: Could not close server")
                raise SystemExit(-1)
            alertText.insert(END, "\n\nClosing server...")
            alert.update()
            alertText.insert(END, "\nServer Closed.")
            alert.update()
            Button(alert, text='close', command=alert.destroy).pack()
            alert.mainloop()
            raise SystemExit(0)

    def getStuff(self):
        return self.theClient, self.to_a, self.usn, self.unpw, self.sujeto, self.mes

    def send(self):
        self.theClient = self.client.get()
        self.to_a = self.e1.get()
        self.usn = self.e2.get()
        self.unpw = self.e3.get()
        self.sujeto = self.e4.get()
        self.mes = self.e5.get('0.0', END)
        self.root.destroy()

    def main(self):
        self.root = Tk()
        self.root.title("Compose Email")

        l0 = Label(self.root, text="Select A Client")
        l0.pack()
        self.client = StringVar(self.root)
        self.client.set("Gmail") # initial value

        option = OptionMenu(self.root, self.client, "Gmail")#, "Yahoo", "Hotmail", "Aol")
        option.pack()

        l1 = Label(self.root, text="Enter the recepient:", font=("Helvetica Neue", "14", "normal"))
        l2 = Label(self.root, text="Enter your email address:", font=("Helvetica Neue", "14", "normal"))
        l3 = Label(self.root, text="Enter your password: ", font=("Helvetica Neue", "14", "normal"))
        l4 = Label(self.root, text="Subject:", font=("Helvetica Neue", "14", "normal"))
        l5 = Label(self.root, text="Message:", font=("Helvetica Neue", "14", "normal"))
        sendb = Button(self.root, text="Send", command=self.send)
        self.e1 = Entry(self.root, width=60, font=("Helvetica Neue", "14", "normal"))
        self.e2 = Entry(self.root, width=60, font=("Helvetica Neue", "14", "normal"))
        self.e3 = Entry(self.root, show="*", width=60, font=("Helvetica Neue", "14", "normal"))
        self.e4 = Entry(self.root, width=60, font=("Helvetica Neue", "14", "normal"))
        self.e5 = Text(self.root, font=("Helvetica Neue", "14", "normal"), wrap="word", height=12, width=60)
        l1.pack()
        self.e1.pack()
        l2.pack()
        self.e2.pack()
        l3.pack()
        self.e3.pack()
        l4.pack()
        self.e4.pack()
        l5.pack()
        self.e5.pack()
        sendb.pack()
        self.root.mainloop()


def main():
    a = Application()
    a.main()
    Client, recp, un, pw, sject, msg = a.getStuff()
    sub = sject + " \n"
    a.doSend(Client, recp, un, pw, sub, msg)


if __name__ == '__main__':
    main()
