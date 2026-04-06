#Credit Churane Wale Ki Ma Ki Ch*t
#Credit Churane Wale Ki Ma Ki Ch*t
#Credit Churane Wale Ki Ma Ki Ch*t
#Credit Churane Wale Ki Ma Ki Ch*t
import sys , time ,os ,ctypes ,msvcrt
from beyondmem import MemFurqan , enable_vt

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except:
        return False
    
if not is_admin():
    script = os.path.abspath(__file__)
    params = f'"{script}"'
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)
    sys.exit(0)

#CONFIGURATION 
PROCESS = "HD-Player"
AIMBOT_AOB =( "FF FF FF FF FF FF FF FF 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 "
    "?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? "
    "?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? "
    "?? ?? ?? ?? ?? "
    "00 00 00 00 00 00 00 00 00 00 00 00 A5 43")

TARGET_OFFSET = 0x80   #BODY
WRITE_OFFSET = 0x7C    #HEAD

def main():
    enable_vt()
    mem = MemFurqan()


    while True:
        os.system("cls")
        print("Jnl Codex Aimbot Engine")
        print(f"connecting to {PROCESS}...")

        if not mem.open_process_by_name(PROCESS):
            print(f"Process name could not be found")
            print("Press  q key to exit...")
            ch = msvcrt.getch().lower()
            if ch =='q' : break
            continue 

        print (f"connected PID : {mem.the_proc_id}")
        print("Press F to inject Aimbot")

        while True:
           if msvcrt.kbhit() :
            key = msvcrt.getwch().lower()
            if key == 'f':
               print("scanning for entities")
               found = mem.AoBScan(0x10000,0x7FFFFFEFFFF, AIMBOT_AOB)

               if not found :
                   print("no entities found")
                   break
               
               count = 0
               for base in found :
                   try :
                       target_addr = base + WRITE_OFFSET
                       source_addr = base + TARGET_OFFSET

                       val_bytes = mem.read_bytes(source_addr, 4)
                       if val_bytes :
                           if mem._write_raw(target_addr,val_bytes) :
                               count += 1   
                   except:                         
                            
                       continue
                   
                   if count > 0 :
                       print(f"applied aimbot to {count} entities" )
                   else:
                       print("no entities found")
            elif key == 'q' :
                   sys.exit(0)
        time.sleep(0.01)
        
if __name__ == "__main__":
    main()


          


