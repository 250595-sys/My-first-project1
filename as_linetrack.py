import sys
import time
import random
import math

class Program():
  __interpretation_started_timestamp__ = time.time() * 1000

  pi = 3.141592653589793

  def execMain(self):

    
    
    while bool(1):
      if (brick.sensor("A1").read() < 5 and brick.sensor("A2").read() > 5):
        brick.motor("M3").setPower(20)
        
        brick.motor("M4").setPower(40)
        
      else:
        if (brick.sensor("A1").read() > 5 and brick.sensor("A2").read() < 5):
          brick.motor("M4").setPower(20)
          
          brick.motor("M3").setPower(40)
          
        else:
          brick.motor("M3").setPower(40)
          brick.motor("M4").setPower(40)
          
    brick.stop()
    return

def main():
  program = Program()
  program.execMain()

if __name__ == '__main__':
  main()
