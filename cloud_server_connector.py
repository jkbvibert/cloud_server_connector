import sys, subprocess, os
print("Which server?")
print("1.\tTidal Agent 1 (ITG - <server1>)")
print("2.\tTidal Agent 2 (ITG - <server2>)")
print("3.\tTidal Agent 3 (PRO - <server3>)")
print("4.\tTidal Agent 4 (PRO - <server4>)")
print("5.\tVertica Monitoring Dashboard (<server5>)")
print("6.\t<server6>")
print("7.\t<server7>")
print("8.\t<server8>")
print("9.\t<server9>")
print("10.\t<server10>")
print("11.\t<server11>")
print("E.\tExit")
choice = input("Enter your choice: ")
if str(choice).lower() == 'e':
    sys.exit(0)
if choice == '1':
    p = subprocess.Popen('cmd.exe /c %s\\Desktop\\putty.exe -ssh vibertj@<server1>' % os.environ['USERPROFILE'])
elif choice == '2':
    p = subprocess.Popen('cmd.exe /c %s\\Desktop\\putty.exe -ssh vibertj@<server2>' % os.environ['USERPROFILE'])
elif choice == '3':                                                                                   
    p = subprocess.Popen('cmd.exe /c %s\\Desktop\\putty.exe -ssh vibertj@<server3>' % os.environ['USERPROFILE'])
elif choice == '4':                                                                                   
    p = subprocess.Popen('cmd.exe /c %s\\Desktop\\putty.exe -ssh vibertj@<server4>' % os.environ['USERPROFILE'])
elif choice == '5' or choice == '6' or choice == '7' or choice == '8' or choice == '9' or choice == '10' or choice == '11':
    print("1.\tRDP")
    print("2.\tWindows Explorer")
    print("E.\tExit")
    choice2 = input("Enter your choice: ")
    if choice2 == '1':
        if choice == '5':
            p = subprocess.Popen('cmd.exe /c mstsc /v:<windows_server>')
        elif choice == '6':                                          
            p = subprocess.Popen('cmd.exe /c mstsc /v:<windows_server>')
        elif choice == '7':                                          
            p = subprocess.Popen('cmd.exe /c mstsc /v:<windows_server>')
        elif choice == '8':                                          
            p = subprocess.Popen('cmd.exe /c mstsc /v:<windows_server>')
        elif choice == '9':                                          
            p = subprocess.Popen('cmd.exe /c mstsc /v:<windows_server>')
        elif choice == '10':                                        
            p = subprocess.Popen('cmd.exe /c mstsc /v:<windows_server>')
        elif choice == '11':                                        
            p = subprocess.Popen('cmd.exe /c mstsc /v:<windows_server>')
        else:
            sys.exit(1)
    elif choice2 == '2':
        if choice == '5':
            p = subprocess.Popen('cmd.exe /c start \\\<windows_server>')
        elif choice == '6':
            p = subprocess.Popen('cmd.exe /c start \\\<windows_server>')
        elif choice == '7':
            p = subprocess.Popen('cmd.exe /c start \\\<windows_server>')
        elif choice == '8':
            p = subprocess.Popen('cmd.exe /c start \\\<windows_server>')
        elif choice == '9':
            p = subprocess.Popen('cmd.exe /c start \\\<windows_server>')
        elif choice == '10':
            p = subprocess.Popen('cmd.exe /c start \\\<windows_server>')
        elif choice == '11':
            p = subprocess.Popen('cmd.exe /c start \\\<windows_server>')
        else:
            sys.exit(1)
    elif str(choice).lower() == 'e':
        sys.exit(0)
else:
    sys.exit(1)
