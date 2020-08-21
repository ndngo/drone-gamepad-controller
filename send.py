import socket
import pygame

UDP_IP = "192.168.10.1"
UDP_PORT = 8889
COMMAND = "command"

print("UDP target IP:", UDP_IP)
print("UDP target port:", UDP_PORT)
print("message:", COMMAND)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

pygame.init()

j = pygame.joystick.Joystick(0)
j.init()

print("{}: {}".format(j.get_id(), j.get_name()))
done = False

try:
  while True:
    events = pygame.event.get()
    for event in events:
      if event.type == pygame.JOYBUTTONDOWN:
        if j.get_button(0):
          print("A")
          COMMAND = "land"
        elif j.get_button(1):
          print("B")
        elif j.get_button(2):
          print("X")
        elif j.get_button(3):
          print("Y")
          COMMAND = "takeoff"
        elif j.get_button(4):
          print("LB")
        elif j.get_button(5):
          print("RB")
        elif j.get_button(6):
          print("BACK")
        elif j.get_button(7):
          print("START")
          print("Entering SDK mode.")
          COMMAND = "command"
        elif j.get_button(8):
          print("LEFT STICK")
        elif j.get_button(9):
          print("RIGHT STICK")
        else:
          print("unknown button")

      elif event.type == pygame.JOYAXISMOTION:
        if (round(j.get_axis(0), 3) > 0.05):
          COMMAND = "right 20"
          print("right 20")
        elif (round(j.get_axis(0), 3) < -0.05):
          COMMAND = "left 20"
          print("left 20")
        if (round(j.get_axis(1), 3) > 0.05):
          COMMAND = "back 20"
          print("back 20")
        elif (round(j.get_axis(1), 3) < -0.05):
          COMMAND = "forward 20"
          print("forward 20")

      if COMMAND != "":
        sock.sendto(COMMAND.encode('utf-8'), (UDP_IP, UDP_PORT))
        command = ""
          
except KeyboardInterrupt:
  print("EXITING NOW")
  j.quit()