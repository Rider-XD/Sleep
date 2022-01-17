# module
import os,sys,time,random
from time import sleep
# MY COLOR
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
G = '\33[33;7m' # KUNING TEPAK
my_color = [
 P, M, H, K, B, U, O, N, G]
warna = random.choice(my_color)
# IN ROOM
def nanya():
        nanya =raw_input("\033[34;1mApakah \033[32;1m anda \033[35;1m ingin \033[36;1matack lagi? \033[36;1m[\033[32;1mY\033[34;1m/\033[35;1mT\033[33;1m] \033[35;1m~\033[33;1m=> ")
        if nanya =="Y" or nanya =="y":
                menu()
        elif nanya =="T" or nanya =="t":
                auto("\033[35;1mBye \033[32;1mBye \033[33;1m:)")
                time.sleep(1)
                sys.exit()
        elif nanya =="" or nanya =='':
                auto("\033[32;1mJangan \033[35;1msampe \033[36;1mkosong \033[32;1mya")
                time.sleep(1)
                nanya()
        else:
                auto("\033[32;1mSalah, \033[35;1mMasukkan \033[36;1minput \033[32;1mpilihan \033[36;1mdengan \033[33;1mbenar!")
                time.sleep(1)
                nanya()
def auto(z):
  for e in z + '\n':
    sys.stdout.write(e)
    sys.stdout.flush()
    time.sleep(0.05)
def exe():
  titik = ['\x1b[1;96m.   ', '\x1b[1;95m..  ', '\x1b[1;96m... ','\x1b[1;95m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
  for x in titik
  print "\r [+] Wait %s"%(x),
  sys.stdout.flush
  time.sleep(1)
def main():
  os.system("clear")
  exe()
  auto("\n %sWelcome User Termux%s")%(O,N)
  print "%s________________________________"%(K)
  print "%s[%s+%s] %sAuthor : Reza Alfauzan   %s[%s+%s]"%(P,O,P,N,P,O,P)
  print "%s[%s+%s] %sFrom : Indonesian        %s[%s+%s]"%(P,O,P,N,P,O,P)
  print "%s[%s+%s] %sDont Change Author!!     %s[%s+%s]"%(P,O,P,N,P,O,P)
  print "%s________________________________"%(K)
  print "%s(%s1%s)%s.Send Trojan"%(P,O,P,N)
  print "%s(%s2%s)%s.Send Virus"%(P,O,P,N)
  kontol = raw_input("$s[%s+%s] %sPilih : %s")%(P,O,P,N)
  if pilih =='1':
    os.system("clear")
    print "%s(%s__________________________%s)"%(K,O,K)
    print "%s(%s__________________________%s)"%(K,O,K)
    nomor = raw_input("%sMasukkan %sNomor %sTarget : %s")%(N,N,N,K)
    jumlah = int(input("\033[31;1mMasukkan \033[35;1mjumlahnya : "))
    
    try:
      for i in range(jumlah):
        print "\033[34;1mBerhasil \033[36;1mmengirim \033[33;1mTrojan \033[35;1m\033[36;1mKe \033[36;1m=>",
        time.sleep(0.1)
    except KeyboardInterrupt:
      print "\033[36;1m### \033[33;1mSelesai \033[32;1m###"
      nanya()
   elif pilih =='2':
    os.system("clear")
    print "%s(%s__________________________%s)"%(K,O,K)
    print "%s(%s__________________________%s)"%(K,O,K)
    nomor = raw_input("%sMasukkan %sNomor %sTarget : %s")%(N,N,N,K)
    jumlah = int(input("\033[31;1mMasukkan \033[35;1mjumlahnya : "))
    
    try:
      for i in range(jumlah):
        print "\033[34;1mBerhasil \033[36;1mmengirim \033[33;1mVirus \033[35;1m\033[36;1mKe \033[36;1m=>",
        time.sleep(0.1)
    except KeyboardInterrupt:
      print "\033[36;1m### \033[33;1mSelesai \033[32;1m###"
      nanya()
menu()
