import pygame
import time

def init_joystick():
    pygame.joystick.quit()
    pygame.joystick.init()
    count = pygame.joystick.get_count()
    print(f"[INFO] Joysticks connected: {count}")
    if count == 0:
        print("[WARN] No gamepad detected.")
        return None
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print(f"[SUCCESS] Connected to: {joystick.get_name()} (ID: {joystick.get_id()})")
    print(f"[DEBUG] Buttons: {joystick.get_numbuttons()}, Axes: {joystick.get_numaxes()}")
    return joystick

def read_buttons_and_axes(joystick):
    pygame.event.pump()
    button_pressed = False

    # Buttons
    for button in range(joystick.get_numbuttons()):
        if joystick.get_button(button):
            print(f"➡️ Button {button} is pressed")
            button_pressed = True
    if not button_pressed:
        print("No buttons pressed.")

    # D-pad (axes)
    horizontal_axis = joystick.get_axis(0)  # X-axis
    vertical_axis = joystick.get_axis(1)    # Y-axis

    if horizontal_axis < -0.5:
        print("⬅️ D-Pad Left")
    elif horizontal_axis > 0.5:
        print("➡️ D-Pad Right")

    if vertical_axis < -0.5:
        print("⬆️ D-Pad Up")
    elif vertical_axis > 0.5:
        print("⬇️ D-Pad Down")

def run():
    print("📡 Starting Gamepad Monitor...")
    pygame.init()
    joystick = init_joystick()

    try:
        while True:
            print("🔁 --- New Loop Iteration ---")
            if joystick is None:
                print("[STATUS] Waiting for gamepad...")
                time.sleep(2)
                joystick = init_joystick()
                continue

            if not joystick.get_init():
                print("[ERROR] Gamepad not initialized, retrying...")
                joystick = None
                time.sleep(2)
                continue

            try:
                read_buttons_and_axes(joystick)
            except pygame.error as e:
                print(f"[ERROR] Pygame error: {e}")
                joystick = None

            time.sleep(0.1)

    except KeyboardInterrupt:
        print("\n🛑 Stopping Gamepad Monitor.")
    finally:
        pygame.quit()
        print("🧹 Pygame cleaned up and exited.")

if __name__ == "__main__":
    run()
